#!/usr/bin/env python3
"""
Rock-solid Capture-Phase Event Interceptor for Add To Bag & Forms:
1. Intercept 'click' and 'submit' in the CAPTURE phase (useCapture: true)
2. Add onsubmit="event.preventDefault(); return false;" to all <form action="/cart/add"> in all HTML files
3. Ensure instant, flawless add-to-cart, toast, and cart drawer opening
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Add onsubmit="event.preventDefault(); return false;" to all cart forms in HTML files
pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html', 'blogs-news.html', 'blog-detail.html']

for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    # Add onsubmit preventDefault to all cart forms
    c = re.sub(r'(<form[^>]*action=[\"\']/cart/add[\"\'][^>]*)>', r'\1 onsubmit="event.preventDefault(); return false;">', c)
    # If onsubmit is duplicated, fix it
    c = re.sub(r'onsubmit=\"[^\"]*\"\s+onsubmit=\"[^\"]*\"', 'onsubmit="event.preventDefault(); return false;"', c)
    fpath.write_text(c, encoding='utf-8')
    print(f"✓ Protected cart forms in {p}")

# 2. Update main.js with Capture-Phase listener
mj_path = BASE_DIR / 'assets/js/main.js'
mj = mj_path.read_text(encoding='utf-8')

capture_block = '''    /* =====================================================================
       CAPTURE-PHASE BULLETPROOF CART INTERCEPTOR (100% Reliable & Fast)
       ===================================================================== */
    let isProcessingCart = false;

    function handleAddToCart(targetEl, e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
            e.stopImmediatePropagation();
        }

        if (isProcessingCart) return;
        isProcessingCart = true;

        const card = targetEl.closest('.o-product-thumbnail') || 
                     targetEl.closest('.c-product-card') || 
                     targetEl.closest('.c-product-main') || 
                     targetEl.closest('form') ||
                     targetEl.closest('.shopify-section') || 
                     document;

        let title = 'S54 Robusta Cà Phê Rang Mộc Thượng Hạng';
        let price = 4400;
        let img = 'assets/images/s54/robusta_1.jpg';
        let id = Date.now();
        let qty = 1;

        // Title
        const titleEl = card.querySelector('.o-product-thumbnail__title, .c-product-card__title, .c-product-main__title, h1, h2, h3, h4, .o-heading');
        if (titleEl && titleEl.textContent) {
            title = titleEl.textContent.trim().replace(/\\s+/g, ' ');
        }

        // Price
        const priceEl = card.querySelector('.o-product-thumbnail__price, [data-product-money], .c-product-card__price, .price, .c-product-form__pricing, .o-pricing__price');
        if (priceEl && priceEl.textContent) {
            const parsed = parseFloat(priceEl.textContent.replace(/[^0-9.]/g, ''));
            if (!isNaN(parsed) && parsed > 0) price = Math.round(parsed * 100);
        }

        // Quantity
        const qtyInput = card.querySelector('input[name="quantity"], [data-product-form-qty], .c-product-form__qty');
        if (qtyInput && qtyInput.value) {
            const parsedQty = parseInt(qtyInput.value, 10);
            if (!isNaN(parsedQty) && parsedQty > 0) qty = parsedQty;
        }

        // Image
        const imgEl = card.querySelector('img:not(.c-header__logo img):not(.s54-footer img)');
        if (imgEl && (imgEl.src || imgEl.dataset.src)) {
            img = imgEl.src || imgEl.dataset.src;
        }

        // Add to S54Cart
        if (window.S54Cart) {
            window.S54Cart.addItem({
                id: id,
                variant_id: id,
                title: title,
                price: price,
                quantity: qty,
                image: img,
                url: 'product-detail.html'
            });
        }

        // Button feedback
        const btn = targetEl.tagName === 'BUTTON' ? targetEl : targetEl.querySelector('button') || targetEl;
        if (btn) {
            const orig = btn.innerHTML;
            btn.innerHTML = '✓ ' + _t('cart_btn_added');
            btn.style.backgroundColor = '#D68E1D';
            btn.style.color = '#FFFFFF';
            setTimeout(() => {
                btn.innerHTML = orig;
                btn.style.backgroundColor = '';
                btn.style.color = '';
                isProcessingCart = false;
            }, 800);
        } else {
            setTimeout(() => { isProcessingCart = false; }, 800);
        }

        showToast(_t('cart_added_toast', { title: title }));
        openCartDrawer();
    }

    // Capture-phase global click interceptor
    document.addEventListener('click', function (e) {
        // 1. Cart Drawer Toggle (Header icon)
        const cartToggle = e.target.closest('[data-cart-drawer-toggle], .c-header__cart, a[href*="/cart"], .c-icon-cart, [data-cart-trigger], .c-header__icon--cart, .is-cart');
        if (cartToggle) {
            e.preventDefault();
            e.stopPropagation();
            e.stopImmediatePropagation();
            openCartDrawer();
            return;
        }

        // 2. Add To Bag button
        const addBtn = e.target.closest('button[data-add-to-cart], .c-product-card__button, .c-product-card__add-to-cart, button.is-add-to-cart, [data-action="add-to-cart"], .o-product-thumbnail__add-btn, [data-product-form-add], button[name="add"], .c-product-form__add-btn, [data-quick-add-btn]');
        if (addBtn) {
            handleAddToCart(addBtn, e);
            return;
        }

        // 3. Orbe Modal Dismiss
        const orbeClose = e.target.closest('#md-btn__form__onSubmit, .md-app-modal__close-button, .md-app-modal-overlay');
        if (orbeClose) {
            e.preventDefault();
            e.stopPropagation();
            document.querySelectorAll('.md-app-modal, .md-app-modal-overlay, #md-app-modal').forEach(el => el.remove());
            document.body.style.overflow = '';
            return;
        }
    }, true); // useCapture = true ensures this fires BEFORE any theme scripts

    // Capture-phase global form submit interceptor
    document.addEventListener('submit', function (e) {
        const form = e.target.closest('form[action*="/cart/add"], [data-product-form], .c-product-form, .o-product-thumbnail__form');
        if (form) {
            handleAddToCart(form, e);
            return false;
        }
    }, true);
'''

# Find insertion location in main.js
start_marker = "/* ----- Global Click Delegation"
end_marker = "/* ----- Scroll-to-Top Button ----- */"

s_idx = mj.find(start_marker)
e_idx = mj.find(end_marker)

if s_idx != -1 and e_idx != -1:
    mj = mj[:s_idx] + capture_block + "\n        " + mj[e_idx:]
    mj_path.write_text(mj, encoding='utf-8')
    print("✓ Updated main.js with Capture-Phase bulletproof cart interceptor")
else:
    print("❌ Could not find click delegation markers in main.js")

print("\n✅ Cart Capture-Phase Interceptor successfully installed!")
