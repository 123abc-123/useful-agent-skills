"""Validate the repository's Markdown catalog without accessing the network."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "MAINTENANCE.md",
    "CHANGELOG.md",
    "catalog/skills.md",
    "catalog/harness.md",
    "catalog/learning-resources.md",
    "catalog/discovery-sources.md",
    "catalog/watchlist.md",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")


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

    if len(all_urls) < 20:
        errors.append(f"expected at least 20 distinct external resources, found {len(all_urls)}")

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Catalog validation passed: {len(REQUIRED_FILES)} files, {len(all_urls)} distinct URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
