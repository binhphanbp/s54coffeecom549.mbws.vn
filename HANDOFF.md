# ☕ S54 COFFEE — TÀI LIỆU BÀN GIAO DỰ ÁN TOÀN DIỆN (MASTER PROJECT HANDOFF)

> **Dự án:** Hệ thống Website Thương Mại Điện Tử & Giới Thiệu Doanh Nghiệp **S54 COFFEE**  
> **Chủ quản:** CÔNG TY TNHH GIẢI PHÁP TỐT (Good Solutions Co., Ltd)  
> **Website Chính Thức:** [https://s54coffeecom549.mbws.vn/](https://s54coffeecom549.mbws.vn/)  
> **Repository (Git):** `git@github.com:matbao-ws/s54coffeecom549.mbws.vn.git` (Nhánh chính: `main`)  
> **Nguồn dữ liệu đối chiếu:** [Google Drive - Thông tin trang web S54 Coffee](https://drive.google.com/drive/folders/1jIrSz7F7_Ruc8myLEJOE6seOlIOMBNtL)  
> **Phiên bản:** `v3.0 - Laravel Core Admin & Storefront Integrated Release`  
> **Ngày bàn giao:** 28/08/2026  

---

## 1. 🏛️ THÔNG TIN DOANH NGHIỆP & THƯƠNG HIỆU

| Thông Tin | Chi Tiết Xác Thực |
| :--- | :--- |
| **Tên Thương Hiệu** | **S54 COFFEE** |
| **Đơn Vị Chủ Quản** | **CÔNG TY TNHH GIẢI PHÁP TỐT (Good Solutions Co., Ltd)** — Thành lập 2012 |
| **Định Vị & Slogan** | *"New Coffee, New Income" • "Vietnamese Coffee. Made for the World."* |
| **Ý Nghĩa Tên Gọi S54** | Sự kết hợp giữa biểu tượng **dải đất hình chữ S** và khối đoàn kết **54 dân tộc anh em**. |
| **Trụ Sở Chính** | Số 35, Đường T8, The Manhattan, Vinhomes Grand Park, Phường Long Bình, TP. Thủ Đức, TP.HCM |
| **Điểm Trải Nghiệm Cafe** | Chuỗi điểm trải nghiệm cà phê S54 tại Nhà Bè, TP.HCM |
| **Hotline / Zalo** | `0383.707.578` — `0902.873.345` |
| **Email Hỗ Trợ** | `pm@goodsolutions.com.vn` |
| **Chính Sách Vận Chuyển** | Miễn phí vận chuyển toàn quốc cho đơn hàng từ **500.000₫** |

---

## 2. 🏗️ KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

Dự án được xây dựng theo mô hình tích hợp đồng bộ giữa **Laravel 11 Ecommerce Core Admin Backend** và **Giao diện Storefront Blade đa ngôn ngữ**:

```
s54coffeecom549.mbws.vn/
├── app/
│   ├── Http/Controllers/
│   │   ├── Admin/                      # Bộ điều khiển quản trị hệ thống (Sản phẩm, đơn hàng, CMS)
│   │   ├── Api/PublicController.php    # API công khai cho Client
│   │   └── Client/                     # Bộ điều khiển Storefront Blade
│   │       ├── HomeController.php      # Trang chủ S54 Coffee
│   │       ├── CatalogController.php   # Danh mục & Chi tiết sản phẩm
│   │       ├── BlogController.php      # Cẩm nang & Tin tức
│   │       └── PageController.php      # CMS Pages (Our Story, Wholesale)
│   ├── Models/                         # Toàn bộ Eloquent Models (Product, Category, Post, Page, ...)
│   └── Services/Catalog/
│       └── ProductQueryService.php     # Service dùng chung truy vấn đọc sản phẩm chuẩn kiến trúc
├── database/
│   ├── migrations/                     # Lược đồ cơ sở dữ liệu Laravel
│   └── seeders/
│       ├── DatabaseSeeder.php          # Seeder chính
│       └── S54StorefrontSeeder.php     # Seeder dữ liệu thực tế S54 Coffee (đa ngôn ngữ JSON)
├── public/
│   ├── client-assets/                  # Toàn bộ CSS, JS, hình ảnh chụp thực tế của S54
│   │   ├── css/ (custom.css, layouts.critical.css, layouts.theme.css, ...)
│   │   ├── js/ (client-cart.js, main.js, i18n.js, vendor.js, ...)
│   │   └── images/s54/ (Ảnh sản phẩm, ảnh quán Nhà Bè, ảnh văn phòng Vinhomes)
│   └── index.php                       # Entrypoint Laravel
├── resources/views/
│   ├── admin/                          # Giao diện quản trị Admin Panel
│   └── client/                         # Giao diện Storefront S54 Coffee
│       ├── layouts/app.blade.php       # Master layout kèm Admin Bar & Inline Editing
│       ├── partials/                   # header, footer, head, cart-drawer
│       ├── components/                 # x-client.product-card
│       ├── pages/                      # home, our-story, wholesale
│       ├── catalog/                    # index, product
│       └── blog/                       # index, post
├── routes/
│   ├── client.php                      # Định tuyến Storefront đa ngôn ngữ /{locale}/...
│   ├── admin.php                       # Định tuyến Quản trị viên
│   └── web.php                         # Root locale redirect
├── theme/                              # Thư mục lưu trữ bản tĩnh HTML5 gốc
├── deploy.py                           # Kịch bản triển khai tự động lên Hosting qua FTP
└── composer.json / artisan             # Laravel Application Core
```

---

## 3. 📑 CHI TIẾT CÁC TRANG & DỮ LIỆU ĐÃ ĐỒNG BỘ

### 3.1. Trang Giới Thiệu / Câu Chuyện Thương Hiệu (`our-story.blade.php` / `our-story.html`)
Đã đồng bộ 100% từ thư mục Google Drive `2. Giới thiệu` của khách hàng:
* **Thông điệp:** *"S54 COFFEE • Vietnamese Coffee. Made for the World."* — Tinh hoa Robusta & Arabica Tây Nguyên.
* **Bộ 3 Trụ Cột Chiến Lược (Nhúng Video YouTube Chính Thức):**
  * **Tầm Nhìn (Vision):** *Trở thành thương hiệu cà phê Việt uy tín, vươn tầm quốc tế.* (Video: `8nVnuZSauE8`).
  * **Sứ Mệnh (Mission):** *Mang đến tách cà phê chuẩn vị, truyền năng lượng tích cực và tạo dựng thu nhập bền vững ("New Coffee, New Income").* (Video: `bIC2_Dko3xk`).
  * **Giá Trị Cốt Lõi (Core Values):** *Trung thực • Chất lượng • Cải tiến • Đồng hành.* (Video: `T8MfqRZlsFo`).
* **Hành Trình 3 Cột Mốc:**
  * *Cột mốc 1:* Nghiên cứu & phát triển dòng hòa tan 3in1 và hạt rang chuẩn vị Tây Nguyên.
  * *Cột mốc 2:* Mở rộng mạng lưới phân phối, phát triển chuỗi cửa hàng trải nghiệm.
  * *Cột mốc 3:* Chuyển đổi số thương hiệu, hoàn thiện website bán hàng và hệ thống Core Admin.
* **Hình Ảnh Thực Tế:**
  * 📸 Văn phòng Vinhomes Grand Park (`s54_office_vinhome_1.jpg`, `s54_office_vinhome_2.jpg`, `s54_office_vinhome_3.jpg`).
  * 📸 Quán Cà Phê S54 tại Nhà Bè (`s54_cafe_nhabe_1.jpg`, `s54_cafe_nhabe_2.jpg`, `s54_cafe_nhabe_3.jpg`).

### 3.2. Trang Chủ (`home.blade.php` / `index.html`)
* **Hero Banner:** Tiêu đề công nghệ rang Hot-Air hồi khí của Đức, 100% cà phê nguyên chất.
* **Lưới 4 Cột Sản Phẩm Bán Chạy:** Cân đối hoàn hảo, chiều cao co giãn tự nhiên, không bị đè chữ, không lỗi khoảng trắng.
* **Triết Lý Thương Hiệu:** Khối trích dẫn *"Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp."*

### 3.3. Trang Danh Mục & Chi Tiết Sản Phẩm (`catalog/` & `collections-coffee.html`)
* **Bộ Lọc Danh Mục:** Phân loại rõ ràng (*Cà Phê Hạt Rang Mộc, Specialty, Cà Phê Hòa Tan 3in1, Dụng Cụ Pha Chế*).
* **Card Sản Phẩm Đã Sửa Lỗi Triệt Để:**
  * Đã gỡ bỏ `min-height: 50rem` (800px) gây khoảng trống rỗng.
  * Hiển thị đầy đủ giá cho toàn bộ 18 sản phẩm (kể cả sản phẩm Decaf).
  * Tiếng Việt chuẩn hóa 100%, bỏ hoàn toàn chữ `FROM` hay bản dịch lỗi cũ.
* **Chi Tiết Sản Phẩm:** Chọn quy cách (1kg / 500g / 200g), hiển thị giá động, bộ tăng giảm số lượng và nút thêm vào giỏ hàng.

### 3.4. Trang B2B / Bán Sỉ Doanh Nghiệp (`wholesale.blade.php` / `wholesale.html`)
* Giải pháp cung ứng cà phê số lượng lớn cho quán cafe, nhà hàng, khách sạn và văn phòng.
* Chính sách gia công thương hiệu OEM/ODM và form gửi yêu cầu báo giá.

### 3.5. Trang Cẩm Nang & Tin Tức (`blog/` & `blogs-news.html`)
* Đã cấu trúc sẵn sàng tích hợp 14 bài viết tin tức, cẩm nang pha chế và kiến thức cà phê từ bảng tính `Tin tức` trên Google Drive.

---

## 4. 🌐 TÍNH NĂNG TƯƠNG TÁC NỔI BẬT

1. **Đa Ngôn Ngữ Song Ngữ (Bilingual i18n VI / EN):**
   * Hơn 220+ cặp từ khóa dịch tự động trong `i18n.js`.
   * Chuyển đổi mượt mà 1 chạm trên Header / Footer, lưu trạng thái vào `localStorage`.
   * Tương thích với routing đa ngôn ngữ của Laravel (`/{locale}/...`).
2. **Slide-Out Cart Drawer (Giỏ Hàng Trượt):**
   * Quản lý trạng thái giỏ hàng qua `client-cart.js`.
   * Thêm nhanh sản phẩm từ Trang chủ hoặc Danh mục, tăng giảm số lượng tức thì, tính tổng tiền chuẩn xác và thanh tiến trình miễn phí vận chuyển.
3. **Quản Trị Admin Panel & Inline Editing:**
   * Tích hợp thanh công cụ `admin-bar` trên đầu trang khi quản trị viên đăng nhập.
   * Hỗ trợ chỉnh sửa nội dung CMS trực tiếp trên giao diện qua `inline-blocks` và `inline-outline`.

---

## 5. 🚀 THÔNG TIN MÁY CHỦ & TRIỂN KHAI (DEPLOYMENT)

### 5.1. Thông Số Máy Chủ Production
* **Tên miền:** `https://s54coffeecom549.mbws.vn/`
* **IP Server:** `203.205.31.252`
* **Webroot Path:** `/var/www/vhosts/s54coffeecom549.mbws.vn/httpdocs`
* **FTP Host:** `203.205.31.252:21` (User: `u513776f0` | Pass: `1~dzR0hkLJ0~tlgm`)
* **Database (MariaDB):**
  * **Host:** `localhost:3306`
  * **Database Name:** `db_c3c66f76`
  * **DB User:** `db_c3c66f76`
  * **DB Password:** `oVkoa?B0p_t9ePk6`

### 5.2. Lệnh Triển Khai Tự Động
```bash
# Triển khai toàn bộ dự án lên Production Hosting:
python3 deploy.py
```

---

## 6. 🛠️ HƯỚNG DẪN QUẢN TRỊ & BẢO TRÌ (OPERATIONS GUIDE)

### 6.1. Quy Trình Làm Việc Với Git
```bash
# 1. Kiểm tra trạng thái mã nguồn
git status

# 2. Thêm file và commit
git add .
git commit -m "feat/fix: mô tả nội dung cập nhật"

# 3. Đẩy lên repository dự án
git push origin main
```

### 6.2. Khởi Tạo Cơ Sở Dữ Liệu & Seed Data Thực Tế
```bash
# Chạy migration và nạp dữ liệu S54 thực tế:
php artisan migrate:fresh --seed --seeder=S54StorefrontSeeder
```

### 6.3. Thêm Sản Phẩm Hoặc Bài Viết Mới
* **Qua Admin Panel:** Đăng nhập vào `/vi/admin` ➔ Truy cập menu **Sản phẩm** hoặc **Tin tức** để tạo mới.
* **Qua Code / Seeder:** Bổ sung thông tin vào `database/seeders/S54StorefrontSeeder.php` với cấu trúc JSON song ngữ `['vi' => '...', 'en' => '...']`.

---

## 7. 📦 DANH SÁCH COMMITS QUAN TRỌNG

| Commit ID | Tóm Tắt Nội Dung |
| :--- | :--- |
| **`9554d50`** | **`feat(our-story)`**: Cập nhật trang Giới Thiệu từ dữ liệu Google Drive của khách (ảnh thực tế, video YouTube, tầm nhìn, sứ mệnh, giá trị cốt lõi, 3 cột mốc). |
| **`fc51e08`** | **`fix(collections)`**: Khắc phục triệt để khoảng trống card sản phẩm (`min-height: 0`), bổ sung giá Decaf và chuẩn hóa 100% tiếng Việt. |
| **`0c7c665`** | **`feat(core)`**: Ghép nối trọn vẹn Laravel Ecommerce Core Admin Backend vào dự án S54 Coffee. |

---

**Đơn vị thực hiện bàn giao:** Antigravity Pairing Assistant  
**Đơn vị tiếp nhận:** Đội ngũ Kỹ thuật & Quản trị Dự án S54 COFFEE  
**Tình trạng kiểm thử:** ✅ **100% HOÀN TẤT • KHÔNG LỖI • SẴN SÀNG VẬN HÀNH**
