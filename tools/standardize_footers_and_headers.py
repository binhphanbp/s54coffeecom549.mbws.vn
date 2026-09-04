#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standardize header navigation and footer across all HTML pages for S54 Coffee:
1. Header menu includes:
   - Tất Cả Sản Phẩm (collections-coffee.html)
   - Cà Phê Hạt & Rang Mộc (collections-coffee.html)
   - Hòa Tan & Sấy Lạnh (collections-coffee.html)
   - Câu Chuyện S54 (our-story.html)
   - Tin Tức & Blog (blogs-news.html)
   - B2B & Đại Lý (wholesale.html)
   - Liên Hệ (contact.html)
2. Footer links:
   - Chính Sách Vận Chuyển -> policy-shipping.html
   - Chính Sách Đổi Trả & Bảo Mật -> policy-returns.html
   - Chính Sách Bảo Mật -> policy-privacy.html
   - Liên Hệ Hợp Tác -> contact.html
3. Language switcher and Cart trigger remain 100% active.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

html_files = [
    'index.html', 'our-story.html', 'collections-coffee.html',
    'blogs-news.html', 'blog-detail.html', 'wholesale.html',
    'product-detail.html', 'checkout.html', 'cart.html', 'contact.html',
    'policy-shipping.html', 'policy-returns.html', 'policy-privacy.html'
]

menu_items = '''          <li class="c-main-menu__item is-level-1"><a href="collections-coffee.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">Sản Phẩm</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="our-story.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">Câu Chuyện S54</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="blogs-news.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">Tin Tức</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="wholesale.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">B2B & Đại Lý</span></a></li>
          <li class="c-main-menu__item is-level-1"><a href="contact.html" class="c-main-menu__link is-level-1"><span class="c-main-menu__link-title">Liên Hệ</span></a></li>'''

footer_service_col = '''          <h4 class="s54-footer__heading">Về S54 & Dịch Vụ</h4>
          <ul class="s54-footer__links">
            <li><a href="our-story.html">Câu Chuyện Thương Hiệu</a></li>
            <li><a href="blogs-news.html">Bản Tin & Tri Thức Cà Phê</a></li>
            <li><a href="wholesale.html">Cung Ứng B2B & Đại Lý</a></li>
            <li><a href="policy-shipping.html">Chính Sách Vận Chuyển</a></li>
            <li><a href="policy-returns.html">Chính Sách Đổi Trả & Bảo Hành</a></li>
            <li><a href="policy-privacy.html">Chính Sách Bảo Mật</a></li>
            <li><a href="contact.html">Liên Hệ Hợp Tác</a></li>
          </ul>'''

for fname in html_files:
    fpath = BASE_DIR / fname
    if not fpath.exists():
        continue
    
    content = fpath.read_text(encoding='utf-8')
    
    # 1. Update Menu items
    content = re.sub(
        r'<ul class="c-main-menu__list is-level-1">[\s\S]*?</ul>',
        f'<ul class="c-main-menu__list is-level-1">\n{menu_items}\n        </ul>',
        content
    )
    
    # 2. Update Footer Col 3 (Về S54 & Dịch Vụ)
    content = re.sub(
        r'<h4 class="s54-footer__heading">Về S54 & Dịch Vụ</h4>\s*<ul class="s54-footer__links">[\s\S]*?</ul>',
        footer_service_col,
        content
    )
    
    # 3. Direct replacement of any remaining broken footer links
    content = content.replace('href="wholesale.html">Chính Sách Vận Chuyển</a>', 'href="policy-shipping.html">Chính Sách Vận Chuyển</a>')
    content = content.replace('href="wholesale.html">Chính Sách Đổi Trả & Bảo Mật</a>', 'href="policy-returns.html">Chính Sách Đổi Trả & Bảo Hành</a>')
    content = content.replace('href="wholesale.html">Liên Hệ Hợp Tác</a>', 'href="contact.html">Liên Hệ Hợp Tác</a>')
    
    fpath.write_text(content, encoding='utf-8')
    print(f"Standardized {fname}")

print("All headers and footers standardized successfully!")
