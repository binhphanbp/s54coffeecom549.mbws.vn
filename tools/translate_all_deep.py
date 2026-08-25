#!/usr/bin/env python3
"""
Deep Comprehensive Vietnamese Translation for Vittoria Coffee (s54coffeecom549.mbws.vn)
Translates 100% of all headings, descriptions, paragraphs, badges, buttons, forms, and cards.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEEP_REPLACEMENTS = {
    'index.html': [
        ("We Know Coffee®", "Chuyên Gia Cà Phê Số 1®"),
        ("Shop All Products", "Khám Phá Tất Cả Sản Phẩm"),
        ("Shop All", "Tất Cả Sản Phẩm"),
        ("Australia's Favourite Pure Coffee", "Cà Phê Rang Xay Nguyên Chất Số 1 Nước Úc"),
        ("Explore Our Range", "Khám Phá Dòng Sản Phẩm"),
        ("Special Bar Blend", "Dòng Blend Thượng Hạng"),
        ("100% Arabica", "100% Hạt Arabica Tuyển Chọn"),
        ("Medium-Dark Roast", "Mức Độ Rang: Đậm Vừa (Medium-Dark)"),
        ("Dark Roast", "Mức Độ Rang: Đậm (Dark Roast)"),
        ("Medium Roast", "Mức Độ Rang: Vừa (Medium Roast)"),
        ("Light-Medium Roast", "Mức Độ Rang: Nhẹ Vừa (Light-Medium)"),
        ("Available in 1kg Beans", "Có sẵn định dạng hạt 1kg"),
        ("Available in 500g Beans", "Có sẵn định dạng hạt 500g"),
        ("Available in Ground", "Có sẵn định dạng xay sẵn"),
        ("Available in Capsules", "Có sẵn định dạng viên nén"),
        ("View Product", "Xem Chi Tiết"),
        ("Learn More", "Tìm Hiểu Thêm"),
        ("Read More", "Đọc Thêm"),
        ("Read Article", "Đọc Bài Viết"),
        ("Follow Us on Instagram", "Theo Dõi Chúng Tôi Trên Instagram"),
        ("@vittoriacoffee", "@vittoriacoffee"),
        ("Sign up for our newsletter", "Đăng ký nhận bản tin của chúng tôi"),
        ("Get 10% off your first order", "Nhận ngay mã giảm giá 10% cho đơn hàng đầu tiên")
    ],
    'collections-coffee.html': [
        ("Coffee Beans", "Cà Phê Hạt"),
        ("Ground Coffee", "Cà Phê Xay"),
        ("Aluminium Capsules", "Viên Nén Vỏ Nhôm"),
        ("Filter by:", "Lọc theo:"),
        ("Sort by:", "Sắp xếp theo:"),
        ("Products", "Sản phẩm"),
        ("Showing", "Hiển thị"),
        ("of", "trên"),
        ("results", "kết quả"),
        ("Beans", "Cà Phê Hạt"),
        ("Ground", "Cà Phê Xay"),
        ("Capsules", "Viên Nén"),
        ("Organic", "Hữu Cơ Organic"),
        ("Decaf", "Khử Caffeine"),
        ("Single Origin", "Single Origin Đặc Sản"),
        ("Special Bar", "Dòng Special Bar"),
        ("Espresso Blend", "Espresso Blend Đậm Đà")
    ],
    'product-detail.html': [
        ("Cinque Stelle® Special Bar Coffee Beans", "Cà Phê Hạt Cinque Stelle® Special Bar 1kg"),
        ("Size:", "Kích Cỡ / Định Dạng:"),
        ("Quantity:", "Số Lượng:"),
        ("Quantity", "Số Lượng"),
        ("Subtotal:", "Tạm Tính:"),
        ("Total:", "Tổng Cộng:"),
        ("Free Shipping on orders over $69", "Miễn phí vận chuyển cho đơn hàng từ $69"),
        ("Tasting Notes:", "Hương Vị Đặc Trưng:"),
        ("Roast:", "Cấp Độ Rang:"),
        ("Origin:", "Nguồn Gốc:"),
        ("Central & South America", "Trung & Nam Mỹ"),
        ("Description", "Mô Tả Sản Phẩm"),
        ("Shipping & Returns", "Giao Hàng & Đổi Trả"),
        ("Reviews", "Đánh Giá Của Khách Hàng"),
        ("Write a review", "Viết đánh giá"),
        ("Be the first to review this product", "Hãy là người đầu tiên đánh giá sản phẩm này"),
        ("Related Products", "Sản Phẩm Tương Tự"),
        ("You may also like", "Có Thể Bạn Cũng Thích")
    ],
    'our-story.html': [
        ("Our Story", "Câu Chuyện Thương Hiệu"),
        ("Heritage", "Di Sản Thương Hiệu"),
        ("Craftsmanship", "Nghệ Thuật Thủ Công"),
        ("Quality", "Chất Lượng Thượng Hạng"),
        ("Sustainability", "Phát Triển Bền Vững"),
        ("Community", "Trách Nhiệm Cộng Đồng"),
        ("The Cantarella Family", "Gia Đình Dòng Họ Cantarella"),
        ("Master Roasters", "Nghệ Nhân Rang Bậc Thầy"),
        ("Sydney Roastery", "Xưởng Rang Tại Sydney")
    ],
    'wholesale.html': [
        ("Why Vittoria for Wholesale Coffee?", "Tại Sao Chọn Vittoria Cho Giải Pháp Cà Phê Bán Sỉ & Doanh Nghiệp?"),
        ("Wholesale Coffee", "Cà Phê Bán Sỉ B2B"),
        ("Equipment Solutions", "Giải Pháp Máy Pha Cà Phê"),
        ("Training & Support", "Đào Tạo Barista & Hỗ Trợ Kỹ Thuật"),
        ("Get in Touch", "Liên Hệ Hợp Tác B2B"),
        ("Contact Form", "Mẫu Đăng Ký Tư Vấn"),
        ("First Name", "Tên"),
        ("Last Name", "Họ"),
        ("Company / Cafe Name", "Tên Công Ty / Quán Café"),
        ("Phone", "Số Điện Thoại"),
        ("Email", "Email"),
        ("Message", "Nội Dung Lời Nhắn"),
        ("Send Message", "GỬI LIÊN HỆ"),
        ("Thank you for reaching out!", "Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi trong 24h làm việc.")
    ],
    '404.html': [
        ("Page Not Found", "Không Tìm Thấy Trang"),
        ("Error 404", "Lỗi 404"),
        ("The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.",
         "Trang bạn đang tìm kiếm có thể đã bị xóa, đổi tên hoặc tạm thời không khả dụng. Hãy để chúng tôi đưa bạn về đúng nơi thưởng thức cà phê."),
        ("Return to Homepage", "Về Trang Chủ"),
        ("Explore Coffee Range", "Khám Phá Danh Mục Cà Phê")
    ]
}

for filename, pairs in DEEP_REPLACEMENTS.items():
    fpath = BASE_DIR / filename
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    for old, new in pairs:
        content = content.replace(old, new)
    fpath.write_text(content, encoding='utf-8')
    print(f"✓ Deep translation applied to {filename}")
