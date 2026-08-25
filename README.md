# Vittoria Coffee Website Replica (100% Pixel-Perfect Clone)

Giao diện website **Vittoria Coffee** (`https://www.vittoriacoffee.com/`) được cào và tái hiện 100% chuẩn xác về hình ảnh, typography (font độc quyền Neutra2, Domaine, Gilroy), phong cách thiết kế cao cấp và đầy đủ các tính năng tương tác (giỏ hàng trượt, carousel sản phẩm, responsive trên mọi thiết bị).

---

## 🌟 Tính Năng Nổi Bật (Key Features)

- **100% Offline & Tự Chủ Dữ Liệu**: Toàn bộ font chữ, stylesheet, hình ảnh chuẩn HD/Retina và video media đã được tải về cục bộ (`assets/`).
- **Hệ Thống Typography Sang Trọng**:
  - `Neutra2 Text Book` & `Neutra2 Text Demi`
  - `Domaine Regular` & `Domaine Regular Italic`
  - `Gilroy SemiBold`
- **Tương Tác Giỏ Hàng Trượt (Interactive Slide-Out Cart Drawer)**:
  - Thanh tiến trình freeship ($69.00 threshold).
  - Thêm sản phẩm nhanh (Quick Add / Add to Bag).
  - Tăng / giảm số lượng món (+/-) và tính toán tổng tiền trực tiếp.
  - Toast thông báo trạng thái mượt mà.
- **Trọn Bộ Các Trang Chính (Multi-Page Architecture)**:
  - `index.html`: Trang chủ (Hero Banner, Bestsellers Carousel, Collections Grid, Brand Story, Master Roasting Video, Blog Feed, Instagram Gallery, Footer).
  - `collections-coffee.html`: Danh mục toàn bộ các dòng cà phê (Hạt, Viên nén, Hòa tan, Xay sẵn).
  - `product-detail.html`: Trang chi tiết sản phẩm chuẩn chỉnh (Cinque Stelle Special Bar Beans).
  - `our-story.html`: Trang lịch sử thương hiệu cà phê số 1 nước Úc.
  - `wholesale.html`: Trang giải pháp bán sỉ cho doanh nghiệp và quán cafe.
- **Hỗ Trợ Máy Chủ Cục Bộ Tích Hợp (`server.py`)**:
  - Tự động định tuyến Clean URL (`/collections/coffee`, `/products/...`, `/pages/...`).
  - Hỗ trợ Mock API Shopify Cart (`/cart.js`, `/cart/add.js`).
  - Hỗ trợ kết nối chuẩn `localhost:3000` và `127.0.0.1:3000`.

---

## 📁 Cấu Trúc Thư Mục (Project Structure)

```text
s54coffeecom549.mbws.vn/
├── assets/
│   ├── css/              # 12 file CSS (Theme, Layout, Sections, Custom)
│   ├── fonts/            # 10 file font WOFF / WOFF2 (Neutra2, Domaine, Gilroy)
│   ├── images/           # 380+ hình ảnh chất lượng cao & Icon SVG thương hiệu
│   ├── js/               # Theme JS, vendor JS & Bộ điều khiển tương tác (main.js)
│   └── media/            # Video hướng dẫn pha chế MP4 (Desktop & Mobile)
├── index.html            # Trang chủ chính
├── collections-coffee.html # Trang danh mục sản phẩm
├── product-detail.html   # Trang chi tiết sản phẩm
├── our-story.html        # Trang câu chuyện thương hiệu
├── wholesale.html        # Trang bán sỉ
├── server.py             # Máy chủ HTTP cục bộ với Routing & Mock Cart API
├── .gitignore            # Cấu hình bỏ qua tệp tạm
└── README.md             # Tài liệu hướng dẫn dự án
```

---

## 🚀 Hướng Dẫn Chạy Cục Bộ (Quick Start)

### Cách 1: Khởi chạy máy chủ HTTP (Khuyên dùng)
Yêu cầu: Đã cài đặt **Python 3.x**.

```bash
# Di chuyển vào thư mục dự án
cd s54coffeecom549.mbws.vn

# Chạy server
python server.py
```
Sau đó mở trình duyệt và truy cập:
- 👉 **http://localhost:3000/** hoặc **http://127.0.0.1:3000/**

### Cách 2: Mở trực tiếp không cần server (100% Offline)
Nhấp đúp chuột vào tệp `index.html` để mở ngay trên bất kỳ trình duyệt nào (Chrome, Edge, Safari, Firefox).

---

## 🛠️ Công Nghệ Sử Dụng (Tech Stack)
- **HTML5 & CSS3**: Tái cấu trúc chuẩn Responsive, Flexbox, Grid, Clean UI.
- **Vanilla JavaScript**: Tối ưu hiệu năng, không phụ thuộc framework cồng kềnh.
- **Python**: Bộ công cụ tự động hóa cào dữ liệu, biên dịch trang và máy chủ HTTP mini.

---

## 📄 Bản Quyền & Giấy Phép
Dự án được thực hiện nhằm mục đích học tập, nghiên cứu và phát triển giao diện thương mại điện tử chuẩn quốc tế.
Tất cả hình ảnh, logo và nhãn hiệu thuộc về **Vittoria Coffee**.
