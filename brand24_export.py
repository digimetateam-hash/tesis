#!/usr/bin/env python3
"""
Ekspor data Brand24 untuk tesis MBG (periode 2 Maret – 24 Mei 2026).

Pemakaian (dari folder repo):
    python3 brand24_export.py                 -> menampilkan daftar proyek Brand24 (ID dan nama)
    python3 brand24_export.py --project 12345 -> mengunduh data proyek itu ke data/brand24/

Kunci API dibaca dari variabel lingkungan BRAND24_API_KEY atau file .env
(baris BRAND24_API_KEY=...). Kunci tidak pernah dicetak atau disimpan ke file hasil.
"""
import argparse, json, os, sys, time
from datetime import date, timedelta
import requests

BASE = "https://api-data.brand24.com/api-data/v1"
ACCOUNT_ID = 614604830
DATE_FROM, DATE_TO = date(2026, 3, 2), date(2026, 5, 24)
OUT = os.path.join("data", "brand24")


def api_key():
    k = os.environ.get("BRAND24_API_KEY", "").strip()
    if not k:
        for d in (os.getcwd(), os.path.dirname(os.path.abspath(__file__))):
            p = os.path.join(d, ".env")
            if os.path.exists(p):
                for line in open(p, encoding="utf-8"):
                    if line.strip().startswith("BRAND24_API_KEY="):
                        k = line.split("=", 1)[1].strip().strip("'\"")
                        break
            if k:
                break
    if not k or k == "your_brand24_api_key_here":
        sys.exit("BRAND24_API_KEY tidak ditemukan. Isi di file .env: BRAND24_API_KEY=kunci_anda")
    return k


KEY = api_key()


def get(path, params=None):
    for attempt in range(4):
        r = requests.get(BASE + path, headers={"X-Api-Key": KEY, "Accept": "application/json"}, params=params, timeout=60)
        if r.status_code == 429:
            time.sleep(5 * (attempt + 1)); continue
        if r.status_code != 200:
            print(f"  ! {r.status_code} pada {path} {params or ''}: {r.text[:300]}")
            return None
        j = r.json()
        return j.get("message", j)
    return None


def save(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(f"  -> {OUT}/{name}")


def chunks(step_days):
    a = DATE_FROM
    while a <= DATE_TO:
        b = min(a + timedelta(days=step_days - 1), DATE_TO)
        yield a, b
        a = b + timedelta(days=1)


ap = argparse.ArgumentParser()
ap.add_argument("--project", type=int)
a = ap.parse_args()

if not a.project:
    pr = get(f"/account/{ACCOUNT_ID}/projects_list/")
    print(json.dumps(pr, ensure_ascii=False, indent=1)[:4000])
    print("\nPilih ID proyek MBG di atas, lalu jalankan: python3 brand24_export.py --project <ID>")
    sys.exit()

P = a.project
rng = {"date_from": DATE_FROM.isoformat(), "date_to": DATE_TO.isoformat()}
print(f"Proyek {P}, periode {DATE_FROM} s.d. {DATE_TO}")

# 1. Daftar mention (cursor pagination, dipecah per 14 hari agar tidak melewati batas rentang paket)
rows = []
for d1, d2 in chunks(14):
    cur = None
    while True:
        prm = {"date_from": d1.isoformat(), "date_to": d2.isoformat(), "limit": 500}
        if cur: prm["cursor"] = cur
        m = get(f"/project/{P}/mentions", prm)
        if not m: break
        rows += m.get("results", [])
        cur = m.get("cursor")
        if not cur or not m.get("has_more_mentions", True): break
    print(f"  mention {d1}..{d2}: total sementara {len(rows)}")
save("mentions.json", rows)
try:
    import pandas as pd
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "mentions.csv"), index=False)
    print(f"  -> {OUT}/mentions.csv")
except Exception as e:
    print("  (pandas tidak tersedia, CSV dilewati)", e)

# 2. Ringkasan dan akun berpengaruh
for name, path, extra in [
    ("count.json", f"/project/{P}/mentions/count", {}),
    ("reach.json", f"/project/{P}/mentions/reach", {}),
    ("sentiment.json", f"/project/{P}/mentions/sentiment", {}),
    ("most_followers_by_followers.json", f"/project/{P}/most-followers", {"sort_by": "followers_count"}),
    ("most_followers_by_mentions.json", f"/project/{P}/most-followers", {"sort_by": "mentions_count"}),
]:
    print(name); r = get(path, {**rng, **extra})
    if r is not None: save(name, r)
print("daily_metrics.json"); r = get(f"/project/{P}/daily-metrics", {"from": rng["date_from"], "to": rng["date_to"], "includeBySource": "true"})
if r is not None: save("daily_metrics.json", r)

# 3. Pencocokan dengan korpus NodeXL (berdasarkan Tweet-ID dan nama akun)
try:
    import pandas as pd
    D = pd.read_csv(os.path.join("data", "indobert_9_emosi_fixed.csv"), low_memory=False)
    ids = set(D["id"].dropna().astype("int64").astype(str))
    tw = [str(x.get("source", "")).split(":", 1)[1].strip() for x in rows if str(x.get("source", "")).startswith("Tweet-ID")]
    both = ids & set(tw)
    users = set(D["author_username"].astype(str).str.lower())
    auth = []
    for fn in ("most_followers_by_followers.json", "most_followers_by_mentions.json"):
        p = os.path.join(OUT, fn)
        if os.path.exists(p):
            auth += json.load(open(p, encoding="utf-8")).get("authors", [])
    au = {str(x.get("url", "")).rstrip("/").split("/")[-1].lower() for x in auth}
    rep = {"mention_brand24": len(rows), "mention_twitter_brand24": len(tw), "unggahan_korpus": len(ids),
           "tweet_id_cocok": len(both), "akun_berpengaruh_brand24": len(au), "akun_berpengaruh_ada_di_korpus": len(au & users)}
    save("pencocokan_korpus.json", rep); print(json.dumps(rep, indent=1))
except Exception as e:
    print("Pencocokan dilewati:", e)
print("Selesai.")
