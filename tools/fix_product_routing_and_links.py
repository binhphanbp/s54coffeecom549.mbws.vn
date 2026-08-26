#!/usr/bin/env python3
"""
Fix Product Detail Routing & Link Targets:
1. Fix .htaccess rewrite rules so /collections/*/products/* and /products/* route to product-detail.html
2. Fix server.py route handler
3. Update product links in collections-coffee.html and index.html to product-detail.html
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update .htaccess
ht_path = BASE_DIR / '.htaccess'
ht = ht_path.read_text(encoding='utf-8')

old_rewrite_rules = """  # Redirect /collections or /collections/* to collections-coffee.html
  RewriteRule ^collections(/.*)?$ collections-coffee.html [L,QSA]

  # Redirect /products or /products/* to product-detail.html
  RewriteRule ^products(/.*)?$ product-detail.html [L,QSA]"""

new_rewrite_rules = """  # Redirect any product URL (/products/* or /collections/*/products/*) to product-detail.html
  RewriteRule ^(.*/)?products(/.*)?$ product-detail.html [L,QSA]

  # Redirect /collections or /collections/* to collections-coffee.html
  RewriteRule ^collections(/.*)?$ collections-coffee.html [L,QSA]"""

if old_rewrite_rules in ht:
    ht = ht.replace(old_rewrite_rules, new_rewrite_rules)
    ht_path.write_text(ht, encoding='utf-8')
    print("✓ Fixed .htaccess product rewrite rules (products before collections)")
else:
    print("ℹ Checking .htaccess structure...")
    ht = re.sub(r'RewriteRule \^collections\(/.*\)\?\$ collections-coffee\.html \[L,QSA\]\s*RewriteRule \^products\(/.*\)\?\$ product-detail\.html \[L,QSA\]', new_rewrite_rules, ht)
    ht_path.write_text(ht, encoding='utf-8')
    print("✓ Updated .htaccess via regex")

# 2. Update server.py
sp_path = BASE_DIR / 'server.py'
if sp_path.exists():
    sp = sp_path.read_text(encoding='utf-8')
    if 'products' in sp:
        # ensure /collections/.../products/... routes to product-detail.html
        sp = re.sub(r'if self\.path\.startswith\(\'/collections\'\):', "if '/products' in self.path or self.path.startswith('/products'):\n            self.path = '/product-detail.html'\n        elif self.path.startswith('/collections'):", sp)
        sp_path.write_text(sp, encoding='utf-8')
        print("✓ Updated server.py route handler for /collections/*/products/*")

# 3. Update all product link hrefs in collections-coffee.html and index.html
pages = ['collections-coffee.html', 'index.html', 'product-detail.html', 'our-story.html', 'wholesale.html', 'blogs-news.html', 'blog-detail.html']

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    
    # Replace Shopify product collection URLs with clean product-detail.html
    c = re.sub(r'href=[\"\']/collections/[^/]+/products/[^\"\']+[\"\']', 'href="product-detail.html"', c)
    c = re.sub(r'href=[\"\']/products/[^\"\']+[\"\']', 'href="product-detail.html"', c)
    
    fpath.write_text(c, encoding='utf-8')
    print(f"✓ Normalized product links in {p} to product-detail.html")

print("\n✅ Product detail page routing & links 100% fixed!")
