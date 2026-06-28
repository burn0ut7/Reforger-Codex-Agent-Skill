<#
.SYNOPSIS
  Refresh local Arma Reforger game data and generated API references for this skill.

.DESCRIPTION
  This script is deterministic and does not use AI. It discovers the Arma Reforger
  Steam install, finds every data.pak, clones or updates rvost/PakInspector, extracts
  only script files from the pak files into raw/game-data, and scans those
  Enforce Script files into raw/game-data/api-schema.json plus a compact
  markdown index.
#>

[CmdletBinding()]
param(
  [string]$GamePath,
  [string]$SkillRoot,
  [switch]$Force,
  [switch]$SkipExtract,
  [switch]$SkipSchema
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$PakInspectorRepo = 'https://github.com/rvost/PakInspector.git'
$ArmaReforgerAppId = '1874880'

if (-not $SkillRoot) {
  $scriptDirectory = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
  $SkillRoot = (Resolve-Path (Join-Path $scriptDirectory '..')).Path
}

function Write-Step {
  param([string]$Message)
  Write-Host "[reforger] $Message"
}

function Ensure-Directory {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
  }
}

function ConvertTo-SafeName {
  param([string]$Value)
  $safe = $Value -replace '^[A-Za-z]:\\?', ''
  $safe = $safe -replace '[\\/:*?"<>|]+', '_'
  $safe = $safe -replace '\s+', '_'
  if ([string]::IsNullOrWhiteSpace($safe)) {
    return 'root'
  }
  return $safe.Trim('_')
}

function Get-RelativePathCompat {
  param(
    [string]$BasePath,
    [string]$TargetPath
  )

  $baseFullPath = [System.IO.Path]::GetFullPath($BasePath)
  $targetFullPath = [System.IO.Path]::GetFullPath($TargetPath)

  if (-not $baseFullPath.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
    $baseFullPath += [System.IO.Path]::DirectorySeparatorChar
  }

  $baseUri = [System.Uri]::new($baseFullPath)
  $targetUri = [System.Uri]::new($targetFullPath)
  $relativeUri = $baseUri.MakeRelativeUri($targetUri)
  return [System.Uri]::UnescapeDataString($relativeUri.ToString()).Replace('/', [System.IO.Path]::DirectorySeparatorChar)
}

function Get-SteamInstallPaths {
  $paths = New-Object System.Collections.Generic.List[string]

  $registryPaths = @(
    'HKCU:\Software\Valve\Steam',
    'HKLM:\Software\WOW6432Node\Valve\Steam',
    'HKLM:\Software\Valve\Steam'
  )

  foreach ($registryPath in $registryPaths) {
    if (Test-Path $registryPath) {
      $props = Get-ItemProperty -Path $registryPath
      foreach ($name in @('SteamPath', 'InstallPath')) {
        if ($props.PSObject.Properties.Name -contains $name -and $props.$name) {
          $paths.Add(($props.$name -replace '/', '\'))
        }
      }
    }
  }

  foreach ($candidate in @(
      "${env:ProgramFiles(x86)}\Steam",
      "$env:ProgramFiles\Steam"
    )) {
    if ($candidate -and (Test-Path -LiteralPath $candidate)) {
      $paths.Add($candidate)
    }
  }

  $libraryRoots = New-Object System.Collections.Generic.List[string]
  foreach ($steamPath in ($paths | Select-Object -Unique)) {
    $steamApps = Join-Path $steamPath 'steamapps'
    if (Test-Path -LiteralPath $steamApps) {
      $libraryRoots.Add($steamPath)
    }

    $libraryFile = Join-Path $steamApps 'libraryfolders.vdf'
    if (Test-Path -LiteralPath $libraryFile) {
      foreach ($line in Get-Content -LiteralPath $libraryFile) {
        if ($line -match '"path"\s+"([^"]+)"') {
          $libraryPath = ($Matches[1] -replace '\\\\', '\')
          if (Test-Path -LiteralPath (Join-Path $libraryPath 'steamapps')) {
            $libraryRoots.Add($libraryPath)
          }
        }
      }
    }
  }

  return $libraryRoots | Select-Object -Unique
}

function Find-ArmaReforgerPath {
  param([string]$ExplicitPath)

  if ($ExplicitPath) {
    $resolved = Resolve-Path -LiteralPath $ExplicitPath
    return $resolved.Path
  }

  $candidates = New-Object System.Collections.Generic.List[string]
  foreach ($steamRoot in Get-SteamInstallPaths) {
    $candidates.Add((Join-Path $steamRoot 'steamapps\common\Arma Reforger'))
  }

  foreach ($candidate in ($candidates | Select-Object -Unique)) {
    if (Test-Path -LiteralPath $candidate) {
      return (Resolve-Path -LiteralPath $candidate).Path
    }
  }

  throw "Could not find Arma Reforger. Re-run with -GamePath 'C:\Program Files (x86)\Steam\steamapps\common\Arma Reforger'."
}

function Get-GameVersionInfo {
  param([string]$ResolvedGamePath)

  $version = $null
  $buildId = $null
  $manifestPath = $null

  $steamApps = Split-Path (Split-Path $ResolvedGamePath -Parent) -Parent
  $candidateManifest = Join-Path $steamApps "appmanifest_$ArmaReforgerAppId.acf"
  if (Test-Path -LiteralPath $candidateManifest) {
    $manifestPath = $candidateManifest
    foreach ($line in Get-Content -LiteralPath $candidateManifest) {
      if ($line -match '"buildid"\s+"([^"]+)"') {
        $buildId = $Matches[1]
      }
    }
  }

  $exe = Get-ChildItem -LiteralPath $ResolvedGamePath -Filter '*.exe' -File -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

  if ($exe) {
    $fileVersion = [System.Diagnostics.FileVersionInfo]::GetVersionInfo($exe.FullName).FileVersion
    if ($fileVersion) {
      $version = $fileVersion
    }
  }

  if (-not $version -and $buildId) {
    $version = "build-$buildId"
  }
  if (-not $version) {
    $version = 'unknown-' + (Get-Date -Format 'yyyyMMdd-HHmmss')
  }

  $version = ConvertTo-SafeName $version

  [pscustomobject]@{
    Version = $version
    BuildId = $buildId
    ManifestPath = $manifestPath
  }
}

function Ensure-PakInspector {
  param([string]$ToolsRoot)

  Ensure-Directory $ToolsRoot
  $repoRoot = Join-Path $ToolsRoot 'PakInspector'

  if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'git is required to clone/update PakInspector.'
  }

  if (Test-Path -LiteralPath (Join-Path $repoRoot '.git')) {
    Write-Step 'Updating raw/tools/PakInspector'
    & git -C $repoRoot pull --ff-only | Write-Host
  }
  elseif (Test-Path -LiteralPath $repoRoot) {
    throw "tools/PakInspector exists but is not a git checkout: $repoRoot"
  }
  else {
    Write-Step 'Cloning rvost/PakInspector into raw/tools'
    & git clone $PakInspectorRepo $repoRoot | Write-Host
  }

  if ($LASTEXITCODE -ne 0) {
    throw 'Failed to clone or update PakInspector.'
  }

  if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) {
    throw '.NET SDK is required to build PakInspector.'
  }

  $projectPath = Join-Path $repoRoot 'src\PakInspector\PakInspector.csproj'
  Write-Step 'Building PakInspector'
  & dotnet build $projectPath -c Release | Write-Host
  if ($LASTEXITCODE -ne 0) {
    throw 'PakInspector build failed.'
  }

  $publishRoot = Join-Path $repoRoot 'artifacts\publish\win-x64'
  Write-Step 'Publishing PakInspector self-contained executable'
  & dotnet publish $projectPath -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:PublishAot=false -o $publishRoot | Write-Host
  if ($LASTEXITCODE -ne 0) {
    throw 'PakInspector publish failed.'
  }

  $exe = Get-ChildItem -LiteralPath $publishRoot -File -Filter 'PakInspector.exe' -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

  if (-not $exe) {
    $exe = Get-ChildItem -LiteralPath (Join-Path $repoRoot 'src\PakInspector\bin\Release') -Recurse -File -Filter 'PakInspector.exe' |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
  }

  $dll = Get-ChildItem -LiteralPath (Join-Path $repoRoot 'src\PakInspector\bin\Release') -Recurse -File -Filter 'PakInspector.dll' |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

  $commit = (& git -C $repoRoot rev-parse HEAD).Trim()

  [pscustomobject]@{
    RepoRoot = $repoRoot
    Exe = if ($exe) { $exe.FullName } else { $null }
    Dll = if ($dll) { $dll.FullName } else { $null }
    Commit = $commit
  }
}

function Invoke-PakInspectorExtract {
  param(
    [object]$PakInspector,
    [string]$PakFile,
    [string]$OutputDir,
    [string[]]$Files
  )

  Ensure-Directory $OutputDir

  $fileBatches = @()
  if ($Files -and $Files.Count -gt 0) {
    for ($i = 0; $i -lt $Files.Count; $i += 75) {
      $end = [Math]::Min($i + 74, $Files.Count - 1)
      $fileBatches += , @($Files[$i..$end])
    }
  }
  else {
    $fileBatches = @(, @())
  }

  foreach ($batch in $fileBatches) {
    $args = New-Object System.Collections.Generic.List[string]
    $args.Add('extract')
    $args.Add($PakFile)
    $args.Add($OutputDir)
    foreach ($file in $batch) {
      $args.Add('-f')
      $args.Add($file)
    }

    if ($PakInspector.Exe) {
      & $PakInspector.Exe @args
    }
    elseif ($PakInspector.Dll) {
      & dotnet $PakInspector.Dll @args
    }
    else {
      throw 'Could not locate built PakInspector executable or DLL.'
    }

    if ($LASTEXITCODE -ne 0) {
      throw "PakInspector failed while extracting $PakFile"
    }
  }
}

function Get-PakScriptFilePaths {
  param(
    [object]$PakInspector,
    [string]$PakFile
  )

  $tempRoot = Join-Path $env:TEMP ('reforger-pakinspect-' + [guid]::NewGuid().ToString('N'))
  Ensure-Directory $tempRoot

  try {
    Push-Location $tempRoot
    if ($PakInspector.Exe) {
      & $PakInspector.Exe inspect $PakFile -q -s | Write-Host
    }
    elseif ($PakInspector.Dll) {
      & dotnet $PakInspector.Dll inspect $PakFile -q -s | Write-Host
    }
    else {
      throw 'Could not locate built PakInspector executable or DLL.'
    }

    if ($LASTEXITCODE -ne 0) {
      throw "PakInspector failed while inspecting $PakFile"
    }

    $reportPath = Join-Path $tempRoot ([System.IO.Path]::GetFileNameWithoutExtension($PakFile) + '.json')
    $report = Get-Content -LiteralPath $reportPath -Raw | ConvertFrom-Json
    return [string[]]@(
      $report.files |
        Where-Object {
          $extension = [System.IO.Path]::GetExtension($_.path).ToLowerInvariant()
          $extension -in @('.c', '.h')
        } |
        Select-Object -ExpandProperty path
    )
  }
  finally {
    Pop-Location
    if (Test-Path -LiteralPath $tempRoot) {
      Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
  }
}

function Split-Parameters {
  param([string]$Parameters)

  if ([string]::IsNullOrWhiteSpace($Parameters)) {
    return @()
  }

  $items = New-Object System.Collections.Generic.List[object]
  foreach ($part in ($Parameters -split ',')) {
    $trimmed = $part.Trim()
    if (-not $trimmed) {
      continue
    }
    $withoutDefault = ($trimmed -replace '\s*=.*$', '').Trim()
    if ($withoutDefault -match '^(?<mods>(?:(?:out|inout|notnull|ref|autoptr|owned)\s+)*)?(?<type>[A-Za-z_][\w:<>.,\[\]\s]*?)\s+(?<name>[A-Za-z_]\w*)$') {
      $mods = Get-MatchValue -MatchTable $Matches -Name 'mods'
      $items.Add([pscustomobject]@{
          name = $Matches.name
          type = ($Matches.type -replace '\s+', ' ').Trim()
          modifiers = [object[]]@(Split-Modifiers $mods)
          raw = $trimmed
        })
    }
    else {
      $items.Add([pscustomobject]@{
          name = $null
          type = $null
          modifiers = [object[]]@()
          raw = $trimmed
        })
    }
  }
  return $items
}

function Get-MatchValue {
  param(
    [System.Collections.IDictionary]$MatchTable,
    [string]$Name
  )

  if ($MatchTable.Contains($Name)) {
    return $MatchTable[$Name]
  }
  return $null
}

function ConvertTo-JsonArray {
  param([object[]]$Items)
  return [object[]]@($Items | Where-Object { $null -ne $_ -and $_ -ne '' })
}

function Split-Modifiers {
  param([string]$Modifiers)

  if ([string]::IsNullOrWhiteSpace($Modifiers)) {
    return [object[]]@()
  }

  return [object[]]@($Modifiers.Trim() -split '\s+' | Where-Object { $_ })
}

function Get-LineBraceDelta {
  param([string]$Line)

  $withoutLineComment = ($Line -replace '//.*$', '')
  $open = ([regex]::Matches($withoutLineComment, '\{')).Count
  $close = ([regex]::Matches($withoutLineComment, '\}')).Count
  return $open - $close
}

function Take-PendingMetadata {
  param(
    [System.Collections.Generic.List[string]]$Docs,
    [System.Collections.Generic.List[string]]$Attributes
  )

  $metadata = [pscustomobject]@{
    docs = [object[]]@($Docs)
    attributes = [object[]]@($Attributes)
  }
  $Docs.Clear()
  $Attributes.Clear()
  return $metadata
}

function New-ApiSchema {
  param(
    [string]$RawRoot,
    [string]$Version,
    [string]$GamePath
  )

  $classes = New-Object System.Collections.Generic.List[object]
  $enums = New-Object System.Collections.Generic.List[object]
  $functions = New-Object System.Collections.Generic.List[object]
  $classByName = @{}

  $scriptFiles = Get-ChildItem -LiteralPath $RawRoot -Recurse -File -Include '*.c', '*.h' -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match '\\scripts\\|\\Scripts\\|\\script\\|\\Script\\|\\source\\|\\Source\\' }

  foreach ($file in $scriptFiles) {
    $relativeFile = Get-RelativePathCompat -BasePath $RawRoot -TargetPath $file.FullName
    $currentClass = $null
    $currentClassDepth = $null
    $pendingClassOpen = $false
    $braceDepth = 0
    $lineNumber = 0
    $pendingDocs = New-Object System.Collections.Generic.List[string]
    $pendingAttributes = New-Object System.Collections.Generic.List[string]
    $inBlockDoc = $false

    foreach ($line in Get-Content -LiteralPath $file.FullName) {
      $lineNumber++
      $trimmed = $line.Trim()

      if ($currentClass -and -not $pendingClassOpen -and $null -ne $currentClassDepth -and $braceDepth -le $currentClassDepth) {
        $currentClass = $null
        $currentClassDepth = $null
      }

      if ($pendingClassOpen -and $trimmed -match '^\{') {
        $braceDepth += Get-LineBraceDelta $line
        $currentClassDepth = $braceDepth - 1
        $pendingClassOpen = $false
        continue
      }

      if ($trimmed -match '^/\*!|^/\*\*') {
        $inBlockDoc = $true
        $pendingDocs.Add($trimmed)
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      if ($inBlockDoc) {
        $pendingDocs.Add($trimmed)
        if ($trimmed -match '\*/') {
          $inBlockDoc = $false
        }
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      if ($trimmed -match '^(//!|///|\\brief|\\returns)') {
        $pendingDocs.Add($trimmed)
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      if ($trimmed -match '^\[') {
        $pendingAttributes.Add($trimmed)
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      if (-not $trimmed -or $trimmed.StartsWith('//')) {
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      if ($trimmed -match '^(?<mods>(?:(?:modded|sealed)\s+)*)class\s+(?<name>[A-Za-z_]\w*)(?:\s*:\s*(?<extends>[A-Za-z_][\w:<>]*))?') {
        $mods = Get-MatchValue -MatchTable $Matches -Name 'mods'
        $extends = Get-MatchValue -MatchTable $Matches -Name 'extends'
        $metadata = Take-PendingMetadata -Docs $pendingDocs -Attributes $pendingAttributes
        $currentClass = [pscustomobject]@{
          name = $Matches.name
          kind = if ($mods -match '\bmodded\b') { 'modded class' } else { 'class' }
          extends = if ($extends) { $extends } else { $null }
          modifiers = [object[]]@(Split-Modifiers $mods)
          docs = $metadata.docs
          attributes = $metadata.attributes
          file = $relativeFile
          line = $lineNumber
          methods = New-Object System.Collections.Generic.List[object]
          properties = New-Object System.Collections.Generic.List[object]
        }
        $currentClassDepth = $braceDepth
        $pendingClassOpen = ($trimmed -notmatch '\{')
        $classes.Add($currentClass)
        if (-not $classByName.ContainsKey($currentClass.name)) {
          $classByName[$currentClass.name] = $currentClass
        }
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      if ($trimmed -match '^(?<mods>(?:(?:sealed)\s+)*)enum\s+(?<name>[A-Za-z_]\w*)') {
        $mods = Get-MatchValue -MatchTable $Matches -Name 'mods'
        $metadata = Take-PendingMetadata -Docs $pendingDocs -Attributes $pendingAttributes
        $enums.Add([pscustomobject]@{
            name = $Matches.name
            modifiers = [object[]]@(Split-Modifiers $mods)
            docs = $metadata.docs
            attributes = $metadata.attributes
            file = $relativeFile
            line = $lineNumber
          })
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      $declaration = $trimmed -replace '\s+', ' '
      $atMemberDepth = (-not $currentClass) -or ($null -ne $currentClassDepth -and $braceDepth -eq ($currentClassDepth + 1))
      $methodPattern = '^(?<mods>(?:(?:proto|external|override|static|protected|private|sealed|event|virtual|native|owned|final)\s+)*)?(?<return>[A-Za-z_][\w:<>.,\[\]\s]*?)\s+(?<name>[~A-Za-z_]\w*)\s*\((?<params>[^)]*)\)\s*(?:;|\{|$)'
      if ($atMemberDepth -and $declaration -match $methodPattern -and $Matches.name -notin @('if', 'for', 'while', 'switch', 'foreach')) {
        $mods = Get-MatchValue -MatchTable $Matches -Name 'mods'
        $metadata = Take-PendingMetadata -Docs $pendingDocs -Attributes $pendingAttributes
        $method = [pscustomobject]@{
          name = $Matches.name
          returnType = ($Matches.return -replace '\s+', ' ').Trim()
          parameters = [object[]]@(Split-Parameters $Matches.params)
          modifiers = [object[]]@(Split-Modifiers $mods)
          docs = $metadata.docs
          attributes = $metadata.attributes
          signature = $declaration
          file = $relativeFile
          line = $lineNumber
        }

        if ($currentClass) {
          $currentClass.methods.Add($method)
        }
        else {
          $functions.Add($method)
        }
        $braceDepth += Get-LineBraceDelta $line
        continue
      }

      $propertyPattern = '^(?<mods>(?:(?:ref|static|protected|private|const|autoptr|owned|notnull)\s+)*)?(?<type>[A-Za-z_][\w:<>.,\[\]\s]*?)\s+(?<name>[A-Za-z_]\w*)\s*(?:=|;)'
      if ($currentClass -and $atMemberDepth -and $declaration -match $propertyPattern) {
        $mods = Get-MatchValue -MatchTable $Matches -Name 'mods'
        $metadata = Take-PendingMetadata -Docs $pendingDocs -Attributes $pendingAttributes
        $currentClass.properties.Add([pscustomobject]@{
            name = $Matches.name
            type = ($Matches.type -replace '\s+', ' ').Trim()
            modifiers = [object[]]@(Split-Modifiers $mods)
            docs = $metadata.docs
            attributes = $metadata.attributes
            signature = $declaration
            file = $relativeFile
            line = $lineNumber
          })
      }

      if ($trimmed -notmatch '^(//!|///|\\brief|\\returns|\[)') {
        if ($trimmed -notmatch '^(\{|\})') {
          $pendingDocs.Clear()
          $pendingAttributes.Clear()
        }
      }
      $braceDepth += Get-LineBraceDelta $line
    }
  }

  [pscustomobject]@{
    gameVersion = $Version
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    gamePath = $GamePath
    sourceRoot = $RawRoot
    counts = [pscustomobject]@{
      scriptFiles = @($scriptFiles).Count
      classes = $classes.Count
      enums = $enums.Count
      functions = $functions.Count
    }
    classes = @($classes | Sort-Object name, file, line)
    enums = @($enums | Sort-Object name, file, line)
    functions = @($functions | Sort-Object name, file, line)
  }
}

function Write-ApiIndex {
  param(
    [object]$Schema,
    [string]$OutputPath
  )

  $lines = New-Object System.Collections.Generic.List[string]
  $allMethods = New-Object System.Collections.Generic.List[object]
  foreach ($class in $Schema.classes) {
    foreach ($method in $class.methods) {
      $allMethods.Add([pscustomobject]@{
          className = $class.name
          name = $method.name
          returnType = $method.returnType
          signature = $method.signature
          file = $method.file
          line = $method.line
        })
    }
  }

  $lines.Add("# Arma Reforger API Index")
  $lines.Add('')
  $lines.Add("Generated: $($Schema.generatedAt)")
  $lines.Add("Game version: $($Schema.gameVersion)")
  $lines.Add('')
  $lines.Add("Counts: $($Schema.counts.scriptFiles) script files, $($Schema.counts.classes) classes, $($Schema.counts.enums) enums, $($Schema.counts.functions) global functions, $($allMethods.Count) class methods.")
  $lines.Add('')
  $lines.Add('## Classes')
  foreach ($class in $Schema.classes) {
    $extends = if ($class.extends) { " : $($class.extends)" } else { '' }
    $lines.Add(("- `{0}{1}` - {2}:{3} ({4} methods, {5} properties)" -f $class.name, $extends, $class.file, $class.line, $class.methods.Count, $class.properties.Count))
  }
  $lines.Add('')
  $lines.Add('## Enums')
  foreach ($enum in $Schema.enums) {
    $lines.Add(("- `{0}` - {1}:{2}" -f $enum.name, $enum.file, $enum.line))
  }
  $lines.Add('')
  $lines.Add('## Global Functions')
  foreach ($function in $Schema.functions) {
    $signature = if ($function.signature) { $function.signature } else { "$($function.returnType) $($function.name)(...)" }
    $lines.Add(("- `{0}` - {1}:{2}" -f $signature, $function.file, $function.line))
  }
  $lines.Add('')
  $lines.Add('## Methods')
  foreach ($method in ($allMethods | Sort-Object className, name, file, line)) {
    $signature = if ($method.signature) { $method.signature } else { "$($method.returnType) $($method.name)(...)" }
    $lines.Add(("- `{0}.{1}` - `{2}` - {3}:{4}" -f $method.className, $method.name, $signature, $method.file, $method.line))
  }

  Set-Content -LiteralPath $OutputPath -Value $lines -Encoding UTF8
}

$rawRoot = Join-Path $SkillRoot 'raw'
$gameDataRoot = Join-Path $rawRoot 'game-data'
$toolsRoot = Join-Path $rawRoot 'tools'

$resolvedGamePath = Find-ArmaReforgerPath -ExplicitPath $GamePath
Write-Step "Game path: $resolvedGamePath"

$versionInfo = Get-GameVersionInfo -ResolvedGamePath $resolvedGamePath
$version = $versionInfo.Version
Write-Step "Game version key: $version"

$pakFiles = @(Get-ChildItem -LiteralPath $resolvedGamePath -Recurse -File -Filter 'data.pak')
if ($pakFiles.Count -eq 0) {
  throw "No data.pak files found under $resolvedGamePath"
}
Write-Step "Found $($pakFiles.Count) data.pak file(s)"

$pakInspector = Ensure-PakInspector -ToolsRoot $toolsRoot

$pakManifest = New-Object System.Collections.Generic.List[object]
if (-not $SkipExtract) {
  if (Test-Path -LiteralPath $gameDataRoot) {
    Write-Step "Deleting existing game data: $gameDataRoot"
    Remove-Item -LiteralPath $gameDataRoot -Recurse -Force
  }
  Ensure-Directory $gameDataRoot

  foreach ($pak in $pakFiles) {
    $relativePak = Get-RelativePathCompat -BasePath $resolvedGamePath -TargetPath $pak.FullName
    $targetName = ConvertTo-SafeName ([System.IO.Path]::GetDirectoryName($relativePak))
    $targetRoot = Join-Path $gameDataRoot $targetName
    $scriptFiles = @(Get-PakScriptFilePaths -PakInspector $pakInspector -PakFile $pak.FullName)

    if ($scriptFiles.Count -eq 0) {
      Write-Step "Skipping $relativePak because it contains no .c/.h script files"
    }
    else {
      Write-Step "Extracting $($scriptFiles.Count) script file(s) from $relativePak"
      Invoke-PakInspectorExtract -PakInspector $pakInspector -PakFile $pak.FullName -OutputDir $targetRoot -Files $scriptFiles
    }

    $hash = Get-FileHash -LiteralPath $pak.FullName -Algorithm SHA256
    $pakManifest.Add([pscustomobject]@{
        path = $pak.FullName
        relativePath = $relativePak
        sha256 = $hash.Hash
        scriptFileCount = $scriptFiles.Count
        extractedTo = if ($scriptFiles.Count -gt 0) { $targetRoot } else { $null }
      })
  }
}

$schema = $null
if (-not $SkipSchema) {
  if (-not (Test-Path -LiteralPath $gameDataRoot)) {
    throw "Cannot generate schema because raw game data does not exist: $gameDataRoot"
  }

  Write-Step 'Generating deterministic API schema'
  $schema = New-ApiSchema -RawRoot $gameDataRoot -Version $version -GamePath $resolvedGamePath
  $schemaPath = Join-Path $gameDataRoot 'api-schema.json'
  $schema | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $schemaPath -Encoding UTF8

  $indexPath = Join-Path $gameDataRoot 'api-index.md'
  Write-ApiIndex -Schema $schema -OutputPath $indexPath
}

$schemaCounts = $null
if ($schema) {
  $schemaCounts = $schema.counts
}

$pakManifestArray = @()
foreach ($entry in $pakManifest) {
  $pakManifestArray += $entry
}

$manifest = [pscustomobject]@{
  generatedAt = (Get-Date).ToUniversalTime().ToString('o')
  gamePath = $resolvedGamePath
  gameVersion = $version
  buildId = $versionInfo.BuildId
  appManifest = $versionInfo.ManifestPath
  pakInspector = [pscustomobject]@{
    repo = $PakInspectorRepo
    commit = $pakInspector.Commit
    path = $pakInspector.RepoRoot
  }
  pakFiles = $pakManifestArray
  schema = $schemaCounts
}

$manifestPath = Join-Path $gameDataRoot 'manifest.json'
$manifest | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

Write-Step "Wrote manifest: $manifestPath"
if ($schema) {
  Write-Step "Schema counts: $($schema.counts.scriptFiles) script files, $($schema.counts.classes) classes, $($schema.counts.enums) enums, $($schema.counts.functions) functions"
}
