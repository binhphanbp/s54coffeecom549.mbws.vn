/**
 * S54 COFFEE - Master Internationalization (i18n) Engine
 * 100% Comprehensive Bidirectional Translation: Vietnamese (Canonical Default) & English
 */
(function () {
    'use strict';

    const STORAGE_KEY = 's54_storefront_lang';

    // Comprehensive Modular Translation Dictionary (VI <-> EN)
    const translationPairs = [
        // 1. TOPBAR & NAVIGATION
        ["Miễn phí vận chuyển toàn quốc cho đơn từ 599.000₫ • Hotline: 0383.707.578", "Free nationwide shipping on orders over 599,000₫ • Hotline: (+84) 383 707 578"],
        ["MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578", "FREE NATIONWIDE SHIPPING ON ORDERS OVER 599,000₫ • HOTLINE: (+84) 383 707 578"],
        ["Tất Cả Sản Phẩm", "All Products"],
        ["TẤT CẢ SẢN PHẨM", "ALL PRODUCTS"],
        ["Cà Phê Hạt & Rang Mộc", "Coffee Beans & Roast"],
        ["CÀ PHÊ HẠT & RANG MỘC", "COFFEE BEANS & ROAST"],
        ["Hòa Tan & Sấy Lạnh", "Instant & Freeze-Dried"],
        ["HÒA TAN & SẤY LẠNH", "INSTANT & FREEZE-DRIED"],
        ["Câu Chuyện S54", "Our Story"],
        ["CÂU CHUYỆN S54", "OUR STORY"],
        ["B2B & Đại Lý", "B2B & Wholesale"],
        ["B2B & ĐẠI LÝ", "B2B & WHOLESALE"],
        ["Tin Tức & Kiến Thức Cà Phê", "News & Coffee Insights"],
        ["Góc Thưởng Thức S54", "S54 Coffee Journal"],
        ["Liên Hệ Hợp Tác", "Partner Contact"],
        ["LIÊN HỆ HỢP TÁC", "PARTNER CONTACT"],

        // 2. HERO & HOMEPAGE EDITORIAL
        ["Tinh Hoa Cà Phê Việt®", "The Essence of Vietnamese Coffee®"],
        ["Tinh Hoa<br/>Cà Phê Việt®", "The Essence of<br/>Vietnamese Coffee®"],
        ["100% Cà phê rang mộc nguyên chất từ vùng đất đỏ Tây Nguyên", "100% Pure roasted coffee beans from Central Highlands volcanic soil"],
        ["MUA SẮM NGAY", "SHOP NOW"],
        ["Mua Sắm Ngay", "Shop Now"],
        ["HỢP TÁC B2B & ĐẠI LÝ", "B2B & WHOLESALE PARTNER"],
        ["Hợp Tác B2B & Đại Lý", "B2B & Wholesale Partner"],
        ["TÌM HIỂU THÊM", "LEARN MORE"],
        ["Tìm Hiểu Thêm", "Learn More"],
        ["XEM THÊM", "VIEW MORE"],
        ["Xem Thêm", "View More"],
        ["XEM TẤT CẢ", "VIEW ALL"],
        ["Xem Tất Cả", "View All"],
        ["ĐỌC BÀI VIẾT", "READ ARTICLE"],
        ["Đọc Bài Viết", "Read Article"],
        ["Đọc Tiếp →", "Read More →"],
        ["Khám Phá Dòng Cà Phê S54", "Discover S54 Coffee Range"],
        ["“S54 Coffee mang đến giải pháp cà phê sạch nguyên chất, đậm đà vị truyền thống và phong cách hiện đại cho hàng triệu người tiêu dùng.”", "“S54 Coffee delivers pure, clean coffee solutions with authentic rich flavor and modern style to millions of consumers.”"],
        ["Hơn 12 Năm Kinh Nghiệm & Đam Mê Cà Phê Sạch", "Over 12 Years of Clean Coffee Passion & Expertise"],
        ["Thành lập từ năm 2012 bởi Công ty TNHH Giải Pháp Tốt (Good Solutions), S54 Coffee tự hào kế thừa tinh hoa cà phê Robusta & Arabica từ vùng đất đỏ bazan Tây Nguyên (Đắk Lắk, Lâm Đồng). Chúng tôi áp dụng quy trình kiểm soát nghiêm ngặt từ hạt giống, nông trại thông minh đến công nghệ rang mộc hiện đại, lưu giữ trọn vẹn hương thơm tự nhiên và hậu vị sâu lắng đặc trưng của cà phê Việt.", "Established in 2012 by Good Solutions Co., Ltd, S54 Coffee inherits the finest Robusta & Arabica beans from the Central Highlands (Dak Lak, Lam Dong). We employ rigorous quality control from smart farming to modern artisan roasting."],
        ["Nghệ Thuật Pha Chế & Thưởng Thức Cà Phê S54 Chuẩn Vị", "The Art of Brewing & Enjoying Authentic S54 Coffee"],
        ["Cùng chuyên gia S54 Coffee khám phá bí quyết chiết xuất tách Espresso thơm ngậy với lớp crema dày sánh mịn hoặc pha phin truyền thống đậm đà khó quên.", "Join S54 Coffee experts to discover the secrets of brewing rich Espresso with golden crema or traditional Vietnamese drip coffee."],

        // 3. PRODUCT DETAIL & ACCORDIONS
        ["Mô Tả Sản Phẩm", "Product Description"],
        ["Nguồn Gốc & Vùng Trồng", "Origins & Sourcing"],
        ["Vùng trồng Đắk Lắk & Cầu Đất (Lâm Đồng), sơ chế ướt và phơi giàn tự nhiên.", "Origins from Dak Lak & Cau Dat (Lam Dong), fully washed & naturally raised bed dried."],
        ["Thông Số Chiết Xuất Chuẩn", "Extraction Parameters"],
        ["Nhiệt độ pha: 90°C - 93°C<br>Lượng bột cà phê (Dose in): 20g - 22g<br>Lượng chiết xuất (Dose out): 40ml - 45ml<br>Thời gian chiết xuất: 25 - 30 giây",
         "Brew Temperature: 90°C - 93°C<br>Dose in: 20g - 22g<br>Dose out: 40ml - 45ml<br>Extraction Time: 25 - 30 seconds"],
        ["Cấp Độ Rang", "Roast Profile"],
        ["Rang Vừa Đậm (Medium-Dark)", "Medium-Dark Roast"],
        ["Rang Vừa (Medium Roast)", "Medium Roast"],
        ["Rang Đậm (Dark Roast)", "Dark Roast"],
        ["Chọn Quy Cách", "Select Size"],
        ["Khối Lượng:", "Size:"],
        ["Đăng Ký Định Kỳ & Tiết Kiệm 25%", "Subscribe & Save 25%"],
        ["Độc Quyền Online", "Online Exclusive"],
        ["ĐỘC QUYỀN ONLINE", "ONLINE EXCLUSIVE"],
        ["Độc quyền online", "Online exclusive"],
        ["Còn Hàng", "In Stock"],
        ["Hết Hàng", "Sold Out"],
        ["HẾT HÀNG", "SOLD OUT"],
        ["Hết hàng", "Sold out"],
        ["THÊM VÀO GIỎ", "ADD TO BAG"],
        ["Thêm Vào Giỏ", "Add to Bag"],
        ["ĐÃ THÊM!", "ADDED!"],
        ["Số Lượng", "Quantity"],
        ["SỐ LƯỢNG", "QUANTITY"],
        ["Sản Phẩm Cùng Dòng", "Related Products"],
        ["Có Thể Bạn Cũng Thích", "You May Also Like"],
        ["Đánh Giá Từ Khách Hàng", "Customer Reviews"],
        ["Viết Đánh Giá", "Write A Review"],
        ["Dựa trên 765 đánh giá thực tế", "Based on 765 customer reviews"],
        ["Số Sao Đánh Giá", "Star Rating"],
        ["Đánh giá 4.8 trên 5 sao", "Rated 4.8 out of 5 stars"],
        ["Đánh giá 4.7 trên 5 sao", "Rated 4.7 out of 5 stars"],
        ["Đánh giá 4.9 trên 5 sao", "Rated 4.9 out of 5 stars"],
        ["Đánh Giá", "Reviews"],
        ["Sao", "Stars"],

        // 4. COLLECTION & FACETED FILTERS
        ["BỘ LỌC & SẮP XẾP", "FILTERS & SORTING"],
        ["Bộ Lọc & Sắp Xếp", "Filters & Sorting"],
        ["BỘ LỌC", "FILTERS"],
        ["Bộ Lọc", "Filters"],
        ["Xóa Tất Cả", "Clear All"],
        ["Áp Dụng", "Apply Filters"],
        ["Danh Mục", "Category"],
        ["Phương Pháp Pha", "Brewing Method"],
        ["Khoảng Giá", "Price Range"],
        ["Sắp Xếp Theo", "Sort by"],
        ["Nổi Bật", "Featured"],
        ["NỔI BẬT", "FEATURED"],
        ["Bán Chạy Nhất", "Best Selling"],
        ["Giá: Thấp Đến Cao", "Price: Low to High"],
        ["Giá: Cao Đến Thấp", "Price: High to Low"],
        ["Tên: A Đến Z", "Name: A to Z"],
        ["Tên: Z Đến A", "Name: Z to A"],
        ["Cũ Nhất", "Date: Old to New"],
        ["Mới Nhất", "Date: New to Old"],
        ["Dòng Specialty Tuyển Chọn", "Exclusive Specialty Range"],
        ["Dòng cà phê thượng hạng phục vụ tại các nhà hàng & quán cafe cao cấp", "Our premiere blend, served in leading restaurants & premium cafes"],
        ["Độ rang đậm đà, mang lại hương vị espresso nồng nàn và mạnh mẽ", "Our darkest roast offering a bold and intense cup"],
        ["Hương vị caramel ngọt ngào, thơm bùi hạt rang và hậu vị thanh êm", "A medium blend with sweet caramel and toasted nut notes"],
        ["Đậm đà, béo ngậy với nốt hương sô cô la đen nguyên chất", "Rich and full-bodied blend with hints of dark chocolate"],
        ["Cân bằng, êm dịu, hoàn hảo cho gu thưởng thức mỗi ngày", "Smooth and balanced everyday blend"],
        ["Rang đậm truyền thống với nốt hương khói thơm nồng", "A dark roast blend with intense smoky notes"],
        ["Dòng blend phục vụ khách sạn & nhà hàng được ưa chuộng nhất", "Our most popular blend for luxury hotels & restaurants"],

        // 5. PRODUCT NAMES
        ["Cinque Stelle® Dòng Special Bar Thượng Hạng Cà Phê Hạt", "Cinque Stelle® Special Bar Premium Coffee Beans"],
        ["Oro™ Dòng Special Bar Cà Phê Hạt", "Oro™ Special Bar Coffee Beans"],
        ["Nero Dòng Special Bar Cà Phê Hạt", "Nero Special Bar Coffee Beans"],
        ["S54 Robusta Rang Mộc Nguyên Chất", "S54 Pure Roasted Robusta Beans"],
        ["S54 Arabica Cầu Đất Thượng Hạng", "S54 Premium Cau Dat Arabica"],
        ["S54 Hòa Tan 3-in-1 Hộp 456g", "S54 3-in-1 Instant Coffee (456g)"],
        ["S54 Cà Phê Sấy Lạnh Cao Cấp", "S54 Premium Freeze-Dried Coffee"],
        ["S54 Cà Phê Túi Lọc Drip Bag", "S54 Drip Bag Filter Coffee"],
        ["Cà Phê Hòa Tan 3in1 (456g)", "3-in-1 Instant Coffee (456g)"],
        ["Cà Phê Sấy Lạnh Cao Cấp", "Premium Freeze-Dried Coffee"],
        ["Cà Phê Túi Lọc Drip Bag", "Drip Bag Coffee Sachets"],
        ["Cà Phê Xay Pha Phin", "Traditional Drip Ground Coffee"],

        // 6. CART DRAWER
        ["Giỏ Hàng Của Bạn", "Your Bag"],
        ["TIẾN HÀNH THANH TOÁN", "PROCEED TO CHECKOUT"],
        ["Tiến Hành Thanh Toán", "Proceed to Checkout"],
        ["Tạm Tính", "Subtotal"],
        ["Giỏ hàng của bạn đang trống.", "Your bag is currently empty."],
        ["Bắt Đầu Mua Sắm", "Start Shopping"],
        ["🎉 Bạn đã được MIỄN PHÍ VẬN CHUYỂN!", "🎉 You qualify for FREE Delivery!"],
        ["Thêm 599.000₫ nữa để được MIỄN PHÍ VẬN CHUYỂN", "Add 599,000₫ more for FREE Shipping"],

        // 7. WHOLESALE & B2B
        ["Chương Trình Đối Tác & Đại Lý Cà Phê S54", "S54 Coffee Partner & Wholesale Program"],
        ["Nguồn Cà Phê Nguyên Chất S54", "S54 Pure Coffee Supply"],
        ["Đối Tác Tiêu Biểu", "Featured Partners & Case Studies"],
        ["Khách Hàng & Đối Tác Nói Gì Về Chúng Tôi", "What Our Clients & Partners Say"],
        ["Đào Tạo Barista & Chuyển Giao Công Nghệ Pha Chế", "Barista Training & Brewing Knowledge Transfer"],
        ["Thiết Bị & Máy Pha Cà Phê Chuyên Nghiệp", "Professional Espresso Machines & Equipment"],
        ["Thiết Kế Quầy Bar & Bộ Nhận Diện Thương Hiệu", "Bar Setup & Custom Brand Identity"],
        ["Hỗ Trợ Marketing & Thu Hút Khách Hàng", "Marketing & Customer Acquisition Support"],
        ["Thương Hiệu Vì Cộng Đồng & Nông Dân Việt", "Community Brand Supporting Vietnamese Farmers"],
        ["Doanh Nghiệp Uy Tín & Cam Kết Dài Lâu", "Trusted Enterprise & Long-term Commitment"],
        ["Liên Hệ Hợp Tác Ngay Hôm Nay", "Get In Touch & Partner With Us Today"],
        ["Họ và Tên *", "Full Name *"],
        ["Tên Quán / Doanh Nghiệp *", "Cafe / Business Name *"],
        ["Số Điện Thoại *", "Phone Number *"],
        ["Email Liên Hệ *", "Email Address *"],
        ["Địa Chỉ Quán / Tỉnh Thành *", "Location / City *"],
        ["Mô Hình Kinh Doanh", "Business Model"],
        ["Nhu Cầu Sản Lượng Dự Kiến (kg/tháng)", "Estimated Monthly Volume (kg/month)"],
        ["Nội Dung Cần Tư Vấn & Yêu Cầu Mẫu Thử", "Inquiry Details & Sample Request"],
        ["GỬI YÊU CẦU TƯ VẤN & NHẬN MẪU THỬ", "SUBMIT INQUIRY & REQUEST SAMPLES"],

        
        // HERO BANNERS (STORY & WHOLESALE)
        ["Câu Chuyện Thương Hiệu S54", "S54 Brand Story & Heritage"],
        ["Hành trình hơn 12 năm kiến tạo giá trị từ Công ty TNHH Giải Pháp Tốt (Good Solutions), chuẩn hóa nguồn cà phê sạch nguyên chất từ vùng đất đỏ Tây Nguyên và lan tỏa tinh hoa cà phê Việt.", "Over 12 years journey by Good Solutions Co., Ltd, standardizing pure clean coffee from Central Highlands red soil and spreading the essence of Vietnamese coffee."],
        ["HÀNH TRÌNH 12+ NĂM DI SẢN (2012 - 2026)", "12+ YEARS HERITAGE JOURNEY (2012 - 2026)"],
        ["Cung Ứng B2B & Đại Lý S54", "S54 B2B & Wholesale Supply"],
        ["Đối tác chiến lược cung ứng nguồn cà phê sạch nguyên chất, thiết bị máy pha chuyên nghiệp và chuyển giao kỹ thuật pha chế cho hơn 500+ chuỗi nhà hàng, khách sạn & quán cafe.", "Strategic partner supplying pure roasted coffee, commercial espresso machines, and brewing technology transfer for over 500+ restaurants, hotels & cafes."],
        ["GIẢI PHÁP CUNG ỨNG B2B TOÀN DIỆN", "COMPREHENSIVE B2B COFFEE SOLUTIONS"],
        ["🌱 Vùng Trồng Đắk Lắk & Cầu Đất", "🌱 Dak Lak & Cau Dat Origins"],
        ["🔥 Công Nghệ Rang Hot-Air Hiện Đại", "🔥 Advanced Hot-Air Artisan Roasting"],
        ["🤝 Đồng Hành Cùng Nông Dân Việt", "🤝 Supporting Vietnamese Farmers"],
        ["☕ Chiết Khấu Đại Lý Tới 35%", "☕ Wholesale Margin Up To 35%"],
        ["📦 Gia Công OEM/ODM Xuất Khẩu", "📦 Private Label OEM/ODM Export"],
        ["🎓 Đào Tạo Barista Chuyên Nghiệp", "🎓 Professional Barista Training"],

        // AUTHENTIC S54 STORY TIMELINE & PHILOSOPHY
        ["“Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.” — Triết lý Good Solutions & S54 Coffee.", "“To establish good solutions in providing quality coffee with unmatched levels of service.” — Philosophy of Good Solutions & S54 Coffee."],
        ["Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.", "To establish good solutions in providing quality coffee with unmatched levels of service."],
        ["Triết lý Good Solutions & S54 Coffee.", "Philosophy of Good Solutions & S54 Coffee."],
        ["GIAI ĐOẠN 2012 - KHỞI NGUỒN ĐAM MÊ", "2012 - OUR PASSION & FOUNDING"],
        ["Thành Lập Good Solutions & Khát Vọng Cà Phê Sạch", "Founding of Good Solutions & Pure Clean Coffee Vision"],
        ["Năm 2012, Công ty TNHH Giải Pháp Tốt (Good Solutions) chính thức được thành lập với mục tiêu thiết lập những chuẩn mực mới cho ngành cà phê Việt Nam. Chứng kiến thực trạng cà phê pha tạp bắp đậu trên thị trường, những người sáng lập S54 đã quyết tâm xây dựng thương hiệu cà phê rang mộc 100% nguyên chất, minh bạch từ nguồn gốc nông trại đến từng tách cà phê trao tay người tiêu dùng.", "In 2012, Good Solutions Co., Ltd was established to set new standards for Vietnamese coffee. Witnessing widespread adulterated coffee on the market, S54 founders committed to building a 100% pure roasted coffee brand, transparent from farm origins to every cup served."],
        ["VÙNG TRỒNG NGUYÊN LIỆU", "COFFEE FARMING ORIGINS"],
        ["Liên Kết Nông Trại Đắk Lắk & Cầu Đất (Lâm Đồng)", "Partnering with Dak Lak & Cau Dat (Lam Dong) Farms"],
        ["S54 Coffee trực tiếp liên kết và bao tiêu sản lượng tại các nông trại thổ nhưỡng bazan màu mỡ ở Buôn Ma Thuột (Đắk Lắk) và Cầu Đất (Lâm Đồng) ở độ cao lý tưởng từ 800m - 1.500m. Chúng tôi kiên định quy chuẩn thu hái quả chín mọng trên cây đạt tỷ lệ trên 95%, áp dụng phương pháp sơ chế ướt (Full Washed) và phơi giàn kính tự nhiên để bảo tồn tối đa hương vị nguyên bản của thổ nhưỡng Việt Nam.", "S54 Coffee directly partners and secures harvest with fertile basalt soil farms in Buon Ma Thuot (Dak Lak) and Cau Dat (Lam Dong) at altitudes from 800m - 1,500m. We adhere to harvesting >95% ripe cherries, applying full-washed processing and natural greenhouse raised beds to preserve authentic Vietnamese terroir."],
        ["CÔNG NGHỆ SẢN XUẤT", "ROASTING TECHNOLOGY"],
        ["Công Nghệ Rang Hot-Air Chuẩn HACCP & ISO", "Hot-Air Roasting Technology with HACCP & ISO Standards"],
        ["Đầu tư nhà máy rang hiện đại với công nghệ khí nóng Hot-Air hồi lưu, S54 kiểm soát chính xác từng profile nhiệt độ và thời gian rang cho từng mẻ hạt. Công nghệ này giúp hạt cà phê chín đều từ lõi ra vỏ, không cháy cạnh, triệt tiêu vị khét và làm nổi bật các nốt hương sô cô la, caramel, thảo mộc tự nhiên cùng hậu vị ngọt thanh êm dịu.", "Investing in modern roasting facilities with recirculating Hot-Air convection, S54 precisely controls temperature profiles and roasting time. This ensures beans roast evenly from core to surface without burnt edges, highlighting notes of dark chocolate, caramel, and sweet smooth aftertaste."],
        ["ĐỔI MỚI SẢN PHẨM", "PRODUCT INNOVATION"],
        ["Đột Phá Hòa Tan 3-in-1 (456g) & Sấy Lạnh Cao Cấp", "Breakthrough 3-in-1 Instant (456g) & Premium Freeze-Dried Coffee"],
        ["Đáp ứng nhịp sống hiện đại mà vẫn giữ vững chuẩn mực gu thưởng thức, S54 Coffee phát triển thành công dòng cà phê hòa tan 3-in-1 hộp 456g đậm đà và cà phê sấy lạnh thăng hoa cao cấp. Quy trình trích ly và sấy ở nhiệt độ âm giúp giữ lại hơn 99% hợp chất hương thơm tự nhiên của hạt Robusta & Arabica thượng hạng.", "Meeting modern lifestyles while preserving authentic taste, S54 Coffee developed rich 3-in-1 instant coffee (456g box) and premium freeze-dried coffee. Sub-zero extraction and freeze-drying retain over 99% of the natural aromatic compounds of premium Robusta & Arabica beans."],
        ["ĐỒNG HÀNH & PHÁT TRIỂN", "COMMUNITY & GROWTH"],
        ["Đào Tạo Barista & Cung Ứng B2B Toàn Diện", "Barista Training & Comprehensive B2B Supply"],
        ["Không chỉ là nhà cung cấp nguyên liệu, S54 Coffee là đối tác chiến lược đồng hành cùng hơn 500+ nhà hàng, khách sạn và quán cà phê. Chúng tôi đào tạo kỹ năng Barista chuyên sâu, chuyển giao công thức pha chế độc quyền, setup quầy bar và cung cấp các dòng máy pha espresso công nghiệp tiêu chuẩn quốc tế.", "More than an ingredient supplier, S54 Coffee is a strategic partner accompanying 500+ restaurants, hotels, and cafes. We provide in-depth Barista training, exclusive brewing recipes, bar setup, and commercial espresso machinery."],

        // COLLECTION FILTER TABS
        ["ONLINE EXCLUSIVE", "ONLINE EXCLUSIVE"],
        ["BEANS", "COFFEE BEANS"],
        ["SPECIALTY CÀ PHÊ HẠT", "SPECIALTY BEANS"],
        ["BLENDS", "COFFEE BLENDS"],
        ["FEATURED", "FEATURED"],
        ["ALL", "ALL"],
// 8. OUR STORY
        ["Khởi Nguồn Đam Mê & Thành Lập Good Solutions (2012)", "Our Passion & The Founding of Good Solutions (2012)"],
        ["Triết Lý “NEW COFFEE, NEW INCOME”", "The “NEW COFFEE, NEW INCOME” Philosophy"],
        ["Chuẩn Hóa Vùng Trồng Robusta Đắk Lắk & Arabica Cầu Đất", "Standardizing Robusta Dak Lak & Arabica Cau Dat Origins"],
        ["Công Nghệ Rang Mộc Hot-Air Hiện Đại", "Advanced Hot-Air Artisan Roasting Technology"],
        ["Đột Phá Cà Phê Hòa Tan 3-in-1 (456g) & Sấy Lạnh", "Breakthrough 3-in-1 Instant (456g) & Freeze-Dried Coffee"],
        ["Giải Pháp Cung Ứng B2B & Đại Lý Toàn Diện", "Comprehensive B2B & Wholesale Supply Solutions"],
        ["4 Giá Trị Cốt Lõi: Minh Bạch & Bền Vững", "4 Core Values: Transparency & Sustainability"],
        ["Tầm Nhìn Vươn Tầm Toàn Cầu — “Hơn Cả Cà Phê”", "Global Vision — “More Than Just Coffee”"],
        ["Hơn 12 Năm Đồng Hành Cùng Hàng Triệu Tách Cà Phê Việt", "Over 12 Years Accompanying Millions of Vietnamese Coffee Cups"],

        // 9. BLOG & NEWS
        ["Tất Cả Bài Viết", "All Articles"],
        ["Kiến Thức Cà Phê", "Coffee Insights"],
        ["Câu Chuyện S54", "S54 Stories"],
        ["Hướng Dẫn Pha Chế", "Brewing Guides"],
        ["Bản Tin Extracts", "Extracts Newsletter"],
        ["Các Bài Viết Mới Nhất", "Latest Articles"],
        ["5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết", "5 Amazing Benefits of Drinking Coffee You Might Not Know"],
        ["Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp", "How to Distinguish Pure Roasted Coffee vs Adulterated Blends"],
        ["← Quay lại Tin Tức", "← Back to News"],
        ["← Xem Tất Cả Bài Viết", "← View All Articles"],

        // 10. FOOTER & LEGAL
        ["CÔNG TY TNHH GIẢI PHÁP TỐT", "GOOD SOLUTIONS COMPANY LIMITED"],
        ["Sản Phẩm S54", "S54 Products"],
        ["Về S54 & Dịch Vụ", "About S54 & Services"],
        ["Đăng Ký Nhận Ưu Đãi", "Subscribe for Offers"],
        ["Nhận ngay voucher ưu đãi 15% cho đơn hàng đầu tiên cùng cẩm nang pha chế độc quyền từ S54 Coffee.", "Get 15% off your first order plus an exclusive brewing guide from S54 Coffee."],
        ["Nhập địa chỉ email của bạn...", "Enter your email address..."],
        ["Kết Nối Với Chúng Tôi:", "Connect With Us:"],
        ["Chính Sách Đổi Trả & Bảo Mật", "Returns & Privacy Policy"],
        ["Chính Sách Vận Chuyển", "Shipping Policy"],
        ["Nông Trại & Công Nghệ Rang", "Smart Farming & Roasting"],
        ["Gia Cung OEM/ODM Xuất Khẩu", "Private Label OEM/ODM Export"],
        ["Gia Công OEM/ODM Xuất Khẩu", "Private Label OEM/ODM Export"],
        ["Chuyển Khoản", "Bank Transfer"],
        ["Giữ toàn quyền bản quyền.", "All rights reserved."],

        // 11. 404 PAGE
        ["Không Tìm Thấy Trang", "Page Not Found"],
        ["Trang bạn đang tìm kiếm có thể đã bị xóa, đổi tên hoặc tạm thời không khả dụng. Hãy để chúng tôi đưa bạn về đúng nơi thưởng thức cà phê.", "The page you are looking for might have been removed, had its name changed, or is temporarily unavailable. Let us help you find the right brew."],
        ["Về Trang Chủ", "Back to Home"],
        ["Khám Phá Danh Mục Cà Phê", "Explore Coffee Catalog"]
    ];

    let currentLang = 'vi';

    function initLanguage() {
        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            if (saved === 'en' || saved === 'vi') {
                currentLang = saved;
            }
        } catch (e) {
            console.warn('[S54I18n] Storage access error', e);
        }
    }

    function translatePage(targetLang) {
        if (targetLang !== 'vi' && targetLang !== 'en') return;
        const fromIdx = currentLang === 'vi' ? 0 : 1;
        const toIdx = targetLang === 'vi' ? 0 : 1;
        currentLang = targetLang;

        try {
            localStorage.setItem(STORAGE_KEY, targetLang);
        } catch (e) {}

        document.documentElement.lang = targetLang;

        // Traverse all DOM text nodes
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function (node) {
                    if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
                    const parent = node.parentElement;
                    if (!parent) return NodeFilter.FILTER_REJECT;
                    const tag = parent.tagName;
                    if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'NOSCRIPT') {
                        return NodeFilter.FILTER_REJECT;
                    }
                    return NodeFilter.FILTER_ACCEPT;
                }
            },
            false
        );

        const textNodes = [];
        let curr = walker.nextNode();
        while (curr) {
            textNodes.push(curr);
            curr = walker.nextNode();
        }

        textNodes.forEach(node => {
            let val = node.nodeValue;
            translationPairs.forEach(([vi, en]) => {
                const searchStr = fromIdx === 0 ? vi : en;
                const replaceStr = toIdx === 0 ? vi : en;
                if (searchStr && replaceStr && val.includes(searchStr)) {
                    val = val.split(searchStr).join(replaceStr);
                }
            });
            if (val !== node.nodeValue) {
                node.nodeValue = val;
            }
        });

        // Translate inputs and placeholders
        document.querySelectorAll('input[placeholder], textarea[placeholder]').forEach(el => {
            let ph = el.getAttribute('placeholder');
            translationPairs.forEach(([vi, en]) => {
                const searchStr = fromIdx === 0 ? vi : en;
                const replaceStr = toIdx === 0 ? vi : en;
                if (ph && ph.includes(searchStr)) {
                    ph = ph.split(searchStr).join(replaceStr);
                }
            });
            if (ph) el.setAttribute('placeholder', ph);
        });

        // Update Switcher UI Buttons
        updateSwitcherUI();

        // Dispatch Language Changed event for dynamic components (Cart Drawer, Toasts, etc.)
        window.dispatchEvent(new CustomEvent('language:changed', { detail: { language: targetLang } }));
    }

    function updateSwitcherUI() {
        document.querySelectorAll('.c-lang-btn[data-lang]').forEach(btn => {
            const lang = btn.getAttribute('data-lang');
            if (lang === currentLang) {
                btn.classList.add('is-active');
            } else {
                btn.classList.remove('is-active');
            }
        });
    }

    // Public API
    window.S54I18n = {
        setLanguage: translatePage,
        getLanguage: function () { return currentLang; },
        translate: translatePage
    };

    // Auto-init on load
    initLanguage();
    document.addEventListener('DOMContentLoaded', () => {
        // Delegate click events for language switcher buttons
        document.addEventListener('click', (e) => {
            const btn = e.target.closest('[data-lang]');
            if (btn) {
                e.preventDefault();
                e.stopPropagation();
                const targetLang = btn.getAttribute('data-lang');
                if (targetLang && targetLang !== currentLang) {
                    translatePage(targetLang);
                }
            }
        });

        if (currentLang === 'en') {
            translatePage('en');
        } else {
            updateSwitcherUI();
        }
    });

    // Dynamic Filter Pills Localizer (collections-coffee.html)
    function localizeFilterPills() {
        var currentLang = getLang();
        var filterBtns = document.querySelectorAll('.c-faceted-nav__filters-featured button, .c-faceted-nav__filters-featured .o-btn, [data-facet-button]');
        var viMap = {
            'ALL': 'TẤT CẢ',
            'ONLINE EXCLUSIVE': 'ĐỘC QUYỀN ONLINE',
            'BEANS': 'CÀ PHÊ HẠT',
            'SPECIALTY CÀ PHÊ HẠT': 'SPECIALTY CAO CẤP',
            'BLENDS': 'CÀ PHÊ BLEND',
            'SINGLE ORIGIN': 'SINGLE ORIGIN',
            'GROUND': 'CÀ PHÊ XAY',
            'FEATURED': 'NỔI BẬT'
        };
        var enMap = {
            'TẤT CẢ': 'ALL',
            'ĐỘC QUYỀN ONLINE': 'ONLINE EXCLUSIVE',
            'CÀ PHÊ HẠT': 'COFFEE BEANS',
            'SPECIALTY CAO CẤP': 'SPECIALTY BEANS',
            'SPECIALTY CÀ PHÊ HẠT': 'SPECIALTY BEANS',
            'CÀ PHÊ BLEND': 'COFFEE BLENDS',
            'CÀ PHÊ XAY': 'GROUND COFFEE',
            'NỔI BẬT': 'FEATURED'
        };

        filterBtns.forEach(function(btn) {
            var txt = (btn.textContent || '').trim();
            if (currentLang === 'vi') {
                if (viMap[txt]) btn.textContent = viMap[txt];
            } else {
                if (enMap[txt]) btn.textContent = enMap[txt];
            }
        });
    }

    // Observe dynamic filter insertion
    var filterNav = document.querySelector('[data-filters-featured]');
    if (filterNav) {
        var obs = new MutationObserver(function() {
            localizeFilterPills();
        });
        obs.observe(filterNav, { childList: true, subtree: true });
        setTimeout(localizeFilterPills, 100);
        setTimeout(localizeFilterPills, 500);
        setTimeout(localizeFilterPills, 1200);
    }

})();
