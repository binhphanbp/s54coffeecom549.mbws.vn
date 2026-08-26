#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html', 'blogs-news.html', 'blog-detail.html']

legacy_cart_pattern = r'<div id=\"shopify-section-cart-drawer\"[\s\S]*?</div><div class=\"c-cart-drawer__loader\"></div>'

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    if 'shopify-section-cart-drawer' in c:
        c = re.sub(legacy_cart_pattern, '', c)
        fpath.write_text(c, encoding='utf-8')
        print(f"✓ Removed conflicting legacy Shopify cart drawer snippet from {p}")
    else:
        print(f"ℹ No legacy cart drawer snippet in {p}")

print("\n✅ Cleaned up all legacy cart drawer duplicates!")
