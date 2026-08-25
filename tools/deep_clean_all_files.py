#!/usr/bin/env python3
"""
DEEP CLEAN: Systematically replace ALL remaining Vittoria/AUD/placeholder references
across ALL HTML files with S54 Coffee / VND / Vietnamese data.
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

# ========================================================================
# Price mapping: AUD -> VND
# ========================================================================
PRICE_MAP = {
    '$56.50 AUD': '145.000₫', '$63.00 AUD': '185.000₫',
    '$60.50 AUD': '150.000₫', '$55.00 AUD': '165.000₫',
    '$53.50 AUD': '155.000₫', '$48.50 AUD': '125.000₫',
    '$44.00 AUD': '185.000₫', '$42.00 AUD': '195.000₫',
    '$41.00 AUD': '195.000₫', '$38.00 AUD': '135.000₫',
    '$36.00 AUD': '150.000₫', '$30.00 AUD': '95.000₫',
    '$16.30 AUD': '55.000₫',  '$45.38 AUD': '125.000₫',
    'From $9.50 AUD': '35.000₫',
    '$9.50 AUD': '35.000₫',
    '$0.00': '0₫',
}

# ========================================================================
# Product name mapping
# ========================================================================
PRODUCT_MAP = {
    'Cinque Stelle Special Bar Beans': 'S54 Robusta Rang Mộc Nguyên Chất',
    'Cinque Stelle Beans': 'S54 Robusta Rang Mộc',
    'Oro Coffee Beans': 'S54 Arabica Cầu Đất Thượng Hạng',
    'Espresso Coffee Beans': 'S54 Cà Phê Túi Lọc Drip Bag',
    'Mountain Grown Beans': 'S54 Xay Sẵn Pha Phin Chuẩn Vị',
    'Organic Coffee Beans': 'S54 Cà Phê Hòa Tan 3-in-1',
    'Black Valley Beans': 'S54 Cà Phê Sấy Lạnh Freeze-Dried',
    'Original Drinking Chocolate 60g': 'S54 Cacao Uống Liền 60g',
    'Original Drinking Chocolate': 'S54 Cacao Uống Liền',
    'Italian-style drinking chocolate': 'Bột cacao hòa tan thượng hạng',
    'BUY ANY 2 SAVE 15%': 'MUA 2 GIẢM 15%',
    'BUY ANY 3 SAVE 20%': 'MUA 3 GIẢM 20%',
    'Subscribe and save 25%': 'Đăng ký mua định kỳ giảm 25%',
    'How subscriptions work': 'Cách mua hàng định kỳ',
    'Products are automatically delivered on your schedule. No obligation, modify or cancel your subscription anytime.': 
        'Sản phẩm sẽ được giao tự động theo lịch của bạn. Không ràng buộc, thay đổi hoặc hủy bất kỳ lúc nào.',
}

# ========================================================================
# Brand/company replacements
# ========================================================================
BRAND_MAP = {
    'Vittoria Coffee': 'S54 COFFEE',
    'vittoria coffee': 'S54 Coffee',
    'Vittoria': 'S54',
    'vittoria': 's54',
    'Cantarella': 'Good Solutions',
    'Les Schirato': 'Paul Hieu',
    '"Australia"': '"Vietnam"',
    "'Australia'": "'Vietnam'",
    'data-country="Australia"': 'data-country="Vietnam"',
    'mdApp_currentCountryCodeName = \'Australia\'': 'mdApp_currentCountryCodeName = \'Vietnam\'',
}

# ========================================================================
# URL replacements
# ========================================================================
URL_MAP = {
    'https://www.vittoriacoffee.com/cdn/s/trekkie.storefront.cc6f2681670fc14d7585bd9923d994cbe5e92b02.min.js': '',
    'https://www.vittoriacoffee.com/cdn/shopifycloud/storefront/assets/shop_events_listener-4e26a9ce.js': '',
    'https://www.vittoriacoffee.com/cdn/shopifycloud/perf-kit/shopify-perf-kit-3.8.4.min.js': '',
    'https://www.vittoriacoffee.com/api/collect': '',
    'https://www.vittoriacoffee.com/collections/coffee-accessories': '#',
    '/collections/vittoria-coffee-subscriptions': '#',
    'https://www.vittoriacoffee.com/pages/help-desk': '#',
    'https://www.vittoriacoffee.com': 'https://s54coffeecom549.mbws.vn',
    '//www.vittoriacoffee.com': '',
    '"currency":"AUD"': '"currency":"VND"',
    'window.Currency.currency = "AUD"': 'window.Currency.currency = "VND"',
}

# ========================================================================
# Image path replacements (old Vittoria images -> S54 images)
# ========================================================================
IMAGE_MAP = {
    '132_vit-homepage-banner-desktop-2_2560x.jpg': 's54/banner_main.jpg',
    '159_vit-homepage-banner-desktop_1920x.jpg': 's54/banner_main.jpg',
    '207_vit-homepage-banner-mobile-2_1x.jpg': 's54/banner_main.jpg',
    '133_Vittoria_Coffee_Logo_Gold_400x.svg': 's54/s54_logo.png',
    '083_230919_Vittoria_Silverwater_R_45_2000x.jpg': 's54/roasting_facility.png',
    '049_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_500x.png': 's54/robusta_1.jpg',
    '000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png': 's54/robusta_1.jpg',
    '091_MicrosoftTeams-image_279_500x.png': 's54/arabica_beans.jpg',
    '151_ground_1kg_esp_f_R_Car_3_500x.png': 's54/robusta_2.jpg',
    '014_inst_100g_clas_f_V2_d7df202b-71d9-4a81-a29d-9af211d42e34_500x.png': 's54/instant_3in1_1.jpg',
    '247_bag_20pack_esp_f_V2_500x.png': 's54/freeze_dried_blend.jpg',
    '064_roasting-page-video_1650x.jpg': 's54/roasting_facility.png',
    '177_roasting-page-video_1x.jpg': 's54/roasting_facility.png',
    '101_vit-homepage-brewtorial-image-v2_3ff75815-e31b-48b3-80b3-fb3331adb615_1600x.jpg': 's54/banner_main.jpg',
    '018_VittoriaSL_0462.jpg': 's54/blog_cup.jpg',
    '155_how-to-store-coffee-beans-so-they-stay-fresh_94c51018-4a67-47de-aea1-3dd60b9a74b6_1024x.webp': 's54/blog_cup.jpg',
    '194_australian-coffee-types_c18a2ba3-6bcd-422a-8377-f3d4d7b2e7a0_1024x.svg': 's54/instant_3in1_2.jpg',
    '004_website-blog-post-image.png': 's54/robusta_3.jpg',
}

# ========================================================================
# Navigation / Menu text replacements
# ========================================================================
MENU_MAP = {
    'Khám Phá Các Loại Cà Phê Phong Cách Nước Úc': 'Các Loại Cà Phê Đặc Sản S54',
    'Cách Bảo Quản Hạt Cà Phê Sau Khi Mở Gói Để Luôn Tươi Mới': 'Bí Quyết Bảo Quản Cà Phê Luôn Tươi Mới',
    'Subscriptions': 'Mua Hàng Định Kỳ',
    'Coffee Accessories': 'Phụ Kiện Cà Phê',
    'Help Desk': 'Hỗ Trợ Khách Hàng',
    'Help &amp; Support': 'Hỗ Trợ & Liên Hệ',
}

# ========================================================================
# Content text (blog / hero / story) replacements
# ========================================================================
CONTENT_MAP = {
    'Phong Cách Nước Úc': 'Phong Cách Việt Nam',
    'từ Úc': 'từ Việt Nam',
    'tại Úc': 'tại Việt Nam',
    'Nước Úc': 'Việt Nam',
    'nước Úc': 'Việt Nam',
    'ở Úc': 'ở Việt Nam',
    'của Úc': 'của Việt Nam',
}

total_replacements = 0

html_files = list(BASE.glob('*.html'))
js_files = [BASE / 'assets' / 'js' / 'main.js', BASE / 'assets' / 'js' / 'i18n.js']
all_files = html_files + [f for f in js_files if f.exists()]

for filepath in all_files:
    c = filepath.read_text(encoding='utf-8')
    original = c
    count = 0
    
    # Apply all replacement maps
    for old, new in {**PRICE_MAP, **PRODUCT_MAP, **BRAND_MAP, **URL_MAP, **MENU_MAP, **CONTENT_MAP}.items():
        if old in c:
            occurrences = c.count(old)
            c = c.replace(old, new)
            count += occurrences
    
    # Replace image paths
    for old_img, new_img in IMAGE_MAP.items():
        pattern = f'assets/images/{old_img}'
        replacement = f'assets/images/{new_img}'
        if pattern in c:
            occurrences = c.count(pattern)
            c = c.replace(pattern, replacement)
            count += occurrences
    
    # Clean up broken external script tags that now have empty src
    c = re.sub(r'<script[^>]*src=""\s*[^>]*>.*?</script>', '', c, flags=re.DOTALL)
    c = re.sub(r"source_url:\s*\"\"", 'source_url: ""', c)
    
    # Replace any remaining "$XX.XX AUD" patterns
    def replace_aud_price(match):
        val = float(match.group(1))
        vnd = int(val * 25000)
        formatted = f"{vnd:,}".replace(',', '.')
        return f"{formatted}₫"
    c = re.sub(r'\$(\d+\.\d{2})\s*AUD', replace_aud_price, c)
    
    # Replace data-money="$XX.XX AUD"
    def replace_data_money(match):
        val = float(match.group(1))
        vnd = int(val * 25000)
        return f'data-money="{vnd}"'
    c = re.sub(r'data-money="\$(\d+\.\d{2})\s*AUD?"', replace_data_money, c)
    c = re.sub(r'data-money="\$(\d+\.\d{2})"', replace_data_money, c)
    
    # Clean remaining LD+JSON with Vittoria
    c = re.sub(
        r'<script type="application/ld\+json">.*?S54 COFFEE.*?</script>',
        '<script type="application/ld+json">{"@context":"http://schema.org/","@type":"Organization","name":"S54 COFFEE","url":"https://s54coffeecom549.mbws.vn","sameAs":[]}</script>',
        c, flags=re.DOTALL
    )
    
    if c != original:
        filepath.write_text(c, encoding='utf-8')
        total_replacements += count
        print(f"  ✓ {filepath.name}: {count}+ replacements")
    else:
        print(f"  - {filepath.name}: no changes needed")

print(f"\n✅ Deep clean complete: {total_replacements}+ total replacements across {len(all_files)} files")
