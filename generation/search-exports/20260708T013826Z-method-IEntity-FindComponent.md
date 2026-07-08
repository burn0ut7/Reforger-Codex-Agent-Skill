# Reforger Search Export

Human review artifact only. The query script does not read this file, indexes do not depend on it, and Codex must not use it as source truth.

## Inputs

- Command: `method`
- Command line: `py -3 scripts/query-reforger-data.py method IEntity FindComponent --human-log --limit 1`
- Working directory: `C:\Users\Gray\Documents\VS\Reforger-Codex-Agent-Skill`
- Game-data commit: `2735631ce1400eaf9f1761c66cdee10c46921d37`
- Indexes scanned: `symbols`
- Limit: `1`
- Filters: `{"generatedOnly": false, "handwrittenOnly": false, "kind": null, "module": null, "topic": null}`

## Results

- Total matches before limit: `3`
- Returned results: `1`

## Output

```text
[reforger-query] matches: 1 returned / 3 total

1.
method IEntity.FindComponent
  signature: proto external Managed FindComponent(typename typeName);
  modifiers: proto, external
  docs: Finds first occurance of the coresponding component. \param typeName type of the component
  source: scripts/Core/generated/Entities/IEntity.c:524
  generated: true
```
