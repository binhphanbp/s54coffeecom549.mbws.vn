#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path('HANDOFF.md')
c = handoff_path.read_text(encoding='utf-8')

old_sitemap = """| Trang | Đường Dẫn Tương Đối | Chức Năng Chính |
| :--- | :--- | :--- |
| **Trang Chủ** | `index.html` | Header cố định, Hero Banner kính mờ, Carousel dòng sản phẩm, Khối câu chuyện rang xay 12+ năm, Hướng dẫn pha chế, Sản phẩm bán chạy, Bản tin & Footer pháp lý |
| **Danh Mục Cà Phê** | `collections-coffee.html` | Lưới sản phẩm cà phê toàn diện, bộ lọc phân loại, sắp xếp và thêm nhanh vào giỏ |
| **Chi Tiết Sản Phẩm** | `product-detail.html` | Bộ sưu tập ảnh sản phẩm độ phân giải cao, lựa chọn mua 1 lần hoặc định kỳ, mô tả hương vị, hướng dẫn pha chế |
| **Về Chúng Tôi** | `our-story.html` | Câu chuyện thương hiệu từ 2012, triết lý kinh doanh minh bạch, vùng nguyên liệu Tây Nguyên và sứ mệnh toàn cầu |
| **B2B & Bán Sỉ** | `wholesale.html` | Giải pháp cung ứng cà phê số lượng lớn cho quán, chuỗi F&B, khách sạn, dịch vụ gia công thương hiệu OEM/ODM & Form đăng ký đối tác |
| **Trang 404** | `404.html` | Trang báo lỗi 404 chuẩn nhận diện thương hiệu với nút điều hướng về trang chủ |"""

new_sitemap = """| Trang | Đường Dẫn Tương Đối | Chức Năng Chính |
| :--- | :--- | :--- |
| **Trang Chủ** | `index.html` | Header cố định, Hero Banner kính mờ, Carousel dòng sản phẩm, Khối câu chuyện rang xay 12+ năm, Hướng dẫn pha chế, Sản phẩm bán chạy, Tin tức mới nhất & Footer pháp lý |
| **Danh Mục Cà Phê** | `collections-coffee.html` | Lưới sản phẩm cà phê toàn diện, bộ lọc phân loại, sắp xếp và thêm nhanh vào giỏ |
| **Chi Tiết Sản Phẩm** | `product-detail.html` | Bộ sưu tập ảnh sản phẩm độ phân giải cao, lựa chọn mua 1 lần hoặc định kỳ, mô tả hương vị, hướng dẫn pha chế |
| **Tin Tức & Blog** | `blogs-news.html` (`/blogs/news`) | Danh mục tin tức, chia sẻ kiến thức cà phê sạch, cẩm nang pha chế, bản tin S54 Extracts |
| **Chi Tiết Bài Viết** | `blog-detail.html` | Trang bài viết chuyên sâu: 5 Lợi ích của việc uống cà phê, kiến thức dinh dưỡng & sức khỏe |
| **Về Chúng Tôi** | `our-story.html` | Câu chuyện thương hiệu từ 2012, triết lý kinh doanh minh bạch, vùng nguyên liệu Tây Nguyên và sứ mệnh toàn cầu |
| **B2B & Bán Sỉ** | `wholesale.html` | Giải pháp cung ứng cà phê số lượng lớn cho quán, chuỗi F&B, khách sạn, dịch vụ gia công thương hiệu OEM/ODM & Form đăng ký đối tác |
| **Trang 404** | `404.html` | Trang báo lỗi 404 chuẩn nhận diện thương hiệu với nút điều hướng về trang chủ |"""

c = c.replace(old_sitemap, new_sitemap)
handoff_path.write_text(c, encoding='utf-8')
print("✓ Updated HANDOFF.md with blog pages")
