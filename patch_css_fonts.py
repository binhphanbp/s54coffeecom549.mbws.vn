import re
from pathlib import Path

BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')
CSS_DIR = BASE_DIR / 'assets' / 'css'

font_replacements = {
    r'https?://(?:www\.)?vittoriacoffee\.com/cdn/shop/t/\d+/assets/(domaine-regular\.woff2?)': r'../fonts/\1',
    r'https?://(?:www\.)?vittoriacoffee\.com/cdn/shop/t/\d+/assets/(domainedispnar-regularitalic\.woff2?)': r'../fonts/\1',
    r'https?://(?:www\.)?vittoriacoffee\.com/cdn/shop/t/\d+/assets/(gilroy-semibold\.woff2?)': r'../fonts/\1',
    r'https?://(?:www\.)?vittoriacoffee\.com/cdn/shop/t/\d+/assets/(neutra2text-book-webfont\.woff2?)': r'../fonts/\1',
    r'https?://(?:www\.)?vittoriacoffee\.com/cdn/shop/t/\d+/assets/(neutra2text-demi-webfont\.woff2?)': r'../fonts/\1',
    r'//www\.vittoriacoffee\.com/cdn/shop/t/\d+/assets/(domaine-regular\.woff2?)': r'../fonts/\1',
    r'//www\.vittoriacoffee\.com/cdn/shop/t/\d+/assets/(domainedispnar-regularitalic\.woff2?)': r'../fonts/\1',
    r'//www\.vittoriacoffee\.com/cdn/shop/t/\d+/assets/(gilroy-semibold\.woff2?)': r'../fonts/\1',
    r'//www\.vittoriacoffee\.com/cdn/shop/t/\d+/assets/(neutra2text-book-webfont\.woff2?)': r'../fonts/\1',
    r'//www\.vittoriacoffee\.com/cdn/shop/t/\d+/assets/(neutra2text-demi-webfont\.woff2?)': r'../fonts/\1',
}

for css_file in CSS_DIR.glob('*.css'):
    with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    for pattern, repl in font_replacements.items():
        if re.search(pattern, content):
            content = re.sub(pattern, repl, content)
            modified = True
            
    if modified:
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Patched fonts in {css_file.name}')

print('CSS fonts patching done!')
