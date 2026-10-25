#!/usr/bin/env python3
"""Validate every Agent Skill in this repository using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD)\b|\[TODO", re.IGNORECASE)
PUBLIC_REPO_FORBIDDEN_PATTERNS = {
    "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    "GitHub token": re.compile(r"(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\r\n]+\\"),
    "private Unix home path": re.compile(r"/home/[^/\s]+/"),
}


def frontmatter_value(block: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", block)
    if not match:
        return None
    return match.group(1).strip().strip('"\'')


def validate_local_links(markdown_file: Path, text: str, errors: list[str]) -> None:
    for match in MARKDOWN_LINK_RE.finditer(text):
        raw_target = match.group(1).strip().strip("<>")
        if raw_target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_without_fragment = unquote(raw_target.split("#", 1)[0])
        if not target_without_fragment:
            continue
        target = markdown_file.parent / target_without_fragment
        if not target.exists():
            errors.append(
                f"{markdown_file.relative_to(ROOT)}: broken local link {raw_target!r}"
            )


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not NAME_RE.fullmatch(skill_dir.name):
        errors.append(f"{skill_dir.relative_to(ROOT)}: invalid skill directory name")

    if not skill_file.is_file():
        errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
        return errors

    text = skill_file.read_text(encoding="utf-8-sig")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{skill_file.relative_to(ROOT)}: invalid YAML frontmatter block")
        return errors

    block = match.group(1)
    name = frontmatter_value(block, "name")
    description = frontmatter_value(block, "description")

    if name != skill_dir.name:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: name {name!r} must match {skill_dir.name!r}"
        )
    if not description:
        errors.append(f"{skill_file.relative_to(ROOT)}: description is required")
    elif len(description) > 1024:
        errors.append(f"{skill_file.relative_to(ROOT)}: description exceeds 1024 characters")

    for markdown_file in skill_dir.rglob("*.md"):
        markdown = markdown_file.read_text(encoding="utf-8-sig")
        if PLACEHOLDER_RE.search(markdown):
            errors.append(f"{markdown_file.relative_to(ROOT)}: unfinished placeholder found")
        validate_local_links(markdown_file, markdown, errors)

    for text_file in skill_dir.rglob("*"):
        if not text_file.is_file():
            continue
        try:
            content = text_file.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue
        for label, pattern in PUBLIC_REPO_FORBIDDEN_PATTERNS.items():
            if pattern.search(content):
                errors.append(
                    f"{text_file.relative_to(ROOT)}: possible {label} in public skill"
                )

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERROR: skills/ directory is missing", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("ERROR: no skill directories found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s): {', '.join(p.name for p in skill_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
