#!/usr/bin/env python3
"""
Unify and perfect Header and Hero across all storefront pages:
- Logo clearly placed on the Left
- Navigation clean in the Center
- Hotline & Cart Bag on the Right
- Clean Topbar with VI/EN Switcher
- Zero whitespace gap bugs
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HEADER_HTML = '''<div id="shopify-section-header" class="shopify-section c-section c-section__header">
  <header class="c-header is-milk" data-header>
    <div class="c-header__topbar" data-topbar>
      <div class="c-header__topbar-messages">
        <a href="collections-coffee.html" class="c-header__topbar-message o-subtitle">MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578</a>
      </div>
      <div class="c-lang-switcher c-lang-switcher--header" data-lang-switcher>
        <button type="button" class="c-lang-btn is-active" data-lang="vi" aria-label="Tiếng Việt">🇻🇳 VI</button>
        <span class="c-lang-divider">|</span>
        <button type="button" class="c-lang-btn" data-lang="en" aria-label="English">🇬🇧 EN</button>
      </div>
    </div>

    <div id="c-h-inner" class="c-header__inner">
      <button class="c-header__link is-mobile-only" data-menu-toggle aria-label="Toggle Menu">
        <svg fill="none" class="c-header__icon is-hamburger" viewBox="0 0 24 24" width="24" height="24"><path d="M3 12h18M3 6h18M3 18h18" stroke="#2F221A" stroke-width="2" stroke-linecap="round"/></svg>
      </button>

      <a href="index.html" class="c-header__logo" title="S54 COFFEE">
        <img src="assets/images/s54/s54_logo.png" alt="S54 COFFEE" width="180" height="38" />
      </a>

      <nav class="c-main-menu" data-main-menu>
        <div class="c-main-menu__header is-mobile-only">
          <a href="index.html" class="c-main-menu__logo">
            <img src="assets/images/s54/s54_logo.png" alt="S54 COFFEE" width="140" />
          </a>
          <button class="c-main-menu__close" data-menu-close aria-label="Close Menu">✕</button>
        </div>
        <ul class="c-main-menu__list is-level-1">
          <li class="c-main-menu__item is-level-1"><a href="collections-coffee.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">TẤT CẢ SẢN PHẨM</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="collections-coffee.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">CÀ PHÊ HẠT & RANG MỘC</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="collections-coffee.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">HÒA TAN & SẤY LẠNH</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="our-story.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">CÂU CHUYỆN S54</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="wholesale.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">B2B & ĐẠI LÝ</span></a></li>
        </ul>
      </nav>

      <ul id="c-h-add" class="c-header__additional">
        <li class="c-header__additional-item is-hotline is-desktop-only">
          <a href="tel:0383707578" class="c-header__phone-link">
            <span class="c-header__phone-icon">📞</span>
            <span class="c-header__phone-text">0383.707.578</span>
          </a>
        </li>
        <li class="c-header__additional-item">
          <button type="button" class="c-header__link is-cart" data-cart-drawer-toggle aria-label="Cart" style="position: relative; background: none; border: none; cursor: pointer; padding: 6px;">
            <svg fill="none" class="c-header__icon is-cart" viewBox="0 0 24 24" width="22" height="22" stroke="#2F221A" stroke-width="1.8"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            <span class="c-header__cart-count" data-cart-count>0</span>
          </button>
        </li>
      </ul>
    </div>
  </header>
</div>'''

pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    
    # Replace from shopify-section-header up to end of header
    c = re.sub(
        r'<div id="shopify-section-header" class="shopify-section c-section c-section__header">[\s\S]*?<!-- END sections: app-group -->',
        HEADER_HTML + '\n<!-- END sections: app-group -->',
        c
    )
    # Also handle if app-group comment not present
    c = re.sub(
        r'<div id="shopify-section-header" class="shopify-section c-section c-section__header">[\s\S]*?(?=<main\b)',
        HEADER_HTML + '\n',
        c
    )
    
    fpath.write_text(c, encoding='utf-8')
    print(f"✓ Replaced header in {p} with perfect standard header")

print("\n✅ Header successfully updated on all pages!")
