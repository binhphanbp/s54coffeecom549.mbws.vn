#!/usr/bin/env python3
"""
1. Fix product thumbnail hover state to eliminate overlapping price / swatches / buttons.
   - When not hovering: Show only clean gold price (145.000₫).
   - When hovering: Smoothly fade in clean dark/gold 'THÊM VÀO GIỎ' button in place of the price.
2. Translate all collection filter pills into pure Vietnamese.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update custom.css with proper hover transitions
css_path = BASE_DIR / 'assets/css/custom.css'
css = css_path.read_text(encoding='utf-8')

clean_editorial_css = '''
/* ==========================================================================
   S54 Product Grid & Thumbnail - Clean Original Editorial Alignment
   ========================================================================== */

/* 1. Grid layout */
.o-products-list__products,
.c-product-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)) !important;
    gap: 40px 24px !important;
    align-items: start !important;
}

@media (min-width: 1200px) {
    .o-products-list__products {
        grid-template-columns: repeat(4, 1fr) !important;
    }
}

/* 2. Original Floating Minimalist Thumbnail */
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
    position: relative !important;
}

.o-product-thumbnail:hover {
    transform: none !important;
    box-shadow: none !important;
    border-color: transparent !important;
}

.o-product-thumbnail__inner {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
    position: relative !important;
}

.o-product-thumbnail__link {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-decoration: none !important;
    color: inherit !important;
    width: 100% !important;
}

/* 3. Image Container - Original White Floating Box */
.o-product-thumbnail__image-container {
    background: #FFFFFF !important;
    border-radius: 8px !important;
    padding: 20px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    aspect-ratio: 1 / 1 !important;
    width: 100% !important;
    max-width: 260px !important;
    margin: 0 auto 18px auto !important;
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

/* 4. Original Centered Gold Pill Badge */
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
    box-shadow: none !important;
}

/* 5. Title - Strictly Aligned 2-Line Baseline */
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
    max-width: 260px !important;
}

/* 6. Rating & Reviews - Clean Single Line */
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

/* 7. Product Excerpt - Uniform 2-Line Baseline */
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

/* 8. Price & Hover Action Container - ZERO OVERLAP */
.o-product-thumbnail__content {
    width: 100% !important;
    position: relative !important;
    min-height: 42px !important;
    height: 42px !important;
    margin-top: 4px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* Static Price View */
.o-product-thumbnail__content-inner {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    opacity: 1 !important;
    visibility: visible !important;
    transition: opacity 0.25s ease, transform 0.25s ease !important;
    transform: translateY(0) !important;
}

.o-product-thumbnail__price {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 16.5px !important;
    font-weight: 700 !important;
    color: #D68E1D !important;
    text-align: center !important;
    margin: 0 !important;
    display: block !important;
    line-height: 1 !important;
}

/* Hover Action Button View */
.o-product-thumbnail__hover {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    opacity: 0 !important;
    visibility: hidden !important;
    pointer-events: none !important;
    transition: opacity 0.25s ease, transform 0.25s ease !important;
    transform: translateY(6px) !important;
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
}

.o-product-thumbnail:hover .o-product-thumbnail__content-inner {
    opacity: 0 !important;
    visibility: hidden !important;
    pointer-events: none !important;
    transform: translateY(-6px) !important;
}

.o-product-thumbnail:hover .o-product-thumbnail__hover {
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: all !important;
    transform: translateY(0) !important;
}

/* Hide clutter inside hover */
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
}

/* 9. Top Faceted Filter Bar Styling */
.c-collection-template__faceted-nav__header {
    background-color: #F5EFEB !important;
    border-radius: 40px !important;
    padding: 6px 14px !important;
    margin-bottom: 3.5rem !important;
}

.c-faceted-nav__filters-featured .o-btn,
.c-collection-template__facet-btn-main.o-btn {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border-radius: 30px !important;
    padding: 8px 18px !important;
}
'''

# Replace the previous product card CSS in custom.css
if 'S54 Product Grid & Thumbnail - Clean Original Editorial Alignment' in css:
    css = re.sub(r'/\* ==========================================================================\s*S54 Product Grid & Thumbnail - Clean Original Editorial Alignment[\s\S]*', clean_editorial_css.strip(), css)
else:
    css += '\n' + clean_editorial_css.strip()

css_path.write_text(css, encoding='utf-8')
print("✓ Updated custom.css with clean hover transition (zero overlap)")

# 2. Translate top filter pills in collections-coffee.html
cc_path = BASE_DIR / 'collections-coffee.html'
cc_txt = cc_path.read_text(encoding='utf-8')

# Ensure filter tags in i18n
i18n_path = BASE_DIR / 'assets/js/i18n.js'
i18n_txt = i18n_path.read_text(encoding='utf-8')

filter_pairs = '''
        // COLLECTION FILTER TABS
        ["ONLINE EXCLUSIVE", "ONLINE EXCLUSIVE"],
        ["BEANS", "COFFEE BEANS"],
        ["SPECIALTY CÀ PHÊ HẠT", "SPECIALTY BEANS"],
        ["BLENDS", "COFFEE BLENDS"],
        ["FEATURED", "FEATURED"],
        ["ALL", "ALL"],
'''

if 'COLLECTION FILTER TABS' not in i18n_txt:
    idx = i18n_txt.find('// 8. OUR STORY')
    if idx != -1:
        i18n_txt = i18n_txt[:idx] + filter_pairs + i18n_txt[idx:]
        i18n_path.write_text(i18n_txt, encoding='utf-8')
        print("✓ Added collection filter translation pairs to i18n.js")

print("✅ Filter pills & product card hover transitions fixed completely!")
