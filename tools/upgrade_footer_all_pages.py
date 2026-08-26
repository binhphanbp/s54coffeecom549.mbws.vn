#!/usr/bin/env python3
"""
Upgrade Footer across all 6 pages with pixel-perfect UX/UI:
- S54 COFFEE & Good Solutions Co., Ltd full legal information
- Structured 4-column e-commerce footer layout
- Direct links to products, story, B2B wholesale, contact
- Newsletter subscription form with interactive feedback
- Social icons (Facebook, Zalo, YouTube)
- Domestic & International payment badges (COD, Chuyển khoản, VNPAY, Momo, VISA)
- Footer language switcher
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FOOTER_HTML = '''<div id="shopify-section-footer" class="shopify-section c-section c-section__footer">
  <footer class="c-footer s54-footer" data-footer>
    <div class="s54-footer__container">
      
      <!-- Top Grid: 4 Clean Columns -->
      <div class="s54-footer__grid">
        
        <!-- Col 1: Brand Identity & Legal Info -->
        <div class="s54-footer__col s54-footer__col--brand">
          <a href="index.html" class="s54-footer__logo-link">
            <img src="assets/images/s54/s54_logo.png" alt="S54 COFFEE" class="s54-footer__logo-img" />
          </a>
          <p class="s54-footer__company-name">CÔNG TY TNHH GIẢI PHÁP TỐT</p>
          <p class="s54-footer__brand-tagline">"New Coffee, New Income" — Tinh hoa cà phê Việt rang mộc thượng hạng từ năm 2012.</p>
          
          <ul class="s54-footer__contact-list">
            <li>
              <span class="s54-footer__contact-icon">📍</span>
              <span>Số 35, Đường T8, Manhattan, Vinhomes Grand Park, P. Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh</span>
            </li>
            <li>
              <span class="s54-footer__contact-icon">📞</span>
              <span>Hotline: <a href="tel:0383707578">0383.707.578</a> — <a href="tel:0902873345">0902.873.345</a></span>
            </li>
            <li>
              <span class="s54-footer__contact-icon">✉️</span>
              <span>Email: <a href="mailto:pm@goodsolutions.com.vn">pm@goodsolutions.com.vn</a></span>
            </li>
            <li>
              <span class="s54-footer__contact-icon">🌐</span>
              <span>Website: <a href="https://goodsolutions.com.vn" target="_blank" rel="noopener">goodsolutions.com.vn</a></span>
            </li>
          </ul>
        </div>

        <!-- Col 2: Sản Phẩm & Mua Sắm -->
        <div class="s54-footer__col">
          <h4 class="s54-footer__heading">Sản Phẩm S54</h4>
          <ul class="s54-footer__links">
            <li><a href="collections-coffee.html">Tất Cả Sản Phẩm</a></li>
            <li><a href="collections-coffee.html">S54 Robusta Rang Mộc</a></li>
            <li><a href="collections-coffee.html">S54 Arabica Cầu Đất</a></li>
            <li><a href="collections-coffee.html">Cà Phê Hòa Tan 3in1 (456g)</a></li>
            <li><a href="collections-coffee.html">Cà Phê Sấy Lạnh Cao Cấp</a></li>
            <li><a href="collections-coffee.html">Cà Phê Túi Lọc Drip Bag</a></li>
            <li><a href="collections-coffee.html">Cà Phê Xay Pha Phin</a></li>
          </ul>
        </div>

        <!-- Col 3: Về S54 & Dịch Vụ -->
        <div class="s54-footer__col">
          <h4 class="s54-footer__heading">Về S54 & Dịch Vụ</h4>
          <ul class="s54-footer__links">
            <li><a href="our-story.html">Câu Chuyện Thương Hiệu</a></li>
            <li><a href="our-story.html">Nông Trại & Công Nghệ Rang</a></li>
            <li><a href="wholesale.html">Cung Ứng B2B & Đại Lý</a></li>
            <li><a href="wholesale.html">Gia Công OEM/ODM Xuất Khẩu</a></li>
            <li><a href="wholesale.html">Chính Sách Vận Chuyển</a></li>
            <li><a href="wholesale.html">Chính Sách Đổi Trả & Bảo Mật</a></li>
            <li><a href="wholesale.html">Liên Hệ Hợp Tác</a></li>
          </ul>
        </div>

        <!-- Col 4: Đăng Ký Nhận Tin & Kết Nối -->
        <div class="s54-footer__col s54-footer__col--newsletter">
          <h4 class="s54-footer__heading">Đăng Ký Nhận Ưu Đãi</h4>
          <p class="s54-footer__newsletter-desc">Nhận ngay voucher ưu đãi 15% cho đơn hàng đầu tiên cùng cẩm nang pha chế độc quyền từ S54 Coffee.</p>
          
          <form class="s54-footer__form" onsubmit="event.preventDefault(); alert('Cảm ơn bạn đã đăng ký nhận tin từ S54 Coffee!');">
            <div class="s54-footer__input-wrap">
              <input type="email" class="s54-footer__input" placeholder="Nhập địa chỉ email của bạn..." required />
              <button type="submit" class="s54-footer__submit-btn" aria-label="Đăng ký">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
            </div>
          </form>

          <div class="s54-footer__social-wrap">
            <span class="s54-footer__social-title">Kết Nối Với Chúng Tôi:</span>
            <div class="s54-footer__social-icons">
              <a href="https://facebook.com/goodsolutions.vn" target="_blank" rel="noopener" class="s54-footer__social-btn" aria-label="Facebook">
                <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
              </a>
              <a href="https://zalo.me/0383707578" target="_blank" rel="noopener" class="s54-footer__social-btn" aria-label="Zalo">
                <span style="font-weight: 800; font-size: 11px;">Zalo</span>
              </a>
              <a href="https://youtube.com" target="_blank" rel="noopener" class="s54-footer__social-btn" aria-label="YouTube">
                <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Bar: Legal Copyright, Payment Badges & Language Switcher -->
      <div class="s54-footer__bottom">
        <div class="s54-footer__copyright">
          © 2026 <strong>S54 COFFEE</strong> by <strong>Good Solutions Co., Ltd</strong>. Giữ toàn quyền bản quyền.
        </div>
        
        <div class="s54-footer__payments">
          <span class="s54-footer__pay-badge">Chuyển Khoản</span>
          <span class="s54-footer__pay-badge">COD</span>
          <span class="s54-footer__pay-badge">VNPAY</span>
          <span class="s54-footer__pay-badge">Momo</span>
          <span class="s54-footer__pay-badge">VISA</span>
          <span class="s54-footer__pay-badge">Mastercard</span>
        </div>

        <div class="c-lang-switcher c-lang-switcher--footer" data-lang-switcher>
          <button type="button" class="c-lang-btn is-active" data-lang="vi" aria-label="Tiếng Việt">🇻🇳 Tiếng Việt</button>
          <span class="c-lang-divider">|</span>
          <button type="button" class="c-lang-btn" data-lang="en" aria-label="English">🇬🇧 English</button>
        </div>
      </div>

    </div>
  </footer>
</div>'''

pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    
    # Replace shopify-section-footer block
    c = re.sub(
        r'<div id="shopify-section-footer" class="shopify-section c-section c-section__footer">[\s\S]*?</div>(?=\s*<div id="shopify-section-cart-drawer"|\s*<div id="md-footer-selector-block"|\s*<!-- BEGIN app snippet -->|\s*<script|\s*</body|\Z)',
        FOOTER_HTML,
        c
    )
    
    fpath.write_text(c, encoding='utf-8')
    print(f"✓ Upgraded footer in {p}")

print("\n✅ All pages upgraded with luxury S54 Footer!")
