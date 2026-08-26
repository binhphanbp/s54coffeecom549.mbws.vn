#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update collections-coffee.html hero section
coll_path = BASE_DIR / 'collections-coffee.html'
coll_html = coll_path.read_text(encoding='utf-8')

hero_pattern = r'<section\s+class=\"c-hero-banner[\s\S]*?</section>'

perfect_hero = '''<section class="c-hero-banner s54-coll-hero">
  <div class="s54-coll-hero__bg">
    <img src="assets/images/s54/collection_hero_beans.jpg" alt="S54 Cà Phê Hạt Rang Mộc" class="s54-coll-hero__img">
    <div class="s54-coll-hero__gradient"></div>
  </div>
  <div class="s54-coll-hero__content">
    <nav class="o-breadcrumbs s54-coll-hero__breadcrumbs" role="navigation" aria-label="breadcrumbs">
      <a href="index.html">Trang Chủ</a>
      <span class="s54-coll-hero__divider">/</span>
      <span class="s54-coll-hero__active-crumb">Cà Phê Hạt Rang Mộc</span>
    </nav>
    <h1 class="s54-coll-hero__title">
      Cà Phê Hạt Rang Mộc Thượng Hạng
    </h1>
    <p class="s54-coll-hero__subtitle">
      Khám phá các dòng cà phê hạt Robusta & Arabica nguyên chất thượng hạng S54. Tuyển chọn từ thủ phủ cà phê Tây Nguyên, rang mộc 100% không tẩm ướp hương liệu, giữ trọn hương thơm mộc mạc và hậu vị ngọt sâu đậm đà.
    </p>
    <div class="s54-coll-hero__badges">
      <span class="s54-coll-hero__badge">☕ 100% Rang Mộc Tự Nhiên</span>
      <span class="s54-coll-hero__badge">🌿 Nông Sản Cao Nguyên Việt Nam</span>
      <span class="s54-coll-hero__badge">🚚 Freeship Đơn Từ 599.000₫</span>
    </div>
  </div>
</section>'''

coll_html = re.sub(hero_pattern, perfect_hero, coll_html)
coll_path.write_text(coll_html, encoding='utf-8')
print("✓ Updated collections-coffee.html with clean dedicated class hero banner")

# 2. Add high-contrast CSS rules in custom.css
css_path = BASE_DIR / 'assets/css/custom.css'
css_content = css_path.read_text(encoding='utf-8')

hero_css = '''
/* ==========================================================================
   S54 COLLECTION HERO BANNER - MASTER HIGH-CONTRAST LUXURY STYLES
   ========================================================================== */
.s54-coll-hero {
    position: relative !important;
    background-color: #1A110C !important;
    min-height: 380px !important;
    display: flex !important;
    align-items: center !important;
    overflow: hidden !important;
    border-bottom: 1px solid #2F221A !important;
}

.s54-coll-hero__bg {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    z-index: 1 !important;
}

.s54-coll-hero__img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center !important;
    filter: brightness(0.45) !important;
}

.s54-coll-hero__gradient {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, rgba(26,17,12,0.94) 0%, rgba(26,17,12,0.80) 50%, rgba(26,17,12,0.45) 100%) !important;
}

.s54-coll-hero__content {
    position: relative !important;
    z-index: 2 !important;
    width: 100% !important;
    max-width: 1280px !important;
    margin: 0 auto !important;
    padding: 64px 32px 56px !important;
}

.s54-coll-hero__breadcrumbs {
    margin-bottom: 16px !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

.s54-coll-hero__breadcrumbs a {
    color: #D8CEBE !important;
    text-decoration: none !important;
    transition: color 0.2s ease !important;
}

.s54-coll-hero__breadcrumbs a:hover {
    color: #E2B96B !important;
}

.s54-coll-hero__divider {
    color: #AC8A62 !important;
}

.s54-coll-hero__active-crumb {
    color: #E2B96B !important;
    font-weight: 600 !important;
}

.s54-coll-hero__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 52px !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    margin: 0 0 16px !important;
    line-height: 1.15 !important;
    text-shadow: 0 2px 16px rgba(0,0,0,0.6) !important;
}

.s54-coll-hero__subtitle {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 15.5px !important;
    line-height: 1.65 !important;
    color: #FAF5EE !important;
    max-width: 680px !important;
    margin: 0 0 24px !important;
    font-weight: 400 !important;
    text-shadow: 0 1px 6px rgba(0,0,0,0.5) !important;
}

.s54-coll-hero__badges {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 12px !important;
    align-items: center !important;
}

.s54-coll-hero__badge {
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    padding: 7px 16px !important;
    background: rgba(255,255,255,0.12) !important;
    border: 1px solid rgba(226,185,107,0.45) !important;
    border-radius: 20px !important;
    color: #FFFFFF !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    backdrop-filter: blur(6px) !important;
    -webkit-backdrop-filter: blur(6px) !important;
}

@media (max-width: 767px) {
    .s54-coll-hero {
        min-height: 320px !important;
    }
    .s54-coll-hero__content {
        padding: 40px 20px 32px !important;
    }
    .s54-coll-hero__title {
        font-size: 34px !important;
    }
    .s54-coll-hero__subtitle {
        font-size: 14px !important;
    }
}
'''

if '.s54-coll-hero__title' not in css_content:
    css_content += hero_css
else:
    # replace existing block
    css_content = re.sub(r'/\* ==========================================================================\s*S54 COLLECTION HERO BANNER[\s\S]*?@media \(max-width: 767px\) \{[\s\S]*?\}\s*\}', hero_css.strip(), css_content)

css_path.write_text(css_content, encoding='utf-8')
print("✓ Added pure high-contrast master CSS for collection hero")

print("✅ Collection Hero Banner completely perfected!")
