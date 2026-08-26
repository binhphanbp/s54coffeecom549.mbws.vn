#!/usr/bin/env python3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

mj_path = BASE_DIR / 'assets/js/main.js'
mj = mj_path.read_text(encoding='utf-8')

start_tag = "/* ----- Global Click Delegation"
end_tag = "// Close Orbe modal"

start_idx = mj.find(start_tag)
end_idx = mj.find(end_tag)

if start_idx != -1 and end_idx != -1:
    click_handler_new = """/* ----- Global Click Delegation & Smooth Cart Integration ----- */
        let isCartBusy = false;

        document.addEventListener('click', (e) => {
            // Cart Icon Toggle
            const cartToggle = e.target.closest('[data-cart-drawer-toggle], .c-header__cart, a[href*="/cart"], .c-icon-cart, [data-cart-trigger], .c-header__icon--cart, .is-cart');
            if (cartToggle) {
                e.preventDefault();
                e.stopPropagation();
                e.stopImmediatePropagation();
                openCartDrawer();
                return;
            }

            // Add To Bag Button (Cards, Carousels, Product Forms)
            const addBtn = e.target.closest('button[data-add-to-cart], .c-product-card__button, .c-product-card__add-to-cart, button.is-add-to-cart, [data-action="add-to-cart"], .o-product-thumbnail__add-btn, [data-product-form-add], button[name="add"], .c-product-form__add-btn');
            if (addBtn) {
                e.preventDefault();
                e.stopPropagation();
                e.stopImmediatePropagation();

                if (isCartBusy) return;
                isCartBusy = true;

                const card = addBtn.closest('.o-product-thumbnail') || addBtn.closest('.c-product-card') || addBtn.closest('[data-product-card]') || addBtn.closest('.c-product-main') || addBtn.closest('.shopify-section') || document;
                
                let title = 'S54 Robusta Cà Phê Rang Mộc Nguyên Chất';
                let price = 4400;
                let img = 'assets/images/s54/robusta_1.jpg';
                let id = Date.now();

                const titleEl = card.querySelector('.o-product-thumbnail__title, .c-product-card__title, .c-product-main__title, h1, h2, h3, h4, .o-heading');
                if (titleEl && titleEl.textContent) {
                    title = titleEl.textContent.trim().replace(/\\s+/g, ' ');
                }

                const priceEl = card.querySelector('.o-product-thumbnail__price, [data-product-money], .c-product-card__price, .price, .c-product-form__pricing');
                if (priceEl && priceEl.textContent) {
                    const parsed = parseFloat(priceEl.textContent.replace(/[^0-9.]/g, ''));
                    if (!isNaN(parsed) && parsed > 0) price = Math.round(parsed * 100);
                }

                const imgEl = card.querySelector('img:not(.c-header__logo img)');
                if (imgEl && (imgEl.src || imgEl.dataset.src)) {
                    img = imgEl.src || imgEl.dataset.src;
                }

                if (window.S54Cart) {
                    window.S54Cart.addItem({
                        id,
                        variant_id: id,
                        title,
                        price,
                        quantity: 1,
                        image: img,
                        url: 'product-detail.html'
                    });
                }

                // Button visual feedback
                const originalText = addBtn.innerHTML;
                addBtn.innerHTML = '✓ ' + _t('cart_btn_added');
                addBtn.style.backgroundColor = '#D68E1D';
                addBtn.style.color = '#FFFFFF';
                addBtn.style.borderColor = '#D68E1D';

                setTimeout(() => {
                    addBtn.innerHTML = originalText;
                    addBtn.style.backgroundColor = '';
                    addBtn.style.color = '';
                    addBtn.style.borderColor = '';
                    isCartBusy = false;
                }, 800);

                showToast(_t('cart_added_toast', { title }));
                openCartDrawer();
                return;
            }

            """
    mj = mj[:start_idx] + click_handler_new + mj[end_idx:]
    mj_path.write_text(mj, encoding='utf-8')
    print("✓ Successfully replaced click delegation in main.js")
else:
    print("❌ Could not find start or end tag in main.js")

print("✅ main.js updated successfully!")
