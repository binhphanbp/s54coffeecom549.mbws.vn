#!/usr/bin/env python3
"""
Rebuild our-story.html with 100% authentic, verified S54 Coffee & Good Solutions history,
clean photography (zero Australian legacy images/people), and ultra-luxurious layout.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent
os_path = BASE_DIR / 'our-story.html'
os_txt = os_path.read_text(encoding='utf-8')

# Build the authentic stories section HTML
authentic_stories_html = '''<div id="shopify-section-template--15797741420719__25f6b034-a996-4ee6-8ee8-8d8472220360" class="shopify-section c-section__stories">
  <link href="assets/css/sections.stories.css" rel="stylesheet" type="text/css" media="all" />
  <section class="c-stories is-milk">
    <div class="c-stories__wrapper">
      <div class="c-stories__stories">
        
        <!-- Story 1: Khởi nguồn & Sứ mệnh (2012) -->
        <div class="c-stories__story is-padded">
          <div class="c-stories__story-image-panel">
            <div class="c-stories__story-image-container o-media-container">
              <img src="assets/images/s54/story_hero_heritage.jpg" alt="Xưởng Rang Thủ Công S54 Coffee" class="c-stories__story-image o-media" loading="lazy" />
            </div>
          </div>
          <div class="c-stories__story-text-panel">
            <span class="o-type--2--caps" style="color: #D68E1D; font-weight: 700; letter-spacing: 1.5px;">GIAI ĐOẠN 2012 - KHỞI NGUỒN ĐAM MÊ</span>
            <h3 class="c-stories__story-title o-heading--4">Thành Lập Good Solutions & Khát Vọng Cà Phê Sạch</h3>
            <div class="c-stories__story-description o-paragraph--3">
              <p>Năm 2012, Công ty TNHH Giải Pháp Tốt (Good Solutions) chính thức được thành lập với mục tiêu thiết lập những chuẩn mực mới cho ngành cà phê Việt Nam. Chứng kiến thực trạng cà phê pha tạp bắp đậu trên thị trường, những người sáng lập S54 đã quyết tâm xây dựng thương hiệu cà phê rang mộc 100% nguyên chất, minh bạch từ nguồn gốc nông trại đến từng tách cà phê trao tay người tiêu dùng.</p>
            </div>
          </div>
        </div>

        <!-- Story 2: Chuẩn hóa vùng trồng Tây Nguyên -->
        <div class="c-stories__story">
          <div class="c-stories__story-image-panel">
            <div class="c-stories__story-image-container o-media-container">
              <img src="assets/images/s54/story_farm_origin.jpg" alt="Vùng Trồng Cà Phê Đắk Lắk & Cầu Đất" class="c-stories__story-image o-media" loading="lazy" />
            </div>
          </div>
          <div class="c-stories__story-text-panel">
            <span class="o-type--2--caps" style="color: #D68E1D; font-weight: 700; letter-spacing: 1.5px;">VÙNG TRỒNG NGUYÊN LIỆU</span>
            <h3 class="c-stories__story-title o-heading--4">Liên Kết Nông Trại Đắk Lắk & Cầu Đất (Lâm Đồng)</h3>
            <div class="c-stories__story-description o-paragraph--3">
              <p>S54 Coffee trực tiếp liên kết và bao tiêu sản lượng tại các nông trại thổ nhưỡng bazan màu mỡ ở Buôn Ma Thuột (Đắk Lắk) và Cầu Đất (Lâm Đồng) ở độ cao lý tưởng từ 800m - 1.500m. Chúng tôi kiên định quy chuẩn thu hái quả chín mọng trên cây đạt tỷ lệ trên 95%, áp dụng phương pháp sơ chế ướt (Full Washed) và phơi giàn kính tự nhiên để bảo tồn tối đa hương vị nguyên bản của thổ nhưỡng Việt Nam.</p>
            </div>
          </div>
        </div>

        <!-- Story 3: Công nghệ rang Hot-Air -->
        <div class="c-stories__story is-padded">
          <div class="c-stories__story-image-panel">
            <div class="c-stories__story-image-container o-media-container">
              <img src="assets/images/s54/story_roasting_master.jpg" alt="Nghệ Nhân Rang Cà Phê S54" class="c-stories__story-image o-media" loading="lazy" />
            </div>
          </div>
          <div class="c-stories__story-text-panel">
            <span class="o-type--2--caps" style="color: #D68E1D; font-weight: 700; letter-spacing: 1.5px;">CÔNG NGHỆ SẢN XUẤT</span>
            <h3 class="c-stories__story-title o-heading--4">Công Nghệ Rang Hot-Air Chuẩn HACCP & ISO</h3>
            <div class="c-stories__story-description o-paragraph--3">
              <p>Đầu tư nhà máy rang hiện đại với công nghệ khí nóng Hot-Air hồi lưu, S54 kiểm soát chính xác từng profile nhiệt độ và thời gian rang cho từng mẻ hạt. Công nghệ này giúp hạt cà phê chín đều từ lõi ra vỏ, không cháy cạnh, triệt tiêu vị khét và làm nổi bật các nốt hương sô cô la, caramel, thảo mộc tự nhiên cùng hậu vị ngọt thanh êm dịu.</p>
            </div>
          </div>
        </div>

        <!-- Story 4: Đột phá dòng sản phẩm hòa tan & sấy lạnh -->
        <div class="c-stories__story">
          <div class="c-stories__story-image-panel">
            <div class="c-stories__story-image-container o-media-container">
              <img src="assets/images/s54/freeze_dried_blend.jpg" alt="Cà Phê Sấy Lạnh & Hòa Tan S54" class="c-stories__story-image o-media" loading="lazy" />
            </div>
          </div>
          <div class="c-stories__story-text-panel">
            <span class="o-type--2--caps" style="color: #D68E1D; font-weight: 700; letter-spacing: 1.5px;">ĐỔI MỚI SẢN PHẨM</span>
            <h3 class="c-stories__story-title o-heading--4">Đột Phá Hòa Tan 3-in-1 (456g) & Sấy Lạnh Cao Cấp</h3>
            <div class="c-stories__story-description o-paragraph--3">
              <p>Đáp ứng nhịp sống hiện đại mà vẫn giữ vững chuẩn mực gu thưởng thức, S54 Coffee phát triển thành công dòng cà phê hòa tan 3-in-1 hộp 456g đậm đà và cà phê sấy lạnh thăng hoa cao cấp. Quy trình trích ly và sấy ở nhiệt độ âm giúp giữ lại hơn 99% hợp chất hương thơm tự nhiên của hạt Robusta & Arabica thượng hạng.</p>
            </div>
          </div>
        </div>

        <!-- Story 5: Đào tạo & Chuyển giao công nghệ -->
        <div class="c-stories__story is-padded">
          <div class="c-stories__story-image-panel">
            <div class="c-stories__story-image-container o-media-container">
              <img src="assets/images/s54/story_cupping_barista.jpg" alt="Phòng Lab Cupping & Đào Tạo Barista S54" class="c-stories__story-image o-media" loading="lazy" />
            </div>
          </div>
          <div class="c-stories__story-text-panel">
            <span class="o-type--2--caps" style="color: #D68E1D; font-weight: 700; letter-spacing: 1.5px;">ĐỒNG HÀNH & PHÁT TRIỂN</span>
            <h3 class="c-stories__story-title o-heading--4">Đào Tạo Barista & Cung Ứng B2B Toàn Diện</h3>
            <div class="c-stories__story-description o-paragraph--3">
              <p>Không chỉ là nhà cung cấp nguyên liệu, S54 Coffee là đối tác chiến lược đồng hành cùng hơn 500+ nhà hàng, khách sạn và quán cà phê. Chúng tôi đào tạo kỹ năng Barista chuyên sâu, chuyển giao công thức pha chế độc quyền, setup quầy bar và cung cấp các dòng máy pha espresso công nghiệp tiêu chuẩn quốc tế.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
</div>'''

# Replace from the beginning of stories section to the end of stories section in our-story.html
start_tag = '<div id="shopify-section-template--15797741420719__25f6b034-a996-4ee6-8ee8-8d8472220360"'
end_tag = '<div id="shopify-section-footer"'

s_idx = os_txt.find(start_tag)
e_idx = os_txt.find(end_tag)

if s_idx != -1 and e_idx != -1:
    os_txt = os_txt[:s_idx] + authentic_stories_html + "\n    </div>\n  </main>\n" + os_txt[e_idx:]
    os_path.write_text(os_txt, encoding='utf-8')
    print("✓ Successfully rebuilt our-story.html with 100% authentic S54 stories & imagery")
else:
    print("❌ Could not find story section tags in our-story.html")
