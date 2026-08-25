/**
 * Vittoria Coffee - Internationalization (i18n) Engine
 * Full Bilingual Support: Vietnamese (Default/Preferred) & English
 */
(function () {
    'use strict';

    const STORAGE_KEY = 'vittoria_storefront_lang';
    
    // Complete Vietnamese & English Dictionary
    const dictionary = {
        en: {
            // Header & Announcement
            "announcement_freeship": "Free Shipping: Orders over $69†",
            "nav_shop_all": "Shop All",
            "nav_shop_category": "Shop By Category",
            "nav_coffee_beans": "Coffee Beans",
            "nav_ground_coffee": "Ground Coffee",
            "nav_capsules": "Capsules",
            "nav_instant": "Instant",
            "nav_ready_to_mix": "Ready-to-Mix Sachets",
            "nav_coffee_bags": "Coffee Bags",
            "nav_drinking_chocolate": "Drinking Chocolate",
            "nav_accessories": "Accessories",
            "nav_subscriptions": "Subscriptions",
            "nav_learn": "Learn",
            "nav_our_story": "Our Story",
            "nav_roasting": "Roasting",
            "nav_news": "News",
            "nav_community": "Community",
            "nav_brewing_guides": "Brewing Guides",
            "nav_sub_benefits": "Benefits of a Coffee Subscription",
            "nav_wholesale": "Wholesale",
            "nav_business": "Business",
            "nav_bag": "Bag",
            "search_placeholder": "Try 'espresso'...",
            "skip_content": "Skip to content",

            // Cart Drawer & Toasts
            "cart_title": "Your Bag",
            "cart_empty_title": "Your bag is currently empty.",
            "cart_start_shopping": "Start Shopping",
            "cart_subtotal": "Subtotal",
            "cart_checkout": "CHECKOUT",
            "cart_freeship_qualified": "🎉 You qualify for FREE Delivery!",
            "cart_freeship_remaining": "You're {amount} away from FREE shipping!",
            "cart_added_toast": "✓ Added \"{title}\" to your Bag",
            "cart_btn_added": "ADDED!",
            "cart_btn_add": "ADD TO BAG",
            "cart_btn_quick_add": "Quick Add",
            "cart_subscribe_save": "SUBSCRIBE AND SAVE",
            "cart_proceed_checkout": "Proceeding to Secure Checkout...",

            // Common Homepage
            "home_hero_title": "Cinque Stelle",
            "home_hero_subtitle": "Australia's Favourite Premium Blend",
            "home_hero_cta": "Shop Now",
            "home_bestsellers_title": "Bestsellers",
            "home_roasting_title": "Master Roasters Since 1958",
            "home_roasting_desc": "For over 60 years, our master roasters have carefully selected and roasted 100% Arabica beans in Sydney, Australia.",
            "home_discover_more": "Discover More",
            "home_explore_range": "Explore Our Range",
            "home_beans_title": "Coffee Beans",
            "home_capsules_title": "Aluminium Capsules",
            "home_instant_title": "Special Blend Instant",
            "home_latest_articles": "Latest from the Roastery",
            "home_newsletter_title": "Stay in Touch",
            "home_newsletter_desc": "Subscribe to receive 10% off your first online order.",
            "home_newsletter_placeholder": "Enter your email",
            "home_newsletter_btn": "Subscribe",
            "home_newsletter_success": "Thank you! 10% discount code sent to {email}",

            // Collections Page
            "coll_all_title": "All Coffee Products",
            "coll_subtitle": "Premium blends & single origins freshly roasted in Sydney.",
            "coll_filter_btn": "Filter & Sort",
            "coll_filter_title": "Filter By",
            "coll_roast_profile": "Roast Profile",
            "coll_roast_medium": "Medium Roast",
            "coll_roast_dark": "Dark Roast",
            "coll_roast_extra_dark": "Extra Dark Roast",
            "coll_format": "Format",
            "coll_format_beans": "Whole Beans",
            "coll_format_ground": "Ground",
            "coll_format_capsules": "Capsules",
            "coll_sort_by": "Sort By",
            "coll_sort_featured": "Featured",
            "coll_sort_best_selling": "Best Selling",
            "coll_sort_price_low": "Price: Low to High",
            "coll_sort_price_high": "Price: High to Low",

            // Product Detail Page
            "pdp_brand": "Vittoria Coffee",
            "pdp_title": "Cinque Stelle® Special Bar Coffee Beans",
            "pdp_desc": "Our premiere and most complex espresso blend. Initially developed as an after-dinner espresso famously served at Australia's most recognized restaurants.",
            "pdp_select_format": "Select Format",
            "pdp_one_time": "One-time purchase",
            "pdp_subscribe": "Subscribe & Save 10%",
            "pdp_deliver_every": "Deliver every 4 weeks",
            "pdp_tasting_notes": "Tasting Notes",
            "pdp_roast_level": "Roast Level",
            "pdp_brewing_tips": "Brewing Tips",
            "pdp_faqs": "Frequently Asked Questions",
            "pdp_reviews": "Customer Reviews",
            "pdp_in_stock": "In Stock — Fast Australia-wide Delivery",

            // Our Story Page
            "story_title": "Our Story",
            "story_subtitle": "Australia's No.1 Pure Coffee Brand",
            "story_p1": "Established in 1958 by two Italian brothers, Orazio and Carmelo Cantarella, Vittoria Coffee pioneered the espresso revolution in Australia.",
            "story_heritage_title": "Italian Heritage, Australian Made",
            "story_quality_title": "Uncompromising Quality",
            "story_quality_desc": "Every blend is crafted with 100% premium Arabica coffee beans, master roasted to perfection in our Sydney roastery.",

            // Wholesale Page
            "wholesale_title": "Wholesale & Business Solutions",
            "wholesale_subtitle": "Partner with Australia's premier coffee supplier for your café, restaurant, hotel or workplace.",
            "wholesale_equip_title": "Commercial Equipment",
            "wholesale_equip_desc": "From La Marzocco to Faema, we supply state-of-the-art espresso machinery.",
            "wholesale_training_title": "Barista Training",
            "wholesale_training_desc": "Comprehensive training programs at our state-of-the-art coffee academies.",
            "wholesale_form_title": "Partner with Us",
            "wholesale_form_name": "Full Name",
            "wholesale_form_business": "Business Name",
            "wholesale_form_email": "Email Address",
            "wholesale_form_phone": "Phone Number",
            "wholesale_form_type": "Business Type",
            "wholesale_form_submit": "Submit Enquiry",
            "wholesale_form_success": "Thank you! Our wholesale team will get in touch shortly.",

            // 404 Page
            "404_title": "Page Not Found",
            "404_desc": "The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.",
            "404_btn_home": "Return to Homepage",
            "404_btn_explore": "Explore Coffee Range",

            // Footer
            "footer_about": "About Vittoria",
            "footer_shop": "Shop",
            "footer_support": "Customer Support",
            "footer_contact": "Contact Us",
            "footer_rights": "© 2026 Vittoria Coffee. All rights reserved."
        },
        vi: {
            // Header & Announcement
            "announcement_freeship": "Miễn Phí Giao Hàng: Đơn Hàng Từ $69†",
            "nav_shop_all": "Tất Cả Sản Phẩm",
            "nav_shop_category": "Danh Mục Cà Phê",
            "nav_coffee_beans": "Cà Phê Hạt (Beans)",
            "nav_ground_coffee": "Cà Phê Xay (Ground)",
            "nav_capsules": "Viên Nén (Capsules)",
            "nav_instant": "Cà Phê Hòa Tan",
            "nav_ready_to_mix": "Gói Pha Tiện Lợi",
            "nav_coffee_bags": "Túi Lọc Cà Phê",
            "nav_drinking_chocolate": "Sô-cô-la Uống",
            "nav_accessories": "Phụ Kiện Pha Chế",
            "nav_subscriptions": "Đăng Ký Định Kỳ",
            "nav_learn": "Khám Phá",
            "nav_our_story": "Câu Chuyện Thương Hiệu",
            "nav_roasting": "Quy Trình Rang Xay",
            "nav_news": "Tin Tức & Blog",
            "nav_community": "Cộng Đồng",
            "nav_brewing_guides": "Hướng Dẫn Pha Chế",
            "nav_sub_benefits": "Ưu Đãi Đặt Định Kỳ",
            "nav_wholesale": "Bán Sỉ B2B",
            "nav_business": "Giải Pháp Doanh Nghiệp",
            "nav_bag": "Giỏ Hàng",
            "search_placeholder": "Tìm kiếm 'espresso', 'cinque stelle'...",
            "skip_content": "Chuyển đến nội dung chính",

            // Cart Drawer & Toasts
            "cart_title": "Giỏ Hàng Của Bạn",
            "cart_empty_title": "Giỏ hàng của bạn đang trống.",
            "cart_start_shopping": "Bắt Đầu Mua Sắm",
            "cart_subtotal": "Tạm Tính",
            "cart_checkout": "TIẾN HÀNH THANH TOÁN",
            "cart_freeship_qualified": "🎉 Bạn đã được MIỄN PHÍ VẬN CHUYỂN!",
            "cart_freeship_remaining": "Mua thêm {amount} để được MIỄN PHÍ VẬN CHUYỂN!",
            "cart_added_toast": "✓ Đã thêm \"{title}\" vào Giỏ Hàng",
            "cart_btn_added": "ĐÃ THÊM!",
            "cart_btn_add": "THÊM VÀO GIỎ",
            "cart_btn_quick_add": "Thêm Nhanh",
            "cart_subscribe_save": "ĐẶT ĐỊNH KỲ & TIẾT KIỆM 10%",
            "cart_proceed_checkout": "Đang chuyển đến cổng thanh toán bảo mật...",

            // Common Homepage
            "home_hero_title": "Cinque Stelle",
            "home_hero_subtitle": "Dòng Cà Phê Thượng Hạng Được Yêu Thích Số 1 Nước Úc",
            "home_hero_cta": "Khám Phá Ngay",
            "home_bestsellers_title": "Sản Phẩm Bán Chạy Nhất",
            "home_roasting_title": "Nghệ Thuật Rang Cà Phê Thủ Công Từ 1958",
            "home_roasting_desc": "Hơn 60 năm qua, các nghệ nhân rang bậc thầy của chúng tôi luôn chọn lọc và rang thủ công 100% hạt Arabica thượng hạng tại xưởng rang Sydney, Úc.",
            "home_discover_more": "Tìm Hiểu Thêm",
            "home_explore_range": "Khám Phá Toàn Bộ Dòng Sản Phẩm",
            "home_beans_title": "Cà Phê Hạt Nguyên Chất",
            "home_capsules_title": "Viên Nén Vỏ Nhôm Cao Cấp",
            "home_instant_title": "Cà Phê Hòa Tan Đặc Biệt",
            "home_latest_articles": "Tin Tức Mới Nhất Từ Xưởng Rang",
            "home_newsletter_title": "Đăng Ký Nhận Bản Tin",
            "home_newsletter_desc": "Đăng ký email để nhận ngay mã ưu đãi giảm 10% cho đơn hàng đầu tiên.",
            "home_newsletter_placeholder": "Nhập địa chỉ email của bạn",
            "home_newsletter_btn": "Đăng Ký Ngay",
            "home_newsletter_success": "Cảm ơn bạn! Mã giảm giá 10% đã được gửi đến {email}",

            // Collections Page
            "coll_all_title": "Tất Cả Sản Phẩm Cà Phê",
            "coll_subtitle": "Các dòng blend cao cấp & single origin được rang mới mỗi ngày tại Sydney.",
            "coll_filter_btn": "Bộ Lọc & Sắp Xếp",
            "coll_filter_title": "Lọc Sản Phẩm Theo",
            "coll_roast_profile": "Mức Độ Rang (Roast Profile)",
            "coll_roast_medium": "Rang Vừa (Medium Roast)",
            "coll_roast_dark": "Rang Đậm (Dark Roast)",
            "coll_roast_extra_dark": "Rang Rất Đậm (Extra Dark)",
            "coll_format": "Định Dạng",
            "coll_format_beans": "Cà Phê Hạt Nguyên",
            "coll_format_ground": "Cà Phê Xay Sẵn",
            "coll_format_capsules": "Viên Nén Capsule",
            "coll_sort_by": "Sắp Xếp Theo",
            "coll_sort_featured": "Nổi Bật Nhất",
            "coll_sort_best_selling": "Bán Chạy Nhất",
            "coll_sort_price_low": "Giá: Từ Thấp Đến Cao",
            "coll_sort_price_high": "Giá: Từ Cao Đến Thấp",

            // Product Detail Page
            "pdp_brand": "Vittoria Coffee",
            "pdp_title": "Cà Phê Hạt Cinque Stelle® Special Bar 1kg",
            "pdp_desc": "Dòng blend espresso phức hợp và cao cấp bậc nhất của chúng tôi. Được chế tác độc quyền cho các nhà hàng danh tiếng và khách sạn cao cấp nhất nước Úc.",
            "pdp_select_format": "Chọn Định Dạng / Kích Cỡ",
            "pdp_one_time": "Mua một lần",
            "pdp_subscribe": "Đặt định kỳ & Tiết kiệm 10%",
            "pdp_deliver_every": "Giao hàng định kỳ mỗi 4 tuần",
            "pdp_tasting_notes": "Hương Vị Đặc Trưng (Tasting Notes)",
            "pdp_roast_level": "Cấp Độ Rang",
            "pdp_brewing_tips": "Hướng Dẫn Pha Chế Chuẩn Barista",
            "pdp_faqs": "Câu Hỏi Thường Gặp (FAQs)",
            "pdp_reviews": "Đánh Giá Từ Khách Hàng",
            "pdp_in_stock": "Còn Hàng — Giao Hàng Toàn Quốc Nhanh Chóng",

            // Our Story Page
            "story_title": "Câu Chuyện Thương Hiệu",
            "story_subtitle": "Thương Hiệu Cà Phê Rang Xay Nguyên Chất Số 1 Nước Úc",
            "story_p1": "Được sáng lập năm 1958 bởi hai anh em người Ý Orazio và Carmelo Cantarella, Vittoria Coffee là người tiên phong cho làn sóng thưởng thức espresso tại Úc.",
            "story_heritage_title": "Di Sản Nước Ý, Chế Tác Tại Nước Úc",
            "story_quality_title": "Chất Lượng Thượng Hạng Không Thỏa Hiệp",
            "story_quality_desc": "Từng mẻ cà phê được chế tác hoàn toàn từ 100% hạt Arabica chất lượng cao, rang đến độ hoàn hảo tại xưởng rang Sydney.",

            // Wholesale Page
            "wholesale_title": "Giải Pháp Bán Sỉ & Doanh Nghiệp (B2B)",
            "wholesale_subtitle": "Đối tác cung cấp cà phê cao cấp hàng đầu cho quán café, nhà hàng, khách sạn và văn phòng làm việc.",
            "wholesale_equip_title": "Hệ Thống Máy Pha Cà Phê Chuyên Nghiệp",
            "wholesale_equip_desc": "Phân phối chính hãng các dòng máy pha espresso đẳng cấp thế giới: La Marzocco, Faema, Mazzer.",
            "wholesale_training_title": "Đào Tạo Barista Chuyên Nghiệp",
            "wholesale_training_desc": "Chương trình đào tạo toàn diện tại học viện cà phê chuẩn quốc tế của chúng tôi.",
            "wholesale_form_title": "Đăng Ký Tư Vấn & Hợp Tác B2B",
            "wholesale_form_name": "Họ và Tên",
            "wholesale_form_business": "Tên Doanh Nghiệp / Quán Café",
            "wholesale_form_email": "Địa Chỉ Email",
            "wholesale_form_phone": "Số Điện Thoại",
            "wholesale_form_type": "Mô Hình Doanh Nghiệp",
            "wholesale_form_submit": "Gửi Thông Tin Hợp Tác",
            "wholesale_form_success": "Cảm ơn bạn! Đội ngũ tư vấn B2B sẽ liên hệ với bạn trong thời gian sớm nhất.",

            // 404 Page
            "404_title": "Không Tìm Thấy Trang",
            "404_desc": "Trang bạn đang tìm kiếm có thể đã bị xóa, đổi tên hoặc tạm thời không khả dụng. Hãy để chúng tôi đưa bạn về đúng nơi.",
            "404_btn_home": "Về Trang Chủ",
            "404_btn_explore": "Khám Phá Sản Phẩm Cà Phê",

            // Footer
            "footer_about": "Về Vittoria Coffee",
            "footer_shop": "Cửa Hàng",
            "footer_support": "Hỗ Trợ Khách Hàng",
            "footer_contact": "Liên Hệ",
            "footer_rights": "© 2026 Vittoria Coffee. Bảo lưu mọi quyền."
        }
    };

    // Text replacement map for automated DOM translations
    const phraseMap = [
        // Navigation & General
        [/Free Shipping:\s*Orders over \$69[†*]?/gi, "announcement_freeship"],
        [/Shop All/gi, "nav_shop_all"],
        [/Shop By Category/gi, "nav_shop_category"],
        [/Coffee Beans/gi, "nav_coffee_beans"],
        [/Ground Coffee/gi, "nav_ground_coffee"],
        [/Aluminium Capsules|Capsules/gi, "nav_capsules"],
        [/Instant Coffee|Instant/gi, "nav_instant"],
        [/Our Story/gi, "nav_our_story"],
        [/Wholesale/gi, "nav_wholesale"],
        [/Business/gi, "nav_business"],
        [/Subscriptions/gi, "nav_subscriptions"],
        [/Brewing Guides/gi, "nav_brewing_guides"],
        [/Community/gi, "nav_community"],
        [/Roasting/gi, "nav_roasting"],
        [/News/gi, "nav_news"],
        [/Shop Now/gi, "home_hero_cta"],
        [/Discover More/gi, "home_discover_more"],
        [/Explore Our Range/gi, "home_explore_range"],
        [/Bestsellers/gi, "home_bestsellers_title"],
        [/ADD TO BAG/gi, "cart_btn_add"],
        [/Quick Add/gi, "cart_btn_quick_add"],
        [/SUBSCRIBE AND SAVE/gi, "cart_subscribe_save"],
        [/CHECKOUT/gi, "cart_checkout"],
        [/Subtotal/gi, "cart_subtotal"],
        [/Your Bag/gi, "cart_title"],
        [/Return to Homepage/gi, "404_btn_home"],
        [/Explore Coffee Range/gi, "404_btn_explore"],
        [/Page Not Found/gi, "404_title"]
    ];

    let currentLang = 'vi'; // Default to Vietnamese per user requirement

    function initLanguage() {
        // 1. Check URL param ?lang=vi or ?lang=en
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        if (urlLang && (urlLang === 'vi' || urlLang === 'en')) {
            currentLang = urlLang;
            try { localStorage.setItem(STORAGE_KEY, urlLang); } catch (e) {}
            return;
        }

        // 2. Check localStorage
        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            if (saved && (saved === 'vi' || saved === 'en')) {
                currentLang = saved;
                return;
            }
        } catch (e) {}

        // Default: vi
        currentLang = 'vi';
    }

    function t(key, params) {
        const langDict = dictionary[currentLang] || dictionary.en;
        let text = langDict[key] || dictionary.en[key] || key;
        if (params && typeof params === 'object') {
            Object.keys(params).forEach(k => {
                text = text.replace(new RegExp(`\\{${k}\\}`, 'g'), params[k]);
            });
        }
        return text;
    }

    function setLanguage(lang) {
        if (lang !== 'vi' && lang !== 'en') return;
        currentLang = lang;
        try {
            localStorage.setItem(STORAGE_KEY, lang);
        } catch (e) {}

        document.documentElement.setAttribute('lang', lang === 'vi' ? 'vi' : 'en');
        applyTranslations();
        updateSwitcherUI();
        window.dispatchEvent(new CustomEvent('language:changed', { detail: { language: lang } }));
    }

    function applyTranslations() {
        const dict = dictionary[currentLang] || dictionary.en;

        // 1. Explicit data-i18n attributes
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                el.textContent = dict[key];
            }
        });

        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) {
                el.setAttribute('placeholder', dict[key]);
            }
        });

        // 2. Automated Smart Translations across common elements
        document.querySelectorAll('.c-header__topbar-message, .c-announcement-bar').forEach(el => {
            el.textContent = t('announcement_freeship');
        });

        document.querySelectorAll('.c-cart-drawer__title').forEach(el => {
            el.textContent = t('cart_title');
        });

        document.querySelectorAll('.c-cart-drawer__checkout-btn').forEach(el => {
            el.textContent = t('cart_checkout');
        });

        document.querySelectorAll('.c-cart-drawer__subtotal span:first-child').forEach(el => {
            el.textContent = t('cart_subtotal');
        });

        document.querySelectorAll('input[type="text"][name="q"]').forEach(el => {
            el.setAttribute('placeholder', t('search_placeholder'));
        });

        document.querySelectorAll('.c-main-menu__link-title, .c-navigation__link-title, .o-heading--6, .o-subtitle').forEach(el => {
            const raw = el.textContent.trim();
            for (let [regex, key] of phraseMap) {
                if (regex.test(raw)) {
                    el.textContent = t(key);
                    break;
                }
            }
        });

        document.querySelectorAll('button, a.o-btn, .o-btn').forEach(btn => {
            const raw = btn.textContent.trim();
            if (raw === 'Shop Now' || raw === 'Khám Phá Ngay') {
                btn.textContent = t('home_hero_cta');
            } else if (raw === 'ADD TO BAG' || raw === 'THÊM VÀO GIỎ') {
                btn.textContent = t('cart_btn_add');
            } else if (raw === 'Quick Add' || raw === 'Thêm Nhanh') {
                btn.textContent = t('cart_btn_quick_add');
            } else if (raw === 'Start Shopping' || raw === 'Bắt Đầu Mua Sắm') {
                btn.textContent = t('cart_start_shopping');
            }
        });
    }

    function renderLanguageSwitcher() {
        // Inject switcher into Header / Topbar
        const topbars = document.querySelectorAll('.c-header__topbar, .c-announcement-bar');
        topbars.forEach(topbar => {
            if (topbar.querySelector('.c-lang-switcher')) return;

            const switcher = document.createElement('div');
            switcher.className = 'c-lang-switcher';
            switcher.innerHTML = `
                <button type="button" class="c-lang-btn ${currentLang === 'vi' ? 'is-active' : ''}" data-lang="vi" title="Tiếng Việt">
                    <span class="c-lang-flag">🇻🇳</span> VN
                </button>
                <span class="c-lang-divider">|</span>
                <button type="button" class="c-lang-btn ${currentLang === 'en' ? 'is-active' : ''}" data-lang="en" title="English">
                    <span class="c-lang-flag">🇬🇧</span> EN
                </button>
            `;

            topbar.style.display = 'flex';
            topbar.style.justifyContent = 'space-between';
            topbar.style.alignItems = 'center';
            topbar.appendChild(switcher);
        });

        // Inject into Footer
        const footers = document.querySelectorAll('footer .c-footer__bottom, footer div:last-child');
        footers.forEach(foot => {
            if (foot.querySelector('.c-lang-switcher--footer')) return;

            const footerSwitcher = document.createElement('div');
            footerSwitcher.className = 'c-lang-switcher c-lang-switcher--footer';
            footerSwitcher.style.margin = '16px auto';
            footerSwitcher.innerHTML = `
                <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-right: 8px; color: #AC8A62;">Language / Ngôn ngữ:</span>
                <button type="button" class="c-lang-btn ${currentLang === 'vi' ? 'is-active' : ''}" data-lang="vi">
                    🇻🇳 Tiếng Việt
                </button>
                <span class="c-lang-divider">|</span>
                <button type="button" class="c-lang-btn ${currentLang === 'en' ? 'is-active' : ''}" data-lang="en">
                    🇬🇧 English
                </button>
            `;
            foot.appendChild(footerSwitcher);
        });

        // Delegate switcher click events
        document.addEventListener('click', (e) => {
            const btn = e.target.closest('[data-lang]');
            if (btn) {
                e.preventDefault();
                const targetLang = btn.getAttribute('data-lang');
                if (targetLang) {
                    setLanguage(targetLang);
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
        t: t,
        setLanguage: setLanguage,
        getLanguage: function () { return currentLang; },
        dictionary: dictionary
    };

    // Auto-init on load
    initLanguage();
    document.addEventListener('DOMContentLoaded', () => {
        document.documentElement.setAttribute('lang', currentLang === 'vi' ? 'vi' : 'en');
        renderLanguageSwitcher();
        applyTranslations();
    });
})();
