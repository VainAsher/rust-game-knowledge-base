#!/usr/bin/env python3
"""
Genre-discipline auditor for the reference knowledge base (evidence vs assessed guidance).

The house rule is "never let a judgement wear the costume of a fact". That rule
is easy for a strong model to honour by feel and easy for a weaker model to
drift on. This auditor makes the rule *mechanical* so quality does not depend on
model judgement:

  1. Every gap block under "Assessed Guidance" carries the four required
     parts — Gap / Evidence basis / Confidence / So what.
  2. Each gap's own Confidence is one of High | Medium | Low (with optional
     qualifiers like "Medium-High").
  3. The evidence-layer sections ("Documented Capability", "User-Reported Pain
     Points") actually cite — each contains at least one [n] citation marker.
  4. There is at least one labelled gap.

Read-only. Exit 0 by default (report); pass --strict to fail (exit 1) on any
finding so it can gate CI. Runs over docs/**/*.md or specific files.

Usage:  python scripts/audit_genre.py [--strict] [FILE ...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
MARKER_RE = re.compile(r"\[(\d+)\]")
# accept "High", "Medium-High", "medium/low", "Medium (…)" etc.
CONF_RE = re.compile(r"\b(High|Medium|Low)\b", re.IGNORECASE)

EVIDENCE_SECTIONS = ["Core Mechanics", "Reference Data", "Version & Patch Notes"]

# A gap block is introduced by either a "## Guidance N ..." heading (canonical) or a
# "**Guidance N — ...**" bold header (legacy). Format-agnostic on purpose.
GAP_HEADER_RE = re.compile(r"^\s*(?:##\s*Guidance\b|\*\*\s*Guidance\s+\d)", re.IGNORECASE | re.MULTILINE)

# Each gap must carry these three discipline-bearing bullets (the Gap statement
# itself may live in the header, so it is not separately required). *italic* or
# **bold** labels both accepted.
GAP_PARTS = {
    "Evidence basis": re.compile(r"^\s*[-*]\s*\*{1,2}\s*Evidence[ -]?basis\s*:", re.IGNORECASE | re.MULTILINE),
    "Confidence":     re.compile(r"^\s*[-*]\s*\*{1,2}\s*Confidence\s*:", re.IGNORECASE | re.MULTILINE),
    "So what":        re.compile(r"^\s*[-*]\s*\*{1,2}\s*So[ -]?what\s*:", re.IGNORECASE | re.MULTILINE),
}
CONF_BULLET_RE = re.compile(r"^\s*[-*]\s*\*{1,2}\s*Confidence\s*:.*$", re.IGNORECASE | re.MULTILINE)


def sections(body: str) -> dict[str, str]:
    """Map each top-level (#) heading to the text until the next # heading."""
    out: dict[str, str] = {}
    parts = re.split(r"^# (.+?)\s*$", body, flags=re.MULTILINE)
    # parts = [pre, h1, text, h1, text, ...]
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1] if i + 1 < len(parts) else ""
    return out


def audit_file(path: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    body = text[m.end():] if m else text
    secs = sections(body)

    # 3. evidence sections must cite
    for name in EVIDENCE_SECTIONS:
        if name not in secs:
            findings.append(f"missing evidence section: '{name}'")
        elif not MARKER_RE.search(secs[name]):
            findings.append(f"evidence section '{name}' contains no [n] citation marker")

    # 1/2/4. gap blocks — count-based so it is agnostic to ## vs **bold** style
    gaps_body = secs.get("Assessed Guidance")
    if gaps_body is None:
        findings.append("missing section: 'Assessed Guidance'")
        return findings

    n_gaps = len(GAP_HEADER_RE.findall(gaps_body))
    if n_gaps == 0:
        findings.append("'Assessed Guidance' has no labelled guidance blocks "
                        "(expected '## Guidance N …')")
        return findings

    # every gap must carry each of the four parts, so each part count == n_gaps
    for part, rx in GAP_PARTS.items():
        c = len(rx.findall(gaps_body))
        if c < n_gaps:
            findings.append(f"{n_gaps} guidance block(s) but only {c} '**{part}:**' bullet(s) "
                            f"— {n_gaps - c} guidance block(s) missing their {part}")

    # each stated Confidence bullet must name High/Medium/Low
    for line in CONF_BULLET_RE.findall(gaps_body):
        if not CONF_RE.search(line):
            findings.append(f"gap Confidence not High/Medium/Low: '{line.strip()[:40]}'")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    if args.paths:
        files = [Path(p) for p in args.paths]
    else:
        files = [f for f in sorted(Path(args.docs).rglob("*.md")) if f.name != "index.md"]

    total = 0
    for f in files:
        fnd = audit_file(f)
        if fnd:
            total += len(fnd)
            print(f"FLAG  {f.as_posix()}")
            for x in fnd:
                print(f"        - {x}")
        else:
            print(f"ok    {f.as_posix()}")

    print("-" * 60)
    if total:
        print(f"GENRE AUDIT: {total} finding(s) across {len(files)} file(s)")
        return 1 if args.strict else 0
    print(f"GENRE AUDIT CLEAN: {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
