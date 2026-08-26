# ☕ S54 COFFEE — TÀI LIỆU BÀN GIAO DỰ ÁN (PROJECT HANDOFF DOCUMENT)

> **Dự án:** Website Thương Mại Điện Tử & Giới Thiệu Doanh Nghiệp S54 COFFEE  
> **Khách hàng:** CÔNG TY TNHH GIẢI PHÁP TỐT (Good Solutions Co., Ltd)  
> **Website Chính Thức (Mới):** [https://s54coffeecom549.mbws.vn/](https://s54coffeecom549.mbws.vn/)  
> **Website Cũ Tham Chiếu:** [https://goodsolutions.com.vn/](https://goodsolutions.com.vn/)  
> **Mã Nguồn (Git):** `git@github.com:binhphanbp/s54coffeecom549.mbws.vn.git` (Nhánh: `main`)  
> **Ngày Bàn Giao:** 25/08/2026  
> **Phiên Bản:** 2.0 (Production Release)

---

## 1. 🏛️ THÔNG TIN DOANH NGHIỆP & NHẬN DIỆN THƯƠNG HIỆU

| Mục | Chi Tiết |
| :--- | :--- |
| **Tên Thương Hiệu** | **S54 COFFEE** |
| **Tên Pháp Nhân** | **CÔNG TY TNHH GIẢI PHÁP TỐT (GOOD SOLUTIONS COMPANY LIMITED)** |
| **Slogan** | *"New Coffee, New Income" • "Tinh Hoa Cà Phê Việt - Rang Mộc Nguyên Chất"* |
| **Năm Thành Lập** | 2012 |
| **Ban Lãnh Đạo** | **Nguyễn Xuân Hiếu (Mr. Paul Hieu)** — CEO & **Tony Hoan** — Founder |
| **Trụ Sở Chính** | Số 35, Đường T8, Manhattan, Vinhomes Grand Park, Phường Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh, Việt Nam |
| **Hotline / Zalo** | `(+84) 383 707 578` — `(+84) 902 873 345` |
| **Email Liên Hệ** | `pm@goodsolutions.com.vn` |
| **Chính Sách Giao Hàng** | Miễn phí vận chuyển toàn quốc cho đơn hàng từ **599.000₫** |

---

## 2. 🏗️ KIẾN TRÚC KỸ THUẬT & DESIGN SYSTEM

### 2.1. Tech Stack
* **Frontend:** Static HTML5 Semantic, CSS3 Modular (Grid & Flexbox), JavaScript ES6+ (No jQuery dependency for core features).
* **Typography:** 
  * *Tiêu đề / Hero / Headings:* Google Font **`Cormorant Garamond`** (Nét thanh lịch, cổ điển, đậm chất thương hiệu di sản).
  * *Nội dung / Menu / Nút / UI:* Google Font **`Plus Jakarta Sans`** (Hiện đại, tối ưu hiển thị tiếng Việt có dấu, rõ nét ở mọi kích thước màn hình).
* **Bảng Màu (Color Palette):**
  * **Espresso Deep Brown:** `#2F221A` (Màu nhận diện chủ đạo, tạo chiều sâu).
  * **Warm Amber Gold:** `#D68E1D` (Màu điểm nhấn CTA, badge ưu đãi, hover link).
  * **Crema Cream:** `#FAF8F5` (Màu nền ấm, giảm mỏi mắt, tăng tính sang trọng).
  * **Warm Border / Divider:** `#EBE7E1` / `#D8CEBE`.

### 2.2. Các Module Tính Năng Nổi Bật
1. **Đa Ngôn Ngữ Song Ngữ Chuẩn Chỉnh (i18n):**
   * **Tiếng Việt (Mặc định)** và **Tiếng Anh (Secondary)**.
   * Chuyển đổi mượt mà bằng nút `[🇻🇳 VI] | [🇬🇧 EN]` trên Topbar và Footer.
   * Tự động lưu ngôn ngữ người dùng vào `localStorage` (`s54_storefront_lang`).
2. **Slide-out Cart Drawer:**
   * Giỏ hàng trượt êm ái từ cạnh phải, cập nhật số lượng realtime.
   * Thanh tiến trình miễn phí vận chuyển tự động tính khoảng cách tới mốc 599.000₫.
   * Định dạng tiền tệ thông minh (`Intl.NumberFormat` theo VND / USD tùy chọn).
3. **Responsive & Mobile-First:**
   * Header co giãn thông minh, menu trượt Sidebar cho điện thoại và máy tính bảng.
   * Nút bấm gọi Hotline nhanh `tel:0383707578` tích hợp ngay trên Header.
   * Nút **Cuộn lên đầu trang (Scroll-To-Top)** tự động xuất hiện khi cuộn qua 300px.

---

## 3. ☕ DANH MỤC TRANG & SẢN PHẨM TRỌNG TÂM

### 3.1. Bản Đồ Trang (Sitemap)
| Trang | Đường Dẫn Tương Đối | Chức Năng Chính |
| :--- | :--- | :--- |
| **Trang Chủ** | `index.html` | Header cố định, Hero Banner kính mờ, Carousel dòng sản phẩm, Khối câu chuyện rang xay 12+ năm, Hướng dẫn pha chế, Sản phẩm bán chạy, Tin tức mới nhất & Footer pháp lý |
| **Danh Mục Cà Phê** | `collections-coffee.html` | Lưới sản phẩm cà phê toàn diện, bộ lọc phân loại, sắp xếp và thêm nhanh vào giỏ |
| **Chi Tiết Sản Phẩm** | `product-detail.html` | Bộ sưu tập ảnh sản phẩm độ phân giải cao, lựa chọn mua 1 lần hoặc định kỳ, mô tả hương vị, hướng dẫn pha chế |
| **Tin Tức & Blog** | `blogs-news.html` (`/blogs/news`) | Danh mục tin tức, chia sẻ kiến thức cà phê sạch, cẩm nang pha chế, bản tin S54 Extracts |
| **Chi Tiết Bài Viết** | `blog-detail.html` | Trang bài viết chuyên sâu: 5 Lợi ích của việc uống cà phê, kiến thức dinh dưỡng & sức khỏe |
| **Về Chúng Tôi** | `our-story.html` | Câu chuyện thương hiệu từ 2012, triết lý kinh doanh minh bạch, vùng nguyên liệu Tây Nguyên và sứ mệnh toàn cầu |
| **B2B & Bán Sỉ** | `wholesale.html` | Giải pháp cung ứng cà phê số lượng lớn cho quán, chuỗi F&B, khách sạn, dịch vụ gia công thương hiệu OEM/ODM & Form đăng ký đối tác |
| **Trang 404** | `404.html` | Trang báo lỗi 404 chuẩn nhận diện thương hiệu với nút điều hướng về trang chủ |

### 3.2. Danh Mục Sản Phẩm Đã Đồng Bộ
1. **S54 Robusta Cà Phê Rang Mộc Nguyên Chất** — `150.000₫` (250g / 500g / 1kg)
2. **S54 Arabica Cầu Đất Thượng Hạng** — `185.000₫`
3. **Cà Phê Hòa Tan S54 Instant Coffee 3in1** — `125.000₫` (Hộp 456g / 24 gói)
4. **Cà Phê Sấy Lạnh S54 Freeze-Dried Blend** — `195.000₫`
5. **Cà Phê Túi Lọc Drip Bag S54** — `135.000₫`
6. **S54 Cà Phê Xay Pha Phin Truyền Thống** — `150.000₫`

---

## 4. 🚀 HỆ THỐNG MÁY CHỦ & THÔNG TIN TRIỂN KHAI

### 4.1. Thông Tin Server & Hosting
* **Live Domain:** `https://s54coffeecom549.mbws.vn/`
* **IP Máy Chủ:** `203.205.31.252`
* **Quản Trị Hosting:** Plesk Obsidian Panel
* **Webroot Directory:** `/var/www/vhosts/s54coffeecom549.mbws.vn/httpdocs`
* **FTP Host:** `203.205.31.252:21`
* **FTP Username:** `u513776f0`
* **FTP Password:** `1~dzR0hkLJ0~tlgm`
* **Database (MariaDB):**
  * **Host:** `localhost:3306`
  * **Database Name:** `db_c3c66f76`
  * **DB User:** `db_c3c66f76`
  * **DB Password:** `oVkoa?B0p_t9ePk6`

### 4.2. Quy Trình Triển Khai Tự Động (CI/CD Pipeline)
Toàn bộ mã nguồn và tài nguyên được đóng gói và cập nhật trực tiếp lên máy chủ qua kịch bản tự động `deploy.py`:
```bash
# Lệnh cập nhật website lên Production trong 1 bước:
python3 deploy.py
```
**Quy trình 4 bước tự động:**
1. Đóng gói mã nguồn `deploy.zip` (tự động bỏ qua `.git`, `.venv`, file rác).
2. Tải `deploy.zip` và `extractor.php` lên thư mục `/httpdocs` qua giao thức FTP an toàn.
3. Kích hoạt giải nén máy chủ và tự động xóa file zip sau khi hoàn tất.
4. Chạy kiểm tra HTTP Endpoint (Status 200 OK) xác nhận thành công.

---

## 5. 🛠️ HƯỚNG DẪN BẢO TRÌ & MỞ RỘNG (MAINTENANCE GUIDE)

### 5.1. Cập Nhật Thông Tin Hoặc Số Điện Thoại
* Mở file `assets/js/main.js` hoặc file HTML tương ứng, tìm kiếm số điện thoại `0383.707.578` hoặc email `pm@goodsolutions.com.vn` để thay đổi.
* Chạy `python3 deploy.py` để đẩy cập nhật lên máy chủ.

### 5.2. Thêm Sản Phẩm Mới Hoặc Đổi Giá
* Hình ảnh sản phẩm lưu tại thư mục: `assets/images/s54/`.
* Mở `collections-coffee.html` hoặc `index.html`, sao chép khối `o-product-thumbnail` và cập nhật tiêu đề, hình ảnh và giá VND.
* Khai báo cặp từ khóa tương ứng trong `assets/js/i18n.js` nếu muốn hỗ trợ song ngữ.

### 5.3. Quy Trình Làm Việc Với Git
```bash
# Kiểm tra thay đổi
git status

# Commit và đẩy lên GitHub
git add .
git commit -m "feat/fix: mô tả thay đổi"
git push origin main

# Triển khai lên Production
python3 deploy.py
```

---

**Bàn giao bởi:** Antigravity Pairing Assistant  
**Đơn vị tiếp nhận:** Đội ngũ Kỹ thuật & Quản trị Website S54 COFFEE  
**Trạng thái:** ✅ SẴN SÀNG VẬN HÀNH & KINH DOANH
