@echo off
REM on-hyperart reader — mirrors sisters (hyperwar / takeover)
py -3 tools\build_site.py
py -3 -m http.server 10968 --bind 127.0.0.1 --directory site
