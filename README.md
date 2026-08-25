# Vittoria Coffee Storefront (Standardized & Production-Ready Replica)

Dự án giao diện website thương mại điện tử **Vittoria Coffee** (`https://www.vittoriacoffee.com/`) đã được chuẩn hóa toàn diện theo kiến trúc module sạch (Clean Architecture), sẵn sàng triển khai trên hệ thống Mat Bao Web Services hoặc preview cục bộ trên mọi nền tảng (Linux, Windows, macOS).

---

## 🌟 Điểm Nổi Bật Của Dự Án

- **100% Offline & Tự Chủ Dữ Liệu**: Toàn bộ font chữ độc quyền, stylesheets, 380+ hình ảnh chất lượng cao và video media đều được lưu trữ cục bộ (`assets/`).
- **Hệ Thống Typography Chuẩn Quốc Tế**:
  - `Neutra2 Text Book` & `Neutra2 Text Demi`
  - `Domaine Regular` & `Domaine Regular Italic`
  - `Gilroy SemiBold`
- **Kiến Trúc Module JavaScript Chuyên Nghiệp**:
  - `assets/js/cart-mock.js`: Quản lý mock state giỏ hàng, tự động đồng bộ qua `sessionStorage`, intercept fetch API `/cart...` theo chuẩn Shopify AJAX API.
  - `assets/js/main.js`: Điều khiển giao diện giỏ hàng trượt (Slide-out Cart Drawer), thanh tiến trình Freeship $69, tăng giảm số lượng (+/-), carousels và video player.
- **Trọn Bộ 5 Trang Chính + Trang Báo Lỗi 404**:
  - `index.html`: Trang chủ đầy đủ các khối nội dung, video xưởng rang, bestsellers.
  - `collections-coffee.html`: Danh mục toàn bộ các dòng sản phẩm cà phê.
  - `product-detail.html`: Trang chi tiết sản phẩm chuẩn chỉnh (Cinque Stelle Special Bar Beans).
  - `our-story.html`: Trang câu chuyện di sản và thương hiệu.
  - `wholesale.html`: Trang giải pháp bán sỉ B2B.
  - `404.html`: Trang thông báo không tìm thấy trang với giao diện sang trọng.
- **Tiêu Chuẩn SEO & Máy Chủ**:
  - `.htaccess`: Cấu hình URL Rewrite (Clean URL), Gzip/Brotli Compression, Browser Caching và Security Headers.
  - `robots.txt` & `sitemap.xml`: Chuẩn hóa cấu trúc thu thập dữ liệu tìm kiếm.
  - `server.py`: Máy chủ HTTP mini đa luồng hỗ trợ Clean URL và Shopify Mock Cart API.

---

## 📁 Cấu Trúc Thư Mục Chuẩn

```text
s54coffeecom549.mbws.vn/
├── assets/
│   ├── css/              # 12+ Stylesheets module hóa (Theme, Layout, Sections, Custom)
│   ├── fonts/            # Webfonts chuẩn WOFF / WOFF2 (Neutra2, Domaine, Gilroy)
│   ├── icons/            # Brand SVG icons
│   ├── images/           # 380+ hình ảnh chất lượng cao Retina/HD
│   ├── js/               # Theme JS, vendor.js, main.js và cart-mock.js
│   └── media/            # Video MP4 giới thiệu & hướng dẫn pha chế
├── index.html            # Trang chủ
├── collections-coffee.html # Danh mục sản phẩm
├── product-detail.html   # Chi tiết sản phẩm
├── our-story.html        # Câu chuyện thương hiệu
├── wholesale.html        # Bán buôn / Bán sỉ
├── 404.html              # Trang báo lỗi 404
├── .htaccess             # Cấu hình máy chủ Apache/LiteSpeed
├── robots.txt            # Chỉ dẫn crawler
├── sitemap.xml           # Sơ đồ trang web SEO
├── server.py             # Máy chủ preview cục bộ đa nền tảng
├── cart.js               # Dữ liệu mẫu giỏ hàng JSON
├── tools/                # Thư mục công cụ scraper, builder & raw data
│   ├── raw_html/         # Dữ liệu cào gốc
│   ├── build_all_pages.py
│   ├── compile_pages_fast.py
│   └── ...
├── .gitignore
└── README.md
```

---

## 🚀 Hướng Dẫn Khởi Chạy

### Cách 1: Chạy qua Python Preview Server (Khuyên dùng)
Yêu cầu: Python 3.8+ (tương thích cả Linux, macOS và Windows).

```bash
# Di chuyển vào thư mục dự án
cd clients/s54coffeecom549.mbws.vn

# Khởi chạy server
python3 server.py
```
Mở trình duyệt truy cập:
- 👉 **http://localhost:3000/** hoặc **http://127.0.0.1:3000/**

**Các Clean URLs được hỗ trợ:**
- `/` -> Trang chủ
- `/collections/coffee` -> Danh mục sản phẩm
- `/products/cinque-stelle-beans` -> Chi tiết sản phẩm
- `/pages/our-story` -> Câu chuyện thương hiệu
- `/pages/wholesale` -> Bán sỉ
- `/cart.js` -> Mock API giỏ hàng

### Cách 2: Mở trực tiếp (100% Offline)
Nhấp đúp chuột vào bất kỳ file `.html` (`index.html`, `collections-coffee.html`, `product-detail.html`, `our-story.html`, `wholesale.html`, `404.html`) để xem ngay trên trình duyệt mà không cần internet hay máy chủ.

---

## 🛠️ Công Nghệ & Tiêu Chuẩn

- **Frontend**: HTML5 Semantic, CSS3 Modular, Vanilla JavaScript (ES6+).
- **Typography**: `@font-face` tự chủ với WOFF2/WOFF (Neutra2, Domaine, Gilroy).
- **Backend / Mock API**: Python 3 SocketServer đa luồng, RESTful JSON responses.
- **Server Configuration**: Apache/LiteSpeed `.htaccess` với Deflate, Mod_Expires, Mod_Rewrite.
