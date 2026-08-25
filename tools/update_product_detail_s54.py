#!/usr/bin/env python3
import re
from pathlib import Path

pd_file = Path('product-detail.html')
c = pd_file.read_text(encoding='utf-8')

# Title & Headings
c = re.sub(r'<h1 class="c-product-main__title[^"]*">.*?</h1>', '<h1 class="c-product-main__title o-heading--2">S54 Robusta Cà Phê Rang Nguyên Chất</h1>', c)
c = re.sub(r'Cinque Stelle', 'S54 Robusta', c)

# Product Images
c = re.sub(r'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_.*?\.png', 'assets/images/s54/robusta_1.jpg', c)
c = re.sub(r'assets/images/049_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_.*?\.png', 'assets/images/s54/robusta_2.jpg', c)
c = re.sub(r'assets/images/151_ground_1kg_esp_f_R_Car_3_.*?\.png', 'assets/images/s54/robusta_3.jpg', c)

# Price
c = re.sub(r'\$60\.50 AUD', '150.000₫', c)
c = re.sub(r'\$45\.38 AUD', '125.000₫', c)

# Description Tab
desc = """<p>☕ <strong>Cà Phê Hạt Rang S54 Robusta – Nguyên Chất 100%</strong></p>
<p>Bạn đang tìm kiếm một loại cà phê đậm đà, thơm nồng, đánh thức mọi giác quan? <strong>S54 Robusta</strong> chính là sự lựa chọn hoàn hảo!</p>
<ul>
<li>✅ <strong>100% hạt cà phê Robusta nguyên chất</strong> – được tuyển chọn kỹ lưỡng từ vùng đất đỏ bazan Tây Nguyên.</li>
<li>✅ <strong>Rang mộc truyền thống</strong> – giữ trọn hương vị đậm đà, hậu vị ngọt sâu lắng đặc trưng của Robusta Việt Nam.</li>
<li>✅ <strong>Không pha trộn, không tẩm ướp hương liệu</strong> – cho ly cà phê nguyên bản, tinh khiết và an toàn tuyệt đối.</li>
<li>✅ <strong>Đa dạng cách pha</strong> – Thích hợp pha phin truyền thống, pha máy gia đình hoặc chiết xuất Espresso tạo lớp crema vàng óng, thơm ngậy.</li>
</ul>
<p>👉 <strong>Khối lượng tịnh:</strong> 250g, 500g & 1kg.<br>👉 <strong>Bao bì van 1 chiều:</strong> Sang trọng, tiện bảo quản và lưu giữ trọn vẹn hương thơm tươi mới.</p>"""

c = re.sub(r'<div class="c-product-tabs__content" data-tab-content="description">[\s\S]*?</div>', f'<div class="c-product-tabs__content" data-tab-content="description">{desc}</div>', c)

pd_file.write_text(c, encoding='utf-8')
print("✓ Updated product-detail.html with authentic S54 Robusta data")
