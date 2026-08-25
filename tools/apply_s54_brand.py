#!/usr/bin/env python3
"""
Apply S54 COFFEE / Good Solutions client brand data across the entire website.
- Brand: S54 COFFEE
- Company: CÔNG TY TNHH GIẢI PHÁP TỐT (Good Solutions Co., Ltd)
- Address: Số 35, Đường T8, Manhattan, Vinhomes Grand Park, Phường Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh
- Hotline: (+84) 383 707 578 - (+84) 902 873 345
- Email: pm@goodsolutions.com.vn
- Products: S54 Robusta, S54 Arabica, S54 Instant 3in1, S54 Freeze-Dried Blend
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print("=" * 70)
print("  Applying S54 Coffee & Good Solutions Client Data")
print("=" * 70)

# =====================================================================
# 1. Update index.html
# =====================================================================
index_file = BASE_DIR / 'index.html'
if index_file.exists():
    c = index_file.read_text(encoding='utf-8')
    
    # Title & Meta
    c = re.sub(r'<title>.*?</title>', '<title>S54 COFFEE - Cà Phê Rang Xay & Hòa Tan Thượng Hạng | Good Solutions</title>', c)
    c = re.sub(r'content="Australia&#39;s No\.1 pure coffee brand.*?"', 'content="S54 COFFEE - Thương hiệu cà phê nguyên chất thượng hạng của Công ty TNHH Giải Pháp Tốt. Cung cấp cà phê hạt rang mộc, cà phê hòa tan 3in1, cà phê sấy lạnh và dịch vụ B2B toàn quốc."', c)
    c = re.sub(r'content="Vittoria Coffee"', 'content="S54 COFFEE"', c)
    
    # Topbar message
    c = re.sub(r'MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ \$69†', 'MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578', c)
    
    # Logos
    c = re.sub(r'assets/images/133_Vittoria_Coffee_Logo_Gold_400x\.svg', 'assets/images/s54/s54_logo.png', c)
    c = re.sub(r'title="Vittoria Coffee"', 'title="S54 COFFEE"', c)
    
    # Hero Banner
    c = re.sub(r'Chuyên Gia Cà Phê Số 1®', 'S54 COFFEE - Tinh Hoa Cà Phê Việt®', c)
    c = re.sub(r'assets/images/207_vit-homepage-banner-mobile-2_1x\.jpg', 'assets/images/s54/banner_main.jpg', c)
    c = re.sub(r'assets/images/159_vit-homepage-banner-desktop_1920x\.jpg', 'assets/images/s54/banner_main.jpg', c)
    
    # Product Carousel Header & Quote
    c = re.sub(r'<span>Khám Phá <em><br/></em>Dòng Sản Phẩm</span>', '<span>Khám Phá <em><br/></em>Dòng Cà Phê S54</span>', c)
    c = re.sub(r'“Khát vọng của chúng tôi là mang đến cho người yêu cà phê những hạt cà phê rang tươi mới và thượng hạng nhất ở mọi định dạng thưởng thức\.”<br/><strong><br/>Les Schirato, Giám Đốc Điều Hành \(CEO\)</strong>', '“S54 Coffee mang đến giải pháp cà phê sạch nguyên chất, đậm đà vị truyền thống và phong cách hiện đại cho hàng triệu người tiêu dùng.”<br/><strong><br/>Mr. Paul Hieu (CEO) & Tony Hoan (Founder)</strong>', c)
    
    # Carousel Product Tiles
    c = re.sub(r'assets/images/049_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_500x\.png', 'assets/images/s54/robusta_1.jpg', c)
    c = re.sub(r'assets/images/091_MicrosoftTeams-image_279_500x\.png', 'assets/images/s54/arabica_beans.jpg', c)
    c = re.sub(r'assets/images/151_ground_1kg_esp_f_R_Car_3_500x\.png', 'assets/images/s54/robusta_2.jpg', c)
    c = re.sub(r'assets/images/014_inst_100g_clas_f_V2_d7df202b-71d9-4a81-a29d-9af211d42e34_500x\.png', 'assets/images/s54/instant_3in1_1.jpg', c)
    c = re.sub(r'assets/images/247_bag_20pack_esp_f_V2_500x\.png', 'assets/images/s54/freeze_dried_blend.jpg', c)
    
    # Roasting Expertise Section
    c = re.sub(r'Hơn 65 Năm Kinh Nghiệm Rang Xay Thủ Công', 'Hơn 12 Năm Kinh Nghiệm & Đam Mê Cà Phê Sạch', c)
    c = re.sub(r'assets/images/083_230919_Vittoria_Silverwater_R_45_2000x\.jpg', 'assets/images/s54/roasting_facility.png', c)
    c = re.sub(r'Được thành lập vào năm 1958 tại Úc.*?</p>', 'Thành lập từ năm 2012 bởi Công ty TNHH Giải Pháp Tốt (Good Solutions), S54 Coffee tự hào kế thừa tinh hoa cà phê Robusta & Arabica từ vùng đất đỏ bazan Tây Nguyên, ứng dụng công nghệ rang mộc hiện đại giữ trọn hương thơm tự nhiên và hậu vị sâu lắng.</p>', c)
    c = re.sub(r'Quy Trình Rang Xay', 'Về Chúng Tôi', c)
    
    # Video Section
    c = re.sub(r'Nghệ thuật chiết xuất tách Espresso hoàn hảo', 'Nghệ Thuật Thưởng Thức Cà Phê S54 Chuẩn Vị', c)
    c = re.sub(r'Cùng chuyên gia của chúng tôi khám phá các bước căn chỉnh máy pha.*?</p>', 'Khám phá bí quyết pha phin truyền thống đậm đà và pha máy tạo lớp crema vàng óng cùng S54 Coffee.</p>', c)
    
    # Italian Heritage / Story Section
    c = re.sub(r'Di Sản Nước Ý, Chế Tác Tại Nước Úc', 'Tinh Hoa Cà Phê Việt - New Coffee, New Income', c)
    c = re.sub(r'Từ năm 1958, gia đình Cantarella.*?</p>', 'Với triết lý "Thiết lập các giải pháp tốt nhất trong việc cung cấp Cà phê Chất lượng", Good Solutions đồng hành cùng người nông dân và khách hàng để xây dựng chuỗi giá trị cà phê bền vững vươn tầm thế giới.</p>', c)
    c = re.sub(r'Đọc Câu Chuyện Của Chúng Tôi', 'Khám Phá S54 Coffee', c)
    
    # Footer Info
    c = re.sub(r'Số 35, Đường T8.*?</p>', 'Số 35, Đường T8, Manhattan, Vinhomes Grand Park, P. Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh, Việt Nam</p>', c)
    
    # Replace Footer Copyright & Company Block
    footer_pattern = r'<div class="c-footer__bottom-bar">[\s\S]*?</div>\s*</div>'
    footer_replacement = '''<div class="c-footer__bottom-bar">
  <div class="c-footer__company-info" style="font-size: 12px; line-height: 1.6; color: #8C7B70;">
    <strong style="color: #2F221A; font-size: 13px;">CÔNG TY TNHH GIẢI PHÁP TỐT (GOOD SOLUTIONS CO., LTD)</strong><br>
    📍 Địa chỉ: Số 35, Đường T8, Manhattan, Vinhomes Grand Park, P. Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh<br>
    📞 Hotline: (+84) 383 707 578 - (+84) 902 873 345 | ✉️ Email: pm@goodsolutions.com.vn | 🌐 Website: goodsolutions.com.vn<br>
    &copy; 2026 S54 COFFEE by Good Solutions Co., Ltd. All rights reserved.
  </div>
  <div class="c-footer__payment-icons">
    <span class="c-footer__payment-badge">Chuyển Khoản</span>
    <span class="c-footer__payment-badge">COD</span>
    <span class="c-footer__payment-badge">VISA</span>
    <span class="c-footer__payment-badge">Mastercard</span>
    <span class="c-footer__payment-badge">VNPAY</span>
    <span class="c-footer__payment-badge">Momo</span>
  </div>
</div>'''
    c = re.sub(footer_pattern, footer_replacement, c)
    
    index_file.write_text(c, encoding='utf-8')
    print("  ✓ Updated index.html with S54 brand data")

# =====================================================================
# 2. Update our-story.html
# =====================================================================
story_file = BASE_DIR / 'our-story.html'
if story_file.exists():
    c = story_file.read_text(encoding='utf-8')
    c = re.sub(r'<title>.*?</title>', '<title>Về Chúng Tôi - Câu Chuyện Thương Hiệu S54 Coffee | Good Solutions</title>', c)
    c = re.sub(r'assets/images/133_Vittoria_Coffee_Logo_Gold_400x\.svg', 'assets/images/s54/s54_logo.png', c)
    c = re.sub(r'title="Vittoria Coffee"', 'title="S54 COFFEE"', c)
    c = re.sub(r'MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ \$69†', 'MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578', c)
    
    # Story Headings & Content
    c = re.sub(r'Hơn 65 Năm Đam Mê Cà Phê', 'Hơn 12 Năm Đồng Hành Cùng Hạt Cà Phê Việt', c)
    c = re.sub(r'Năm 1958, hai anh em Orazio và Carmelo Cantarella.*?</p>', 'Công ty TNHH Giải Pháp Tốt (Good Solutions Co., Ltd) được thành lập vào năm 2012 dưới sự lãnh đạo của Giám đốc điều hành Paul Hieu & Nhà sáng lập Tony Hoan. Với triết lý: "Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với dịch vụ khách hàng không ai sánh kịp", chúng tôi cam kết nâng tầm hạt cà phê Việt Nam đến khắp toàn cầu.</p>', c)
    
    story_file.write_text(c, encoding='utf-8')
    print("  ✓ Updated our-story.html with S54 brand data")

# =====================================================================
# 3. Update wholesale.html (B2B & Dịch Vụ Đại Lý)
# =====================================================================
ws_file = BASE_DIR / 'wholesale.html'
if ws_file.exists():
    c = ws_file.read_text(encoding='utf-8')
    c = re.sub(r'<title>.*?</title>', '<title>Chính Sách Đại Lý & Cung Ứng B2B - S54 Coffee | Good Solutions</title>', c)
    c = re.sub(r'assets/images/133_Vittoria_Coffee_Logo_Gold_400x\.svg', 'assets/images/s54/s54_logo.png', c)
    c = re.sub(r'title="Vittoria Coffee"', 'title="S54 COFFEE"', c)
    c = re.sub(r'MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ \$69†', 'MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578', c)
    
    # Wholesale Title & Description
    c = re.sub(r'Hợp Tác Bán Buôn & Cung Ứng Doanh Nghiệp', 'Dịch Vụ Cung Ứng Cà Phê B2B & Gia Công OEM/ODM', c)
    c = re.sub(r'Chúng tôi cung cấp giải pháp cà phê trọn gói cho quán cà phê, nhà hàng.*?</p>', 'Good Solutions cung cấp cà phê hạt rang mộc, cà phê hòa tan số lượng lớn cho quán cà phê, chuỗi F&B, khách sạn, văn phòng doanh nghiệp và dịch vụ gia công thương hiệu riêng (OEM/ODM) xuất khẩu quốc tế.</p>', c)
    
    ws_file.write_text(c, encoding='utf-8')
    print("  ✓ Updated wholesale.html with S54 brand data")

# =====================================================================
# 4. Update collections-coffee.html
# =====================================================================
coll_file = BASE_DIR / 'collections-coffee.html'
if coll_file.exists():
    c = coll_file.read_text(encoding='utf-8')
    c = re.sub(r'<title>.*?</title>', '<title>Tất Cả Sản Phẩm Cà Phê S54 Coffee | Good Solutions</title>', c)
    c = re.sub(r'assets/images/133_Vittoria_Coffee_Logo_Gold_400x\.svg', 'assets/images/s54/s54_logo.png', c)
    c = re.sub(r'MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ \$69†', 'MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578', c)
    
    coll_file.write_text(c, encoding='utf-8')
    print("  ✓ Updated collections-coffee.html with S54 brand data")

# =====================================================================
# 5. Update product-detail.html & 404.html
# =====================================================================
for p in ['product-detail.html', '404.html']:
    pf = BASE_DIR / p
    if pf.exists():
        c = pf.read_text(encoding='utf-8')
        c = re.sub(r'assets/images/133_Vittoria_Coffee_Logo_Gold_400x\.svg', 'assets/images/s54/s54_logo.png', c)
        c = re.sub(r'Vittoria Coffee', 'S54 COFFEE', c)
        pf.write_text(c, encoding='utf-8')
        print(f"  ✓ Updated {p} with S54 brand data")

# =====================================================================
# 6. Update main.js & i18n.js strings
# =====================================================================
main_js = BASE_DIR / 'assets' / 'js' / 'main.js'
if main_js.exists():
    c = main_js.read_text(encoding='utf-8')
    c = re.sub(r'freeShippingThreshold\s*=\s*69\.00', 'freeShippingThreshold = 599000', c)
    c = re.sub(r'Cinque Stelle Special Bar Beans', 'S54 Robusta Cà Phê Rang Mộc Nguyên Chất', c)
    c = re.sub(r'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x\.png', 'assets/images/s54/robusta_1.jpg', c)
    main_js.write_text(c, encoding='utf-8')
    print("  ✓ Updated main.js with S54 cart data")

print("\n✅ All pages and scripts successfully updated with S54 Coffee / Good Solutions brand data!")
