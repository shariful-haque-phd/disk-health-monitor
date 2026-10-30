# Execution record — Disk Health Monitor

**Status:** Local execution completed using bundled fixtures.  
**Python:** 3.13.5  
**Execution time:** 1.63 seconds in the packaging environment (not a standardized benchmark).  
**Method:** `python src/disk_health.py --json sample/smartctl.json`

## Observed output

![Observed output](../assets/result.svg)

| Field | Observed value |
|:--|--:|
| Temperature c | 39 |
| Power on hours | 2100 |
| Percentage used | 8 |
| Available spare percent | 100 |
| Media errors | 0 |

**Raw output:** [execution.txt](../results/execution.txt)  
**Command records and SHA-256 digests:** [execution.json](../results/execution.json)

## Interpretation

Results were computed on the included test fixtures. They demonstrate one successful invocation, not measured generalization, comparative performance, system availability or operational readiness. If the fixtures or application are synthetic, values remain synthetic or simulated.
