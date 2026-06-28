param(
    [string]$RepoUrl = "https://github.com/BohemiaInteractive/Arma-Reforger-Samples.git",
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

$skillRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$rawRoot = Join-Path $skillRoot "raw"
$samplesPath = Join-Path $rawRoot "samples"

New-Item -ItemType Directory -Force -Path $rawRoot | Out-Null

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "git is required to update Arma Reforger samples."
}

$resolvedRawRoot = (Resolve-Path $rawRoot).Path

if (Test-Path $samplesPath) {
    $resolvedSamples = (Resolve-Path $samplesPath).Path
    if (-not $resolvedSamples.StartsWith($resolvedRawRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to update samples outside raw folder: $resolvedSamples"
    }

    if (-not (Test-Path (Join-Path $samplesPath ".git"))) {
        throw "Samples path exists but is not a git repository: $samplesPath"
    }

    git -C $samplesPath fetch origin $Branch
    git -C $samplesPath reset --hard "origin/$Branch"
    git -C $samplesPath clean -fdx
} else {
    git clone --branch $Branch $RepoUrl $samplesPath
}

$commit = git -C $samplesPath rev-parse HEAD
$remote = git -C $samplesPath remote get-url origin

Write-Host "Updated Arma Reforger samples"
Write-Host "Path: $samplesPath"
Write-Host "Remote: $remote"
Write-Host "Branch: $Branch"
Write-Host "Commit: $commit"
