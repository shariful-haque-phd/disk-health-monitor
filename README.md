# Disk Health Monitor

Reads JSON output from smartctl and converts the most useful SMART/device-health signals into a concise JSON report.

[Research notes](docs/RESEARCH.md) · [Architecture](docs/ARCHITECTURE.md) · [Execution record](docs/RESULTS.md) · [Project site](docs/index.html)

---

## Research context

Can device-health exports be normalized into interpretable disk-maintenance indicators?

The repository provides an inspectable implementation of **smart/nvme health reporting**. It is an exploratory engineering project; broader effectiveness and practical deployment require further study.

## Implemented capabilities

- SMART/NVMe health reporting

## Architecture

```mermaid
flowchart LR
    A["smartctl.json"] --> B["disk_health.py"]
    B --> C["Console / application output"]
```

The diagram is a simplified view of the supplied implementation. Detailed modules and interface assumptions are in [architecture notes](docs/ARCHITECTURE.md).

## Run locally

**Environment:** Python 3.11+ is the documented baseline. Install optional services or hardware drivers when required.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

Run the following commands from the repository root:

```bash
python src/disk_health.py --json sample/smartctl.json
```

**Input:** `sample/smartctl.json`

## Results

**Executed locally** with the included input files. This is an implementation check, not an independently validated benchmark.

![Output from the local execution](assets/result.svg)

| Observed field | Value |
|:--|--:|
| Temperature c | 39 |
| Power on hours | 2100 |
| Percentage used | 8 |
| Available spare percent | 100 |
| Media errors | 0 |

**Execution evidence:** [Full command transcript](results/execution.txt) · [Inputs and checksums](results/execution.json)

**Saved outputs**

- The command writes its results to standard output. See the transcript.

The values above come from the bundled fixtures. Model scores, simulated costs, and resource-use estimates should not be interpreted as real-world deployment results.

## Source structure

- [`src/disk_health.py`](src/disk_health.py)

Documentation is in [`docs/`](docs/). Bundled inputs remain in their original folders. The original project instructions are archived in [`docs/ORIGINAL_README.md`](docs/ORIGINAL_README.md).

## Limits and next research steps

- Results shown here are from local bundled inputs; they are not published research findings or evidence of external deployment.
- Validate domain assumptions and compare against a documented baseline before making performance or reliability claims.
- Extend testing to larger, independently sourced datasets and report reproducibility, failures and relevant ethical risks.

For the methodology and evaluation design, see [the research brief](docs/RESEARCH.md).

## License

See [`LICENSE`](LICENSE). No affiliation, patent, publication, production deployment or independent endorsement is implied.
