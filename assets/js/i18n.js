/**
 * S54 COFFEE - Internationalization (i18n) Engine
 * Full Bidirectional Translation: Vietnamese (Primary/Default) & English
 */
(function () {
    'use strict';

    const STORAGE_KEY = 's54_storefront_lang';

    // Comprehensive Bidirectional Translation Pairs (VI <-> EN)
    const translationPairs = [
        ["Khởi Nguồn Đam Mê & Thành Lập Good Solutions (2012)", "Our Passion & The Founding of Good Solutions (2012)"],
        ["Triết Lý “NEW COFFEE, NEW INCOME”", "The “NEW COFFEE, NEW INCOME” Philosophy"],
        ["Chuẩn Hóa Vùng Trồng Robusta Đắk Lắk & Arabica Cầu Đất", "Standardizing Robusta Dak Lak & Arabica Cau Dat Origins"],
        ["Công Nghệ Rang Mộc Hot-Air Hiện Đại", "Advanced Hot-Air Artisan Roasting Technology"],
        ["Đột Phá Cà Phê Hòa Tan 3-in-1 (456g) & Sấy Lạnh", "Breakthrough 3-in-1 Instant (456g) & Freeze-Dried Coffee"],
        ["Giải Pháp Cung Ứng B2B & Đại Lý Toàn Diện", "Comprehensive B2B & Wholesale Supply Solutions"],
        ["4 Giá Trị Cốt Lõi: Minh Bạch & Bền Vững", "4 Core Values: Transparency & Sustainability"],
        ["Tầm Nhìn Vươn Tầm Toàn Cầu — “Hơn Cả Cà Phê”", "Global Vision — “More Than Just Coffee”"],
        ["Hơn 12 Năm Đồng Hành Cùng Hàng Triệu Tách Cà Phê Việt", "Over 12 Years Accompanying Millions of Vietnamese Coffee Cups"],
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
        ["5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết", "5 Amazing Health Benefits of Coffee You Might Not Know"],
        ["Triết Lý “NEW COFFEE, NEW INCOME” & Hơn Cả Cà Phê", "“NEW COFFEE, NEW INCOME” Philosophy & More Than Coffee"],
        ["Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp", "How to Distinguish Pure Roasted Coffee from Adulterated Blends"],
        ["Khám phá nguồn chất chống oxy hóa dồi dào, tăng cường tập trung, giảm đau đầu và bảo vệ sức khỏe từ cà phê nguyên chất.", "Discover rich antioxidants, enhanced focus, headache relief and health benefits from pure coffee."],
        ["Cà phê không chỉ để thưởng thức mà còn kết nối, truyền cảm hứng và tiếp thêm năng lượng tích cực cho sự nghiệp và cuộc sống.", "Coffee is not only for enjoying, but for connecting, inspiring, and fueling positive energy in life."],
        ["Hướng dẫn phân biệt cà phê sạch nguyên chất 100% không tẩm ướp bắp cau, đậu nành hay hương liệu hóa học nhân tạo.", "A guide to distinguishing 100% pure clean coffee with no corn, soy or artificial flavors."],
        ["S54 Robusta Cà Phê Rang Nguyên Chất 500g / 1kg", "S54 Pure Roasted Robusta Beans 500g / 1kg"],
        ["100% Robusta Đắk Lắk Nguyên Chất", "100% Pure Dak Lak Robusta"],
        // Topbar & Natural Case Menu
        ["Miễn phí vận chuyển toàn quốc cho đơn từ 599.000₫ • Hotline: 0383.707.578", "Free nationwide shipping on orders over 599,000₫ • Hotline: (+84) 383 707 578"],
        ["Tất Cả Sản Phẩm", "All Products"],
        ["Cà Phê Hạt & Rang Mộc", "Coffee Beans & Roast"],
        ["Hòa Tan & Sấy Lạnh", "Instant & Freeze-Dried"],
        ["Câu Chuyện S54", "Our Story"],
        ["B2B & Đại Lý", "B2B & Wholesale"],

        // Hero & Clean Editorial Translations
        ["Tinh Hoa Cà Phê Việt®", "The Essence of Vietnamese Coffee®"],
        ["Tinh Hoa<br/>Cà Phê Việt®", "The Essence of<br/>Vietnamese Coffee®"],
        ["100% Cà phê rang mộc nguyên chất từ vùng đất đỏ Tây Nguyên", "100% Pure roasted coffee beans from Central Highlands red soil"],
        ["MUA SẮM NGAY", "SHOP NOW"],
        ["HỢP TÁC B2B & ĐẠI LÝ", "B2B & WHOLESALE PARTNER"],

        // S54 Coffee Specifics
        ["MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578", "FREE NATIONWIDE SHIPPING ON ORDERS OVER 599,000₫ • HOTLINE: (+84) 383 707 578"],
        ["S54 COFFEE - Tinh Hoa Cà Phê Việt®", "S54 COFFEE - The Essence of Vietnamese Coffee®"],
        ["Khám Phá Dòng Cà Phê S54", "Discover S54 Coffee Range"],
        ["“S54 Coffee mang đến giải pháp cà phê sạch nguyên chất, đậm đà vị truyền thống và phong cách hiện đại cho hàng triệu người tiêu dùng.”", "“S54 Coffee delivers pure, clean coffee solutions with authentic rich flavor and modern style to millions of consumers.”"],
        ["Mr. Paul Hieu (CEO) & Tony Hoan (Founder)", "Mr. Paul Hieu (CEO) & Tony Hoan (Founder)"],
        ["Hơn 12 Năm Kinh Nghiệm & Đam Mê Cà Phê Sạch", "Over 12 Years of Clean Coffee Passion & Expertise"],
        ["Thành lập từ năm 2012 bởi Công ty TNHH Giải Pháp Tốt (Good Solutions), S54 Coffee tự hào kế thừa tinh hoa cà phê Robusta & Arabica từ vùng đất đỏ bazan Tây Nguyên (Đắk Lắk, Lâm Đồng). Chúng tôi áp dụng quy trình kiểm soát nghiêm ngặt từ hạt giống, nông trại thông minh đến công nghệ rang mộc hiện đại, lưu giữ trọn vẹn hương thơm tự nhiên và hậu vị sâu lắng đặc trưng của cà phê Việt.", "Established in 2012 by Good Solutions Co., Ltd, S54 Coffee inherits the finest Robusta & Arabica beans from the Central Highlands (Dak Lak, Lam Dong). We employ rigorous quality control from smart farming to modern artisan roasting."],
        ["Nghệ Thuật Pha Chế & Thưởng Thức Cà Phê S54 Chuẩn Vị", "The Art of Brewing & Enjoying Authentic S54 Coffee"],
        ["Cùng chuyên gia S54 Coffee khám phá bí quyết chiết xuất tách Espresso thơm ngậy với lớp crema dày sánh mịn hoặc pha phin truyền thống đậm đà khó quên.", "Join S54 Coffee experts to discover the secrets of brewing rich Espresso with golden crema or traditional Vietnamese drip coffee."],
        ["S54 Robusta Rang Mộc Nguyên Chất", "S54 Pure Roasted Robusta Beans"],
        ["S54 Arabica Cầu Đất Thượng Hạng", "S54 Premium Cau Dat Arabica"],
        ["S54 Hòa Tan 3-in-1 Hộp 456g", "S54 Instant Coffee 3-in-1 (456g)"],
        ["S54 Cà Phê Sấy Lạnh Cao Cấp", "S54 Premium Freeze-Dried Blend"],
        ["S54 Cà Phê Túi Lọc Drip Bag", "S54 Drip Bag Coffee Sachets"],
        ["S54 Robusta Xay Pha Phin", "S54 Traditional Ground Robusta"],
        ["5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Mỗi Ngày Cho Sức Khỏe", "5 Amazing Health Benefits of Drinking Coffee Daily"],
        ["Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp", "How to Distinguish Pure Artisan Roasted Coffee from Mixed Coffee"],
        ["So Sánh Hương Vị Đậm Đà Của S54 Robusta Và Chua Thanh Của S54 Arabica", "Comparing the Bold Flavor of S54 Robusta with the Crisp Acidity of S54 Arabica"],
        ["Kết Nối Cùng S54 Coffee Trên Mạng Xã Hội", "Connect with S54 Coffee on Social Media"],
        ["Đăng Ký Nhận Ưu Đãi & Tin Tức Cà Phê Mới Nhất", "Subscribe for Exclusive Offers & Coffee News"],
        ["Nhận ngay voucher giảm 15% cho đơn hàng đầu tiên cùng cẩm nang pha chế cà phê độc quyền từ S54 Coffee.", "Get 15% off your first order plus an exclusive brewing guide from S54 Coffee."],
        ["CÔNG TY TNHH GIẢI PHÁP TỐT (GOOD SOLUTIONS CO., LTD)", "GOOD SOLUTIONS COMPANY LIMITED (S54 COFFEE)"],
        ["Số 35, Đường T8, Manhattan, Vinhomes Grand Park, P. Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh", "No. 35, T8 Street, Manhattan, Vinhomes Grand Park, Long Binh Ward, Thu Duc City, HCMC, Vietnam"],
        ["Chính Sách Đại Lý & Cung Ứng B2B", "Wholesale & B2B Supply Policy"],
        ["Dịch Vụ Cung Ứng Cà Phê B2B & Gia Công OEM/ODM", "B2B Coffee Supply & Private Label OEM/ODM Services"],

        // Announcement
        ["MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ $69†", "Free Shipping: Orders over $69†"],
        ["MIỄN PHÍ VẬN CHUYỂN: ĐƠN HÀNG TỪ $69", "Free Shipping: Orders over $69"],
        ["Miễn phí vận chuyển cho đơn hàng từ $69", "Free shipping on orders over $69"],

        // Header & Mega Menu
        ["Tất Cả Sản Phẩm", "Shop All"],
        ["Danh Mục Cà Phê", "Shop By Category"],
        ["Cà Phê Hạt Nguyên", "Coffee Beans"],
        ["Cà Phê Hạt", "Coffee Beans"],
        ["Cà Phê Xay Sẵn", "Ground Coffee"],
        ["Cà Phê Xay", "Ground Coffee"],
        ["Viên Nén Vỏ Nhôm", "Aluminium Capsules"],
        ["Viên Nén Capsule", "Capsules"],
        ["Cà Phê Hòa Tan Đặc Biệt", "Special Blend Instant"],
        ["Cà Phê Hòa Tan", "Instant Coffee"],
        ["Gói Pha Tiện Lợi", "Ready-to-Mix Sachets"],
        ["Túi Lọc Cà Phê", "Coffee Bags"],
        ["Sô-cô-la Uống", "Drinking Chocolate"],
        ["Phụ Kiện Pha Chế", "Accessories"],
        ["Đăng Ký Định Kỳ", "Mua Hàng Định Kỳ"],
        ["Khám Phá", "Learn"],
        ["Câu Chuyện Thương Hiệu", "Our Story"],
        ["Quy Trình Rang Xay", "Roasting"],
        ["Tin Tức & Sự Kiện", "News"],
        ["Tin Tức", "News"],
        ["Cộng Đồng & Di Sản", "Community"],
        ["Cộng Đồng", "Community"],
        ["Hướng Dẫn Pha Chế", "Brewing Guides"],
        ["Ưu Đãi Khi Đặt Cà Phê Định Kỳ", "Benefits of a Coffee Subscription"],
        ["Bán Sỉ B2B", "Wholesale"],
        ["Giải Pháp Doanh Nghiệp", "Business"],
        ["Giỏ Hàng", "Bag"],
        ["Tìm Kiếm", "Search"],

        // Actions & Buttons
        ["Khám Phá Ngay", "Shop Now"],
        ["KHÁM PHÁ NGAY", "SHOP NOW"],
        ["Thêm Nhanh", "Quick Add"],
        ["THÊM VÀO GIỎ", "ADD TO BAG"],
        ["Thêm Vào Giỏ", "Add to Bag"],
        ["Thêm vào giỏ", "Add to bag"],
        ["ĐÃ THÊM!", "ADDED!"],
        ["ĐÃ THÊM", "ADDED"],
        ["Tìm Hiểu Thêm", "Discover More"],
        ["TÌM HIỂU THÊM", "DISCOVER MORE"],
        ["Tìm Hiểu Quy Trình", "Discover More"],
        ["Khám Phá Dòng Sản Phẩm", "Explore Our Range"],
        ["Khám Phá Toàn Bộ Dòng Sản Phẩm", "Explore Our Range"],
        ["Đọc Bài Viết", "Read Article"],
        ["ĐỌC BÀI VIẾT", "READ ARTICLE"],
        ["Đăng Ký", "Subscribe"],
        ["ĐĂNG KÝ", "SUBSCRIBE"],
        ["Đăng Ký Ngay", "Subscribe"],
        ["ĐĂNG KÝ NGAY", "SUBSCRIBE NOW"],
        ["Đặt Định Kỳ & Tiết Kiệm 10%", "Subscribe & Save 10%"],
        ["ĐẶT ĐỊNH KỲ & TIẾT KIỆM 10%", "SUBSCRIBE AND SAVE"],
        ["Mua một lần", "One-time purchase"],
        ["Mua Một Lần", "One-Time Purchase"],
        ["Bắt Đầu Mua Sắm", "Start Shopping"],
        ["TIẾN HÀNH THANH TOÁN", "CHECKOUT"],
        ["Về Trang Chủ", "Return to Homepage"],
        ["Khám Phá Danh Mục Cà Phê", "Explore Coffee Range"],
        ["Khám Phá Sản Phẩm Cà Phê", "Explore Coffee Range"],

        // Homepage Specifics
        ["Chuyên Gia Cà Phê Số 1®", "We Know Coffee®"],
        ["Dòng Cà Phê Thượng Hạng Được Yêu Thích Số 1 Việt Nam", "Australia's Favourite Premium Blend"],
        ["Sản Phẩm Bán Chạy Nhất", "Bestsellers"],
        ["Nghệ Nhân Rang Cà Phê Thủ Công Từ Năm 1958", "Master Roasters Since 1958"],
        ["Hơn 60 năm qua, các nghệ nhân rang bậc thầy của chúng tôi luôn tuyển chọn kỹ lưỡng và rang thủ công 100% hạt Arabica thượng hạng tại xưởng rang Sydney, Australia nhằm mang đến hương vị espresso Ý đích thực.",
         "For over 60 years, our master roasters have carefully selected and roasted 100% Arabica beans in Sydney, Australia."],
        ["Di Sản Nước Ý, Chế Tác Tại Việt Nam", "Italian Heritage, Australian Made"],
        ["Từ xưởng rang đầu tiên tại Sydney năm 1958 đến thương hiệu cà phê rang xay nguyên chất số 1 Việt Nam.",
         "From Sydney's first roastery in 1958 to Australia's favourite pure coffee brand."],
        ["Tin Tức Mới Nhất Từ Xưởng Rang", "Latest from the Roastery"],
        ["Đăng Ký Nhận Bản Tin", "Stay in Touch"],
        ["Đăng ký nhận thông tin độc quyền và mã ưu đãi giảm 10% cho đơn hàng đầu tiên của bạn.",
         "Subscribe to receive 10% off your first online order."],

        // Carousel & Quotes
        ["Khám Phá Dòng Sản Phẩm", "Discover our range"],
        ["“Khát vọng của chúng tôi là mang đến cho người yêu cà phê những hạt cà phê rang tươi mới và thượng hạng nhất ở mọi định dạng thưởng thức.”",
         "“Our ambition is to provide Australians with the best and freshest, roasted coffee in any format they choose.”"],
        ["Paul Hieu, Giám Đốc Điều Hành (CEO)", "Paul Hieu, CEO"],
        ["Hơn 65 Năm Kinh Nghiệm Rang Xay Thủ Công", "Over 65 years of roasting expertise"],
        ["Kết tinh từ ba thế hệ kinh nghiệm gia đình Good Solutions cùng một trong những xưởng rang hiện đại bậc nhất bán cầu nam.",
         "Combining three generations of family experience with one of the most advanced coffee bean roasting facilities in the southern hemisphere."],
        ["Đọc Tin Tức Mới Nhất", "Read the latest news"],
        ["Cập nhật những tin tức và câu chuyện mới nhất từ thương hiệu cà phê rang xay nguyên chất số 1 Việt Nam.^",
         "Stay up to date with the latest news from Australia's No.1 pure coffee brand.^"],
        ["Bí Quyết Bảo Quản Cà Phê Luôn Tươi Mới", "How to Store Coffee Beans Once Opened So They Stay Fresh"],
        ["15 phút đọc", "Fifteen minute read"],
        ["Cà Phê Đặc Sản (Specialty Coffee) Là Gì?", "What is Specialty Coffee?"],
        ["10 phút đọc", "Ten minute read"],
        ["Các Loại Cà Phê Đặc Sản S54", "Australian Coffee Types Explained"],
        ["13 phút đọc", "Thirteen minute read"],
        ["Bản Tin Extracts Số 7", "Extracts Issue no. 7"],
        ["1 phút đọc", "One minute read"],
        ["Nghệ thuật chiết xuất tách Espresso hoàn hảo.", "How to brew the perfect espresso."],
        ["Khám Phá Video Hướng Dẫn", "Explore Brewtorials"],
        ["ĐỘC QUYỀN ONLINE", "ONLINE EXCLUSIVE"],
        ["Dòng blend phục vụ khách sạn & nhà hàng được ưa chuộng nhất", "Our most popular foodservice blend"],
        ["Dòng blend được yêu thích nhất Việt Nam", "Australia's favourite blend"],
        ["Rang đậm cho hương vị dày dặn, thể chất mạnh mẽ", "Dark roasted for a full-bodied flavour"],
        ["Dòng blend đạt chứng nhận Hữu cơ Quốc tế", "Certified Organic blend"],

        // Collections & Filters
        ["Tất Cả Sản Phẩm Cà Phê", "All Coffee Products"],
        ["Bộ sưu tập các dòng cà phê blend và single origin 100% Arabica thượng hạng được rang mới mỗi ngày tại Sydney.",
         "Premium blends & single origins freshly roasted in Sydney."],
        ["Bộ Lọc & Sắp Xếp", "Filter & Sort"],
        ["Lọc Theo", "Filter By"],
        ["Mức Độ Rang", "Roast Profile"],
        ["Rang Vừa (Medium)", "Medium Roast"],
        ["Rang Đậm (Dark)", "Dark Roast"],
        ["Rang Rất Đậm (Extra Dark)", "Extra Dark Roast"],
        ["Sắp Xếp Theo", "Sort By"],
        ["Nổi Bật Nhất", "Featured"],
        ["Bán Chạy Nhất", "Best Selling"],
        ["Giá: Từ Thấp Đến Cao", "Price: Low to High"],
        ["Giá: Từ Cao Đến Thấp", "Price: High to Low"],
        ["Tên: A đến Z", "Alphabetically, A-Z"],
        ["Tên: Z đến A", "Alphabetically, Z-A"],

        // Product Detail
        ["Cà Phê Hạt Cinque Stelle® Special Bar 1kg", "Cinque Stelle® Special Bar Coffee Beans 1kg"],
        ["Cà Phê Hạt Cinque Stelle® Special Bar", "Cinque Stelle® Special Bar Coffee Beans"],
        ["Cà Phê Hạt Cinque Stelle Special Bar", "S54 Robusta Rang Mộc Nguyên Chất"],
        ["Dòng blend espresso phức hợp và cao cấp bậc nhất của chúng tôi.", "Our premiere and most complex espresso blend."],
        ["Ban đầu được chế tác độc quyền cho các nhà hàng danh tiếng hàng đầu Việt Nam, Cinque Stelle mang đến hương vị đậm đà, hậu vị sô-cô-la đen ngọt ngào cùng lớp crema vàng óng sánh mịn.",
         "Initially developed as an after-dinner espresso famously served at Australia's most recognized restaurants."],
        ["Chọn Định Dạng / Kích Cỡ", "Select Format"],
        ["Giao hàng định kỳ mỗi 4 tuần", "Deliver every 4 weeks"],
        ["Giao hàng định kỳ mỗi 2 tuần", "Deliver every 2 weeks"],
        ["Giao hàng định kỳ mỗi 6 tuần", "Deliver every 6 weeks"],
        ["Hương Vị Đặc Trưng (Tasting Notes)", "Tasting Notes"],
        ["Cấp Độ Rang & Nguồn Gốc", "Roast Level & Origin"],
        ["Hướng Dẫn Pha Chế Chuẩn Barista", "Brewing Tips"],
        ["Câu Hỏi Thường Gặp (FAQs)", "Frequently Asked Questions"],
        ["Đánh Giá Của Khách Hàng", "Customer Reviews"],
        ["Còn Hàng", "In Stock"],
        ["Giao Hàng Nhanh Toàn Quốc", "Fast Australia-wide Delivery"],
        ["Hương vị sô-cô-la đen nguyên chất, mật ong rừng, hạt dẻ nướng và lớp crema dày béo mịn.",
         "Dark chocolate, honey, toasted nuts and a rich, velvety crema."],
        ["Khuyên dùng cho máy pha espresso chuyên nghiệp, bình Moka Pot hoặc pha phin truyền thống.",
         "Recommended for commercial espresso machines, Moka pots, and French press."],
        ["Bảo quản cà phê như thế nào để giữ trọn hương vị?", "How should I store my coffee?"],
        ["Bảo quản nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp và đậy kín sau khi mở bao bì.",
         "Store in a cool, dry place away from direct sunlight in an airtight container."],

        // Our Story
        ["Thương Hiệu Cà Phê Rang Xay Nguyên Chất Số 1 Việt Nam", "Australia's No.1 Pure Coffee Brand"],
        ["Được sáng lập vào năm 1958 bởi hai anh em người Ý Orazio và Carmelo Good Solutions, S54 COFFEE đã tiên phong mở đường cho làn sóng văn hóa thưởng thức espresso chuẩn phong cách Ý tại Việt Nam.",
         "Established in 1958 by two Italian brothers, Orazio and Carmelo Good Solutions, S54 COFFEE pioneered the espresso revolution in Australia."],
        ["Chất Lượng Thượng Hạng Không Thỏa Hiệp", "Uncompromising Quality"],
        ["Từng mẻ cà phê được chế tác hoàn toàn từ 100% hạt Arabica thượng hạng tuyển chọn, rang đến độ hoàn hảo tuyệt đối tại xưởng rang Sydney.",
         "Every blend is crafted with 100% premium Arabica coffee beans, master roasted to perfection in our Sydney roastery."],
        ["Truyền Thống Gia Đình Ba Thế Hệ", "A Family Tradition"],
        ["Ba thế hệ trong gia đình Good Solutions luôn tận tâm gìn giữ và phát triển nghệ thuật rang cà phê truyền thống.",
         "Three generations of family dedication to the art of coffee roasting."],
        ["Phát Triển Bền Vững & Trách Nhiệm Cộng Đồng", "Sustainability & Community"],
        ["Cam kết 100% nguồn cung minh bạch, hỗ trợ cộng đồng nông dân vùng trồng cà phê và bảo vệ môi trường bền vững.",
         "Committed to ethical sourcing and supporting coffee farming communities worldwide."],

        // Wholesale
        ["Tại Sao Chọn S54 Cho Giải Pháp Cà Phê Bán Sỉ & Doanh Nghiệp?", "Why S54 for Wholesale Coffee?"],
        ["Giải Pháp Bán Sỉ & Đối Tác Doanh Nghiệp (B2B)", "Wholesale & Business Solutions"],
        ["Đồng hành cùng đối tác cung cấp cà phê thượng hạng cho hơn 3.000+ quán café, nhà hàng, khách sạn cao cấp và tập đoàn lớn.",
         "Partner with Australia's premier coffee supplier for your café, restaurant, hotel or workplace."],
        ["Hệ Thống Máy Pha Cà Phê Chuyên Nghiệp", "Commercial Equipment"],
        ["Phân phối chính hãng các dòng máy pha espresso đẳng cấp thế giới: La Marzocco, Faema, Mazzer với dịch vụ bảo trì 24/7.",
         "From La Marzocco to Faema, we supply state-of-the-art espresso machinery."],
        ["Đào Tạo Barista Chuyên Nghiệp", "Barista Training"],
        ["Chương trình đào tạo kỹ năng chiết xuất, latte art và vận hành quầy bar chuyên sâu tại Học viện Cà phê quốc tế.",
         "Comprehensive training programs at our state-of-the-art coffee academies."],
        ["Đăng Ký Tư Vấn Hợp Tác Doanh Nghiệp", "Partner with Us"],
        ["Họ và Tên", "Full Name"],
        ["Tên Doanh Nghiệp / Chuỗi Quán", "Business Name"],
        ["Địa Chỉ Email", "Email Address"],
        ["Số Điện Thoại", "Phone Number"],
        ["Loại Hình Doanh Nghiệp", "Business Type"],
        ["Gửi Thông Tin Hợp Tác", "Submit Enquiry"],
        ["Quán Café / Nhà Hàng", "Cafe / Restaurant"],
        ["Khách Sạn / Nghỉ Dưỡng", "Hotel / Hospitality"],
        ["Văn Phòng / Doanh Nghiệp", "Office / Workplace"],
        ["Đại Lý Phân Phối", "Distributor"],

        // Cart Drawer
        ["Giỏ Hàng Của Bạn", "Your Bag"],
        ["Giỏ hàng của bạn đang trống.", "Your bag is currently empty."],
        ["Tạm Tính", "Subtotal"],
        ["TẠM TÍNH", "Subtotal"],
        ["🎉 Bạn đã được MIỄN PHÍ VẬN CHUYỂN!", "🎉 You qualify for FREE Delivery!"],
        ["Đang chuyển đến cổng thanh toán bảo mật...", "Proceeding to Secure Checkout..."],

        // 404 Page
        ["Không Tìm Thấy Trang", "Page Not Found"],
        ["Trang bạn đang tìm kiếm có thể đã bị xóa, đổi tên hoặc tạm thời không khả dụng. Hãy để chúng tôi đưa bạn về đúng nơi thưởng thức cà phê.",
         "The page you are looking for might have been removed, had its name changed, or is temporarily unavailable. Let us help you find the right brew."],

        // Footer
        ["Về S54 COFFEE", "About S54"],
        ["Cửa Hàng", "Shop"],
        ["Hỗ Trợ Khách Hàng", "Customer Support"],
        ["Liên Hệ Với Chúng Tôi", "Contact Us"],
        ["Chính Sách Giao Hàng", "Shipping Policy"],
        ["Chính Sách Đổi Trả", "Returns Policy"],
        ["Chính Sách Bảo Mật", "Privacy Policy"],
        ["Điều Khoản & Điều Kiện", "Terms & Conditions"],
        ["© 2026 S54 COFFEE. Bảo lưu mọi quyền.", "© 2026 S54 COFFEE. All rights reserved."],
        ["Bảo lưu mọi quyền.", "All rights reserved."]
    ];

    let currentLang = 'vi'; // Default: Vietnamese (Primary)

    function initLanguage() {
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        if (urlLang === 'en' || urlLang === 'vi') {
            currentLang = urlLang;
            try { localStorage.setItem(STORAGE_KEY, urlLang); } catch (e) {}
            return;
        }

        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            if (saved === 'en' || saved === 'vi') {
                currentLang = saved;
                return;
            }
        } catch (e) {}

        currentLang = 'vi';
    }

    function translatePage(targetLang) {
        currentLang = targetLang;
        try { localStorage.setItem(STORAGE_KEY, targetLang); } catch (e) {}
        document.documentElement.setAttribute('lang', targetLang);

        const fromIdx = targetLang === 'en' ? 0 : 1; // 0 = VI, 1 = EN
        const toIdx = targetLang === 'en' ? 1 : 0;

        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function (node) {
                    if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
                    const parent = node.parentElement;
                    if (!parent) return NodeFilter.FILTER_REJECT;
                    const tag = parent.tagName.toLowerCase();
                    if (tag === 'script' || tag === 'style' || tag === 'noscript' || tag === 'svg' || tag === 'code') {
                        return NodeFilter.FILTER_REJECT;
                    }
                    if (parent.closest('.c-lang-switcher')) return NodeFilter.FILTER_REJECT;
                    return NodeFilter.FILTER_ACCEPT;
                }
            }
        );

        const textNodes = [];
        while (walker.nextNode()) {
            textNodes.push(walker.currentNode);
        }

        textNodes.forEach(node => {
            let val = node.nodeValue;
            translationPairs.forEach(([vi, en]) => {
                const searchStr = fromIdx === 0 ? vi : en;
                const replaceStr = toIdx === 0 ? vi : en;
                if (val.includes(searchStr)) {
                    val = val.split(searchStr).join(replaceStr);
                }
            });
            if (val !== node.nodeValue) {
                node.nodeValue = val;
            }
        });

        // Translate placeholders
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

        updateSwitcherUI();
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

    // Auto-init
    initLanguage();
    document.addEventListener('DOMContentLoaded', () => {
        // Delegate click events for static buttons
        document.addEventListener('click', (e) => {
            const btn = e.target.closest('[data-lang]');
            if (btn) {
                e.preventDefault();
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
})();
