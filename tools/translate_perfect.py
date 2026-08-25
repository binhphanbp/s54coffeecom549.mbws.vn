#!/usr/bin/env python3
"""
Exhaustive 100% Vietnamese Master Translation Script for s54coffeecom549.mbws.vn
Translates every heading, sub-element, HTML inner tag, quote, CEO statement, carousel title, and card label.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

EXACT_REPLACEMENTS = {
    'index.html': [
        # Carousel Header
        ("<span>Discover <em><br/></em>our range</span>", "<span>Khám Phá <em><br/></em>Dòng Sản Phẩm</span>"),
        ("<span>Discover <em><br></em>our range</span>", "<span>Khám Phá <em><br></em>Dòng Sản Phẩm</span>"),
        ("“Our ambition is to provide Australians with the best and freshest, roasted coffee in any format they choose.”<br/><strong><br/>Les Schirato, CEO</strong>",
         "“Khát vọng của chúng tôi là mang đến cho người yêu cà phê những hạt cà phê rang tươi mới và thượng hạng nhất ở mọi định dạng thưởng thức.”<br/><strong><br/>Les Schirato, Giám Đốc Điều Hành (CEO)</strong>"),
        ("“Our ambition is to provide Australians with the best and freshest, roasted coffee in any format they choose.”",
         "“Khát vọng của chúng tôi là mang đến cho người yêu cà phê những hạt cà phê rang tươi mới và thượng hạng nhất ở mọi định dạng thưởng thức.”"),
        ("Les Schirato, CEO", "Les Schirato, Giám Đốc Điều Hành (CEO)"),

        # Category Carousel Tiles
        ('alt="Beans"', 'alt="Cà Phê Hạt"'),
        ('>Beans</h6>', '>Cà Phê Hạt</h6>'),
        ('>Beans<', '>Cà Phê Hạt<'),
        ('alt="Capsules"', 'alt="Viên Nén"'),
        ('>Capsules</h6>', '>Viên Nén Capsule</h6>'),
        ('alt="Ground"', 'alt="Cà Phê Xay"'),
        ('>Ground</h6>', '>Cà Phê Xay</h6>'),
        ('alt="Instant"', 'alt="Cà Phê Hòa Tan"'),
        ('>Instant</h6>', '>Cà Phê Hòa Tan</h6>'),

        # Roasting Expertise Section
        ("Over 65 years of<em> </em>roasting expertise", "Hơn 65 Năm Kinh Nghiệm<em> </em>Rang Xay Thủ Công"),
        ("Over 65 years of roasting expertise", "Hơn 65 Năm Kinh Nghiệm Rang Xay Thủ Công"),
        ("Combining three generations of family experience with one of the most advanced",
         "Kết tinh từ ba thế hệ kinh nghiệm gia đình Cantarella cùng một trong những xưởng rang"),
        ("roasting facilities in the southern hemisphere.", "hiện đại bậc nhất bán cầu nam."),
        (">Roasting Process<", ">Quy Trình Rang Xay<"),

        # News & Articles
        (">Read the latest news<", ">Đọc Tin Tức Mới Nhất<"),
        ("Stay up to date with the latest news from Australia's No.1 pure coffee brand.^",
         "Cập nhật những tin tức và câu chuyện mới nhất từ thương hiệu cà phê rang xay nguyên chất số 1 nước Úc.^"),
        (">View All<", ">Xem Tất Cả<"),
        (">View all<", ">Xem tất cả<"),
        ("How to Store Coffee Beans Once Opened So They Stay Fresh", "Cách Bảo Quản Hạt Cà Phê Sau Khi Mở Gói Để Luôn Tươi Mới"),
        ("Fifteen minute read", "15 phút đọc"),
        ("What is Specialty Coffee?", "Cà Phê Đặc Sản (Specialty Coffee) Là Gì?"),
        ("Ten minute read", "10 phút đọc"),
        ("Australian Coffee Types Explained", "Khám Phá Các Loại Cà Phê Phong Cách Nước Úc"),
        ("Thirteen minute read", "13 phút đọc"),
        ("Extracts Issue no. 7", "Bản Tin Extracts Số 7"),
        ("One minute read", "1 phút đọc"),

        # Video Section
        ("How to brew <br/>the perfect espresso.", "Nghệ thuật chiết xuất <br/>tách Espresso hoàn hảo."),
        ("How to brew <br>the perfect espresso.", "Nghệ thuật chiết xuất <br>tách Espresso hoàn hảo."),
        (">Explore Brewtorials<", ">Khám Phá Video Hướng Dẫn<"),

        # Best Sellers Tab
        (">Our best sellers<", ">Sản Phẩm Bán Chạy Nhất<"),
        (">Coffee</button>", ">Cà Phê</button>"),
        (">Viên Nén Capsule</button>", ">Viên Nén Capsule</button>"),
        (">Instant</button>", ">Hòa Tan</button>"),
        (">Cups</button>", ">Ly Tách</button>"),
        (">All products<", ">Tất Cả Sản Phẩm<"),
        (">All products</option>", ">Tất Cả Sản Phẩm</option>"),
        (">ONLINE EXCLUSIVE", ">ĐỘC QUYỀN ONLINE"),
        ("Our most popular foodservice blend", "Dòng blend phục vụ khách sạn & nhà hàng được ưa chuộng nhất"),
        ("Australia's favourite blend", "Dòng blend được yêu thích nhất nước Úc"),
        ("Dark roasted for a full-bodied flavour", "Rang đậm cho hương vị dày dặn, thể chất mạnh mẽ"),
        ("Certified Organic blend", "Dòng blend đạt chứng nhận Hữu cơ Quốc tế"),

        # Instagram & Community
        ("Follow Us On Instagram", "Theo Dõi Chúng Tôi Trên Instagram"),
        ("Follow us on Instagram", "Theo dõi chúng tôi trên Instagram"),
        ("Tag @vittoriacoffee to be featured", "Gắn thẻ @vittoriacoffee để xuất hiện trên trang của chúng tôi")
    ],

    'collections-coffee.html': [
        (">All Coffee Products<", ">Tất Cả Sản Phẩm Cà Phê<"),
        (">Filter & Sort<", ">Bộ Lọc & Sắp Xếp<"),
        (">Filter By<", ">Lọc Theo<"),
        (">Roast Profile<", ">Mức Độ Rang<"),
        (">Format<", ">Định Dạng<"),
        (">Size<", ">Kích Cỡ<"),
        (">Featured<", ">Nổi Bật<"),
        (">Best Selling<", ">Bán Chạy Nhất<"),
        (">Price: Low to High<", ">Giá: Thấp Đến Cao<"),
        (">Price: High to Low<", ">Giá: Cao Đến Thấp<"),
        (">ONLINE EXCLUSIVE", ">ĐỘC QUYỀN ONLINE"),
        ("Our most popular foodservice blend", "Dòng blend phục vụ khách sạn & nhà hàng được ưa chuộng nhất"),
        ("Australia's favourite blend", "Dòng blend được yêu thích nhất nước Úc"),
        ("Dark roasted for a full-bodied flavour", "Rang đậm cho hương vị dày dặn, thể chất mạnh mẽ"),
        ("Certified Organic blend", "Dòng blend đạt chứng nhận Hữu cơ Quốc tế")
    ],

    'product-detail.html': [
        (">Cinque Stelle® Special Bar Coffee Beans<", ">Cà Phê Hạt Cinque Stelle® Special Bar 1kg<"),
        (">ONLINE EXCLUSIVE", ">ĐỘC QUYỀN ONLINE"),
        (">One-time purchase<", ">Mua một lần<"),
        (">Subscribe & Save 10%<", ">Đặt Định Kỳ & Tiết Kiệm 10%<"),
        (">Deliver every 4 weeks<", ">Giao hàng định kỳ mỗi 4 tuần<"),
        (">Deliver every 2 weeks<", ">Giao hàng định kỳ mỗi 2 tuần<"),
        (">Deliver every 6 weeks<", ">Giao hàng định kỳ mỗi 6 tuần<"),
        (">Tasting Notes<", ">Hương Vị Đặc Trưng (Tasting Notes)<"),
        (">Roast Level<", ">Cấp Độ Rang & Nguồn Gốc<"),
        (">Brewing Tips<", ">Hướng Dẫn Pha Chế Chuẩn Barista<"),
        (">Frequently Asked Questions<", ">Câu Hỏi Thường Gặp (FAQs)<"),
        (">Customer Reviews<", ">Đánh Giá Của Khách Hàng<")
    ],

    'our-story.html': [
        (">Our Story<", ">Câu Chuyện Thương Hiệu<"),
        (">Italian Heritage, Australian Made<", ">Di Sản Nước Ý, Chế Tác Tại Nước Úc<"),
        (">Uncompromising Quality<", ">Chất Lượng Thượng Hạng Không Thỏa Hiệp<"),
        (">A Family Tradition<", ">Truyền Thống Gia Đình Ba Thế Hệ<"),
        (">Sustainability & Community<", ">Phát Triển Bền Vững & Trách Nhiệm Cộng Đồng<")
    ],

    'wholesale.html': [
        (">Why Vittoria for Wholesale Coffee?<", ">Tại Sao Chọn Vittoria Cho Giải Pháp Cà Phê Bán Sỉ & Doanh Nghiệp?<"),
        (">Commercial Equipment<", ">Hệ Thống Máy Pha Cà Phê Chuyên Nghiệp<"),
        (">Barista Training<", ">Đào Tạo Barista Chuyên Nghiệp<"),
        (">Partner with Us<", ">Đăng Ký Tư Vấn Hợp Tác Doanh Nghiệp<"),
        (">Full Name<", ">Họ và Tên<"),
        (">Business Name<", ">Tên Doanh Nghiệp / Chuỗi Quán<"),
        (">Email Address<", ">Địa Chỉ Email<"),
        (">Phone Number<", ">Số Điện Thoại<"),
        (">Submit Enquiry<", ">Gửi Thông Tin Hợp Tác<")
    ],

    '404.html': [
        (">Page Not Found<", ">Không Tìm Thấy Trang<"),
        (">Return to Homepage<", ">Về Trang Chủ<"),
        (">Explore Coffee Range<", ">Khám Phá Danh Mục Cà Phê<")
    ]
}

for filename, pairs in EXACT_REPLACEMENTS.items():
    fpath = BASE_DIR / filename
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    for old, new in pairs:
        content = content.replace(old, new)
    fpath.write_text(content, encoding='utf-8')
    print(f"✓ Replaced exact phrases in {filename}")

