"""Fetch public-domain plates from Wikimedia Commons.

Searches Commons, picks the first file with a PD licence claim, downloads it,
and writes CREDITS.md alongside. Stdlib only.

Usage: py fetch_plates.py <outdir>
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "on-hyperart-layout/0.1 (book production; contact sandraschipal@gmail.com)"}

WANTED = [
    ("fuseli_nightmare", "Fuseli Nightmare 1781"),
    ("waterhouse_mermaid", "Waterhouse A Mermaid 1900"),
    ("klimt_water_serpents", "Klimt Water Serpents I 1904"),
    ("blake_red_dragon", "William Blake Great Red Dragon Woman Clothed with the Sun"),
]


def api(params: dict) -> dict:
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def search(term: str) -> list[str]:
    data = api({
        "action": "query", "list": "search", "srsearch": term,
        "srnamespace": "6", "srlimit": "8",
    })
    return [hit["title"] for hit in data.get("query", {}).get("search", [])]


def info(title: str) -> dict | None:
    data = api({
        "action": "query", "titles": title, "prop": "imageinfo",
        "iiprop": "url|extmetadata|size", "iiurlwidth": "1600",
    })
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        infos = page.get("imageinfo") or []
        if infos:
            return infos[0]
    return None


def lic_ok(meta: dict) -> bool:
    blob = " ".join(str(v.get("value", "")) for v in meta.values()).lower()
    return "public domain" in blob or "pd-" in blob or "cc0" in blob


def main() -> int:
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    credits = ["# Plate credits", ""]
    for slug, term in WANTED:
        print(f"search: {term}")
        picked = None
        for title in search(term):
            inf = info(title)
            if not inf:
                continue
            meta = inf.get("extmetadata", {})
            if lic_ok(meta):
                picked = (title, inf, meta)
                break
        if not picked:
            print(f"  no PD hit for {term}")
            continue
        title, inf, meta = picked
        url = inf.get("thumburl") or inf.get("url")
        ext = os.path.splitext(urllib.parse.urlparse(url).path)[1] or ".jpg"
        path = os.path.join(outdir, slug + ext)
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=120) as r, open(path, "wb") as fh:
            fh.write(r.read())
        def m(key: str) -> str:
            return re.sub(r"<[^>]+>", "", str(meta.get(key, {}).get("value", ""))).strip()
        credits.append(
            f"- **{m('ObjectName') or title}** — {m('Artist')}. {m('DateTimeOriginal')}. "
            f"{m('LicenseShortName')}. Source: {inf.get('descriptionurl')}. "
            f"File: `{os.path.basename(path)}`"
        )
        print(f"  saved {path} ({os.path.getsize(path)} bytes) [{m('LicenseShortName')}]")
    with open(os.path.join(outdir, "CREDITS.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(credits) + "\n")
    print("credits written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
