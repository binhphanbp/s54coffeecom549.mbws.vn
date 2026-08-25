import os
import sys
import re

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

print("=" * 70)
print("     UPGRADING ALL PAGES WITH 100% AUTHENTIC S54 / GOOD SOLUTIONS DATA")
print("=" * 70)

# =========================================================================
# 1. UPGRADE index.html
# =========================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_replacements = [
    (
        'Hơn 65 Năm Kinh Nghiệm Rang Xay Thủ Công',
        'Hơn 12 Năm Kinh Nghiệm & Đam Mê Cà Phê Sạch'
    ),
    (
        'Bí Quyết Bảo Quản Cà Phê Luôn Tươi Mới',
        '5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết'
    ),
    (
        'Cà Phê Đặc Sản (Specialty Coffee) Là Gì?',
        'Triết Lý “NEW COFFEE, NEW INCOME” & Hơn Cả Cà Phê'
    ),
    (
        'Các Loại Cà Phê Đặc Sản S54',
        'Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp'
    ),
    (
        'Khám phá những loại cà phê ngon nhất và bí quyết bảo quản hạt cà phê luôn thơm ngậy.',
        'Khám phá nguồn chất chống oxy hóa dồi dào, tăng cường tập trung, giảm đau đầu và bảo vệ sức khỏe từ cà phê nguyên chất.'
    ),
    (
        'Tìm hiểu tiêu chuẩn cà phê đặc sản và quy trình tuyển chọn hạt cà phê khắt khe của S54.',
        'Cà phê không chỉ để thưởng thức mà còn kết nối, truyền cảm hứng và tiếp thêm năng lượng tích cực cho sự nghiệp và cuộc sống.'
    ),
    (
        'Hành trình từ nông trại đến tách cà phê hoàn hảo cùng các chuyên gia hàng đầu.',
        'Hướng dẫn phân biệt cà phê sạch nguyên chất 100% không tẩm ướp bắp cau, đậu nành hay hương liệu hóa học nhân tạo.'
    )
]

for old, new in index_replacements:
    index_html = index_html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("  [OK] index.html upgraded!")

# =========================================================================
# 2. UPGRADE wholesale.html
# =========================================================================
with open('wholesale.html', 'r', encoding='utf-8') as f:
    wholesale_html = f.read()

wholesale_replacements = [
    ('Wholesale coffee partner program', 'Chương Trình Đối Tác & Đại Lý Cà Phê S54'),
    ('Our coffee', 'Nguồn Cà Phê Nguyên Chất S54'),
    ('Case Studies', 'Đối Tác Tiêu Biểu'),
    ('What our customers have to say', 'Khách Hàng & Đối Tác Nói Gì Về Chúng Tôi'),
    ('Baristas & training', 'Đào Tạo Barista & Chuyển Giao Công Nghệ Pha Chế'),
    ('We recognise the pivotal role of the barista in shaping the coffee experience.', 'Chúng tôi hiểu rằng kỹ năng của Barista quyết định trực tiếp đến trải nghiệm và sự trung thành của khách hàng.'),
    ('Equipment', 'Thiết Bị & Máy Pha Cà Phê Chuyên Nghiệp'),
    ('Bespoke signage', 'Thiết Kế Quầy Bar & Bộ Nhận Diện Thương Hiệu'),
    ('Marketing for\nhospitality businesses', 'Hỗ Trợ Marketing & Thu Hút Khách Hàng'),
    ('Marketing for hospitality businesses', 'Hỗ Trợ Marketing & Thu Hút Khách Hàng'),
    ('We see ourselves as more than just suppliers. We’re an extension of your business, finding ways to help you operate and grow.', 'S54 Coffee và Good Solutions không chỉ là nhà cung ứng hạt cà phê. Chúng tôi là người bạn đồng hành chiến lược, mang đến giải pháp toàn diện giúp quán cà phê và doanh nghiệp của bạn tăng trưởng bền vững.'),
    ('We’re a community brand', 'Thương Hiệu Vì Cộng Đồng & Nông Dân Việt'),
    ('We’re a family business', 'Doanh Nghiệp Uy Tín & Cam Kết Dài Lâu'),
    ('Get in touch', 'Liên Hệ Hợp Tác Ngay Hôm Nay')
]

for old, new in wholesale_replacements:
    wholesale_html = wholesale_html.replace(old, new)

with open('wholesale.html', 'w', encoding='utf-8') as f:
    f.write(wholesale_html)
print("  [OK] wholesale.html upgraded!")

# =========================================================================
# 3. UPGRADE product-detail.html
# =========================================================================
with open('product-detail.html', 'r', encoding='utf-8') as f:
    prod_html = f.read()

prod_replacements = [
    (
        '<title>S54 Robusta Special Bar Coffee Beans 1kg &ndash; S54 COFFEE</title>',
        '<title>S54 Robusta Cà Phê Rang Nguyên Chất 500g / 1kg — S54 COFFEE</title>'
    ),
    (
        '100% Arabica',
        '100% Robusta Đắk Lắk Nguyên Chất'
    ),
    (
        'Medium-dark roast with sweet chocolate and nutty tones',
        'Rang mộc công nghệ cao Hot-Air, đậm đà vị truyền thống, hậu vị ngọt sâu và hương thơm nồng nàn'
    )
]

for old, new in prod_replacements:
    prod_html = prod_html.replace(old, new)

with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(prod_html)
print("  [OK] product-detail.html upgraded!")

print("\nAll HTML pages upgraded with 100% authentic Good Solutions & S54 Coffee content.")
