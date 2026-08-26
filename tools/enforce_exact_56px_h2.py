#!/usr/bin/env python3
import time
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update custom.css with EXACT 56px desktop rules and clean mobile fallback
css_path = BASE_DIR / 'assets/css/custom.css'
c = css_path.read_text(encoding='utf-8')

exact_typography_css = '''/* ==========================================================================
   STRICT TYPOGRAPHIC HIERARCHY (EXACT DESKTOP SIZES)
   H1: 68px (Desktop) / 38px (Mobile)
   H2: 56px (Desktop) / 32px (Mobile)
   H3: 32px (Desktop) / 22px (Mobile)
   H4: 24px (Desktop) / 18px (Mobile)
   H5/H6: 16px
   ========================================================================== */

/* H1 / Primary Hero Headings */
h1,
.o-heading--1,
.s54-hero-title,
.c-hero-banner__title,
.c-hero-banner__title span {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 38px !important;
    line-height: 1.1 !important;
    font-weight: 700 !important;
    letter-spacing: -0.015em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
}

@media (min-width: 768px) {
    h1,
    .o-heading--1,
    .s54-hero-title,
    .c-hero-banner__title,
    .c-hero-banner__title span {
        font-size: 68px !important;
        line-height: 1.08 !important;
    }
}

.s54-hero-title,
.s54-hero-title span {
    color: #FFFFFF !important;
}

/* H2 / Major Section Headings (EXACT 56px on Desktop) */
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
    font-size: 32px !important;
    line-height: 1.2 !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 20px !important;
}

@media (min-width: 768px) {
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
        font-size: 56px !important;
        line-height: 1.12 !important;
    }
}

/* H3 / Subsection Headings */
h3,
.o-heading--3,
.c-featured-collections__tab-title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 22px !important;
    line-height: 1.3 !important;
    font-weight: 600 !important;
    letter-spacing: -0.005em !important;
    color: #2F221A !important;
    margin-top: 0 !important;
    margin-bottom: 16px !important;
}

@media (min-width: 768px) {
    h3,
    .o-heading--3,
    .c-featured-collections__tab-title {
        font-size: 32px !important;
        line-height: 1.22 !important;
    }
}

/* H4 / Cards & Content Blocks */
h4,
.o-heading--4,
.c-article-feed__card-title,
.s54-footer__heading {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 20px !important;
    line-height: 1.35 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

@media (min-width: 768px) {
    h4,
    .o-heading--4,
    .c-article-feed__card-title,
    .s54-footer__heading {
        font-size: 24px !important;
        line-height: 1.3 !important;
    }
}

/* H5 & H6 / Product Card Labels & Subtitles */
h5, h6,
.o-heading--5,
.o-heading--6,
.o-product-thumbnail__title,
.c-product-carousel__product-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 15px !important;
    line-height: 1.4 !important;
    font-weight: 600 !important;
    color: #2F221A !important;
}

/* Ensure nested spans, ems, ps inherit exact font-size */
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

# Replace the typographic hierarchy section
c = re.sub(r'/\* ==========================================================================\s*STRICT TYPOGRAPHIC HIERARCHY[\s\S]*?(?=\n\n/\*|\Z)', exact_typography_css, c)
css_path.write_text(c, encoding='utf-8')
print("✓ Updated custom.css with EXACT 56px on Desktop (>=768px)")

# 2. Add inline <style> block in index.html to 1000% guarantee immediate application without any caching delays
inline_style = f"""<style id="s54-direct-typography-override">
/* S54 DIRECT TYPOGRAPHY OVERRIDE */
@media (min-width: 768px) {{
    h1, .o-heading--1, .s54-hero-title, .c-hero-banner__title, .c-hero-banner__title span {{
        font-size: 68px !important;
        line-height: 1.08 !important;
    }}
    h2, .o-heading--2, .c-product-carousel__title, .c-product-carousel__title span, .c-product-carousel__title p,
    .c-text-and-image__text-title, .c-text-and-image__text-title span, .c-text-and-image__title,
    .c-featured-video__title, .c-featured-video__title span,
    .c-featured-collections__header-title, .c-featured-collections__header-title span,
    .c-featured-collections__title, .c-product-main__title,
    .c-article-feed__title, .c-article-feed__title span {{
        font-size: 56px !important;
        line-height: 1.12 !important;
    }}
    h3, .o-heading--3, .c-featured-collections__tab-title {{
        font-size: 32px !important;
        line-height: 1.22 !important;
    }}
}}
</style>"""

pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']
v_tag = f"assets/css/custom.css?v={int(time.time())}"

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    page_content = fpath.read_text(encoding='utf-8')
    page_content = re.sub(r'assets/css/custom\.css(\?v=[0-9]+)?', v_tag, page_content)
    
    # Remove old inline override if exists
    page_content = re.sub(r'<style id="s54-direct-typography-override">[\s\S]*?</style>', '', page_content)
    # Inject before </head>
    page_content = page_content.replace('</head>', f'{inline_style}\n</head>')
    
    fpath.write_text(page_content, encoding='utf-8')
    print(f"✓ Embedded direct 56px override in {p}")

print("\n✅ Enforced EXACT 56px H2 across all pages!")
