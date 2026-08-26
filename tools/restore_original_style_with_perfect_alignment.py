#!/usr/bin/env python3
"""
Restore the original elegant editorial aesthetic (floating on cream background, centered pill badge)
while fixing the alignment & messy text (straight horizontal baselines, cleaned single-row star ratings).
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent
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
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)) !important;
    gap: 36px 24px !important;
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
    transition: none !important;
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
}

.o-product-thumbnail__link {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-decoration: none !important;
    color: inherit !important;
    width: 100% !important;
}

/* 3. Image Container - Original White Floating Box with Smooth Shadow */
.o-product-thumbnail__image-container {
    background: #FFFFFF !important;
    border-radius: 8px !important;
    padding: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    aspect-ratio: 1 / 1 !important;
    width: 100% !important;
    max-width: 260px !important;
    margin: 0 auto 16px auto !important;
    box-shadow: 0 4px 16px rgba(47, 34, 26, 0.06) !important;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease !important;
    box-sizing: border-box !important;
}

.o-product-thumbnail:hover .o-product-thumbnail__image-container {
    transform: translateY(-6px) !important;
    box-shadow: 0 14px 30px rgba(47, 34, 26, 0.12) !important;
}

.o-product-thumbnail__image-container img,
.o-product-thumbnail__image {
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    background: transparent !important;
    border-radius: 0 !important;
    filter: none !important;
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

/* 8. Price - Uniform Baseline */
.o-product-thumbnail__price {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #D68E1D !important;
    text-align: center !important;
    margin: 0 auto 12px auto !important;
}

/* 9. Content / Form Actions */
.o-product-thumbnail__content {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
}

.o-product-thumbnail__form {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
}

.o-product-thumbnail__hover {
    display: block !important;
    width: 100% !important;
    max-width: 180px !important;
    margin: 0 auto !important;
    opacity: 1 !important;
    visibility: visible !important;
    position: static !important;
    background: transparent !important;
    box-shadow: none !important;
}

.o-product-thumbnail__add-btn {
    width: 100% !important;
    background-color: transparent !important;
    color: #2F221A !important;
    border: 1.5px solid #2F221A !important;
    border-radius: 4px !important;
    padding: 8px 14px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

.o-product-thumbnail__add-btn:hover {
    background-color: #2F221A !important;
    color: #FAF6F1 !important;
    transform: translateY(-1px) !important;
}
'''

# Replace the previous MASTER S54 LUXURY PRODUCT CARD SYSTEM with this clean editorial one
if 'MASTER S54 LUXURY PRODUCT CARD SYSTEM' in css:
    css = re.sub(r'/\* ==========================================================================\s*MASTER S54 LUXURY PRODUCT CARD SYSTEM[\s\S]*', clean_editorial_css.strip(), css)
else:
    css += '\n' + clean_editorial_css.strip()

css_path.write_text(css, encoding='utf-8')
print("✓ Successfully restored original editorial aesthetic with perfectly aligned baselines")
