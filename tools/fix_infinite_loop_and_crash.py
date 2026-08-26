#!/usr/bin/env python3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update main.js
main_js_path = BASE_DIR / 'assets/js/main.js'
mj = main_js_path.read_text(encoding='utf-8')

target_old = """        /* ----- Global Click Delegation ----- */
        document.addEventListener('click', (e) => {
            // Cart Icon
            if (e.target.closest('[data-cart-drawer-toggle], .c-header__cart, a[href*="/cart"], .c-icon-cart, [data-cart-trigger], .c-header__icon--cart')) {
                e.preventDefault();
                openCartDrawer();
                return;
            }

            // Add To Bag
            const addBtn = e.target.closest('button[data-add-to-cart], .c-product-card__button, .c-product-card__add-to-cart, button.is-add-to-cart, [data-action="add-to-cart"], .o-product-thumbnail__add-btn, [data-product-form-add]');
            if (addBtn) {
                e.preventDefault();
                e.stopPropagation();

                const card = addBtn.closest('.o-product-thumbnail') || addBtn.closest('.c-product-card') || addBtn.closest('[data-product-card]') || addBtn.closest('.shopify-section');
                let title = 'S54 Robusta Cà Phê Rang Mộc Nguyên Chất';
                let price = 4400;
                let img = 'assets/images/s54/robusta_1.jpg';
                let id = Date.now();

                if (card) {
                    const titleEl = card.querySelector('.o-product-thumbnail__title, .c-product-card__title, h2, h3, h4, .o-heading');
                    if (titleEl) title = titleEl.textContent.trim().replace(/\\s+/g, ' ');
                    const priceEl = card.querySelector('.o-product-thumbnail__price, [data-product-money], .c-product-card__price, .price');
                    if (priceEl) {
                        const parsed = parseFloat(priceEl.textContent.replace(/[^0-9.]/g, ''));
                        if (!isNaN(parsed) && parsed > 0) price = Math.round(parsed * 100);
                    }
                    const imgEl = card.querySelector('img');
                    if (imgEl && (imgEl.src || imgEl.dataset.src)) img = imgEl.src || imgEl.dataset.src;
                }

                if (window.S54Cart) {
                    window.S54Cart.addItem({
                        id, variant_id: id, title, price,
                        original_price: price, final_price: price, line_price: price,
                        quantity: 1, image: img, url: 'product-detail.html'
                    });
                }

                const originalText = addBtn.textContent;
                addBtn.textContent = _t('cart_btn_added');
                addBtn.style.backgroundColor = '#2F221A';
                addBtn.style.color = '#FFFFFF';
                setTimeout(() => {
                    addBtn.textContent = originalText;
                    addBtn.style.backgroundColor = '';
                    addBtn.style.color = '';
                }, 1200);

                showToast(_t('cart_added_toast', { title }));
                openCartDrawer();
                return;
            }"""

replacement_new = """        /* ----- Global Click Delegation & Mutex Protection ----- */
        let isCartActionInProgress = false;

        document.addEventListener('click', (e) => {
            // Only process genuine user interaction events
            if (e.isTrusted === false) return;

            // Cart Icon Toggle
            if (e.target.closest('[data-cart-drawer-toggle], .c-header__cart, a[href*="/cart"], .c-icon-cart, [data-cart-trigger], .c-header__icon--cart')) {
                e.preventDefault();
                e.stopPropagation();
                openCartDrawer();
                return;
            }

            // Add To Bag Button
            const addBtn = e.target.closest('button[data-add-to-cart], .c-product-card__button, .c-product-card__add-to-cart, button.is-add-to-cart, [data-action="add-to-cart"], .o-product-thumbnail__add-btn, [data-product-form-add]');
            if (addBtn) {
                e.preventDefault();
                e.stopPropagation();

                if (isCartActionInProgress) return;
                isCartActionInProgress = true;

                const card = addBtn.closest('.o-product-thumbnail') || addBtn.closest('.c-product-card') || addBtn.closest('[data-product-card]') || addBtn.closest('.shopify-section') || addBtn.closest('.c-product-main');
                let title = 'S54 Robusta Cà Phê Rang Mộc Nguyên Chất';
                let price = 4400;
                let img = 'assets/images/s54/robusta_1.jpg';
                let id = Date.now();

                if (card) {
                    const titleEl = card.querySelector('.o-product-thumbnail__title, .c-product-card__title, .c-product-main__title, h1, h2, h3, h4, .o-heading');
                    if (titleEl) title = titleEl.textContent.trim().replace(/\\s+/g, ' ');
                    const priceEl = card.querySelector('.o-product-thumbnail__price, [data-product-money], .c-product-card__price, .price, .c-product-form__pricing');
                    if (priceEl) {
                        const parsed = parseFloat(priceEl.textContent.replace(/[^0-9.]/g, ''));
                        if (!isNaN(parsed) && parsed > 0) price = Math.round(parsed * 100);
                    }
                    const imgEl = card.querySelector('img');
                    if (imgEl && (imgEl.src || imgEl.dataset.src)) img = imgEl.src || imgEl.dataset.src;
                }

                if (window.S54Cart) {
                    window.S54Cart.addItem({
                        id, variant_id: id, title, price,
                        original_price: price, final_price: price, line_price: price,
                        quantity: 1, image: img, url: 'product-detail.html'
                    });
                }

                const originalText = addBtn.textContent;
                addBtn.textContent = _t('cart_btn_added');
                addBtn.style.backgroundColor = '#2F221A';
                addBtn.style.color = '#FFFFFF';
                setTimeout(() => {
                    addBtn.textContent = originalText;
                    addBtn.style.backgroundColor = '';
                    addBtn.style.color = '';
                }, 1000);

                showToast(_t('cart_added_toast', { title }));
                openCartDrawer();

                setTimeout(() => {
                    isCartActionInProgress = false;
                }, 350);
                return;
            }"""

if target_old in mj:
    mj = mj.replace(target_old, replacement_new)
    main_js_path.write_text(mj, encoding='utf-8')
    print("✓ Successfully updated main.js click delegation with mutex lock & isTrusted")
else:
    print("ℹ Note: Checking if target_old matches partially in main.js...")
    # fallback find and replace
    start_idx = mj.find("/* ----- Global Click Delegation")
    end_idx = mj.find("// Close Orbe modal", start_idx)
    if start_idx != -1 and end_idx != -1:
        mj = mj[:start_idx] + replacement_new + "\n\n            " + mj[end_idx:]
        main_js_path.write_text(mj, encoding='utf-8')
        print("✓ Successfully replaced click delegation chunk in main.js")

print("✅ main.js updated successfully!")
