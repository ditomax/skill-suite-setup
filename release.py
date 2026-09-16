#!/usr/bin/env python3
"""release — build the public release ZIP of one skillset repo, guarded.

    release.py <idea|maquette|build> [--suites DIR] [--out DIR] [--markers FILE]

Ships only files that git tracks AND that are on the allowlist (setup.py SHIP + the standalone bootstraps).
Refuses if the work folder holds anything but .gitkeep, or if any shipped file carries a customer marker.
"""
from __future__ import annotations
import argparse, io, subprocess, sys, zipfile
from pathlib import Path
import guard
from setup import SHIP, ship_files, die

HERE = Path(__file__).resolve().parent
STANDALONE = {"AGENTS.md", "CLAUDE.md", "START.md", ".gitignore", "profile/README.md"}
WORK = {"idea": "ideas", "maquette": "maquettes", "build": "builds"}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skillset", choices=list(WORK)); ap.add_argument("--suites"); ap.add_argument("--out"); ap.add_argument("--markers")
    a = ap.parse_args()
    base = (Path(a.suites).expanduser() if a.suites else HERE.parent) / a.skillset
    version = (base / "VERSION").read_text().strip()
    work = base / WORK[a.skillset]
    stray = [f for f in work.rglob("*") if f.is_file() and f.name != ".gitkeep"] if work.exists() else []
    if stray:
        die(f"work folder {work.name}/ is not empty ({len(stray)} files) — test runs belong under tests/, never in the dev copy")
    tracked = set(subprocess.run(["git", "ls-files"], cwd=base, capture_output=True, text=True, check=True).stdout.split())
    shipped, _ = ship_files(base)
    wanted = {f.relative_to(base).as_posix() for f in shipped} | STANDALONE | {f"{WORK[a.skillset]}/.gitkeep"}
    files = sorted(wanted & tracked)
    untracked = sorted(wanted - tracked - {".gitignore"})
    if untracked:
        print("warning: on the allowlist but not tracked by git (not shipped, commit first?): " + ", ".join(untracked))
    groups = guard.load_markers(guard.markers_path(a.markers))
    report = guard.scan_files([base / f for f in files], groups)
    if report:
        guard.print_report(report); die("customer markers in release files — refused")
    out = Path(a.out).expanduser() if a.out else HERE / "dist"; out.mkdir(parents=True, exist_ok=True)
    zpath = out / f"{a.skillset}-v{version}.zip"
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(base / f, f"{a.skillset}/{f}")
    zpath.write_bytes(buf.getvalue())
    print(f"built {zpath} ({len(buf.getvalue()) // 1024} KB, {len(files)} files) — guard clean")

if __name__ == "__main__":
    main()
