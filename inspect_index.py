import re
from pathlib import Path

BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')

with open(BASE_DIR / 'index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find any remaining remote image urls (cdn.shopify.com or accentuate.io or vittoriacoffee.com)
remote_imgs = re.findall(r'(?:src|data-src|poster|data-background|data-bg)=["\'](https?://[^"\']+|//[^"\']+)["\']', html)
print(f'Remaining remote image URLs in index.html: {len(remote_imgs)}')
for r in list(set(remote_imgs))[:15]:
    print('Remote:', r)

# check CSS links
css_links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', html)
print('\nCSS links in index.html:')
for c in css_links:
    if '.css' in c:
        print('CSS:', c)

# check local file existence
print('\nChecking local file existence:')
for c in set(css_links):
    if c.startswith('assets/'):
        p = BASE_DIR / c
        print(f'{c} -> exists? {p.exists()}')
