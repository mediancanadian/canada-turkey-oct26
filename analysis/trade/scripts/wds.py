"""Minimal Statistics Canada Web Data Service (WDS) client.
Uses only a generic user agent. No personal details are sent.
Docs: https://www.statcan.gc.ca/en/developers/wds/user-guide
"""
import json, time, urllib.request

URL = "https://www150.statcan.gc.ca/t1/wds/rest/getDataFromCubePidCoordAndLatestNPeriods"
UA = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}


def pad(coord):
    parts = coord.split(".")
    return ".".join(parts + ["0"] * (10 - len(parts)))


def fetch(pid, coords, latest_n, batch=100, pause=0.3):
    """Return dict coord -> list of (refPer 'YYYY-MM', value or None)."""
    out = {}
    coords = [pad(c) for c in coords]
    for i in range(0, len(coords), batch):
        chunk = coords[i:i + batch]
        body = json.dumps([{"productId": pid, "coordinate": c, "latestN": latest_n} for c in chunk]).encode()
        for attempt in range(5):
            try:
                req = urllib.request.Request(URL, data=body, headers=UA, method="POST")
                with urllib.request.urlopen(req, timeout=120) as r:
                    res = json.load(r)
                break
            except Exception as e:  # retry on transient network errors
                print("retry", attempt, e)
                time.sleep(3 * (attempt + 1))
        else:
            raise RuntimeError("WDS failed for chunk starting %d" % i)
        for o in res:
            ob = o["object"]
            if o["status"] != "SUCCESS":
                continue
            out[ob["coordinate"]] = [(p["refPer"][:7], p["value"]) for p in ob["vectorDataPoint"]]
        time.sleep(pause)
    return out
