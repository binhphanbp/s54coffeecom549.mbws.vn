import os
import re
from pathlib import Path

BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')

html_files = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

patterns_to_remove = [
    r'<script[^>]*checkouts/internal/preloads\.js[^>]*></script>',
    r'<link[^>]*checkouts/internal/preloads\.js[^>]*>',
    r'<script[^>]*cdn/shopifycloud/[^>]*></script>',
    r'<script[^>]*shop-js/modules/[^>]*></script>',
    r'<script[^>]*sections\.collection-carousel\.js[^>]*></script>'
]

for hf in html_files:
    file_path = BASE_DIR / hf
    if not file_path.exists():
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean unused Shopify remnant scripts
    for p in patterns_to_remove:
        html = re.sub(p, '', html, flags=re.IGNORECASE)

    # Fix title in our-story.html if missing
    if hf == 'our-story.html':
        if '<title>' not in html:
            html = html.replace('<head>', '<head>\n  <title>Câu Chuyện Thương Hiệu S54 Coffee | 12+ Năm Di Sản Cà Phê Việt</title>')
        else:
            html = re.sub(r'<title>.*?</title>', '<title>Câu Chuyện Thương Hiệu S54 Coffee | 12+ Năm Di Sản Cà Phê Việt</title>', html, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Cleaned {hf}")

print("All HTML files refined and cleaned.")
