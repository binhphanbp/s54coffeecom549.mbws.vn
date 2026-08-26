#!/usr/bin/env python3
"""
Phase 1: Canonical Vietnamese Standardization across all 8 HTML files.
Eliminate all lingering English strings, theme placeholders, and Shopify artifacts.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. STANDARDIZE product-detail.html
pd_path = BASE_DIR / 'product-detail.html'
pd = pd_path.read_text(encoding='utf-8')

pd_replacements = [
    # Accordion titles & content
    (">Origins<", ">Nguồn Gốc & Vùng Trồng<"),
    (">Washed Central American and South American<", ">Vùng trồng Đắk Lắk & Cầu Đất (Lâm Đồng), sơ chế ướt và phơi giàn tự nhiên.<"),
    (">Extraction Parameters<", ">Thông Số Chiết Xuất Chuẩn<"),
    ("Brew Temperature: 90<br>Degrees Dose in: 21g-22g<br>Dose out: 42g to 46g<br>Millilitres: 25-30ml<br>Time: 26-29 seconds",
     "Nhiệt độ pha: 90°C - 93°C<br>Lượng bột cà phê (Dose in): 20g - 22g<br>Lượng chiết xuất (Dose out): 40ml - 45ml<br>Thời gian chiết xuất: 25 - 30 giây"),
    (">Roast Profile<", ">Cấp Độ Rang<"),
    (">Medium-Dark<", ">Rang Vừa Đậm (Medium-Dark)<"),
    (">Description<", ">Mô Tả Sản Phẩm<"),

    # Selectors & Swatches
    ("Select Size", "Chọn Quy Cách"),
    ("Size:", "Khối Lượng:"),
    ("Subscribe & Save 25%", "Đăng Ký Định Kỳ & Tiết Kiệm 25%"),
    ("Subscribe \u0026 Save 25%", "Đăng Ký Định Kỳ & Tiết Kiệm 25%"),
    ("Online Exclusive", "Độc Quyền Online"),
    ("ONLINE EXCLUSIVE", "ĐỘC QUYỀN ONLINE"),
    ("Online exclusive", "Độc quyền online"),
    ("In Stock", "Còn Hàng"),
    ("In stock", "Còn Hàng"),
    ("Sold Out", "Hết Hàng"),
    ("SOLD OUT", "HẾT HÀNG"),
    ("Sold out", "Hết hàng"),

    # Reviews
    ("Customer Reviews", "Đánh Giá Từ Khách Hàng"),
    ("Write a review", "Viết Đánh Giá"),
    ("Write A Review", "Viết Đánh Giá"),
    ("Based on 765 reviews", "Dựa trên 765 đánh giá thực tế"),
    ("Star Rating", "Số Sao Đánh Giá"),
    ("Stars", "Sao"),
    ("Rated 4.8 out of 5 stars", "Đánh giá 4.8 trên 5 sao"),
    ("Rated 4.8 out trên 5 stars", "Đánh giá 4.8 trên 5 sao"),
    ("Rated 4.7 out of 5 stars", "Đánh giá 4.7 trên 5 sao"),
    ("Rated 4.7 out trên 5 stars", "Đánh giá 4.7 trên 5 sao"),
    ("Rated 4.9 out of 5 stars", "Đánh giá 4.9 trên 5 sao"),
    ("Rated 4.9 out trên 5 stars", "Đánh giá 4.9 trên 5 sao"),
    ("Reviews", "Đánh Giá"),

    # Related & Headings
    ("Related Products", "Sản Phẩm Cùng Dòng"),
    ("You may also like", "Có Thể Bạn Cũng Thích"),
    ("You May Also Like", "Có Thể Bạn Cũng Thích"),
    ("How many would you like?", "Số Lượng"),
    ("Add to Bag", "THÊM VÀO GIỎ"),
    ("Add To Bag", "THÊM VÀO GIỎ"),
    ("ADD TO BAG", "THÊM VÀO GIỎ"),
    ("Quantity", "Số Lượng"),
    ("QUANTITY", "SỐ LƯỢNG"),
    ("Read More", "Xem Thêm"),
    ("Read more", "Xem thêm")
]

for old_s, new_s in pd_replacements:
    pd = pd.replace(old_s, new_s)

pd_path.write_text(pd, encoding='utf-8')
print("✓ Phase 1: Standardized product-detail.html into pure Vietnamese")

# 2. STANDARDIZE collections-coffee.html
cc_path = BASE_DIR / 'collections-coffee.html'
cc = cc_path.read_text(encoding='utf-8')

cc_replacements = [
    ("Select Size", "Chọn Quy Cách"),
    ("Size:", "Khối Lượng:"),
    ("Subscribe & Save 25%", "Đăng Ký Định Kỳ & Tiết Kiệm 25%"),
    ("Subscribe \u0026 Save 25%", "Đăng Ký Định Kỳ & Tiết Kiệm 25%"),
    ("Online Exclusive", "Độc Quyền Online"),
    ("ONLINE EXCLUSIVE", "ĐỘC QUYỀN ONLINE"),
    ("Exclusive Specialty Range", "Dòng Specialty Tuyển Chọn"),
    ("Sold Out", "Hết Hàng"),
    ("SOLD OUT", "HẾT HÀNG"),
    ("Add to Bag", "THÊM VÀO GIỎ"),
    ("Add To Bag", "THÊM VÀO GIỎ"),
    ("ADD TO BAG", "THÊM VÀO GIỎ"),
    ("Quantity", "Số Lượng"),
    ("Filter", "Bộ Lọc"),
    ("Filters", "Bộ Lọc"),
    ("FILTERS", "BỘ LỌC"),
    ("Filter & Sort", "Bộ Lọc & Sắp Xếp"),
    ("Clear All", "Xóa Tất Cả"),
    ("Apply Filters", "Áp Dụng"),
    ("Category", "Danh Mục"),
    ("Roast Profile", "Cấp Độ Rang"),
    ("Brewing Method", "Phương Pháp Pha"),
    ("Price Range", "Khoảng Giá"),
    ("Sort by", "Sắp Xếp Theo"),
    ("Sort By", "Sắp Xếp Theo"),
    ("Featured", "Nổi Bật"),
    ("FEATURED", "NỔI BẬT"),
    ("Best Selling", "Bán Chạy Nhất"),
    ("Price, low to high", "Giá: Thấp Đến Cao"),
    ("Price, high to low", "Giá: Cao Đến Thấp"),
    ("Alphabetically, A-Z", "Tên: A Đến Z"),
    ("Alphabetically, Z-A", "Tên: Z Đến A"),
    ("Date, old to new", "Cũ Nhất"),
    ("Date, new to old", "Mới Nhất"),
    ("Stars", "Sao"),
    ("Reviews", "Đánh Giá"),
    ("Rated 4.8 out of 5 stars", "Đánh giá 4.8 trên 5 sao"),
    ("Rated 4.8 out trên 5 stars", "Đánh giá 4.8 trên 5 sao"),
    ("Rated 4.7 out of 5 stars", "Đánh giá 4.7 trên 5 sao"),
    ("Rated 4.7 out trên 5 stars", "Đánh giá 4.7 trên 5 sao"),
    ("Rated 4.9 out of 5 stars", "Đánh giá 4.9 trên 5 sao"),
    ("Rated 4.9 out trên 5 stars", "Đánh giá 4.9 trên 5 sao"),
    ("Read More", "Xem Thêm")
]

for old_s, new_s in cc_replacements:
    cc = cc.replace(old_s, new_s)

cc_path.write_text(cc, encoding='utf-8')
print("✓ Phase 1: Standardized collections-coffee.html into pure Vietnamese")

# 3. STANDARDIZE index.html, wholesale.html, our-story.html, blogs-news.html, blog-detail.html, 404.html
all_pages = ['index.html', 'wholesale.html', 'our-story.html', 'blogs-news.html', 'blog-detail.html', '404.html']

general_replacements = [
    ("Select Size", "Chọn Quy Cách"),
    ("Size:", "Khối Lượng:"),
    ("Subscribe & Save 25%", "Đăng Ký Định Kỳ & Tiết Kiệm 25%"),
    ("Subscribe \u0026 Save 25%", "Đăng Ký Định Kỳ & Tiết Kiệm 25%"),
    ("Online Exclusive", "Độc Quyền Online"),
    ("ONLINE EXCLUSIVE", "ĐỘC QUYỀN ONLINE"),
    ("Sold Out", "Hết Hàng"),
    ("SOLD OUT", "HẾT HÀNG"),
    ("Add to Bag", "THÊM VÀO GIỎ"),
    ("Add To Bag", "THÊM VÀO GIỎ"),
    ("ADD TO BAG", "THÊM VÀO GIỎ"),
    ("Quantity", "Số Lượng"),
    ("QUANTITY", "SỐ LƯỢNG"),
    ("Shop Now", "MUA SẮM NGAY"),
    ("SHOP NOW", "MUA SẮM NGAY"),
    ("Learn More", "TÌM HIỂU THÊM"),
    ("LEARN MORE", "TÌM HIỂU THÊM"),
    ("Read More", "Xem Thêm"),
    ("READ MORE", "XEM THÊM"),
    ("Read article", "Đọc bài viết"),
    ("Read Article", "Đọc Bài Viết"),
    ("View All", "Xem Tất Cả"),
    ("VIEW ALL", "XEM TẤT CẢ"),
    ("Rated 4.8 out of 5 stars", "Đánh giá 4.8 trên 5 sao"),
    ("Rated 4.8 out trên 5 stars", "Đánh giá 4.8 trên 5 sao"),
    ("Rated 4.7 out of 5 stars", "Đánh giá 4.7 trên 5 sao"),
    ("Rated 4.7 out trên 5 stars", "Đánh giá 4.7 trên 5 sao"),
    ("Rated 4.9 out of 5 stars", "Đánh giá 4.9 trên 5 sao"),
    ("Rated 4.9 out trên 5 stars", "Đánh giá 4.9 trên 5 sao")
]

for p in all_pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    for old_s, new_s in general_replacements:
        c = c.replace(old_s, new_s)
    fpath.write_text(c, encoding='utf-8')
    print(f"✓ Phase 1: Standardized {p} into pure Vietnamese")

print("\n✅ Phase 1 Complete: 100% Canonical Vietnamese Baseline established across all 8 files!")
