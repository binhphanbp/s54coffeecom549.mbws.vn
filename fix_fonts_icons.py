import urllib.request
import ssl
from pathlib import Path
import shutil

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0'}
BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')
CSS_DIR = BASE_DIR / 'assets' / 'css'
FONTS_DIR = BASE_DIR / 'assets' / 'fonts'
ICONS_DIR = BASE_DIR / 'assets' / 'icons'
ICONS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Copy fonts to CSS dir as well so relative paths always work
for f in FONTS_DIR.glob('*.woff*'):
    shutil.copy(f, CSS_DIR / f.name)
print('Copied fonts to CSS dir')

# 2. Download missing CSS SVG icons
svgs = [
    'icon-arrow-right.svg',
    'icon-chevron-down.svg',
    'icon-subscription-checked.svg',
    'icon-subscription-select.svg',
    'icon-subscription-unchecked.svg'
]

for s in svgs:
    url = f'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/{s}'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read()
            with open(CSS_DIR / s, 'wb') as f:
                f.write(data)
            with open(ICONS_DIR / s, 'wb') as f:
                f.write(data)
            print(f'Downloaded {s}')
    except Exception as e:
        print(f'Failed {s}: {e}')

# 3. Fix layouts.theme.css font-face URLs to ../fonts/
with open(CSS_DIR / 'layouts.theme.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace url(filename.woff) with url(../fonts/filename.woff)
import re
css = re.sub(r'url\(([a-zA-Z0-9_-]+\.woff2?)\)', r'url(../fonts/\1)', css)
with open(CSS_DIR / 'layouts.theme.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Done fixing fonts and icons!')
