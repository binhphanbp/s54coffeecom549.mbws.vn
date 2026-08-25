import re

i18n_path = 'assets/js/i18n.js'

with open(i18n_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_pairs = [
    ('Khởi Nguồn Đam Mê & Thành Lập Good Solutions (2012)', 'Our Passion & The Founding of Good Solutions (2012)'),
    ('Triết Lý “NEW COFFEE, NEW INCOME”', 'The “NEW COFFEE, NEW INCOME” Philosophy'),
    ('Chuẩn Hóa Vùng Trồng Robusta Đắk Lắk & Arabica Cầu Đất', 'Standardizing Robusta Dak Lak & Arabica Cau Dat Origins'),
    ('Công Nghệ Rang Mộc Hot-Air Hiện Đại', 'Advanced Hot-Air Artisan Roasting Technology'),
    ('Đột Phá Cà Phê Hòa Tan 3-in-1 (456g) & Sấy Lạnh', 'Breakthrough 3-in-1 Instant (456g) & Freeze-Dried Coffee'),
    ('Giải Pháp Cung Ứng B2B & Đại Lý Toàn Diện', 'Comprehensive B2B & Wholesale Supply Solutions'),
    ('4 Giá Trị Cốt Lõi: Minh Bạch & Bền Vững', '4 Core Values: Transparency & Sustainability'),
    ('Tầm Nhìn Vươn Tầm Toàn Cầu — “Hơn Cả Cà Phê”', 'Global Vision — “More Than Just Coffee”'),
    ('Hơn 12 Năm Đồng Hành Cùng Hàng Triệu Tách Cà Phê Việt', 'Over 12 Years Accompanying Millions of Vietnamese Coffee Cups'),
    ('Chương Trình Đối Tác & Đại Lý Cà Phê S54', 'S54 Coffee Partner & Wholesale Program'),
    ('Nguồn Cà Phê Nguyên Chất S54', 'S54 Pure Coffee Supply'),
    ('Đối Tác Tiêu Biểu', 'Featured Partners & Case Studies'),
    ('Khách Hàng & Đối Tác Nói Gì Về Chúng Tôi', 'What Our Clients & Partners Say'),
    ('Đào Tạo Barista & Chuyển Giao Công Nghệ Pha Chế', 'Barista Training & Brewing Knowledge Transfer'),
    ('Thiết Bị & Máy Pha Cà Phê Chuyên Nghiệp', 'Professional Espresso Machines & Equipment'),
    ('Thiết Kế Quầy Bar & Bộ Nhận Diện Thương Hiệu', 'Bar Setup & Custom Brand Identity'),
    ('Hỗ Trợ Marketing & Thu Hút Khách Hàng', 'Marketing & Customer Acquisition Support'),
    ('Thương Hiệu Vì Cộng Đồng & Nông Dân Việt', 'Community Brand Supporting Vietnamese Farmers'),
    ('Doanh Nghiệp Uy Tín & Cam Kết Dài Lâu', 'Trusted Enterprise & Long-term Commitment'),
    ('Liên Hệ Hợp Tác Ngay Hôm Nay', 'Get In Touch & Partner With Us Today'),
    ('5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết', '5 Amazing Health Benefits of Coffee You Might Not Know'),
    ('Triết Lý “NEW COFFEE, NEW INCOME” & Hơn Cả Cà Phê', '“NEW COFFEE, NEW INCOME” Philosophy & More Than Coffee'),
    ('Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp', 'How to Distinguish Pure Roasted Coffee from Adulterated Blends'),
    ('Khám phá nguồn chất chống oxy hóa dồi dào, tăng cường tập trung, giảm đau đầu và bảo vệ sức khỏe từ cà phê nguyên chất.', 'Discover rich antioxidants, enhanced focus, headache relief and health benefits from pure coffee.'),
    ('Cà phê không chỉ để thưởng thức mà còn kết nối, truyền cảm hứng và tiếp thêm năng lượng tích cực cho sự nghiệp và cuộc sống.', 'Coffee is not only for enjoying, but for connecting, inspiring, and fueling positive energy in life.'),
    ('Hướng dẫn phân biệt cà phê sạch nguyên chất 100% không tẩm ướp bắp cau, đậu nành hay hương liệu hóa học nhân tạo.', 'A guide to distinguishing 100% pure clean coffee with no corn, soy or artificial flavors.'),
    ('S54 Robusta Cà Phê Rang Nguyên Chất 500g / 1kg', 'S54 Pure Roasted Robusta Beans 500g / 1kg'),
    ('100% Robusta Đắk Lắk Nguyên Chất', '100% Pure Dak Lak Robusta'),
    ('Rang mộc công nghệ cao Hot-Air, đậm đà vị truyền thống, hậu vị ngọt sâu và hương thơm nồng nàn', 'High-tech Hot-Air artisan roast, rich traditional flavor, deep sweet aftertaste and intense aroma.')
]

# Build JS insertion snippet
insertion = ""
for vi, en in new_pairs:
    escaped_vi = vi.replace('"', '\\"')
    escaped_en = en.replace('"', '\\"')
    insertion += f'        ["{escaped_vi}", "{escaped_en}"],\n'

# Insert after `const translationPairs = [`
js_content = js_content.replace(
    'const translationPairs = [',
    'const translationPairs = [\n' + insertion
)

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Added {len(new_pairs)} authentic bilingual translation pairs to i18n.js!")
