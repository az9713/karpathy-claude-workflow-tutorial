"""Check the explicit publication package before committing; Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    '.gitignore', '.nojekyll', 'README.md', 'index.html', 'assets/tutorial-preview.jpg',
    'expert-workflow-skill-guide.html', 'feynman-skill-creation.html',
    'feynman-oscillator-example.html', 'scripts/check_public_package.py',
    'skills/build-expert-workflow/SKILL.md',
    'skills/build-expert-workflow/references/source-access.md',
    'skills/build-expert-workflow/references/evaluation.md',
    'skills/build-expert-workflow/agents/openai.yaml',
    'skills/feynman-harmonic-oscillator/SKILL.md',
    'skills/feynman-harmonic-oscillator/references/evidence.md',
    'skills/feynman-harmonic-oscillator/evaluations.md',
    'skills/feynman-harmonic-oscillator/scripts/check.py',
    'skills/feynman-harmonic-oscillator/overview.html',
}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate anchor: {attrs['id']}"
            self.ids.add(attrs['id'])
        self.links.extend(attrs[key] for key in ('href', 'src') if key in attrs)


def check():
    tracked = set(subprocess.check_output(
        ['git', 'ls-files'], cwd=ROOT, text=True).splitlines())
    assert not tracked - FILES, f'Unexpected publication files: {tracked - FILES}'
    pages = {}
    for name in sorted(FILES):
        file = ROOT / name
        assert file.is_file(), name
        if file.suffix in ('.jpg', '.png'):
            continue
        text = file.read_text(encoding='utf-8')
        assert not re.search(r'[A-Za-z]:[\\/]Users[\\/]|file:[/]{2}|https?://(?:localhost|127\.0\.0\.1)', text), name
        assert not re.search(r'(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_\-]{20,}', text), name
        assert '\ufffd' not in text, name
        if file.suffix == '.html':
            page = Page()
            page.feed(text)
            pages[name] = page
    checked = 0
    for name, page in pages.items():
        for href in page.links:
            link = urlsplit(href)
            if link.scheme or link.netloc:
                continue
            target = (ROOT / name).parent / unquote(link.path) if link.path else ROOT / name
            resolved = target.resolve()
            assert resolved.is_relative_to(ROOT), (name, href)
            relative = resolved.relative_to(ROOT).as_posix()
            assert relative in FILES, (name, href, 'target excluded from publication')
            if link.fragment and relative in pages:
                assert unquote(link.fragment) in pages[relative].ids, (name, href)
            checked += 1
    print(f'PASS: {len(FILES)} publication files; {len(pages)} HTML pages; {checked} internal links; privacy patterns')


if __name__ == '__main__':
    check()
