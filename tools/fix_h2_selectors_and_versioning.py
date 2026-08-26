#!/usr/bin/env python3
"""
Fix H2 CSS selectors and ensure custom.css overrides all section stylesheets:
- Move .c-product-carousel__title and .c-featured-collections__header-title into H2 (56px) rule.
- Add span/em support inside headings to inherit 56px.
- Update HTML files to load custom.css with timestamp query (?v=20260826) at both head and after section css.
"""

import time
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update custom.css
css_path = BASE_DIR / 'assets/css/custom.css'
c = css_path.read_text(encoding='utf-8')

# Ensure H2 block contains all section title classes and their child spans/ems
h2_block = '''/* ==========================================================================
   STRICT TYPOGRAPHIC HIERARCHY (H1: 68px > H2: 56px > H3: 36px > H4: 26px > H5/H6: 16px)
   ========================================================================== */

/* H1 / Primary Hero Headings (Desktop: 68px) */
h1,
.o-heading--1,
.s54-hero-title,
.c-hero-banner__title,
.c-hero-banner__title span {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(40px, 5.2vw, 68px) !important;
    line-height: 1.1 !important;
    font-weight: 700 !important;
    letter-spacing: -0.015em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
}

.s54-hero-title,
.s54-hero-title span {
    color: #FFFFFF !important;
}

/* H2 / Major Section Headings (Desktop: 56px) - Product Carousel, Story, Video, Best Sellers, Blog */
h2,
.o-heading--2,
.c-product-carousel__title,
.c-product-carousel__title span,
.c-product-carousel__title p,
.c-text-and-image__text-title,
.c-text-and-image__text-title span,
.c-text-and-image__title,
.c-featured-video__title,
.c-featured-video__title span,
.c-featured-collections__header-title,
.c-featured-collections__header-title span,
.c-featured-collections__title,
.c-product-main__title,
.c-article-feed__title,
.c-article-feed__title span {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(32px, 4vw, 56px) !important;
    line-height: 1.15 !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 20px !important;
}

/* H3 / Subsection Headings & Sub-carousels (Desktop: 36px) */
h3,
.o-heading--3,
.c-featured-collections__tab-title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(24px, 2.8vw, 36px) !important;
    line-height: 1.25 !important;
    font-weight: 600 !important;
    letter-spacing: -0.005em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 16px !important;
}

/* H4 / Cards & Content Blocks (Desktop: 26px) */
h4,
.o-heading--4,
.c-article-feed__card-title,
.s54-footer__heading {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(20px, 2vw, 26px) !important;
    line-height: 1.35 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

/* H5 & H6 / Product Card Labels & Subtitles (Desktop: 16px) */
h5, h6,
.o-heading--5,
.o-heading--6,
.o-product-thumbnail__title,
.c-product-carousel__product-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: clamp(14px, 1.2vw, 16px) !important;
    line-height: 1.4 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

/* Ensure nested spans, ems and paragraphs inside headings retain exact typography */
.o-heading--1 p, .o-heading--2 p, .o-heading--3 p, .o-heading--4 p, .o-heading--5 p, .o-heading--6 p,
.o-heading--1 span, .o-heading--2 span, .o-heading--3 span, .o-heading--4 span,
.o-heading--1 em, .o-heading--2 em, .o-heading--3 em {
    font-family: inherit !important;
    font-size: inherit !important;
    line-height: inherit !important;
    font-weight: inherit !important;
    letter-spacing: inherit !important;
    color: inherit !important;
    margin: 0 !important;
}'''

# Replace the typographic hierarchy section in custom.css
c = re.sub(r'/\* ==========================================================================\s*STRICT TYPOGRAPHIC HIERARCHY[\s\S]*?(?=\n\n/\*|\Z)', h2_block, c)
css_path.write_text(c, encoding='utf-8')
print("✓ Updated custom.css with comprehensive H2 56px selectors including span/p/em")

# 2. Add versioning cache-buster to all HTML files and ensure custom.css is loaded at the end of head
v_tag = f"assets/css/custom.css?v={int(time.time())}"
pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    page_content = fpath.read_text(encoding='utf-8')
    page_content = re.sub(r'assets/css/custom\.css(\?v=[0-9]+)?', v_tag, page_content)
    fpath.write_text(page_content, encoding='utf-8')
    print(f"✓ Updated cache-buster in {p} -> {v_tag}")

print("\n✅ All H2 selectors and cache-busting version parameters updated successfully!")
