"""Refresh public GitHub repository popularity; never execute upstream code."""
import concurrent.futures
import datetime
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'content/data'


def main():
    skills = json.loads((DATA / 'recommended-skills.json').read_text(encoding='utf-8'))['skills']
    index = json.loads((DATA / 'tools/index.json').read_text(encoding='utf-8'))
    for category in index['categories']:
        skills += json.loads((DATA / f"tools/{category['slug']}.json").read_text(encoding='utf-8'))['items']
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')

    def fetch(repo):
        url = 'https://api.github.com/repos/' + repo
        request = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'useful-agent-skills'})
        with urllib.request.urlopen(request, timeout=30) as response:
            meta = json.load(response)
        return repo, {'stars': meta['stargazers_count'], 'checked_at': checked,
                      'pushed_at': meta['pushed_at'], 'archived': meta['archived'], 'api_url': url}

    # Fail without overwriting the existing snapshot if any source cannot be read.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        sources = dict(pool.map(fetch, sorted({skill['source'] for skill in skills})))
    (DATA / 'tools/sources.json').write_text(json.dumps({'schema_version': 1, 'repositories': sources}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Fetched GitHub Star counts for {len(sources)} repositories at {checked}')


if __name__ == '__main__':
    main()
