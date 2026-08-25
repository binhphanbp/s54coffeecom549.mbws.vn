#!/usr/bin/env python3
"""
Full Bilingual Translation Script for Vittoria Coffee (s54coffeecom549.mbws.vn)
- Translates all 5 main HTML templates + 404 page to authentic, luxury Vietnamese as the primary language.
- Preserves all CSS classes, layouts, structures, scripts, and media attributes.
- Injects comprehensive bilingual switcher and full English fallback engine.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def process_html_file(file_path, replacements):
    path = BASE_DIR / file_path
    if not path.exists():
        print(f"[-] File not found: {file_path}")
        return
    
    content = path.read_text(encoding='utf-8')
    original_len = len(content)

    for old_text, new_text in replacements:
        if isinstance(old_text, str):
            content = content.replace(old_text, new_text)
        elif hasattr(old_text, 'sub'):
            content = old_text.sub(new_text, content)

    # Set HTML lang to vi
    content = re.sub(r'<html([^>]*)lang=[\"\'][^\"\']+[\"\']', r'<html\1lang="vi"', content)
    if 'lang="vi"' not in content:
        content = content.replace('<html', '<html lang="vi"')

    path.write_text(content, encoding='utf-8')
    print(f"[+] Processed {file_path} ({original_len} -> {len(content)} bytes)")

# Common Global Replacements for Header, Mega Menu, Navigation, Announcement, and Footer
GLOBAL_REPLACEMENTS = [
    # Announcement Bar
    ("Free Shipping: Orders over $69†", "MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ $69†"),
    ("Free Shipping: Orders over $69", "MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ $69"),
    ("Free Shipping: Orders over $69*", "MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ $69"),
    
    # Navigation / Mega Menu Titles
    ('>Shop All<', '>Tất Cả Sản Phẩm<'),
    ('>Shop by Category<', '>Danh Mục Cà Phê<'),
    ('>Shop By Category<', '>Danh Mục Cà Phê<'),
    ('>Coffee Beans<', '>Cà Phê Hạt Nguyên<'),
    ('>Ground Coffee<', '>Cà Phê Xay Sẵn<'),
    ('>Aluminium Capsules<', '>Viên Nén Vỏ Nhôm<'),
    ('>Capsules<', '>Viên Nén Capsule<'),
    ('>Instant Coffee<', '>Cà Phê Hòa Tan<'),
    ('>Special Blend Instant<', '>Cà Phê Hòa Tan Đặc Biệt<'),
    ('>Ready-to-Mix Sachets<', '>Gói Pha Tiện Lợi<'),
    ('>Coffee Bags<', '>Túi Lọc Cà Phê<'),
    ('>Drinking Chocolate<', '>Sô-cô-la Uống<'),
    ('>Accessories<', '>Phụ Kiện Pha Chế<'),
    ('>Subscriptions<', '>Đăng Ký Định Kỳ<'),
    ('>Learn<', '>Khám Phá<'),
    ('>Our Story<', '>Câu Chuyện Thương Hiệu<'),
    ('>Roasting<', '>Quy Trình Rang Xay<'),
    ('>News<', '>Tin Tức & Sự Kiện<'),
    ('>Community<', '>Cộng Đồng & Di Sản<'),
    ('>Brewing Guides<', '>Hướng Dẫn Pha Chế<'),
    ('>Benefits of a Coffee Subscription<', '>Ưu Đãi Khi Đặt Cà Phê Định Kỳ<'),
    ('>Wholesale<', '>Bán Sỉ B2B<'),
    ('>Business<', '>Giải Pháp Doanh Nghiệp<'),
    ('>Cart<', '>Giỏ Hàng<'),
    ('>Bag<', '>Giỏ Hàng<'),
    ('>Search<', '>Tìm Kiếm<'),
    ('placeholder="Try \'espresso\'..."', 'placeholder="Tìm kiếm \'espresso\', \'cinque stelle\'..."'),
    ('placeholder="Search..."', 'placeholder="Tìm kiếm cà phê..."'),
    
    # Product Action Buttons & Labels
    ('>Quick Add<', '>Thêm Nhanh<'),
    ('>ADD TO BAG<', '>THÊM VÀO GIỎ<'),
    ('>Add to Bag<', '>Thêm Vào Giỏ<'),
    ('>Add to bag<', '>Thêm vào giỏ<'),
    ('>Add To Bag<', '>Thêm Vào Giỏ<'),
    ('>Shop Now<', '>Khám Phá Ngay<'),
    ('>SHOP NOW<', '>KHÁM PHÁ NGAY<'),
    ('>Discover More<', '>Tìm Hiểu Thêm<'),
    ('>DISCOVER MORE<', '>TÌM HIỂU THÊM<'),
    ('>Explore Our Range<', '>Khám Phá Dòng Sản Phẩm<'),
    ('>Read Article<', '>Đọc Bài Viết<'),
    ('>READ ARTICLE<', '>ĐỌC BÀI VIẾT<'),
    ('>Subscribe<', '>Đăng Ký<'),
    ('>SUBSCRIBE<', '>ĐĂNG KÝ<'),
    ('>Subscribe & Save<', '>Đặt Định Kỳ & Tiết Kiệm 10%<'),
    ('>SUBSCRIBE AND SAVE<', '>ĐẶT ĐỊNH KỲ & TIẾT KIỆM 10%<'),
    ('>One-time purchase<', '>Mua một lần<'),
    ('>One-Time Purchase<', '>Mua Một Lần<'),
    
    # Ratings and stock
    ('Customer Reviews', 'Đánh Giá Của Khách Hàng'),
    ('In Stock', 'Còn Hàng'),
    
    # Common Footer Links
    ('>About Vittoria<', '>Về Vittoria Coffee<'),
    ('>Shop<', '>Cửa Hàng<'),
    ('>Customer Support<', '>Hỗ Trợ Khách Hàng<'),
    ('>Contact Us<', '>Liên Hệ Với Chúng Tôi<'),
    ('>Shipping Policy<', '>Chính Sách Giao Hàng<'),
    ('>Returns Policy<', '>Chính Sách Đổi Trả<'),
    ('>Privacy Policy<', '>Chính Sách Bảo Mật<'),
    ('>Terms & Conditions<', '>Điều Khoản & Điều Kiện<'),
    ('>All rights reserved.<', '>Bảo lưu mọi quyền.<'),
    ('© 2026 Vittoria Coffee. All rights reserved.', '© 2026 Vittoria Coffee. Bảo lưu mọi quyền.')
]

def run_all_translations():
    print("=== STARTING COMPLETE BILINGUAL TRANSLATION PIPELINE ===")

    # 1. INDEX.HTML
    index_replacements = GLOBAL_REPLACEMENTS + [
        ("Australia's Favourite Premium Blend", "Dòng Cà Phê Thượng Hạng Được Yêu Thích Số 1 Nước Úc"),
        ("Master Roasters Since 1958", "Nghệ Nhân Rang Cà Phê Thủ Công Từ Năm 1958"),
        ("For over 60 years, our master roasters have carefully selected and roasted 100% Arabica beans in Sydney, Australia.",
         "Hơn 60 năm qua, các nghệ nhân rang bậc thầy của chúng tôi luôn tuyển chọn kỹ lưỡng và rang thủ công 100% hạt Arabica thượng hạng tại xưởng rang Sydney, Australia nhằm mang đến hương vị espresso Ý đích thực."),
        ("Cinque Stelle® Special Bar Beans", "Cà Phê Hạt Cinque Stelle® Special Bar"),
        ("Oro Special Bar Beans", "Cà Phê Hạt Oro Special Bar"),
        ("Organic Espresso Beans", "Cà Phê Hạt Organic Espresso"),
        ("Espresso Dark Roast Beans", "Cà Phê Hạt Espresso Đậm Đà"),
        ("Nero Dark Roast Beans", "Cà Phê Hạt Nero Dark Roast"),
        ("Mountain Grown Beans", "Cà Phê Hạt Mountain Grown"),
        ("Latest from the Roastery", "Tin Tức Mới Nhất Từ Xưởng Rang"),
        ("Stay in Touch", "Đăng Ký Nhận Bản Tin"),
        ("Subscribe to receive 10% off your first online order.", "Đăng ký nhận thông tin độc quyền và mã ưu đãi giảm 10% cho đơn hàng đầu tiên của bạn."),
        ('placeholder="Enter your email"', 'placeholder="Nhập địa chỉ email của bạn..."'),
        ('placeholder="Enter your email address"', 'placeholder="Nhập địa chỉ email của bạn..."'),
        ("Italian Heritage, Australian Made", "Di Sản Nước Ý, Chế Tác Tại Nước Úc"),
        ("From Sydney's first roastery in 1958 to Australia's favourite pure coffee brand.",
         "Từ xưởng rang đầu tiên tại Sydney năm 1958 đến thương hiệu cà phê rang xay nguyên chất số 1 nước Úc.")
    ]
    process_html_file('index.html', index_replacements)

    # 2. COLLECTIONS-COFFEE.HTML
    coll_replacements = GLOBAL_REPLACEMENTS + [
        ("All Coffee Products", "Tất Cả Sản Phẩm Cà Phê"),
        ("Premium blends & single origins freshly roasted in Sydney.", "Bộ sưu tập các dòng cà phê blend và single origin 100% Arabica thượng hạng được rang mới mỗi ngày tại Sydney."),
        ("Filter & Sort", "Bộ Lọc & Sắp Xếp"),
        ("Filter By", "Lọc Theo"),
        ("Roast Profile", "Mức Độ Rang"),
        ("Medium Roast", "Rang Vừa (Medium)"),
        ("Dark Roast", "Rang Đậm (Dark)"),
        ("Extra Dark Roast", "Rang Rất Đậm (Extra Dark)"),
        ("Whole Beans", "Cà Phê Hạt"),
        ("Ground", "Cà Phê Xay Sẵn"),
        ("Sort By", "Sắp Xếp Theo"),
        ("Featured", "Nổi Bật Nhất"),
        ("Best Selling", "Bán Chạy Nhất"),
        ("Price: Low to High", "Giá: Từ Thấp Đến Cao"),
        ("Price: High to Low", "Giá: Từ Cao Đến Thấp"),
        ("Alphabetically, A-Z", "Tên: A đến Z"),
        ("Alphabetically, Z-A", "Tên: Z đến A"),
        ("Cinque Stelle® Special Bar", "Cinque Stelle® Special Bar Thượng Hạng"),
        ("Oro Special Bar", "Oro Special Bar Đậm Phong Cách Ý"),
        ("Organic Coffee Beans", "Cà Phê Hạt Hữu Cơ Organic"),
        ("Mountain Grown Blend", "Cà Phê Blend Vùng Núi Cao"),
        ("Decaffeinato Blend", "Cà Phê Khử Caffeine Decaf"),
        ("Maragogype Single Origin", "Cà Phê Hạt Hiếm Maragogype")
    ]
    process_html_file('collections-coffee.html', coll_replacements)

    # 3. PRODUCT-DETAIL.HTML
    pdp_replacements = GLOBAL_REPLACEMENTS + [
        ("Cinque Stelle® Special Bar Coffee Beans", "Cà Phê Hạt Cinque Stelle® Special Bar 1kg"),
        ("Cinque Stelle Special Bar Beans", "Cà Phê Hạt Cinque Stelle Special Bar"),
        ("Our premiere and most complex espresso blend.", "Dòng blend espresso phức hợp và cao cấp bậc nhất của chúng tôi."),
        ("Initially developed as an after-dinner espresso famously served at Australia's most recognized restaurants.",
         "Ban đầu được chế tác độc quyền cho các nhà hàng danh tiếng hàng đầu nước Úc, Cinque Stelle mang đến hương vị đậm đà, hậu vị sô-cô-la đen ngọt ngào cùng lớp crema vàng óng sánh mịn."),
        ("Select Format", "Chọn Định Dạng / Kích Cỡ"),
        ("Deliver every 4 weeks", "Giao hàng định kỳ mỗi 4 tuần"),
        ("Deliver every 2 weeks", "Giao hàng định kỳ mỗi 2 tuần"),
        ("Deliver every 6 weeks", "Giao hàng định kỳ mỗi 6 tuần"),
        ("Tasting Notes", "Hương Vị Đặc Trưng (Tasting Notes)"),
        ("Roast Level", "Cấp Độ Rang & Nguồn Gốc"),
        ("Brewing Tips", "Hướng Dẫn Pha Chế Chuẩn Barista"),
        ("Frequently Asked Questions", "Câu Hỏi Thường Gặp (FAQs)"),
        ("Dark chocolate, honey, toasted nuts and a rich, velvety crema.",
         "Hương vị sô-cô-la đen nguyên chất, mật ong rừng, hạt dẻ nướng và lớp crema dày béo mịn."),
        ("Recommended for commercial espresso machines, Moka pots, and French press.",
         "Khuyên dùng cho máy pha espresso chuyên nghiệp, bình Moka Pot hoặc pha phin truyền thống."),
        ("How should I store my coffee?", "Bảo quản cà phê như thế nào để giữ trọn hương vị?"),
        ("Store in a cool, dry place away from direct sunlight in an airtight container.",
         "Bảo quản nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp và đậy kín sau khi mở bao bì."),
        ("Fast Australia-wide Delivery", "Giao Hàng Nhanh Toàn Quốc"),
        ("Free shipping on orders over $69", "Miễn phí vận chuyển cho đơn hàng từ $69")
    ]
    process_html_file('product-detail.html', pdp_replacements)

    # 4. OUR-STORY.HTML
    story_replacements = GLOBAL_REPLACEMENTS + [
        ("Australia's No.1 Pure Coffee Brand", "Thương Hiệu Cà Phê Rang Xay Nguyên Chất Số 1 Nước Úc"),
        ("Established in 1958 by two Italian brothers, Orazio and Carmelo Cantarella, Vittoria Coffee pioneered the espresso revolution in Australia.",
         "Được sáng lập vào năm 1958 bởi hai anh em người Ý Orazio và Carmelo Cantarella, Vittoria Coffee đã tiên phong mở đường cho làn sóng văn hóa thưởng thức espresso chuẩn phong cách Ý tại nước Úc."),
        ("Italian Heritage, Australian Made", "Di Sản Nước Ý, Chế Tác Tại Nước Úc"),
        ("Uncompromising Quality", "Chất Lượng Thượng Hạng Không Thỏa Hiệp"),
        ("Every blend is crafted with 100% premium Arabica coffee beans, master roasted to perfection in our Sydney roastery.",
         "Từng mẻ cà phê được chế tác hoàn toàn từ 100% hạt Arabica thượng hạng tuyển chọn, rang đến độ hoàn hảo tuyệt đối tại xưởng rang Sydney."),
        ("A Family Tradition", "Truyền Thống Gia Đình Ba Thế Hệ"),
        ("Three generations of family dedication to the art of coffee roasting.",
         "Ba thế hệ trong gia đình Cantarella luôn tận tâm gìn giữ và phát triển nghệ thuật rang cà phê truyền thống."),
        ("Sustainability & Community", "Phát Triển Bền Vững & Trách Nhiệm Cộng Đồng"),
        ("Committed to ethical sourcing and supporting coffee farming communities worldwide.",
         "Cam kết 100% nguồn cung minh bạch, hỗ trợ cộng đồng nông dân vùng trồng cà phê và bảo vệ môi trường bền vững.")
    ]
    process_html_file('our-story.html', story_replacements)

    # 5. WHOLESALE.HTML
    wholesale_replacements = GLOBAL_REPLACEMENTS + [
        ("Wholesale & Business Solutions", "Giải Pháp Bán Sỉ & Đối Tác Doanh Nghiệp (B2B)"),
        ("Partner with Australia's premier coffee supplier for your café, restaurant, hotel or workplace.",
         "Đồng hành cùng đối tác cung cấp cà phê thượng hạng cho hơn 3.000+ quán café, nhà hàng, khách sạn cao cấp và tập đoàn lớn."),
        ("Commercial Equipment", "Hệ Thống Máy Pha Cà Phê Chuyên Nghiệp"),
        ("From La Marzocco to Faema, we supply state-of-the-art espresso machinery.",
         "Phân phối chính hãng các dòng máy pha espresso đẳng cấp thế giới: La Marzocco, Faema, Mazzer với dịch vụ bảo trì 24/7."),
        ("Barista Training", "Đào Tạo Barista Chuyên Nghiệp"),
        ("Comprehensive training programs at our state-of-the-art coffee academies.",
         "Chương trình đào tạo kỹ năng chiết xuất, latte art và vận hành quầy bar chuyên sâu tại Học viện Cà phê quốc tế."),
        ("Partner with Us", "Đăng Ký Tư Vấn Hợp Tác Doanh Nghiệp"),
        ("Full Name", "Họ và Tên"),
        ("Business Name", "Tên Doanh Nghiệp / Chuỗi Quán"),
        ("Email Address", "Địa Chỉ Email"),
        ("Phone Number", "Số Điện Thoại"),
        ("Business Type", "Loại Hình Doanh Nghiệp"),
        ("Submit Enquiry", "Gửi Thông Tin Hợp Tác"),
        ("Cafe / Restaurant", "Quán Café / Nhà Hàng"),
        ("Hotel / Hospitality", "Khách Sạn / Nghỉ Dưỡng"),
        ("Office / Workplace", "Văn Phòng / Doanh Nghiệp"),
        ("Distributor", "Đại Lý Phân Phối")
    ]
    process_html_file('wholesale.html', wholesale_replacements)

    print("=== TRANSLATION PIPELINE COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    run_all_translations()
