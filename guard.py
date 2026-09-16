#!/usr/bin/env python3
"""guard — customer-data guard for the skill suite.

Scans files for markers from a private list (default: ../guard-markers.txt, i.e. skill-suite-dev/guard-markers.txt;
override with --markers or SUITE_GUARD_MARKERS). Exit 1 on any hit outside the allowed group.

    guard.py scan <path>... [--allow GROUP] [--markers FILE]     files or folders (recursive, text files only)
    guard.py staged [--markers FILE]                              the files staged in the current git repo (pre-commit)
"""
from __future__ import annotations
import argparse, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_EXT = {".md", ".txt", ".yaml", ".yml", ".py", ".sh", ".html", ".js", ".css", ".json", ".csv", ""}
SKIP_DIRS = {".git", "__pycache__", "node_modules"}

def markers_path(explicit: str | None) -> Path:
    for cand in (explicit, os.environ.get("SUITE_GUARD_MARKERS"), HERE.parent / "guard-markers.txt"):
        if cand and Path(cand).exists():
            return Path(cand)
    sys.exit("guard: no marker list found — expected skill-suite-dev/guard-markers.txt, --markers or SUITE_GUARD_MARKERS")

def load_markers(path: Path) -> dict[str, list[re.Pattern]]:
    groups: dict[str, list[re.Pattern]] = {}
    group = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            group = line[1:-1].strip().lower(); groups.setdefault(group, []); continue
        if group is None:
            sys.exit(f"guard: marker before any [group] in {path}")
        pat = line[3:] if line.startswith("re:") else r"(?<!\w)" + re.escape(line) + r"(?!\w)"
        groups[group].append(re.compile(pat, re.IGNORECASE))
    return groups

def scan_text(text: str, groups: dict[str, list[re.Pattern]], allow: str | None = None) -> list[tuple[str, str, int]]:
    hits = []
    for g, pats in groups.items():
        if allow and g == allow.lower():
            continue
        for p in pats:
            for m in p.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                hits.append((g, m.group(0), line))
    return hits

def iter_files(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file() and not (set(f.relative_to(p).parts) & SKIP_DIRS) and f.suffix.lower() in TEXT_EXT:
                    yield f
        elif p.is_file():
            yield p

def scan_files(files, groups, allow=None, marker_file: Path | None = None) -> dict[str, list]:
    report = {}
    for f in files:
        f = Path(f)
        if marker_file and f.resolve() == marker_file.resolve():
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        hits = scan_text(text, groups, allow)
        if hits:
            report[str(f)] = hits
    return report

def print_report(report: dict, allow=None) -> int:
    if not report:
        print(f"guard: clean" + (f" (allowed group: {allow})" if allow else ""))
        return 0
    for f, hits in report.items():
        seen = sorted({(g, m) for g, m, _ in hits})
        lines = sorted({l for _, _, l in hits})[:5]
        print(f"guard: HIT {f} — " + ", ".join(f"{m} [{g}]" for g, m in seen) + f" (lines {', '.join(map(str, lines))}{'…' if len(hits) > 5 else ''})")
    print(f"guard: {len(report)} file(s) with customer markers — refused")
    return 1

def cmd_scan(args):
    mp = markers_path(args.markers); groups = load_markers(mp)
    return print_report(scan_files(iter_files(args.paths), groups, args.allow, mp), args.allow)

def cmd_staged(args):
    mp = markers_path(args.markers); groups = load_markers(mp)
    names = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"], capture_output=True, text=True, check=True).stdout.split()
    report = {}
    for n in names:
        if Path(n).suffix.lower() not in TEXT_EXT:
            continue
        blob = subprocess.run(["git", "show", f":{n}"], capture_output=True, text=True)
        if blob.returncode != 0:
            continue
        hits = scan_text(blob.stdout, groups)
        if hits:
            report[n] = hits
    return print_report(report)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("scan"); p.add_argument("paths", nargs="+"); p.add_argument("--allow"); p.add_argument("--markers"); p.set_defaults(fn=cmd_scan)
    p = sub.add_parser("staged"); p.add_argument("--markers"); p.set_defaults(fn=cmd_staged)
    args = ap.parse_args()
    sys.exit(args.fn(args))

if __name__ == "__main__":
    main()
