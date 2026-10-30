# Architecture — Disk Health Monitor

```mermaid
flowchart LR
    A["smartctl.json"] --> B["disk_health.py"]
    B --> C["Console / application output"]
```

## Inputs

- `sample/smartctl.json`

## Source files

- `src/disk_health.py`

## Output



This representation is intended for source navigation. It does not imply a production deployment or undisclosed components. The editable diagram is available as [`architecture.mmd`](architecture.mmd).
