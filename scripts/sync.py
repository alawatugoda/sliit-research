#!/usr/bin/env python3
"""
Sync staff publication stats from OpenAlex.
Reads data/members.json, updates works_count / cited_by_count / h_index / last_synced.
"""
import json, time, datetime, pathlib, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).parent.parent
MEMBERS_FILE = ROOT / "data" / "members.json"
MAILTO = "research@sliit.lk"

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"SLIIT-Research-Sync/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def main():
    members = json.loads(MEMBERS_FILE.read_text())
    updated = 0

    for m in members:
        oa_id = m.get("openalex_id")
        if not oa_id:
            continue
        url = f"https://api.openalex.org/authors/{oa_id}?mailto={MAILTO}"
        try:
            data = fetch_json(url)
            m["works_count"]     = data.get("works_count")
            m["cited_by_count"]  = data.get("cited_by_count")
            m["h_index"]         = (data.get("summary_stats") or {}).get("h_index")
            m["last_synced"]     = datetime.datetime.utcnow().isoformat() + "Z"
            updated += 1
            print(f"  ✓ {m['name']}  —  {m['works_count']} works, {m['cited_by_count']} citations")
        except Exception as e:
            print(f"  ✗ {m['name']}  ({oa_id}): {e}")
        time.sleep(0.5)  # be polite to the API

    MEMBERS_FILE.write_text(json.dumps(members, indent=2, ensure_ascii=False))
    print(f"\nDone. {updated}/{len(members)} members synced.")

if __name__ == "__main__":
    main()
