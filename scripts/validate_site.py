"""Fail the release gate on broken local references or missing generated content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.stylesheets = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.stylesheets.append(attrs.get('href'))


root = Path(sys.argv[1]).resolve()
readme = Path('README.md').read_text(encoding='utf-8')
start, end = '<!--START_SECTION:activity-->', '<!--END_SECTION:activity-->'
errors = []
if not (readme.count(start) == readme.count(end) == 1 and readme.index(start) < readme.index(end)):
    errors.append('README must contain exactly one ordered pair of activity markers')
homepage = root / 'index.html'
if not homepage.exists():
    errors.append('Missing generated index.html')
    home = ''
else:
    home = homepage.read_text(encoding='utf-8')
if 'Recent activity' not in home:
    errors.append('Homepage is missing the rendered README activity heading')
if '{% include' in home or 'include_relative README.md' in home:
    errors.append('Homepage contains unexpanded Liquid')
documents = {p: Document(p.read_text(encoding='utf-8')) for p in root.rglob('*.html')}
if homepage in documents and not documents[homepage].stylesheets:
    errors.append('Homepage has no stylesheet')
base = '/devops-pages-lab'
for path, doc in documents.items():
    for ref in doc.links:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        local = unquote(url.path)
        if local == base or local.startswith(base + '/'):
            local = local[len(base):]
        target = (root / local.lstrip('/') if local.startswith('/') else path.parent / local).resolve() if local else path
        if not target.is_relative_to(root):
            errors.append(f'{path.name}: reference escapes site: {ref}')
            continue
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{path.name}: broken local link: {ref}')
        elif url.fragment and target in documents and unquote(url.fragment) not in documents[target].ids:
            errors.append(f'{path.name}: missing fragment: {ref}')
if errors:
    print('\n'.join('ERROR: ' + error for error in errors))
    sys.exit(1)
print(f'PASS: README markers, rendered activity and local references in {len(documents)} HTML pages')
