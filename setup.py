#!/usr/bin/env python3
"""skill-suite-setup — build customer-specific deliveries of the skill suite.

Zero dependencies (Python >= 3.10). See documentation/setup-skill-design.md in skill-suite-dev.

    setup.py new    <customer> [--customer-dir DIR] [--code X] [--language en|de]
    setup.py check  <customer> [--customer-dir DIR] [--suites DIR]
    setup.py build  <customer> [--customer-dir DIR] [--suites DIR] [--out DIR] [--force]
    setup.py prompt <customer> idea-collect [--customer-dir DIR] [--suites DIR] [--out DIR]
    setup.py list   [--customer-dir DIR]
"""
from __future__ import annotations
import argparse, datetime, io, re, sys, zipfile
from pathlib import Path
import guard

HERE = Path(__file__).resolve().parent
# What ships from a skillset — an allowlist, never "everything minus a strip list". Anything else is reported, not shipped.
SHIP = ("VERSION", "RULES.md", "QUESTIONS.md", "README.md", "CHANGELOG.md", "LICENSE", "ATTRIBUTION.md", "MANIFEST.md",
        "LICENSES/*", "checklists/*.md", "templates/*.md", "skills/*/SKILL.md")
NOT_SHIPPED_SILENTLY = {"AGENTS.md", "CLAUDE.md", "START.md", ".gitignore", ".DS_Store", "profile/README.md", "hooks/pre-commit", "ideas/.gitkeep", "maquettes/.gitkeep", "builds/.gitkeep"}

def ship_files(base: Path) -> tuple[list[Path], list[Path]]:
    """(files to ship, files present but not shipped and not expected — for the report)."""
    shipped = set()
    for pat in SHIP:
        shipped.update(f for f in base.glob(pat) if f.is_file())
    others = [f for f in base.rglob("*") if f.is_file() and f not in shipped and f.name != ".DS_Store"
              and ".git" not in f.parts and "examples" not in f.parts and f.relative_to(base).as_posix() not in NOT_SHIPPED_SILENTLY]
    return sorted(shipped), sorted(others)
SKILLSETS = ("idea", "maquette", "build")
PLATFORM_HINTS = {
    "en": {
        "cowork": "**Claude (Cowork):** new task → connect folder → select the folder. Claude reads `CLAUDE.md` automatically.",
        "chatgpt-codex": "**ChatGPT app (Codex mode):** \"Open project\" → select the folder. Codex reads `AGENTS.md` automatically.",
        "vibe-cli": "**Mistral Vibe CLI:** change into the folder in a terminal and start `vibe`. It reads `AGENTS.md` automatically.",
        "other": "Open the folder in your AI app; it must be able to read and write files in it. Then say: \"Read AGENTS.md and begin.\"",
    },
    "de": {
        "cowork": "**Claude (Cowork):** neue Aufgabe → Ordner verbinden → den Ordner wählen. Claude liest `CLAUDE.md` automatisch.",
        "chatgpt-codex": "**ChatGPT-App (Codex-Modus):** „Projekt öffnen“ → den Ordner wählen. Codex liest `AGENTS.md` automatisch.",
        "vibe-cli": "**Mistral Vibe CLI:** im Terminal in den Ordner wechseln und `vibe` starten. Es liest `AGENTS.md` automatisch.",
        "other": "Öffnen Sie den Ordner in Ihrer KI-Anwendung; sie muss darin Dateien lesen und schreiben können. Dann sagen Sie: „Lies AGENTS.md und beginne.“",
    },
}

# ---------- tiny YAML subset: flat keys, [a, b] lists, one nesting level ----------
def load_yaml(path: Path) -> dict:
    data: dict = {}
    current: dict | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indented = line.startswith("  ")
        key, _, val = line.strip().partition(":")
        val = val.strip()
        if indented and current is not None:
            current[key] = _scalar(val)
        elif val == "":
            current = {}
            data[key] = current
        else:
            current = None
            data[key] = _scalar(val)
    return data

def _scalar(v: str):
    if v.startswith("[") and v.endswith("]"):
        return [x.strip() for x in v[1:-1].split(",") if x.strip()]
    if v.isdigit():
        return int(v)
    return v.strip('"').strip("'")

def dump_yaml(data: dict) -> str:
    out = []
    for k, v in data.items():
        if isinstance(v, dict):
            out.append(f"{k}:")
            out += [f"  {a}: {b}" for a, b in v.items()]
        elif isinstance(v, list):
            out.append(f"{k}: [{', '.join(v)}]")
        else:
            out.append(f"{k}: {v}")
    return "\n".join(out) + "\n"

# ---------- helpers ----------
def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr); sys.exit(1)

def customer_dir(args) -> Path:
    base = Path(args.customer_dir).expanduser() if args.customer_dir else HERE / "customers"
    return base / args.customer

def suites_dir(args) -> Path:
    return Path(args.suites).expanduser() if args.suites else HERE.parent

def render(text: str, ctx: dict) -> str:
    for k, v in ctx.items():
        text = text.replace("{{" + k + "}}", str(v))
    left = re.findall(r"\{\{(\w+)\}\}", text)
    if left:
        die(f"unrendered placeholders: {sorted(set(left))}")
    return text

def read_compat() -> list[dict]:
    rows = []
    for line in (HERE / "compat.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not line.startswith("| ---") and not line.startswith("| setup"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.append(dict(zip(["setup", "idea", "maquette", "build", "H1", "H2", "tested", "note"], cells)))
    return rows

def question_ids(suite_path: Path) -> set[str]:
    ids = set()
    for line in (suite_path / "QUESTIONS.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not line.startswith("| ---") and not line.startswith("| #"):
            first = line.strip("|").split("|")[0].strip().strip("*")
            if first and first not in ("Gate", "Question", "Skillset"):
                ids.add(first)
    return ids

def profile_questions(cust: Path) -> list[dict]:
    p = cust / "profile" / "questions.md"
    rows = []
    if not p.exists():
        return rows
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not line.startswith("| ---") and not line.startswith("| Skillset"):
            c = [x.strip() for x in line.strip("|").split("|")]
            if len(c) >= 4 and c[0]:
                rows.append({"skillset": c[0], "id": c[1].replace("after", "").strip(), "action": c[2], "value": c[3]})
    return rows

def profile_files(cust: Path) -> list[Path]:
    """Profile files that carry content beyond the template skeleton. profile.md always counts."""
    out = []
    for f in sorted((cust / "profile").glob("*.md")):
        lines = f.read_text(encoding="utf-8").splitlines()
        filled = False
        for i, l in enumerate(lines):
            t = l.strip()
            if not t or t.startswith(("#", "<!--", "| ---")):
                continue
            if "<" in t and ">" in t:            # placeholder
                continue
            if t.endswith(":**"):                # empty bullet
                continue
            if t.startswith("|"):
                if i + 1 < len(lines) and lines[i + 1].startswith("| ---"):
                    continue                     # table header
                cells = [c.strip() for c in t.strip("|").split("|")]
                if not any(cells[1:]):
                    continue                     # row label without content
            filled = True
            break
        if filled or f.name == "profile.md":
            out.append(f)
    return out

# ---------- commands ----------
def cmd_new(args):
    cust = customer_dir(args)
    if cust.exists():
        die(f"{cust} exists")
    compat = read_compat()[0]          # compat.md lists the newest triple first
    ctx = {"customer": args.customer, "code": args.code or args.customer[:3].upper(), "language": args.language,
           "recipient": "<name, role>", "contact": "<name, mail>",
           "v_idea": compat["idea"], "v_maquette": compat["maquette"], "v_build": compat["build"]}
    (cust / "profile").mkdir(parents=True)
    (cust / "customer.yaml").write_text(render((HERE / "templates" / "customer.yaml").read_text(encoding="utf-8"), ctx), encoding="utf-8")
    for t in (HERE / "templates" / "profile").glob("*.md"):
        (cust / "profile" / t.name).write_text(render(t.read_text(encoding="utf-8"), ctx), encoding="utf-8")
    print(f"created {cust} — fill customer.yaml and profile/*.md (skills/setup/SKILL.md guides the dialogue), then: setup.py check {args.customer}")

def load_customer(args) -> tuple[Path, dict]:
    cust = customer_dir(args)
    if not (cust / "customer.yaml").exists():
        die(f"no customer.yaml in {cust}")
    return cust, load_yaml(cust / "customer.yaml")

def cmd_check(args, quiet=False) -> tuple[Path, dict, Path]:
    cust, c = load_customer(args)
    suites = suites_dir(args)
    problems = []
    for s in c["skillsets"]:
        if s not in SKILLSETS:
            problems.append(f"unknown skillset {s}")
            continue
        sp = suites / s
        if not (sp / "VERSION").exists():
            problems.append(f"skillset {s} not found at {sp}"); continue
        have = (sp / "VERSION").read_text().strip()
        want = str(c["versions"].get(s, ""))
        if have != want:
            problems.append(f"{s}: customer.yaml pins {want}, checkout has {have}")
    triple = {k: str(c["versions"].get(k, "-")) for k in SKILLSETS}
    ok = any(all(r[k] == triple[k] for k in SKILLSETS if k in c["skillsets"]) for r in read_compat())
    if not ok:
        problems.append(f"version triple {triple} not in compat.md" + (" (forced)" if getattr(args, "force", False) else ""))
        if not getattr(args, "force", False):
            pass
    for row in profile_questions(cust):
        if row["skillset"] not in c["skillsets"]:
            problems.append(f"questions.md: skillset {row['skillset']} not ordered")
        elif row["action"] not in ("skip", "add"):
            problems.append(f"questions.md: action {row['action']} for {row['id']}")
        elif row["id"] not in question_ids(suites / row["skillset"]):
            problems.append(f"questions.md: unknown question ID {row['skillset']}/{row['id']}")
        elif row["action"] == "skip" and not row["value"]:
            problems.append(f"questions.md: skip {row['id']} needs a value")
    if c.get("language") not in ("en", "de"):
        problems.append(f"language {c.get('language')} — templates exist for en, de")
    fatal = [p for p in problems if not (p.endswith("(forced)"))]
    if problems:
        for p in problems:
            print(("warn: " if p.endswith("(forced)") else "fail: ") + p)
    if fatal:
        sys.exit(1)
    if not quiet:
        print(f"ok: {args.customer} — skillsets {c['skillsets']}, versions {triple}, profile files {[f.name for f in profile_files(cust)]}")
    return cust, c, suites

def cmd_build(args):
    cust, c, suites = cmd_check(args, quiet=True)
    c["build"] = int(c.get("build", 0)) + 1
    today = datetime.date.today().isoformat()
    zipname = f"{c['name']}-suite-v{c['build']}.zip"
    lang = c["language"]
    pfiles = profile_files(cust)
    versions_line = " · ".join(f"{s} {c['versions'][s]}" for s in c["skillsets"])
    ctx = {"customer": c["name"], "code": c["code"], "language": lang, "date": today, "zipname": zipname,
           "skillsets_list": " → ".join(c["skillsets"]), "versions_line": versions_line,
           "contact": c.get("contact", ""), "build": c["build"],
           "platform_hint": "\n\n".join(PLATFORM_HINTS[lang].get(p, PLATFORM_HINTS[lang]["other"]) for p in c.get("platform", ["other"]))}
    out = Path(args.out).expanduser() if args.out else HERE / "dist"
    out.mkdir(parents=True, exist_ok=True)
    root_agents = (HERE / "templates" / "root-AGENTS.md").read_text(encoding="utf-8")
    planning_pointer = (HERE / "templates" / "planning-pointer-AGENTS.md").read_text(encoding="utf-8")
    bootstrap = render((HERE / "templates" / "planning-AGENTS.md").read_text(encoding="utf-8"), ctx)
    start = render((HERE / "templates" / f"start.{lang}.md").read_text(encoding="utf-8"), ctx)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        # everything outside planning/suite and planning/profile is static across builds — an update is `unzip -n`
        z.writestr("AGENTS.md", root_agents); z.writestr("CLAUDE.md", root_agents.replace("AGENTS.md", "CLAUDE.md", 1))
        z.writestr("start.md", start)
        z.writestr("planning/AGENTS.md", planning_pointer)
        z.writestr("planning/CLAUDE.md", planning_pointer.replace("`suite/AGENTS.md`", "`suite/CLAUDE.md`", 1))
        z.writestr("planning/suite/AGENTS.md", bootstrap)
        z.writestr("planning/suite/CLAUDE.md", bootstrap.replace("# AGENTS.md", "# CLAUDE.md", 1))
        z.writestr("planning/suite/VERSION", f"customer={c['name']} · build={c['build']} · {versions_line} · setup={(HERE / 'VERSION').read_text().strip()} · built={today}\n")
        groups = guard.load_markers(guard.markers_path(getattr(args, "markers", None)))
        allow = str(c.get("guard_group", c["name"]))
        for s in c["skillsets"]:
            base = suites / s
            files, others = ship_files(base)
            if others:
                print("not shipped (not on the allowlist): " + ", ".join(str(f.relative_to(base)) for f in others))
            report = guard.scan_files(files, groups)          # suite files: no customer markers of any group
            if report:
                guard.print_report(report); die(f"customer markers in {s} suite files — fix the repo, then build again")
            for f in files:
                z.write(f, f"planning/suite/{s}/{f.relative_to(base).as_posix()}")
            z.writestr(f"planning/{s}/.gitkeep", "")
        for f in pfiles:                                        # profile: header bound to the customer, other groups' markers refused
            first = f.read_text(encoding="utf-8").splitlines()[0] if f.stat().st_size else ""
            if c["name"].lower() not in first.lower():
                die(f"profile file {f.name} does not name customer {c['name']} in its first line ({first!r})")
        report = guard.scan_files(pfiles, groups, allow=allow)
        if report:
            guard.print_report(report, allow); die("profile files carry markers of another customer — refused")
        present = ", ".join(f.name for f in pfiles)
        for f in pfiles:
            text = f.read_text(encoding="utf-8")
            if f.name == "profile.md":
                text = re.sub(r"- \*\*Profile files present:\*\*.*", f"- **Profile files present:** {present}", text)
            z.writestr(f"planning/profile/{f.name}", text)
    (out / zipname).write_bytes(buf.getvalue())
    (out / f"{c['name']}-start.md").write_text(start, encoding="utf-8")
    (cust / "customer.yaml").write_text(dump_yaml(c), encoding="utf-8")
    print(f"built {out / zipname} ({len(buf.getvalue()) // 1024} KB) and {c['name']}-start.md · profile: {present or 'core defaults'}")

HOWTO = {
    "en": "**How to use this file:** open it in a text editor, copy the whole content, paste it into an approved AI chat window, type **start** underneath and send. The AI interviews you about your daily work and writes idea cards; nothing is judged, nothing is dropped. At the end (about 45 minutes) it shows all cards once more — copy them into your reply mail to {{contact}}. Please do not type customer names or other personal data into the chat.",
    "de": "**So verwenden Sie diese Datei:** Öffnen Sie sie mit einem Texteditor, kopieren Sie den gesamten Inhalt, fügen Sie ihn in ein freigegebenes KI-Chatfenster ein, schreiben Sie darunter **start** und senden Sie ab. Die KI führt ein Interview über Ihren Arbeitsalltag und schreibt Ideenkarten; nichts wird bewertet, nichts verworfen. Am Ende (nach etwa 45 Minuten) zeigt sie alle Karten noch einmal — kopieren Sie diese in Ihre Antwort-Mail an {{contact}}. Bitte geben Sie keine Kundennamen oder anderen personenbezogenen Daten in den Chat ein.",
}

def cmd_prompt(args):
    cust, c, suites = cmd_check(args, quiet=True)
    if args.stage != "idea-collect":
        die("only idea-collect has a prompt file")
    skill = (suites / "idea" / "skills" / "idea-collect" / "SKILL.md").read_text(encoding="utf-8")
    body = re.sub(r"^---.*?---\n", "", skill, count=1, flags=re.S)
    card = (suites / "idea" / "templates" / "card.md").read_text(encoding="utf-8")
    scope = cust / "profile" / "scope.md"
    qrows = [r for r in profile_questions(cust) if r["skillset"] == "idea"]
    ctx = {"customer": c["name"], "code": c["code"], "language": c["language"], "contact": c.get("contact", ""),
           "profile_scope": ("## Customer scope\n\n" + scope.read_text(encoding="utf-8")) if scope in profile_files(cust) else "",
           "profile_questions": ("## Tailored questions\n\n" + "\n".join(f"- {r['action']} {r['id']}: {r['value']}" for r in qrows)) if qrows else "",
           "skill_body": body, "card_template": card,
           "address": {"sie": "formal (German: Sie)", "du": "informal (German: du)"}.get(str(c.get("address", "du")).lower(), str(c.get("address", "du"))),
           "howto": HOWTO.get(c["language"], HOWTO["en"]).replace("{{contact}}", str(c.get("contact", "")))}
    out = Path(args.out).expanduser() if args.out else HERE / "dist"
    out.mkdir(parents=True, exist_ok=True)
    p = out / f"{c['name']}-idea-collect-prompt.md"
    p.write_text(render((HERE / "templates" / "prompt-idea-collect.md").read_text(encoding="utf-8"), ctx), encoding="utf-8")
    print(f"wrote {p}")

def cmd_list(args):
    base = Path(args.customer_dir).expanduser() if args.customer_dir else HERE / "customers"
    for d in sorted(base.iterdir()):
        y = d / "customer.yaml"
        if y.exists():
            c = load_yaml(y)
            print(f"{d.name:20s} build {c.get('build', 0)}  {c.get('skillsets')}  {c.get('versions')}")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    def common(p, customer=True):
        if customer:
            p.add_argument("customer")
        p.add_argument("--customer-dir")
        p.add_argument("--suites")
    p = sub.add_parser("new"); common(p); p.add_argument("--code"); p.add_argument("--language", default="en"); p.set_defaults(fn=cmd_new)
    p = sub.add_parser("check"); common(p); p.add_argument("--force", action="store_true"); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("build"); common(p); p.add_argument("--out"); p.add_argument("--force", action="store_true"); p.add_argument("--markers"); p.set_defaults(fn=cmd_build)
    p = sub.add_parser("prompt"); common(p); p.add_argument("stage"); p.add_argument("--out"); p.set_defaults(fn=cmd_prompt)
    p = sub.add_parser("list"); common(p, customer=False); p.set_defaults(fn=cmd_list)
    args = ap.parse_args()
    args.fn(args)

if __name__ == "__main__":
    main()
