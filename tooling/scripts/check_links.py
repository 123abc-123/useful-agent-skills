"""Check external Markdown links while avoiding false failures from rate limits."""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
SOFT_STATUSES = {401, 403, 405, 429}
HARD_STATUSES = {404, 410}
SITE_PREFIX = "https://123abc-123.github.io/useful-agent-skills/"


def collect_links() -> list[str]:
    links: set[str] = set()
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        links.update(LINK.findall(path.read_text(encoding="utf-8")))
    return sorted(links)


def check(url: str, timeout: float) -> tuple[str, str, int | None]:
    if url.startswith(SITE_PREFIX):
        relative = urllib.parse.unquote(url[len(SITE_PREFIX):]).split("#", 1)[0].split("?", 1)[0]
        local = ROOT / "site" / relative
        if not relative or relative.endswith("/"):
            local = local / "index.html"
        return url, "ok" if local.is_file() else "broken", 200 if local.is_file() else 404
    headers = {"User-Agent": "useful-agent-skills-link-check/1.0"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        if method == "GET":
            request.add_header("Range", "bytes=0-1024")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return url, "ok", response.status
        except urllib.error.HTTPError as exc:
            if exc.code in HARD_STATUSES:
                return url, "broken", exc.code
            if exc.code in SOFT_STATUSES:
                return url, "restricted", exc.code
            if method == "GET":
                return url, "transient", exc.code
        except (urllib.error.URLError, TimeoutError, OSError):
            if method == "GET":
                return url, "transient", None
    return url, "transient", None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    links = collect_links()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(lambda url: check(url, args.timeout), links))

    broken = [result for result in results if result[1] == "broken"]
    restricted = [result for result in results if result[1] == "restricted"]
    transient = [result for result in results if result[1] == "transient"]

    for url, _, status in broken:
        print(f"BROKEN {status}: {url}")
    for url, _, status in restricted:
        print(f"RESTRICTED {status}: {url}")
    for url, _, status in transient:
        print(f"TRANSIENT {status or '-'}: {url}")

    print(
        f"Checked {len(links)} links: {len(broken)} broken, "
        f"{len(restricted)} restricted, {len(transient)} transient."
    )
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
