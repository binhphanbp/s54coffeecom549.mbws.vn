#!/usr/bin/env python3
import re
from pathlib import Path

css_path = Path('assets/css/custom.css')
c = css_path.read_text(encoding='utf-8')

# Replace the typographic hierarchy in custom.css
old_block_pattern = r'/\* ==========================================================================\s*STRICT TYPOGRAPHIC HIERARCHY[\s\S]*?(?=\n\n/\*|\Z)'

new_block = '''/* ==========================================================================
   STRICT TYPOGRAPHIC HIERARCHY (H1: 68px > H2: 56px > H3: 36px > H4: 26px > H5/H6: 16px)
   Standardized as requested: H2 is 56px on Desktop with smooth responsive clamp.
   ========================================================================== */

/* H1 / Primary Hero Headings (Desktop: 68px) */
h1,
.o-heading--1,
.s54-hero-title,
.c-hero-banner__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(40px, 5.2vw, 68px) !important;
    line-height: 1.1 !important;
    font-weight: 700 !important;
    letter-spacing: -0.015em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
}

.s54-hero-title {
    color: #FFFFFF !important;
}

/* H2 / Major Section Headings (Desktop: 56px) */
h2,
.o-heading--2,
.c-text-and-image__text-title,
.c-text-and-image__title,
.c-featured-video__title,
.c-product-main__title,
.c-article-feed__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(32px, 4vw, 56px) !important;
    line-height: 1.15 !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 20px !important;
}

/* H3 / Subsection Headings & Carousel Titles (Desktop: 36px) */
h3,
.o-heading--3,
.c-product-carousel__title,
.c-featured-collections__header-title,
.c-featured-collections__title {
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
.c-product-carousel__product-title {
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
.o-product-thumbnail__title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: clamp(14px, 1.2vw, 16px) !important;
    line-height: 1.4 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

/* Ensure nested paragraphs inside headings retain exact typography */
.o-heading--1 p, .o-heading--2 p, .o-heading--3 p, .o-heading--4 p, .o-heading--5 p, .o-heading--6 p {
    font-family: inherit !important;
    font-size: inherit !important;
    line-height: inherit !important;
    font-weight: inherit !important;
    letter-spacing: inherit !important;
    color: inherit !important;
    margin: 0 !important;
}'''

if re.search(old_block_pattern, c):
    c = re.sub(old_block_pattern, new_block, c)
else:
    c = c + '\n\n' + new_block

css_path.write_text(c, encoding='utf-8')
print("✓ Updated H2 to 56px (H1: 68px > H2: 56px) in custom.css")
