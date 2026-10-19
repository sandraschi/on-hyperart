# Install — on-hyperart

Book repo, not a service. Static reader on registered port **11156**
(`just serve`). Not a daemon.

```powershell
# read
Get-Content README.md
Get-Content PRD.md

# lore check (stdlib only)
py -3 tools/lorecheck.py

# read-aloud gate (Windows SAPI fallback, no key needed)
just declaim chapters/01-the-misdirection.md

# static reader
just build
just serve
```

Requires: Python 3.11+, `just` (sisters' justfile syntax).
Optional: GOOGLE_API_KEY for Gemini TTS voice in declaim.
