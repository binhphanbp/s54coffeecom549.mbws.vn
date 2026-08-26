#!/usr/bin/env python3
"""
Master Upgrade of S54 Product Cards (collections-coffee.html, index.html)
Transforms scattered, uneven product cards into a unified, pixel-perfect,
luxury card grid with equal heights, crisp typography, and top-tier alignment.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
css_path = BASE_DIR / 'assets/css/custom.css'
css = css_path.read_text(encoding='utf-8')

card_css = '''
/* ==========================================================================
   MASTER S54 LUXURY PRODUCT CARD SYSTEM (Unified, Equal Height, Pristine UI)
   ========================================================================== */

/* 1. Grid & Flex Uniformity */
.o-products-list__products,
.c-product-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)) !important;
    gap: 24px !important;
    align-items: stretch !important;
}

@media (min-width: 1200px) {
    .o-products-list__products {
        grid-template-columns: repeat(4, 1fr) !important;
    }
}

/* 2. Unified Master Card Box */
.o-product-thumbnail {
    background: #FFFFFF !important;
    border: 1px solid #EBE7E1 !important;
    border-radius: 12px !important;
    padding: 18px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
    box-sizing: border-box !important;
    position: relative !important;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease !important;
    box-shadow: 0 4px 16px rgba(47, 34, 26, 0.04) !important;
    overflow: visible !important;
}

.o-product-thumbnail:hover {
    transform: translateY(-6px) !important;
    box-shadow: 0 16px 36px rgba(47, 34, 26, 0.12) !important;
    border-color: #D68E1D !important;
}

.o-product-thumbnail__inner {
    display: flex !important;
    flex-direction: column !important;
    height: 100% !important;
    justify-content: space-between !important;
}

.o-product-thumbnail__link {
    display: flex !important;
    flex-direction: column !important;
    text-decoration: none !important;
    color: inherit !important;
    flex: 1 0 auto !important;
}

/* 3. Product Image Container & Aspect Ratio */
.o-product-thumbnail__image-container {
    background-color: #FAF8F5 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    padding: 16px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    aspect-ratio: 1 / 1 !important;
    position: relative !important;
    margin-bottom: 14px !important;
    box-shadow: none !important;
}

.o-product-thumbnail__image-container:after,
.o-product-thumbnail__image:after {
    display: none !important;
}

.o-product-thumbnail__image-container img,
.o-product-thumbnail__image {
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    background: transparent !important;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
    filter: drop-shadow(0 4px 12px rgba(47, 34, 26, 0.08)) !important;
}

.o-product-thumbnail:hover .o-product-thumbnail__image-container img,
.o-product-thumbnail:hover .o-product-thumbnail__image {
    transform: scale(1.05) !important;
}

/* 4. Luxury Corner Badge */
.o-product-thumbnail__badge {
    position: absolute !important;
    top: 10px !important;
    left: 10px !important;
    z-index: 10 !important;
    background: rgba(214, 142, 29, 0.94) !important;
    color: #FFFFFF !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 10.5px !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    padding: 4px 10px !important;
    border-radius: 4px !important;
    box-shadow: 0 2px 8px rgba(214, 142, 29, 0.35) !important;
    margin: 0 !important;
    display: inline-block !important;
}

/* 5. Product Title - Strict 2-Line Uniform Height */
.o-product-thumbnail__title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    line-height: 1.35 !important;
    color: #2F221A !important;
    text-align: center !important;
    margin: 0 0 8px 0 !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    height: 42px !important;
    min-height: 42px !important;
}

.o-product-thumbnail:hover .o-product-thumbnail__title {
    color: #D68E1D !important;
}

/* 6. Clean Reviews & Star Rating */
.o-product-thumbnail__star-reviews {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin: 0 0 8px 0 !important;
    min-height: 20px !important;
}

.o-reviews__stars,
.oke-sr-wrapper,
.oke-sr {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 4px !important;
}

.oke-stars-foreground svg,
.oke-stars svg,
.o-reviews__stars svg {
    color: #D68E1D !important;
    fill: #D68E1D !important;
    height: 14px !important;
}

.oke-a11yText,
.oke-sr-label-text {
    display: none !important;
}

.oke-sr-count,
.o-product-thumbnail__star-reviews span {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 12.5px !important;
    font-weight: 600 !important;
    color: #8C7E74 !important;
    margin-left: 4px !important;
}

/* 7. Product Excerpt - Strict 2-Line Height */
.o-product-thumbnail__excerpt {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 13px !important;
    line-height: 1.45 !important;
    color: #6E6259 !important;
    text-align: center !important;
    margin: 0 0 12px 0 !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    height: 38px !important;
    min-height: 38px !important;
}

/* 8. Price Section */
.o-product-thumbnail__price {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #D68E1D !important;
    text-align: center !important;
    margin: 0 0 14px 0 !important;
    letter-spacing: -0.2px !important;
}

/* 9. Content / Hover Actions Form */
.o-product-thumbnail__content {
    margin-top: auto !important;
    width: 100% !important;
}

.o-product-thumbnail__form {
    width: 100% !important;
    margin: 0 !important;
}

/* 10. Add To Cart Button - Always Clean & Prominent */
.o-product-thumbnail__add-btn,
.o-btn.is-primary.is-dark.is-smaller {
    width: 100% !important;
    background-color: #2F221A !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 12px 16px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    display: block !important;
    text-align: center !important;
    box-sizing: border-box !important;
}

.o-product-thumbnail__add-btn:hover,
.o-btn.is-primary.is-dark.is-smaller:hover {
    background-color: #D68E1D !important;
    box-shadow: 0 4px 14px rgba(214, 142, 29, 0.35) !important;
    transform: translateY(-1px) !important;
}

.o-product-thumbnail__hover {
    opacity: 1 !important;
    visibility: visible !important;
    position: static !important;
    transform: none !important;
    width: 100% !important;
    display: block !important;
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
}

.o-product-thumbnail__swatches {
    display: none !important;
}
'''

if 'MASTER S54 LUXURY PRODUCT CARD SYSTEM' not in css:
    css += '\n' + card_css
    css_path.write_text(css, encoding='utf-8')
    print("✓ Added Master S54 Product Card CSS to custom.css")
else:
    # Replace existing
    import re
    css = re.sub(r'/\* ==========================================================================\s*MASTER S54 LUXURY PRODUCT CARD SYSTEM[\s\S]*', card_css.strip(), css)
    css_path.write_text(css, encoding='utf-8')
    print("✓ Replaced Master S54 Product Card CSS in custom.css")
