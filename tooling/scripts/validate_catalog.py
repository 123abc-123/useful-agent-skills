"""Validate the catalog, structured recommendations, prompts, and local skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "SCORING.md",
    "CONTRIBUTING.md",
    "MAINTENANCE.md",
    "CHANGELOG.md",
    "content/catalog/skills.md",
    "content/catalog/recommended-stack.md",
    "content/catalog/prompt-libraries.md",
    "content/catalog/harness.md",
    "content/catalog/learning-resources.md",
    "content/catalog/discovery-sources.md",
    "content/catalog/watchlist.md",
    "content/catalog/README.md",
    "content/catalog/tools/README.md",
    "content/data/recommended-skills.json",
    "content/data/tools/index.json",
    "content/data/prompts.json",
    "site/tools/index.html",
    "site/html-reports.html",
    "tooling/scripts/build_catalog.py",
    "SECURITY.md",
    "content/prompts/README.md",
    "tooling/evals/README.md",
    "tooling/evals/cases/prompts.json",
    "content/case-studies/README.md",
    "content/case-studies/data-leakage-audit.md",
    "content/case-studies/training-nan-debug.md",
    "content/case-studies/paper-to-spike.md",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
LOCAL_MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATUSES = {"verified", "not-run", "passed", "failed", "needs-adaptation"}
RISKS = {"low", "medium", "high"}
PINNING_STATUSES = {"verified", "pending-upstream-commit-verification", "local-main"}
PROMPT_VARIABLE = re.compile(r"\{\{([a-z][a-z0-9_]*)\}\}")
HTML_REPORT_STATUSES = {"recommended", "trial", "needs-adaptation"}


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
    path = ROOT / "content/data/recommended-skills.json"
    if not path.is_file():
        return 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid content/data/recommended-skills.json: {exc}")
        return 0

    if payload.get("schema_version") != 2:
        errors.append("recommended catalog schema_version must be 2")
    skills = payload.get("skills")
    if not isinstance(skills, list) or not skills:
        errors.append("recommended catalog must contain a non-empty skills list")
        return 0

    required = {
        "name", "category", "source", "path", "commit", "license", "purpose",
        "score", "risk", "source_path", "install_syntax", "runtime_pi",
        "runtime_opencode", "last_verified", "pinning_status", "runtime_evidence",
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
        if not ISO_DATE.fullmatch(str(skill["last_verified"])):
            errors.append(f"invalid last_verified for {name}: {skill['last_verified']}")
        if skill["pinning_status"] not in PINNING_STATUSES:
            errors.append(f"invalid pinning_status for {name}: {skill['pinning_status']}")
        if (skill["runtime_pi"] == "passed" or skill["runtime_opencode"] == "passed") and not skill["runtime_evidence"]:
            errors.append(f"passed runtime needs evidence for {name}")
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

    recommended_path = ROOT / "content/catalog/recommended-stack.md"
    if recommended_path.is_file():
        recommended_text = recommended_path.read_text(encoding="utf-8")
        for name in names:
            if f"`{name}`" not in recommended_text:
                errors.append(f"recommended-stack.md does not mention: {name}")

    return len(skills)


def validate_prompt_catalog(errors: list[str]) -> int:
    path = ROOT / "content/data/prompts.json"
    if not path.is_file():
        return 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid content/data/prompts.json: {exc}")
        return 0

    if payload.get("schema_version") != 1:
        errors.append("prompt catalog schema_version must be 1")
    prompts = payload.get("prompts")
    if not isinstance(prompts, list) or not prompts:
        errors.append("prompt catalog must contain a non-empty prompts list")
        return 0

    required = {"name", "category", "path", "purpose", "variables"}
    names: list[str] = []
    for index, prompt in enumerate(prompts, start=1):
        if not isinstance(prompt, dict):
            errors.append(f"prompt #{index} is not an object")
            continue
        missing = sorted(required - set(prompt))
        if missing:
            errors.append(f"prompt #{index} missing: {', '.join(missing)}")
            continue

        name = prompt["name"]
        names.append(name)
        if not isinstance(name, str) or not NAME.fullmatch(name):
            errors.append(f"invalid prompt name: {name!r}")
        variables = prompt["variables"]
        if not isinstance(variables, list) or not variables:
            errors.append(f"prompt variables must be a non-empty list: {name}")
            continue
        if len(variables) != len(set(variables)):
            errors.append(f"duplicate prompt variables: {name}")

        relative = prompt["path"]
        if relative != f"content/prompts/{name}.prompt.md":
            errors.append(f"prompt path does not match name: {name}")
        prompt_path = ROOT / relative
        if not prompt_path.is_file():
            errors.append(f"missing prompt file for {name}: {relative}")
            continue
        frontmatter = parse_frontmatter(prompt_path)
        if frontmatter.get("name") != name:
            errors.append(f"prompt frontmatter name mismatch: {name}")
        if not frontmatter.get("description") or not frontmatter.get("category"):
            errors.append(f"prompt frontmatter is incomplete: {name}")
        if frontmatter.get("category") != prompt["category"]:
            errors.append(f"prompt category mismatch: {name}")

        prompt_text = prompt_path.read_text(encoding="utf-8")
        used_variables = sorted(set(PROMPT_VARIABLE.findall(prompt_text)))
        indexed_variables = sorted(variables)
        if used_variables != indexed_variables:
            errors.append(
                f"prompt variable mismatch for {name}: "
                f"index={indexed_variables}, file={used_variables}"
            )

    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append(f"duplicate prompt names: {', '.join(duplicates)}")

    readme_path = ROOT / "content/prompts/README.md"
    if readme_path.is_file():
        readme_text = readme_path.read_text(encoding="utf-8")
        for name in names:
            if f"{name}.prompt.md" not in readme_text:
                errors.append(f"content/prompts/README.md does not link: {name}")

    validate_prompt_cases(errors, set(names))
    return len(prompts)


def validate_tools_catalog(errors: list[str]) -> tuple[int, int]:
    index_path = ROOT / "content/data/tools/index.json"
    if not index_path.is_file():
        return 0, 0
    try:
        tool_index = json.loads(index_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid content/data/tools/index.json: {exc}")
        return 0, 0
    categories = tool_index.get("categories")
    if not isinstance(categories, list) or not categories:
        errors.append("Tools index must contain categories")
        return 0, 0

    required = {
        "name", "category", "source", "path", "commit", "license", "purpose",
        "output", "compatibility", "score", "status", "risk", "source_path",
        "install_syntax", "runtime_pi", "runtime_opencode", "install",
        "last_verified", "pinning_status", "runtime_evidence",
    }
    total = 0
    slugs: list[str] = []
    for category in categories:
        slug = category.get("slug")
        if not isinstance(slug, str) or not NAME.fullmatch(slug):
            errors.append(f"invalid Tools category slug: {slug!r}")
            continue
        slugs.append(slug)
        data_path = ROOT / f"content/data/tools/{slug}.json"
        markdown_path = ROOT / f"content/catalog/tools/{slug}/README.md"
        page_path = ROOT / f"site/tools/{slug}/index.html"
        for path in (data_path, markdown_path, page_path):
            if not path.is_file():
                errors.append(f"missing Tools category file: {path.relative_to(ROOT)}")
        if not data_path.is_file():
            continue
        try:
            payload = json.loads(data_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"invalid content/data/tools/{slug}.json: {exc}")
            continue
        if payload.get("schema_version") != 2:
            errors.append(f"Tools category {slug} schema_version must be 2")
        items = payload.get("items")
        if not isinstance(items, list) or not items:
            errors.append(f"Tools category {slug} must contain items")
            continue
        total += len(items)
        markdown_text = markdown_path.read_text(encoding="utf-8") if markdown_path.is_file() else ""
        names: list[str] = []
        for item_index, item in enumerate(items, start=1):
            if not isinstance(item, dict):
                errors.append(f"Tools {slug} item #{item_index} is not an object")
                continue
            missing = sorted(required - set(item))
            if missing:
                errors.append(f"Tools {slug} item #{item_index} missing: {', '.join(missing)}")
                continue
            name = item["name"]
            names.append(name)
            if not isinstance(name, str) or not NAME.fullmatch(name):
                errors.append(f"invalid Tools skill name in {slug}: {name!r}")
            if not isinstance(item["score"], int) or not 0 <= item["score"] <= 100:
                errors.append(f"invalid Tools score for {name}")
            if item["status"] not in HTML_REPORT_STATUSES:
                errors.append(f"invalid Tools status for {name}: {item['status']}")
            if item["risk"] not in RISKS:
                errors.append(f"invalid Tools risk for {name}: {item['risk']}")
            for field in ("source_path", "install_syntax", "runtime_pi", "runtime_opencode"):
                if item[field] not in STATUSES:
                    errors.append(f"invalid {field} for Tools skill {name}: {item[field]}")
            if not str(item["path"]).endswith("SKILL.md"):
                errors.append(f"Tools source path must end in SKILL.md: {name}")
            if not SHA40.fullmatch(str(item["commit"])):
                errors.append(f"Tools commit must be a 40-character SHA: {name}")
            if not ISO_DATE.fullmatch(str(item["last_verified"])):
                errors.append(f"invalid Tools last_verified for {name}")
            if item["pinning_status"] not in PINNING_STATUSES:
                errors.append(f"invalid Tools pinning_status for {name}")
            if (item["runtime_pi"] == "passed" or item["runtime_opencode"] == "passed") and not item["runtime_evidence"]:
                errors.append(f"passed Tools runtime needs evidence for {name}")
            if f"`{name}`" not in markdown_text:
                errors.append(f"content/catalog/tools/{slug}/README.md does not mention: {name}")
        duplicates = sorted({name for name in names if names.count(name) > 1})
        if duplicates:
            errors.append(f"duplicate Tools names in {slug}: {', '.join(duplicates)}")
    duplicate_slugs = sorted({slug for slug in slugs if slugs.count(slug) > 1})
    if duplicate_slugs:
        errors.append(f"duplicate Tools category slugs: {', '.join(duplicate_slugs)}")
    return len(slugs), total


def validate_prompt_cases(errors: list[str], prompt_names: set[str]) -> None:
    path = ROOT / "tooling/evals/cases/prompts.json"
    if not path.is_file():
        return
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid tooling/evals/cases/prompts.json: {exc}")
        return
    if payload.get("schema_version") != 1 or payload.get("target_type") != "prompt":
        errors.append("prompt cases must use schema_version 1 and target_type prompt")
    cases = payload.get("cases")
    if not isinstance(cases, list):
        errors.append("prompt cases must contain a cases list")
        return
    targets: list[str] = []
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"prompt case #{index} is not an object")
            continue
        target = case.get("target")
        targets.append(target)
        if target not in prompt_names:
            errors.append(f"prompt case has unknown target: {target}")
        if not case.get("input"):
            errors.append(f"prompt case has empty input: {target}")
        for field in ("must", "must_not"):
            if not isinstance(case.get(field), list) or not case[field]:
                errors.append(f"prompt case {target} needs a non-empty {field} list")
    missing = sorted(prompt_names - set(targets))
    if missing:
        errors.append(f"prompts without regression cases: {', '.join(missing)}")


def validate_local_links(errors: list[str]) -> None:
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for target in LOCAL_MARKDOWN_LINK.findall(text):
            clean_target = target.split("#", 1)[0].strip()
            if not clean_target:
                continue
            resolved = (source.parent / clean_target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"local link escapes repository: {source.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {source.relative_to(ROOT)} -> {target}")


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

    skills_path = ROOT / "content/catalog/skills.md"
    if skills_path.is_file():
        text = skills_path.read_text(encoding="utf-8")
        for label in ("机器学习", "调试", "评测", "安全", "浏览器", "文档", "Harness"):
            if label not in text:
                errors.append(f"skills catalog is missing category marker: {label}")

    recommendation_count = validate_structured_catalog(errors)
    prompt_count = validate_prompt_catalog(errors)
    tool_category_count, tool_item_count = validate_tools_catalog(errors)
    validate_local_links(errors)

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
        f"{prompt_count} prompts, {tool_category_count} Tools categories with {tool_item_count} entries, "
        f"{len(all_urls)} distinct URLs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
