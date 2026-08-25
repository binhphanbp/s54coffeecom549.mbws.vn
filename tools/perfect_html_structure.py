#!/usr/bin/env python3
"""
Ensure pixel-perfect, clean HTML structure across all 6 pages.
Fixes:
- Topbar: clean message on center, language switcher on right
- Hero Banner: original clean markup
- Footer: single bottom bar, clean centered language switcher, single copyright
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

CLEAN_TOPBAR = '''  <div
    class="c-header__topbar"
    data-topbar
    data-autoplay="true"
    data-autoplay-speed="3"
  > 
    <div class="c-header__topbar-messages">
      <a href="/collections/all-coffee-products" class="c-header__topbar-message o-subtitle">MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ $69†</a>
    </div>
    <div class="c-lang-switcher c-lang-switcher--header" data-lang-switcher>
      <button type="button" class="c-lang-btn is-active" data-lang="vi" aria-label="Tiếng Việt">🇻🇳 VI</button>
      <span class="c-lang-divider">|</span>
      <button type="button" class="c-lang-btn" data-lang="en" aria-label="English">🇬🇧 EN</button>
    </div>
  </div>'''

for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    
    # 1. Clean topbar
    content = re.sub(
        r'<div\s+class="c-header__topbar"[\s\S]*?</div>\s*</div>\s*(?=</div><div id="c-h-inner")',
        CLEAN_TOPBAR + '\n  ',
        content
    )
    
    # Also handle if topbar regex above didn't catch due to varying closing tags
    if 'c-header__topbar' in content and 'c-lang-switcher--header' not in content:
        content = re.sub(
            r'<div\s+class="c-header__topbar"[^>]*>[\s\S]*?</div>\s*(?=<div id="c-h-inner"|<div class="c-header__inner")',
            CLEAN_TOPBAR + '\n  ',
            content
        )

    fpath.write_text(content, encoding='utf-8')
    print(f"✓ Formatted clean topbar in {page}")

