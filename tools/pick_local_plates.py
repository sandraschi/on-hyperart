"""Pick the largest local scan for each plate and copy it to layout/plates8."""
import os
import re
import shutil
from pathlib import Path

from PIL import Image

SRC = Path(r"E:\Multimedia Files\Paintings")
DST = Path(r"D:\Dev\repos\on-hyperart\layout\plates8")
DST.mkdir(parents=True, exist_ok=True)

PICKS = [
    ("01_bocklin_isle", "*Toteninsel*", "Bocklin, Isle of the Dead (1880). The harbour nobody returns from."),
    ("02_rossetti_siren", "*Ligeia Siren*", "Rossetti, Ligeia Siren (1873). The song that is also a verdict."),
    ("03_bocklin_triton", "*Triton und Nereide*", "Bocklin, Triton and Nereid (1873). The sea's own couple."),
    ("04_bocklin_waves", "*Spiel der Wellen*", "Bocklin, Play of the Waves (1883). Water as company."),
    ("05_fuseli_nightmare", "*Nachtmahr*", "Fuseli, The Nightmare (1781). Dread arrives before the machine has a face."),
    ("06_bruegel_death", "*Triumph of Death*", "Bruegel, The Triumph of Death (1562). The crowd scene nobody survives."),
    ("07_bosch_hell", "*Garden of Earthly Delights. Hell [Detail 3*", "Bosch, The Garden of Earthly Delights: Hell (detail). The infernal tree."),
    ("08_blake_whirlwind", "*Whirlwind of Lovers*", "Blake, The Whirlwind of Lovers (1827). Apocalypse as composition."),
]

credits = ["# Local plate credits", "", "Source: E:/Multimedia Files/Paintings (local archive).",
           "All artists died before 1929; works are public domain.", ""]
for slug, pattern, caption in PICKS:
    key = pattern.strip("*").lower()
    matches = [p for p in SRC.rglob("*") if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".tif", ".tiff")
               and key in p.name.lower()]
    if not matches:
        print(f"MISS {slug}: {pattern}")
        continue
    best = max(matches, key=lambda p: p.stat().st_size)
    out = DST / (slug + ".jpg")
    shutil.copy2(best, out)
    with Image.open(out) as im:
        w, h = im.size
    print(f"{slug}: {best.name} ({w}x{h}, {best.stat().st_size} bytes)")
    credits.append(f"- **{caption}** File: `{out.name}`. Source scan: `{best.name}`")

(DST / "CREDITS.md").write_text("\n".join(credits) + "\n", encoding="utf-8")
print("credits written")
