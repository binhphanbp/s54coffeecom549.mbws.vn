import re
import os

# 1. Update index.html hero section markup
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_hero_html = """<section class="c-hero-banner is-large is-homepage s54-hero-container">
  <div class="s54-hero-bg-wrapper">
    <picture>
      <source media="(max-width:750px)" srcset="assets/images/016_vit-homepage-banner-mobile-2_750x.jpg">
      <source media="(min-width:751px)" srcset="assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg">
      <img src="assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg" alt="S54 Coffee Hero Banner" class="s54-hero-bg-img" />
    </picture>
    <div class="s54-hero-gradient-overlay"></div>
  </div>

  <div class="s54-hero-content-wrapper">
    <div class="s54-hero-card">
      <div class="s54-hero-badge">
        <span class="s54-badge-sparkle">✨</span> THƯƠNG HIỆU CÀ PHÊ RANG MỘC TỪ 2012
      </div>
      
      <h1 class="s54-hero-title">
        NEW COFFEE,<br/>
        <span class="s54-hero-title-accent">NEW INCOME</span>
      </h1>
      
      <p class="s54-hero-tagline">Tinh Hoa Cà Phê Đất Đỏ Tây Nguyên — Hơn Cả Cà Phê</p>
      
      <p class="s54-hero-description">
        Tuyển chọn 100% hạt Robusta Đắk Lắk & Arabica Cầu Đất chín mọng, rang mộc công nghệ Hot-Air chuẩn Châu Âu. Đậm đà hương vị mộc truyền thống, trọn vẹn hậu vị ngọt sâu và nâng tầm giá trị cho đối tác.
      </p>

      <div class="s54-hero-actions">
        <a href="collections-coffee.html" class="s54-btn s54-btn--primary">
          <span>MUA SẮM NGAY</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="wholesale.html" class="s54-btn s54-btn--secondary">
          <span>HỢP TÁC B2B & ĐẠI LÝ</span>
        </a>
      </div>

      <div class="s54-hero-social-proof">
        <div class="s54-rating-stars">★★★★★</div>
        <div class="s54-rating-text"><strong>4.9/5</strong> từ hơn <strong>10.000+</strong> khách hàng & chuỗi quán tin dùng</div>
      </div>
    </div>
  </div>
</section>

<!-- S54 Value Highlights Strip -->
<div class="s54-features-strip">
  <div class="s54-features-container">
    <div class="s54-feature-item">
      <div class="s54-feature-icon">🌿</div>
      <div class="s54-feature-text">
        <h4 class="s54-feature-title">100% Rang Mộc Nguyên Chất</h4>
        <p class="s54-feature-desc">Không pha độn bắp, đậu nành hay hương liệu hóa học độc hại</p>
      </div>
    </div>
    
    <div class="s54-feature-item">
      <div class="s54-feature-icon">🔥</div>
      <div class="s54-feature-text">
        <h4 class="s54-feature-title">Công Nghệ Hot-Air Châu Âu</h4>
        <p class="s54-feature-desc">Hạt chín đều từ tâm, lưu giữ trọn vẹn tinh dầu & hương thơm mộc</p>
      </div>
    </div>
    
    <div class="s54-feature-item">
      <div class="s54-feature-icon">☕</div>
      <div class="s54-feature-text">
        <h4 class="s54-feature-title">Đa Dạng Gu Thưởng Thức</h4>
        <p class="s54-feature-desc">Cà phê hạt pha máy, pha phin, hòa tan 3-in-1, sấy lạnh thượng hạng</p>
      </div>
    </div>
    
    <div class="s54-feature-item">
      <div class="s54-feature-icon">🚚</div>
      <div class="s54-feature-text">
        <h4 class="s54-feature-title">Freeship Từ 599.000₫</h4>
        <p class="s54-feature-desc">Giao hàng nhanh toàn quốc, hỗ trợ đóng gói quà tặng cao cấp</p>
      </div>
    </div>
  </div>
</div>"""

# Replace hero banner section in index.html
pattern = r'<section class="c-hero-banner is-large is-homepage">[\s\S]*?<\/section>'
if re.search(pattern, html):
    html = re.sub(pattern, new_hero_html, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced Hero section in index.html")
else:
    print("Pattern not found in index.html, checking alternative...")

