#!/usr/bin/env python3
"""
Deep Polish of our-story.html and product-detail.html:
1. Replace all legacy Australian story paragraphs in our-story.html with genuine S54 Good Solutions heritage
2. Translate all review widget UI strings in product-detail.html into Vietnamese
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Clean our-story.html
os_path = BASE_DIR / 'our-story.html'
os_txt = os_path.read_text(encoding='utf-8')

story_replacements = [
    (
        "In the late 90’s, the cafe culture boom led to a surge in coffee brands. As market leaders, we remained committed to coffee expertise with a family-driven approach.",
        "Tiên phong nghiên cứu và ứng dụng công nghệ chế biến hiện đại, S54 Coffee cho ra đời dòng sản phẩm cà phê hòa tan 3-in-1 (hộp 456g) và cà phê sấy lạnh cao cấp, mang hương vị cà phê rang mộc chuẩn vị đến mọi gia đình."
    ),
    (
        "We pioneered the coffee college, teaching espresso and latte art fundamentals, promoted quality and freshness, introduced single origins, and partnered with renowned chefs and cafes.",
        "Chúng tôi chuẩn hóa quy trình đào tạo pha chế, chuyển giao kỹ thuật chiết xuất Espresso và phát triển các dòng sản phẩm chất lượng cao phục vụ đời sống hiện đại."
    ),
    (
        "S54 is synonymous with fine dining culture. Our coffee is served in more hatted restaurants than any other brand, and we have been a proud partner the Good Food Guide awards since 2001.",
        "S54 Coffee tự hào là đối tác cung ứng cà phê rang mộc và thiết bị uy tín cho hàng trăm chuỗi nhà hàng, khách sạn và quán cà phê cao cấp trên toàn quốc, cam kết chất lượng đồng đều và chính sách chiết khấu vượt trội."
    ),
    (
        "We have long supported the arts, film and creative industries.",
        "S54 Coffee luôn tích cực đồng hành cùng các hoạt động văn hóa, khởi nghiệp và các chương trình an sinh xã hội vì cộng đồng nông dân trồng cà phê Việt Nam."
    ),
    (
        "As leaders in coffee, we believe it’s our responsibility to use our voice and resources to push the industry forward.",
        "Với vai trò tiên phong, chúng tôi cam kết phát triển chuỗi giá trị cà phê bền vững, minh bạch và nâng cao thu nhập cho người nông dân Tây Nguyên."
    ),
    (
        "Sustainability is not just a goal, it is a core value.",
        "Phát triển bền vững không chỉ là mục tiêu mà là giá trị cốt lõi trong mọi hoạt động sản xuất và kinh doanh của S54 Coffee."
    )
]

for old_s, new_s in story_replacements:
    os_txt = os_txt.replace(old_s, new_s)

os_path.write_text(os_txt, encoding='utf-8')
print("✓ Polished our-story.html with authentic S54 history")

# 2. Clean reviews widget in product-detail.html
pd_path = BASE_DIR / 'product-detail.html'
pd_txt = pd_path.read_text(encoding='utf-8')

pd_reviews_replacements = [
    ("Write a Review", "Viết Đánh Giá"),
    ("Write a review", "Viết Đánh Giá"),
    ("Based on 527 reviews", "Dựa trên 527 đánh giá"),
    ("Based on 765 reviews", "Dựa trên 765 đánh giá"),
    ("Quality", "Chất Lượng"),
    ("Strength", "Độ Đậm Đà"),
    ("Poor", "Kém"),
    ("Excellent", "Tuyệt Vời"),
    ("Weak", "Nhẹ"),
    ("Strong", "Đậm"),
    ("Filters", "Bộ Lọc"),
    ("Most Recent", "Mới Nhất"),
    ("Oldest", "Cũ Nhất"),
    ("Most Helpful", "Hữu Ích Nhất"),
    ("Highest Rating", "Đánh Giá Cao Nhất"),
    ("Lowest Rating", "Đánh Giá Thấp Nhất"),
    ("Verified Buyer", "Đã Mua Hàng"),
    ("Was this helpful?", "Đánh giá này có hữu ích?"),
    ("people voted yes", "người đồng ý"),
    ("people voted no", "người không đồng ý"),
    ("Reviewing", "Đánh giá sản phẩm"),
    ("I recommend this product", "Tôi khuyên dùng sản phẩm này"),
    ("I Typically Drink My Coffee...", "Gu thưởng thức thường ngày:"),
    ("With Milk", "Pha với sữa"),
    ("Black", "Uống đen nguyên chất"),
    ("Espresso", "Pha máy Espresso"),
    ("Great flavour", "Hương vị rất tuyệt vời"),
    ("Very nice bean mix. Smooth and tasty.", "Hạt cà phê rang rất đều và thơm. Vị đậm đà êm ái."),
    ("Beautiful crema. Delicious coffee", "Lớp crema dày mịn. Cà phê thơm ngon đậm đà"),
    ("Great Coffee", "Cà phê xuất sắc")
]

for old_s, new_s in pd_reviews_replacements:
    pd_txt = pd_txt.replace(old_s, new_s)

pd_path.write_text(pd_txt, encoding='utf-8')
print("✓ Polished product-detail.html review widget text")
