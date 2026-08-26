#!/usr/bin/env python3
"""
Upgrade our-story.html and wholesale.html with high-contrast, luxury S54 Page Hero
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update custom.css with .s54-page-hero
css_path = BASE_DIR / 'assets/css/custom.css'
css = css_path.read_text(encoding='utf-8')

hero_css = '''
/* ==========================================================================
   Master S54 Page Hero (Our Story, Wholesale, Collections)
   High-contrast, pure white typography, rich dark espresso gradient
   ========================================================================== */
.s54-page-hero {
    position: relative;
    width: 100%;
    min-height: 440px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 80px 6% 70px;
    overflow: hidden;
    background-color: #1A110C;
    box-sizing: border-box;
}

.s54-page-hero__bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    transform: scale(1.02);
    z-index: 1;
}

.s54-page-hero__overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(26, 17, 12, 0.95) 0%, rgba(35, 23, 16, 0.82) 48%, rgba(26, 17, 12, 0.6) 100%);
    z-index: 2;
}

.s54-page-hero__container {
    position: relative;
    z-index: 3;
    max-width: 920px;
    margin: 0;
    text-align: left;
}

.s54-page-hero__tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    background: rgba(214, 142, 29, 0.18);
    border: 1px solid rgba(214, 142, 29, 0.45);
    border-radius: 30px;
    color: #F4C472;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
    backdrop-filter: blur(8px);
}

.s54-page-hero__tag-dot {
    width: 7px;
    height: 7px;
    background-color: #D68E1D;
    border-radius: 50%;
    box-shadow: 0 0 8px #D68E1D;
}

.s54-page-hero__title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 54px !important;
    font-weight: 700 !important;
    line-height: 1.15 !important;
    color: #FFFFFF !important;
    margin: 0 0 16px !important;
    letter-spacing: -0.5px !important;
    text-shadow: 0 2px 14px rgba(0, 0, 0, 0.5) !important;
}

.s54-page-hero__subtitle {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 16px !important;
    font-weight: 400 !important;
    line-height: 1.7 !important;
    color: #E6D7C3 !important;
    margin: 0 0 28px !important;
    max-width: 760px !important;
    text-shadow: 0 1px 8px rgba(0, 0, 0, 0.4) !important;
}

.s54-page-hero__badges {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.s54-page-hero__badge {
    display: inline-flex;
    align-items: center;
    padding: 8px 18px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 6px;
    color: #FAF8F5;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    backdrop-filter: blur(10px);
}

@media (max-width: 768px) {
    .s54-page-hero {
        min-height: 380px;
        padding: 50px 20px 45px;
    }
    .s54-page-hero__title {
        font-size: 36px !important;
    }
    .s54-page-hero__subtitle {
        font-size: 14.5px !important;
    }
    .s54-page-hero__badge {
        font-size: 12px;
        padding: 6px 14px;
    }
}
'''

if '.s54-page-hero' not in css:
    css += '\n' + hero_css
    css_path.write_text(css, encoding='utf-8')
    print("✓ Added .s54-page-hero styles to custom.css")

# 2. Upgrade our-story.html hero banner
os_path = BASE_DIR / 'our-story.html'
os_txt = os_path.read_text(encoding='utf-8')

story_hero_html = '''<section class="s54-page-hero s54-page-hero--story">
  <div class="s54-page-hero__bg" style="background-image: url('assets/images/s54/story_hero_heritage.jpg');"></div>
  <div class="s54-page-hero__overlay"></div>
  <div class="s54-page-hero__container">
    <div class="s54-page-hero__tag">
      <span class="s54-page-hero__tag-dot"></span>
      <span>HÀNH TRÌNH 12+ NĂM DI SẢN (2012 - 2026)</span>
    </div>
    <h1 class="s54-page-hero__title">Câu Chuyện Thương Hiệu S54</h1>
    <p class="s54-page-hero__subtitle">Hành trình hơn 12 năm kiến tạo giá trị từ Công ty TNHH Giải Pháp Tốt (Good Solutions), chuẩn hóa nguồn cà phê sạch nguyên chất từ vùng đất đỏ Tây Nguyên và lan tỏa tinh hoa cà phê Việt.</p>
    <div class="s54-page-hero__badges">
      <span class="s54-page-hero__badge">🌱 Vùng Trồng Đắk Lắk & Cầu Đất</span>
      <span class="s54-page-hero__badge">🔥 Công Nghệ Rang Hot-Air Hiện Đại</span>
      <span class="s54-page-hero__badge">🤝 Đồng Hành Cùng Nông Dân Việt</span>
    </div>
  </div>
</section>'''

# Replace old hero section in our-story.html
os_txt = re.sub(r'<div id=\"shopify-section-template--15797741420719__b0567228-522c-42ea-9007-f312d0b5a8a7\"[\s\S]*?</section></div>', story_hero_html, os_txt)
os_path.write_text(os_txt, encoding='utf-8')
print("✓ Upgraded our-story.html with luxury story hero banner")

# 3. Upgrade wholesale.html hero banner
ws_path = BASE_DIR / 'wholesale.html'
ws_txt = ws_path.read_text(encoding='utf-8')

wholesale_hero_html = '''<section class="s54-page-hero s54-page-hero--wholesale">
  <div class="s54-page-hero__bg" style="background-image: url('assets/images/s54/wholesale_hero_b2b.jpg');"></div>
  <div class="s54-page-hero__overlay"></div>
  <div class="s54-page-hero__container">
    <div class="s54-page-hero__tag">
      <span class="s54-page-hero__tag-dot"></span>
      <span>GIẢI PHÁP CUNG ỨNG B2B TOÀN DIỆN</span>
    </div>
    <h1 class="s54-page-hero__title">Cung Ứng B2B & Đại Lý S54</h1>
    <p class="s54-page-hero__subtitle">Đối tác chiến lược cung ứng nguồn cà phê sạch nguyên chất, thiết bị máy pha chuyên nghiệp và chuyển giao kỹ thuật pha chế cho hơn 500+ chuỗi nhà hàng, khách sạn & quán cafe.</p>
    <div class="s54-page-hero__badges">
      <span class="s54-page-hero__badge">☕ Chiết Khấu Đại Lý Tới 35%</span>
      <span class="s54-page-hero__badge">📦 Gia Công OEM/ODM Xuất Khẩu</span>
      <span class="s54-page-hero__badge">🎓 Đào Tạo Barista Chuyên Nghiệp</span>
    </div>
  </div>
</section>'''

ws_txt = re.sub(r'<div id=\"shopify-section-template--15837242130607__426604da-c2e3-4dda-8755-b11c855308ee\"[\s\S]*?</section></div>', wholesale_hero_html, ws_txt)
ws_path.write_text(ws_txt, encoding='utf-8')
print("✓ Upgraded wholesale.html with luxury wholesale hero banner")

print("\n✅ All page hero banners are now breathtaking, ultra-high contrast, and 100% luxury S54 aesthetic!")
