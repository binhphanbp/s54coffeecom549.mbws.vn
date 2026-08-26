#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update index.html
index_path = BASE_DIR / 'index.html'
c = index_path.read_text(encoding='utf-8')

# Replace "Xem Tất Cả" in article feed
c = re.sub(r'href=[\"\']/blogs/news[\"\']', 'href="blogs-news.html"', c)
c = re.sub(r'href=[\"\']/blogs/news/[^\"\']*[\"\']', 'href="blog-detail.html"', c)

# Replace any footer links to /blogs/news
c = c.replace('href="/blogs/news"', 'href="blogs-news.html"')

index_path.write_text(c, encoding='utf-8')
print("✓ Updated blog links in index.html")

# 2. Update other HTML files
pages = ['collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html', 'blogs-news.html', 'blog-detail.html']
for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    page_c = fpath.read_text(encoding='utf-8')
    page_c = page_c.replace('href="/blogs/news"', 'href="blogs-news.html"')
    page_c = re.sub(r'href=[\"\']/blogs/news/[^\"\']*[\"\']', 'href="blog-detail.html"', page_c)
    fpath.write_text(page_c, encoding='utf-8')
    print(f"✓ Updated blog links in {p}")

# 3. Update .htaccess for Production Apache
htaccess_path = BASE_DIR / '.htaccess'
ht = htaccess_path.read_text(encoding='utf-8')
if 'blogs-news.html' not in ht:
    ht = ht.replace(
        'RewriteRule ^(pages/)?(our-story|roasting|community|brewing-guides|news|subscriptions)$ our-story.html [L,QSA]',
        '# Redirect /blogs, /blog, /news to blogs-news.html\n  RewriteRule ^(blogs|blog)(/news)?(/.*)?$ blogs-news.html [L,QSA]\n\n  # Redirect /pages/our-story, roasting, community, subscriptions to our-story.html\n  RewriteRule ^(pages/)?(our-story|roasting|community|brewing-guides|subscriptions)$ our-story.html [L,QSA]'
    )
    htaccess_path.write_text(ht, encoding='utf-8')
    print("✓ Updated .htaccess with blog rewrite rules")

# 4. Update server.py for local server
server_path = BASE_DIR / 'server.py'
srv = server_path.read_text(encoding='utf-8')
if 'blogs-news.html' not in srv:
    srv = srv.replace(
        "elif path.startswith('/pages/our-story')",
        "elif path.startswith('/blogs') or path.startswith('/blog') or path == '/news':\n            self.path = '/blogs-news.html'\n        elif path.startswith('/pages/our-story')"
    )
    server_path.write_text(srv, encoding='utf-8')
    print("✓ Updated server.py with blog route")

print("\n✅ All blog routes, links and rewrites connected seamlessly!")
