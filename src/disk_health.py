import argparse, json, subprocess
from pathlib import Path

def extract(d):
    temp=(d.get("temperature") or {}).get("current")
    poh=(d.get("power_on_time") or {}).get("hours")
    smart=d.get("smart_status",{}).get("passed")
    nvme=d.get("nvme_smart_health_information_log",{})
    return {
        "model":d.get("model_name") or d.get("model_family"),
        "serial_number":d.get("serial_number"),
        "smart_passed":smart,
        "temperature_c":temp,
        "power_on_hours":poh,
        "percentage_used":nvme.get("percentage_used"),
        "available_spare_percent":nvme.get("available_spare"),
        "media_errors":nvme.get("media_errors"),
        "unsafe_shutdowns":nvme.get("unsafe_shutdowns"),
    }

def live(device):
    cp=subprocess.run(["smartctl","-a","-j",device],capture_output=True,text=True,check=False)
    if not cp.stdout.strip():
        raise RuntimeError(cp.stderr.strip() or "smartctl produced no JSON output")
    return json.loads(cp.stdout)

def main():
    ap=argparse.ArgumentParser(); g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--device"); g.add_argument("--json"); a=ap.parse_args()
    d=live(a.device) if a.device else json.loads(Path(a.json).read_text())
    print(json.dumps(extract(d),indent=2))
if __name__=="__main__": main()
