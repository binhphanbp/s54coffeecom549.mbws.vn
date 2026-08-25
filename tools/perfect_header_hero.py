#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update index.html Hero Banner Image to clean high-res hero asset
index_file = BASE_DIR / 'index.html'
c = index_file.read_text(encoding='utf-8')

# Replace banner_main.jpg in hero banner with pristine 132_vit-homepage-banner-desktop-2_2560x.jpg
hero_pattern = r'(<section class="c-hero-banner[\s\S]*?</section>)'

clean_hero = '''<section class="c-hero-banner is-large is-homepage">
  <div class="c-hero-banner__media-container o-media-container">
    <picture>
      <source media="(max-width:750px)" srcset="assets/images/016_vit-homepage-banner-mobile-2_750x.jpg">
      <source media="(min-width:751px)" srcset="assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg">
      <img src="assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg" alt="S54 Coffee Hero Banner" class="c-hero-banner__media o-media" />
    </picture>
    <div class="c-hero-banner__overlay s54-hero-overlay">
      <div class="s54-hero-badge">✨ 100% CÀ PHÊ RANG MỘC NGUYÊN CHẤT</div>
      <h1 class="c-hero-banner__title s54-hero-title">S54 COFFEE<br><span>Tinh Hoa Cà Phê Việt®</span></h1>
      <p class="s54-hero-subtitle">Tuyển chọn từ những hạt cà phê Robusta & Arabica hảo hạng nhất từ vùng đất đỏ bazan Tây Nguyên. Rang mộc truyền thống, đậm đà chuẩn vị.</p>
      <div class="s54-hero-actions">
        <a href="collections-coffee.html" class="s54-btn s54-btn--primary">MUA SẮM NGAY <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        <a href="our-story.html" class="s54-btn s54-btn--secondary">VỀ CHÚNG TÔI</a>
      </div>
    </div>
  </div>
</section>'''

c = re.sub(r'<section class="c-hero-banner is-large[\s\S]*?</section>', clean_hero, c)
index_file.write_text(c, encoding='utf-8')
print("✓ Updated Hero Section in index.html with clean, high-contrast, textless background!")

