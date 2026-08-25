/**
 * Vittoria Coffee - Internationalization (i18n) Engine
 * Full Bidirectional Translation: Vietnamese (Primary/Default) & English
 */
(function () {
    'use strict';

    const STORAGE_KEY = 'vittoria_storefront_lang';

    // Comprehensive Bidirectional Translation Pairs (VI <-> EN)
    const translationPairs = [
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
        ["Đăng Ký Định Kỳ", "Subscriptions"],
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
        ["Khám Phá Sản Phẩm Cà Phê", "Explore Coffee Range"],

        // Homepage Specifics
        ["Dòng Cà Phê Thượng Hạng Được Yêu Thích Số 1 Nước Úc", "Australia's Favourite Premium Blend"],
        ["Sản Phẩm Bán Chạy Nhất", "Bestsellers"],
        ["Nghệ Nhân Rang Cà Phê Thủ Công Từ Năm 1958", "Master Roasters Since 1958"],
        ["Hơn 60 năm qua, các nghệ nhân rang bậc thầy của chúng tôi luôn tuyển chọn kỹ lưỡng và rang thủ công 100% hạt Arabica thượng hạng tại xưởng rang Sydney, Australia nhằm mang đến hương vị espresso Ý đích thực.",
         "For over 60 years, our master roasters have carefully selected and roasted 100% Arabica beans in Sydney, Australia."],
        ["Di Sản Nước Ý, Chế Tác Tại Nước Úc", "Italian Heritage, Australian Made"],
        ["Từ xưởng rang đầu tiên tại Sydney năm 1958 đến thương hiệu cà phê rang xay nguyên chất số 1 nước Úc.",
         "From Sydney's first roastery in 1958 to Australia's favourite pure coffee brand."],
        ["Tin Tức Mới Nhất Từ Xưởng Rang", "Latest from the Roastery"],
        ["Đăng Ký Nhận Bản Tin", "Stay in Touch"],
        ["Đăng ký nhận thông tin độc quyền và mã ưu đãi giảm 10% cho đơn hàng đầu tiên của bạn.",
         "Subscribe to receive 10% off your first online order."],

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
        ["Cà Phê Hạt Cinque Stelle Special Bar", "Cinque Stelle Special Bar Beans"],
        ["Dòng blend espresso phức hợp và cao cấp bậc nhất của chúng tôi.", "Our premiere and most complex espresso blend."],
        ["Ban đầu được chế tác độc quyền cho các nhà hàng danh tiếng hàng đầu nước Úc, Cinque Stelle mang đến hương vị đậm đà, hậu vị sô-cô-la đen ngọt ngào cùng lớp crema vàng óng sánh mịn.",
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
        ["Thương Hiệu Cà Phê Rang Xay Nguyên Chất Số 1 Nước Úc", "Australia's No.1 Pure Coffee Brand"],
        ["Được sáng lập vào năm 1958 bởi hai anh em người Ý Orazio và Carmelo Cantarella, Vittoria Coffee đã tiên phong mở đường cho làn sóng văn hóa thưởng thức espresso chuẩn phong cách Ý tại nước Úc.",
         "Established in 1958 by two Italian brothers, Orazio and Carmelo Cantarella, Vittoria Coffee pioneered the espresso revolution in Australia."],
        ["Chất Lượng Thượng Hạng Không Thỏa Hiệp", "Uncompromising Quality"],
        ["Từng mẻ cà phê được chế tác hoàn toàn từ 100% hạt Arabica thượng hạng tuyển chọn, rang đến độ hoàn hảo tuyệt đối tại xưởng rang Sydney.",
         "Every blend is crafted with 100% premium Arabica coffee beans, master roasted to perfection in our Sydney roastery."],
        ["Truyền Thống Gia Đình Ba Thế Hệ", "A Family Tradition"],
        ["Ba thế hệ trong gia đình Cantarella luôn tận tâm gìn giữ và phát triển nghệ thuật rang cà phê truyền thống.",
         "Three generations of family dedication to the art of coffee roasting."],
        ["Phát Triển Bền Vững & Trách Nhiệm Cộng Đồng", "Sustainability & Community"],
        ["Cam kết 100% nguồn cung minh bạch, hỗ trợ cộng đồng nông dân vùng trồng cà phê và bảo vệ môi trường bền vững.",
         "Committed to ethical sourcing and supporting coffee farming communities worldwide."],

        // Wholesale
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
        ["Trang bạn đang tìm kiếm có thể đã bị xóa, đổi tên hoặc tạm thời không khả dụng. Hãy để chúng tôi đưa bạn về đúng nơi.",
         "The page you are looking for might have been removed, had its name changed, or is temporarily unavailable. Let us help you find the right brew."],

        // Footer
        ["Về Vittoria Coffee", "About Vittoria"],
        ["Cửa Hàng", "Shop"],
        ["Hỗ Trợ Khách Hàng", "Customer Support"],
        ["Liên Hệ Với Chúng Tôi", "Contact Us"],
        ["Chính Sách Giao Hàng", "Shipping Policy"],
        ["Chính Sách Đổi Trả", "Returns Policy"],
        ["Chính Sách Bảo Mật", "Privacy Policy"],
        ["Điều Khoản & Điều Kiện", "Terms & Conditions"],
        ["© 2026 Vittoria Coffee. Bảo lưu mọi quyền.", "© 2026 Vittoria Coffee. All rights reserved."],
        ["Bảo lưu mọi quyền.", "All rights reserved."]
    ];

    let currentLang = 'vi'; // Default to Vietnamese (Primary)

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

        // Default: Vietnamese (Primary)
        currentLang = 'vi';
    }

    function translatePage(targetLang) {
        currentLang = targetLang;
        try { localStorage.setItem(STORAGE_KEY, targetLang); } catch (e) {}
        document.documentElement.setAttribute('lang', targetLang);

        const fromIdx = targetLang === 'en' ? 0 : 1; // 0 = VI, 1 = EN
        const toIdx = targetLang === 'en' ? 1 : 0;

        // Traverse and replace text in all text-containing elements
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
                if (ph.includes(searchStr)) {
                    ph = ph.split(searchStr).join(replaceStr);
                }
            });
            el.setAttribute('placeholder', ph);
        });

        updateSwitcherUI();
        window.dispatchEvent(new CustomEvent('language:changed', { detail: { language: targetLang } }));
    }

    function renderLanguageSwitcher() {
        // 1. Top Announcement Bar Switcher
        const topbars = document.querySelectorAll('.c-header__topbar, .c-announcement-bar');
        topbars.forEach(topbar => {
            if (topbar.querySelector('.c-lang-switcher')) return;

            const switcher = document.createElement('div');
            switcher.className = 'c-lang-switcher';
            switcher.innerHTML = `
                <button type="button" class="c-lang-btn ${currentLang === 'vi' ? 'is-active' : ''}" data-lang="vi" title="Tiếng Việt (Chính)">
                    <span class="c-lang-flag">🇻🇳</span> Tiếng Việt
                </button>
                <span class="c-lang-divider">|</span>
                <button type="button" class="c-lang-btn ${currentLang === 'en' ? 'is-active' : ''}" data-lang="en" title="English">
                    <span class="c-lang-flag">🇬🇧</span> English
                </button>
            `;

            topbar.style.display = 'flex';
            topbar.style.justifyContent = 'space-between';
            topbar.style.alignItems = 'center';
            topbar.appendChild(switcher);
        });

        // 2. Footer Switcher
        const footers = document.querySelectorAll('footer .c-footer__bottom, footer div:last-child');
        footers.forEach(foot => {
            if (foot.querySelector('.c-lang-switcher--footer')) return;

            const footerSwitcher = document.createElement('div');
            footerSwitcher.className = 'c-lang-switcher c-lang-switcher--footer';
            footerSwitcher.style.margin = '16px auto';
            footerSwitcher.innerHTML = `
                <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-right: 8px; color: #AC8A62; font-weight: 600;">Ngôn ngữ / Language:</span>
                <button type="button" class="c-lang-btn ${currentLang === 'vi' ? 'is-active' : ''}" data-lang="vi">
                    🇻🇳 Tiếng Việt (Chính)
                </button>
                <span class="c-lang-divider">|</span>
                <button type="button" class="c-lang-btn ${currentLang === 'en' ? 'is-active' : ''}" data-lang="en">
                    🇬🇧 English
                </button>
            `;
            foot.appendChild(footerSwitcher);
        });

        // 3. Delegate switcher click events
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
    window.VittoriaI18n = {
        setLanguage: translatePage,
        getLanguage: function () { return currentLang; },
        translate: translatePage
    };

    // Auto-init
    initLanguage();
    document.addEventListener('DOMContentLoaded', () => {
        renderLanguageSwitcher();
        if (currentLang === 'en') {
            translatePage('en');
        } else {
            translatePage('vi');
        }
    });
})();
