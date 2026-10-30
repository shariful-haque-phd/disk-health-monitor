# Disk Health Monitor

Reads JSON output from `smartctl` and converts the most useful SMART/device-health signals into a concise JSON report.

## Requirements
Python has no direct dependency, but live collection requires **smartmontools** and appropriate operating-system permissions.

## Live usage
```bash
python src/disk_health.py --device /dev/sda
```

## Offline/sample usage
```bash
python src/disk_health.py --json sample/smartctl.json
```

The tool reports device-reported health indicators. It does not guarantee that a disk will or will not fail.
