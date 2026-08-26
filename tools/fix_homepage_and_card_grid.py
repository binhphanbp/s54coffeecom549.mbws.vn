#!/usr/bin/env python3
"""
Fix Homepage Featured Collections Grid (4 products per row) and Product Card Typography & Buttons
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update custom.css with robust 4-column grid for both index.html and collections-coffee.html
css_path = BASE_DIR / 'assets/css/custom.css'
css = css_path.read_text(encoding='utf-8')

grid_and_card_css = '''
/* ==========================================================================
   S54 Master Product Grid & Thumbnail System (Homepage & Collections)
   ========================================================================== */

/* 1. Grid Layout for Collections Page */
.o-products-list__products,
.c-product-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 36px 24px !important;
    align-items: start !important;
    width: 100% !important;
}

@media (max-width: 1199px) {
    .o-products-list__products,
    .c-product-grid {
        grid-template-columns: repeat(3, 1fr) !important;
    }
}

@media (max-width: 899px) {
    .o-products-list__products,
    .c-product-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 24px 16px !important;
    }
}

@media (max-width: 549px) {
    .o-products-list__products,
    .c-product-grid {
        grid-template-columns: 1fr !important;
    }
}

/* 2. Grid Layout for Homepage Featured Collections */
.c-featured-collections {
    background-color: #FAF8F5 !important;
    padding: 5rem 0 4rem !important;
    margin: 0 !important;
}

.c-featured-collections__products-list.is-active,
.c-featured-collections__products-list {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 36px 24px !important;
    width: 100% !important;
    max-width: 1440px !important;
    margin: 0 auto !important;
    padding: 0 clamp(20px, 4vw, 48px) !important;
    box-sizing: border-box !important;
    overflow: visible !important;
}

@media (max-width: 1199px) {
    .c-featured-collections__products-list.is-active,
    .c-featured-collections__products-list {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}

@media (max-width: 599px) {
    .c-featured-collections__products-list.is-active,
    .c-featured-collections__products-list {
        grid-template-columns: 1fr !important;
        padding: 0 16px !important;
    }
}

.c-featured-collections__product {
    width: 100% !important;
    margin: 0 !important;
    flex-shrink: 1 !important;
}

/* 3. Original Floating Minimalist Thumbnail */
.o-product-thumbnail {
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    box-shadow: none !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    box-sizing: border-box !important;
}

.o-product-thumbnail__inner {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
}

.o-product-thumbnail__link {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-decoration: none !important;
    color: inherit !important;
    width: 100% !important;
}

/* 4. Image Container - White Floating Box */
.o-product-thumbnail__image-container {
    background: #FFFFFF !important;
    border-radius: 8px !important;
    padding: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    aspect-ratio: 1 / 1 !important;
    width: 100% !important;
    max-width: 240px !important;
    margin: 0 auto 16px auto !important;
    box-shadow: 0 4px 18px rgba(47, 34, 26, 0.07) !important;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease !important;
    box-sizing: border-box !important;
}

.o-product-thumbnail:hover .o-product-thumbnail__image-container {
    transform: translateY(-6px) !important;
    box-shadow: 0 14px 32px rgba(47, 34, 26, 0.13) !important;
}

.o-product-thumbnail__image-container img,
.o-product-thumbnail__image {
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    background: transparent !important;
    border-radius: 0 !important;
}

/* 5. Original Centered Gold Pill Badge */
.o-product-thumbnail__badge {
    position: static !important;
    margin: 0 auto 10px auto !important;
    background-color: #D68E1D !important;
    color: #FFFFFF !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    padding: 5px 18px !important;
    border-radius: 20px !important;
    display: inline-block !important;
}

/* 6. Title - Strictly Aligned 2-Line Baseline */
.o-product-thumbnail__title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14.5px !important;
    font-weight: 700 !important;
    line-height: 1.35 !important;
    color: #2F221A !important;
    text-align: center !important;
    margin: 0 auto 8px auto !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    height: 40px !important;
    min-height: 40px !important;
    max-width: 250px !important;
}

/* 7. Rating & Reviews - Clean Single Line */
.o-product-thumbnail__star-reviews {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 4px !important;
    margin: 0 auto 8px auto !important;
    height: 20px !important;
    min-height: 20px !important;
}

.oke-a11yText,
.oke-sr-label-text,
.oke-sr-rating {
    display: none !important;
}

.o-reviews__stars,
.oke-sr-wrapper,
.oke-sr {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 3px !important;
}

.oke-stars-foreground svg,
.oke-stars svg,
.o-reviews__stars svg {
    color: #D68E1D !important;
    fill: #D68E1D !important;
    height: 13px !important;
}

.oke-sr-count,
.o-product-thumbnail__star-reviews span {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 12.5px !important;
    font-weight: 600 !important;
    color: #2F221A !important;
    margin-left: 3px !important;
}

/* 8. Product Excerpt - Uniform 2-Line Baseline */
.o-product-thumbnail__excerpt {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 13px !important;
    line-height: 1.45 !important;
    color: #5C4A3E !important;
    text-align: center !important;
    margin: 0 auto 10px auto !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    height: 38px !important;
    min-height: 38px !important;
    max-width: 240px !important;
}

/* 9. Price & Add To Cart Button - Stacked Vertically with Zero Collision */
.o-product-thumbnail__content {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    margin-top: 4px !important;
    gap: 10px !important;
}

.o-product-thumbnail__content-inner {
    position: static !important;
    display: block !important;
    width: 100% !important;
}

.o-product-thumbnail__price {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 16.5px !important;
    font-weight: 700 !important;
    color: #D68E1D !important;
    text-align: center !important;
    margin: 0 auto !important;
    display: block !important;
    line-height: 1 !important;
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
}

.o-product-thumbnail__hover__pricing,
.o-swatches__swatches,
.o-swatches,
.o-variant-selector__dropdown {
    display: none !important;
}

.o-product-thumbnail__form {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
    margin: 0 !important;
}

.o-product-thumbnail__add-btn {
    background-color: #2F221A !important;
    color: #FAF6F1 !important;
    border: 1px solid #2F221A !important;
    border-radius: 4px !important;
    padding: 10px 24px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    min-width: 160px !important;
    text-align: center !important;
    display: inline-block !important;
}

.o-product-thumbnail__add-btn:hover {
    background-color: #D68E1D !important;
    border-color: #D68E1D !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 12px rgba(214, 142, 29, 0.3) !important;
    transform: translateY(-1px) !important;
}
'''

# Replace the previous product card CSS in custom.css
if 'S54 Product Grid & Thumbnail - Clean Original Editorial Alignment' in css:
    css = re.sub(r'/\* ==========================================================================\s*S54 Product Grid & Thumbnail - Clean Original Editorial Alignment[\s\S]*', grid_and_card_css.strip(), css)
elif 'S54 Master Product Grid & Thumbnail System' in css:
    css = re.sub(r'/\* ==========================================================================\s*S54 Master Product Grid & Thumbnail System[\s\S]*', grid_and_card_css.strip(), css)
else:
    css += '\n' + grid_and_card_css.strip()

css_path.write_text(css, encoding='utf-8')
print("✓ Updated custom.css with 4-column grid for Homepage & Collections")

# 2. Update index.html 'SHOP ALL' -> 'XEM TẤT CẢ SẢN PHẨM'
idx_path = BASE_DIR / 'index.html'
idx_txt = idx_path.read_text(encoding='utf-8')
idx_txt = idx_txt.replace('SHOP ALL', 'Xem Tất Cả Sản Phẩm').replace('Shop All', 'Xem Tất Cả Sản Phẩm')
idx_path.write_text(idx_txt, encoding='utf-8')
print("✓ Localized 'SHOP ALL' on index.html to 'Xem Tất Cả Sản Phẩm'")
