"""Validate the catalog, structured recommendations, and local skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "SCORING.md",
    "CONTRIBUTING.md",
    "MAINTENANCE.md",
    "CHANGELOG.md",
    "catalog/skills.md",
    "catalog/recommended-stack.md",
    "catalog/harness.md",
    "catalog/learning-resources.md",
    "catalog/discovery-sources.md",
    "catalog/watchlist.md",
    "data/recommended-skills.json",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATUSES = {"verified", "not-run", "passed", "failed", "needs-adaptation"}
RISKS = {"low", "medium", "high"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        return {}
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate_structured_catalog(errors: list[str]) -> int:
    path = ROOT / "data/recommended-skills.json"
    if not path.is_file():
        return 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid data/recommended-skills.json: {exc}")
        return 0

    if payload.get("schema_version") != 1:
        errors.append("recommended catalog schema_version must be 1")
    skills = payload.get("skills")
    if not isinstance(skills, list) or not skills:
        errors.append("recommended catalog must contain a non-empty skills list")
        return 0

    required = {
        "name", "category", "source", "path", "commit", "license", "purpose",
        "score", "risk", "source_path", "install_syntax", "runtime_pi",
        "runtime_opencode",
    }
    names: list[str] = []
    for index, skill in enumerate(skills, start=1):
        if not isinstance(skill, dict):
            errors.append(f"recommended skill #{index} is not an object")
            continue
        missing = sorted(required - set(skill))
        if missing:
            errors.append(f"recommended skill #{index} missing: {', '.join(missing)}")
            continue

        name = skill["name"]
        names.append(name)
        if not isinstance(name, str) or not NAME.fullmatch(name):
            errors.append(f"invalid skill name: {name!r}")
        if not isinstance(skill["score"], int) or not 0 <= skill["score"] <= 100:
            errors.append(f"invalid score for {name}")
        if skill["risk"] not in RISKS:
            errors.append(f"invalid risk for {name}: {skill['risk']}")
        for field in ("source_path", "install_syntax", "runtime_pi", "runtime_opencode"):
            if skill[field] not in STATUSES:
                errors.append(f"invalid {field} for {name}: {skill[field]}")
        if not str(skill["path"]).endswith("/SKILL.md"):
            errors.append(f"skill path must end in /SKILL.md: {name}")

        is_local = skill["source"] == "123abc-123/useful-agent-skills"
        if is_local:
            local_path = ROOT / skill["path"]
            if not local_path.is_file():
                errors.append(f"missing local skill file for {name}: {skill['path']}")
            else:
                frontmatter = parse_frontmatter(local_path)
                if frontmatter.get("name") != name:
                    errors.append(f"frontmatter name mismatch for {name}")
                if not frontmatter.get("description"):
                    errors.append(f"missing frontmatter description for {name}")
                if local_path.parent.name != name:
                    errors.append(f"skill folder name mismatch for {name}")
                local_text = local_path.read_text(encoding="utf-8")
                if any(marker in local_text for marker in ("TODO", "PLACEHOLDER", "Example skill")):
                    errors.append(f"unfinished scaffold marker in local skill: {name}")
        elif not SHA40.fullmatch(str(skill["commit"])):
            errors.append(f"external skill commit must be a 40-character SHA: {name}")

    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append(f"duplicate recommended skill names: {', '.join(duplicates)}")

    recommended_path = ROOT / "catalog/recommended-stack.md"
    if recommended_path.is_file():
        recommended_text = recommended_path.read_text(encoding="utf-8")
        for name in names:
            if f"`{name}`" not in recommended_text:
                errors.append(f"recommended-stack.md does not mention: {name}")

    return len(skills)


def main() -> int:
    errors: list[str] = []
    all_urls: set[str] = set()

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"empty file: {relative}")
        if "http://github.com" in text:
            errors.append(f"insecure GitHub link in: {relative}")
        all_urls.update(MARKDOWN_LINK.findall(text))

    skills_path = ROOT / "catalog/skills.md"
    if skills_path.is_file():
        text = skills_path.read_text(encoding="utf-8")
        for label in ("机器学习", "调试", "评测", "安全", "浏览器", "文档", "Harness"):
            if label not in text:
                errors.append(f"skills catalog is missing category marker: {label}")

    recommendation_count = validate_structured_catalog(errors)

    if len(all_urls) < 30:
        errors.append(f"expected at least 30 distinct external resources, found {len(all_urls)}")

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Catalog validation passed: "
        f"{len(REQUIRED_FILES)} files, {recommendation_count} structured recommendations, "
        f"{len(all_urls)} distinct URLs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
