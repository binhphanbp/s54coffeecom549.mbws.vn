#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrade product-detail.html for S54 Coffee:
1. Embed 12 authentic S54 products from drive_data/products.json as window.S54_PRODUCTS.
2. Provide a dynamic router script that binds to URL param ?id=... (supports both 200001-200012 and 1-12).
3. Updates title, meta, breadcrumb, gallery images, H1, pricing, short/long description, and cart payload.
4. Updates related products carousel with authentic S54 products.
5. Removes remaining Australian / Vittoria / Cinque Stelle references.
"""

from pathlib import Path
import json
import re

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / 'drive_data' / 'products.json', encoding='utf-8') as f:
    products = json.load(f)

pd_file = BASE_DIR / 'product-detail.html'
text = pd_file.read_text(encoding='utf-8')

# 1. Clean Australian / Vittoria meta tags
text = re.sub(
    r'<title>.*?</title>',
    '<title id="dynamic-page-title">Túi Cà Phê Hòa Tan 3in1 S54 Coffee 456g | S54 COFFEE</title>',
    text,
    count=1
)
text = re.sub(
    r'<meta name="description" content="[^"]*" />',
    '<meta id="dynamic-meta-desc" name="description" content="Túi cà phê hòa tan 3in1 S54 Coffee 456g (24 gói x 19g). Đậm đà chuẩn vị cà phê Việt, tiện lợi mỗi ngày." />',
    text,
    count=1
)
text = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta id="dynamic-og-title" property="og:title" content="Túi Cà Phê Hòa Tan 3in1 S54 Coffee 456g | S54 COFFEE">',
    text,
    count=1
)
text = re.sub(
    r'<meta property="og:description" content="[^"]*">',
    '<meta id="dynamic-og-desc" property="og:description" content="Túi cà phê hòa tan 3in1 S54 Coffee 456g (24 gói x 19g). Đậm đà chuẩn vị cà phê Việt, tiện lợi mỗi ngày.">',
    text,
    count=1
)
text = re.sub(
    r'<meta name="twitter:title" content="[^"]*">',
    '<meta id="dynamic-tw-title" name="twitter:title" content="Túi Cà Phê Hòa Tan 3in1 S54 Coffee 456g | S54 COFFEE">',
    text,
    count=1
)
text = re.sub(
    r'<meta name="twitter:description" content="[^"]*">',
    '<meta id="dynamic-tw-desc" name="twitter:description" content="Túi cà phê hòa tan 3in1 S54 Coffee 456g (24 gói x 19g). Đậm đà chuẩn vị cà phê Việt, tiện lợi mỗi ngày.">',
    text,
    count=1
)

# 2. Clean intro description paragraph
old_intro = re.search(r'<div class="c-product-main__description--intro">[\s\S]*?</div>', text)
if old_intro:
    new_intro = '''<div class="c-product-main__description--intro">
        <p class="o-paragraph--1" id="dynamic-short-desc">Túi 24 gói x 19g – cà phê hòa tan 3in1 đậm đà, tiện lợi chuẩn vị truyền thống. Sản phẩm được sản xuất từ những hạt cà phê tuyển chọn kỹ lưỡng, mang đến trải nghiệm thưởng thức sảng khoái và tràn đầy năng lượng mỗi ngày.</p>
    </div>'''
    text = text.replace(old_intro.group(0), new_intro)

# 3. Clean breadcrumb
text = re.sub(
    r'<nav class="o-breadcrumbs " role="navigation" aria-label="breadcrumbs">[\s\S]*?</nav>',
    '''<nav class="o-breadcrumbs " role="navigation" aria-label="breadcrumbs">
   <a href="index.html">Trang Chủ</a>
   <span class="o-breadcrumbs__divider" aria-hidden="true">/</span>
   <a href="collections-coffee.html">Sản Phẩm Cà Phê</a>
   <span class="o-breadcrumbs__divider" aria-hidden="true">/</span>
   <span id="dynamic-breadcrumb-title" style="pointer-events: none; color: #8C7D73;">Túi Cà Phê Hòa Tan 3in1 S54 Coffee 456g</span>
 </nav>''',
    text
)

# 4. Clean H1 title and badge
text = re.sub(
    r'<h1 class="c-product-main__title[^"]*">.*?</h1>',
    '<h1 class="c-product-main__title o-heading--2" id="dynamic-product-title">Túi Cà Phê Hòa Tan 3in1 S54 Coffee 456g</h1>',
    text
)
text = re.sub(
    r'<div class="o-badge">.*?</div>',
    '<div class="o-badge" id="dynamic-product-badge">Cà Phê Hòa Tan</div>',
    text
)

# 5. Inject Dynamic Router Script before </body>
products_json_str = json.dumps(products, ensure_ascii=False)

router_script = f'''
<!-- S54 Dynamic Product Detail Router -->
<script>
window.S54_PRODUCTS = {products_json_str};

(function() {{
    function initProductDetail() {{
        const params = new URLSearchParams(window.location.search);
        let pid = params.get('id') || '200003';
        
        // Match product by id or num_id
        let product = window.S54_PRODUCTS.find(p => String(p.id) === String(pid) || String(p.num_id) === String(pid));
        if (!product) {{
            product = window.S54_PRODUCTS[2]; // Default to Túi 456g
        }}

        // 1. Update Title & Meta
        document.title = product.name + " | S54 COFFEE";
        const metaDesc = document.getElementById('dynamic-meta-desc');
        if (metaDesc) metaDesc.setAttribute('content', product.short_desc || product.name);

        const ogTitle = document.getElementById('dynamic-og-title');
        if (ogTitle) ogTitle.setAttribute('content', product.name + " | S54 COFFEE");

        const bcTitle = document.getElementById('dynamic-breadcrumb-title');
        if (bcTitle) bcTitle.textContent = product.name;

        // 2. Update Badge & Headings
        const pBadge = document.getElementById('dynamic-product-badge');
        if (pBadge) pBadge.textContent = product.category;

        const pTitle = document.getElementById('dynamic-product-title');
        if (pTitle) pTitle.textContent = product.name;

        const pShortDesc = document.getElementById('dynamic-short-desc');
        if (pShortDesc && product.short_desc) {{
            pShortDesc.textContent = product.short_desc;
        }}

        // 3. Update Gallery Images
        const galleryImgs = document.querySelectorAll('.c-product-gallery img');
        galleryImgs.forEach(img => {{
            img.src = product.image;
            img.srcset = product.image + ' 1x, ' + product.image + ' 2x';
            img.alt = product.name;
        }});

        const galleryZooms = document.querySelectorAll('.c-product-gallery a.MagicZoom');
        galleryZooms.forEach(a => {{
            a.href = product.image;
        }});

        // 4. Update Prices
        const priceEls = document.querySelectorAll('.o-pricing__money[data-product-money], .o-product-thumbnail__price-sale');
        priceEls.forEach(el => {{
            el.textContent = product.sale_price;
            el.setAttribute('data-money', product.sale_price);
            el.setAttribute('data-product-id', product.id);
        }});

        const compareEls = document.querySelectorAll('.o-pricing__compare, .o-product-thumbnail__price-compare');
        compareEls.forEach(el => {{
            el.textContent = product.regular_price;
            el.setAttribute('data-money', product.regular_price);
        }});

        // 5. Update Description Tab
        const descTab = document.querySelector('.c-product-tabs__content[data-tab-content="description"]');
        if (descTab) {{
            let contentHtml = '<h3>' + product.name + '</h3>';
            if (product.short_desc) {{
                contentHtml += '<p><strong>' + product.short_desc + '</strong></p>';
            }}
            if (product.long_desc) {{
                let parts = product.long_desc.split('\\n');
                parts.forEach(pt => {{
                    pt = pt.trim();
                    if (pt) {{
                        contentHtml += '<p>' + pt + '</p>';
                    }}
                }});
            }} else {{
                contentHtml += '<p>Sản phẩm được tuyển chọn từ những hạt cà phê Robusta & Arabica chất lượng cao nhất của vùng đất đỏ bazan Tây Nguyên, chế biến trên dây chuyền công nghệ hiện đại đảm bảo giữ trọn vẹn hương vị tự nhiên, an toàn và tinh khiết.</p>';
            }}
            descTab.innerHTML = contentHtml;
        }}

        // 6. Connect Quick Add / Add to Cart
        const form = document.querySelector('.c-product-main__form');
        if (form) {{
            const idInput = form.querySelector('input[name="id"]');
            if (idInput) idInput.value = product.id;

            const addBtn = form.querySelector('[data-product-form-add], button[type="submit"]');
            if (addBtn) {{
                addBtn.onclick = function(e) {{
                    e.preventDefault();
                    if (window.CartMock && typeof window.CartMock.addItem === 'function') {{
                        window.CartMock.addItem({{
                            id: product.id,
                            title: product.name,
                            price: parseInt(product.sale_price.replace(/\\D/g, '')) || 65000,
                            image: product.image,
                            quantity: 1
                        }});
                    }} else {{
                        alert('Đã thêm "' + product.name + '" vào giỏ hàng thành công!');
                    }}
                }};
            }}
        }}

        // 7. Update Related Products Cards with Authentic S54 Products
        const relatedTiles = document.querySelectorAll('.c-featured-collections .o-product-thumbnail');
        const otherProds = window.S54_PRODUCTS.filter(p => String(p.id) !== String(product.id));
        relatedTiles.forEach((tile, index) => {{
            if (index < otherProds.length) {{
                const rp = otherProds[index];
                const link = tile.querySelector('a.o-product-thumbnail__link');
                if (link) link.href = 'product-detail.html?id=' + rp.id;

                const img = tile.querySelector('img.o-product-thumbnail__image');
                if (img) {{
                    img.src = rp.image;
                    img.srcset = rp.image + ' 1x, ' + rp.image + ' 2x';
                    img.alt = rp.name;
                }}

                const title = tile.querySelector('.o-product-thumbnail__title');
                if (title) title.textContent = rp.name;

                const excerpt = tile.querySelector('.o-product-thumbnail__excerpt');
                if (excerpt) excerpt.textContent = rp.short_desc || rp.name;

                const price = tile.querySelector('.o-product-thumbnail__price, .o-pricing__money');
                if (price) price.textContent = rp.sale_price;

                const badge = tile.querySelector('.o-product-thumbnail__badge');
                if (badge) badge.textContent = rp.category;
            }}
        }});
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', initProductDetail);
    }} else {{
        initProductDetail();
    }}
}})();
</script>
'''

if 'window.S54_PRODUCTS' not in text:
    text = text.replace('</body>', router_script + '\n</body>')

pd_file.write_text(text, encoding='utf-8')
print("Successfully upgraded product-detail.html with authentic S54 dynamic data!")
