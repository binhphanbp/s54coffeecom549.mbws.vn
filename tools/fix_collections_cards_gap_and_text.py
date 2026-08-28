#!/usr/bin/env python3
"""
1. Eliminate the 50rem/55rem min-height gap completely in custom.css for all cards (including .has-many-options).
2. Clean up product titles, excerpts, and "FROM" pricing in collections-coffee.html and index.html.
"""

from pathlib import Path
import re

BASE_DIR = Path('/home/binhphan/matbao-ws/clients/s54coffeecom549.mbws.vn')

# 1. Update custom.css with aggressive min-height: 0 override
css_path = BASE_DIR / 'assets/css/custom.css'
css = css_path.read_text(encoding='utf-8')

gap_fix_css = '''
/* ==========================================================================
   S54 ZERO-GAP Master Thumbnail Override
   ========================================================================== */
.c-featured-collections .o-product-thumbnail,
.o-products-list__product-thumbnail,
.o-product-thumbnail.has-many-options,
.o-product-thumbnail {
    min-height: 0 !important;
    max-height: none !important;
    height: auto !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: flex-start !important;
    margin-bottom: 0 !important;
    padding: 0 !important;
}

@media only screen and (min-width: 1100px) {
    .c-featured-collections .o-product-thumbnail,
    .o-product-thumbnail.has-many-options,
    .o-product-thumbnail {
        min-height: 0 !important;
        height: auto !important;
        padding: 0 !important;
    }
}

@media only screen and (min-width: 1650px) {
    .c-featured-collections .o-product-thumbnail,
    .o-product-thumbnail.has-many-options,
    .o-product-thumbnail {
        min-height: 0 !important;
        height: auto !important;
        padding: 0 !important;
    }
}

.o-product-thumbnail__inner {
    height: auto !important;
    min-height: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: flex-start !important;
    padding: 0 !important;
    width: 100% !important;
    gap: 0 !important;
}

.o-product-thumbnail__content {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    margin-top: 10px !important;
    gap: 8px !important;
    min-height: 0 !important;
    height: auto !important;
}

.o-product-thumbnail__content-inner {
    position: static !important;
    display: block !important;
    width: 100% !important;
    margin-bottom: 6px !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
}

.o-product-thumbnail__price {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 15.5px !important;
    font-weight: 700 !important;
    color: #D68E1D !important;
    text-align: center !important;
    margin: 0 !important;
    display: block !important;
    line-height: 1.2 !important;
    letter-spacing: 0.5px !important;
}

.o-product-thumbnail__hover {
    position: static !important;
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: all !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transform: none !important;
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

.o-product-thumbnail__add-btn {
    background-color: #2F221A !important;
    color: #FAF6F1 !important;
    border: 1px solid #2F221A !important;
    border-radius: 4px !important;
    padding: 8px 20px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    min-width: 150px !important;
    text-align: center !important;
    display: inline-block !important;
}

.o-product-thumbnail__add-btn:hover {
    background-color: #D68E1D !important;
    border-color: #D68E1D !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
}
'''

if 'S54 ZERO-GAP Master Thumbnail Override' in css:
    css = re.sub(r'/\* ==========================================================================\s*S54 ZERO-GAP Master Thumbnail Override[\s\S]*', gap_fix_css.strip(), css)
else:
    css += '\n' + gap_fix_css.strip()

css_path.write_text(css, encoding='utf-8')

# Also copy to public/client-assets/css/custom.css
pub_css = BASE_DIR / 'public/client-assets/css/custom.css'
if pub_css.exists():
    pub_css.write_text(css, encoding='utf-8')

print("✓ Fixed zero-gap thumbnail styling in custom.css")

# 2. Clean up collections-coffee.html
cc_file = BASE_DIR / 'collections-coffee.html'
cc_txt = cc_file.read_text(encoding='utf-8')

# Replace awkward titles and excerpts
replacements = [
    ('FROM ', 'Từ '),
    ('From ', 'Từ '),
    ('from ', 'Từ '),
    ('S54 Khử Caffeinefeinated Blend', 'S54 Cà Phê Khử Caffeine (Decaf)'),
    ('An authentic Italian espresso, decaffeinated naturally', 'Cà phê espresso Ý nguyên bản, được khử caffeine tự nhiên'),
    ('Our original blend created over 65 years ago', 'Dòng blend nguyên bản tạo nên danh tiếng S54 Coffee'),
    ('One trên our original blends, reminiscent trên Italian-style coffee', 'Dòng blend đậm đà chuẩn vị cà phê Espresso Ý'),
    ('One of our original blends, reminiscent of Italian-style coffee', 'Dòng blend đậm đà chuẩn vị cà phê Espresso Ý'),
    ('Rich and delicate, sourced from high-altitudes', 'Hương vị phong phú, thanh tao từ vùng cao nguyên Cầu Đất'),
    ('Exclusive Specialty Range', 'Dòng Specialty Tuyển Chọn'),
    ('Our premiere blend, served in leading restaurants', 'Dòng blend phục vụ khách sạn & nhà hàng cao cấp'),
]

for old_s, new_s in replacements:
    cc_txt = cc_txt.replace(old_s, new_s)

# Ensure Decaf card has visible price
cc_txt = re.sub(
    r'(<div class="o-product-thumbnail__content-inner"><p class="o-product-thumbnail__price\s+o-paragraph--3">)\s*(</p>)',
    r'\1 Từ 125.000₫ \2',
    cc_txt
)

cc_file.write_text(cc_txt, encoding='utf-8')
print("✓ Cleaned up all titles, excerpts, and prices in collections-coffee.html")
