#!/usr/bin/env python3
import re
from pathlib import Path

css_path = Path('assets/css/custom.css')
c = css_path.read_text(encoding='utf-8')

heading_css = '''
/* ==========================================================================
   STRICT TYPOGRAPHIC HIERARCHY (H1 > H2 > H3 > H4 > H5 > H6)
   Fix: H2 was occasionally larger than H1. Now standardized & proportional.
   ========================================================================== */

/* H1 / Primary Hero Headings */
h1,
.o-heading--1,
.s54-hero-title,
.c-hero-banner__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(34px, 4.2vw, 52px) !important;
    line-height: 1.15 !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
}

.s54-hero-title {
    color: #FFFFFF !important;
}

/* H2 / Major Section Headings (Always ~75% of H1) */
h2,
.o-heading--2,
.c-text-and-image__text-title,
.c-text-and-image__title,
.c-featured-video__title,
.c-product-main__title,
.c-article-feed__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(26px, 3vw, 38px) !important;
    line-height: 1.25 !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 16px !important;
}

/* H3 / Subsection Headings & Carousel Titles */
h3,
.o-heading--3,
.c-product-carousel__title,
.c-featured-collections__header-title,
.c-featured-collections__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(22px, 2.4vw, 30px) !important;
    line-height: 1.3 !important;
    font-weight: 600 !important;
    letter-spacing: -0.005em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 14px !important;
}

/* H4 / Cards & Content Blocks */
h4,
.o-heading--4,
.c-article-feed__card-title,
.c-product-carousel__product-title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(18px, 1.8vw, 24px) !important;
    line-height: 1.35 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

/* H5 & H6 / Product Card Labels & Subtitles */
h5, h6,
.o-heading--5,
.o-heading--6,
.o-product-thumbnail__title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: clamp(14px, 1.2vw, 16px) !important;
    line-height: 1.4 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

/* Ensure paragraph inside headings don't blow up */
.o-heading--1 p, .o-heading--2 p, .o-heading--3 p, .o-heading--4 p, .o-heading--5 p, .o-heading--6 p {
    font-family: inherit !important;
    font-size: inherit !important;
    line-height: inherit !important;
    font-weight: inherit !important;
    letter-spacing: inherit !important;
    color: inherit !important;
    margin: 0 !important;
}
'''

if 'STRICT TYPOGRAPHIC HIERARCHY' not in c:
    c = c + '\n' + heading_css
    css_path.write_text(c, encoding='utf-8')
    print("✓ Added strict typographic hierarchy to custom.css")
else:
    print("ℹ Typographic hierarchy already exists")
