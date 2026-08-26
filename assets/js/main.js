/**
 * Main Interactive Controller for S54 COFFEE Storefront
 * Features: Cart Drawer, Mobile Menu, Scroll-to-Top, Sticky Header, i18n
 */
(function() {
    'use strict';

    const freeShippingThreshold = 599000;

    /* =====================================================================
       i18n Translation Helper with full string dictionary
       ===================================================================== */
    const strings = {
        vi: {
            cart_title: 'Giỏ Hàng Của Bạn',
            cart_checkout: 'TIẾN HÀNH THANH TOÁN',
            cart_subtotal: 'Tạm Tính',
            cart_empty_title: 'Giỏ hàng của bạn đang trống.',
            cart_start_shopping: 'Bắt Đầu Mua Sắm',
            cart_freeship_qualified: '🎉 Bạn đã được MIỄN PHÍ VẬN CHUYỂN!',
            cart_freeship_remaining: 'Thêm {{amount}} nữa để được MIỄN PHÍ VẬN CHUYỂN',
            cart_proceed_checkout: 'Đang chuyển đến cổng thanh toán bảo mật...',
            cart_btn_added: 'ĐÃ THÊM!',
            cart_added_toast: '✓ Đã thêm "{{title}}" vào giỏ hàng',
            home_newsletter_success: '✓ Cảm ơn bạn! Đã đăng ký thành công với {{email}}'
        },
        en: {
            cart_title: 'Your Bag',
            cart_checkout: 'CHECKOUT',
            cart_subtotal: 'Subtotal',
            cart_empty_title: 'Your bag is currently empty.',
            cart_start_shopping: 'Start Shopping',
            cart_freeship_qualified: '🎉 You qualify for FREE Delivery!',
            cart_freeship_remaining: 'Add {{amount}} more for FREE Shipping',
            cart_proceed_checkout: 'Proceeding to Secure Checkout...',
            cart_btn_added: 'ADDED!',
            cart_added_toast: '✓ Added "{{title}}" to your bag',
            home_newsletter_success: '✓ Thank you! Subscribed with {{email}}'
        }
    };

    function _t(key, params) {
        const lang = (window.S54I18n && window.S54I18n.getLanguage) 
            ? window.S54I18n.getLanguage() : 'vi';
        let str = (strings[lang] && strings[lang][key]) || (strings.vi[key]) || key;
        if (params) {
            Object.keys(params).forEach(k => {
                str = str.replace('{{' + k + '}}', params[k]);
            });
        }
        return str;
    }

    function formatPrice(amount) {
        if (typeof amount !== 'number') amount = parseFloat(amount) || 0;
        const lang = (window.S54I18n && window.S54I18n.getLanguage) 
            ? window.S54I18n.getLanguage() : 'vi';
        if (lang === 'vi') {
            const val = amount < 1000 ? amount * 1000 : amount;
            return new Intl.NumberFormat('vi-VN').format(val) + '₫';
        }
        const usdVal = amount > 1000 ? (amount / 25000) : amount;
        return '$' + usdVal.toFixed(2);
    }

    function getCart() {
        if (window.S54Cart && typeof window.S54Cart.getCart === 'function') {
            return window.S54Cart.getCart();
        }
        return window.__s54MockCart || { items: [], total_price: 0, item_count: 0 };
    }

    /* =====================================================================
       Cart Drawer
       ===================================================================== */
    function updateCartUI() {
        const cart = getCart();
        const items = cart.items || [];
        const totalItems = cart.item_count !== undefined ? cart.item_count : items.reduce((sum, item) => sum + item.quantity, 0);
        const subtotal = (cart.total_price !== undefined ? cart.total_price / 100 : items.reduce((sum, item) => sum + ((item.price / 100 || item.price) * item.quantity), 0));

        // Update badge
        document.querySelectorAll('.c-header__cart-count, [data-cart-count], .c-icon-cart__count, .c-cart-count').forEach(badge => {
            badge.textContent = totalItems;
            badge.style.display = totalItems > 0 ? 'inline-flex' : 'none';
        });

        const drawerTitle = document.querySelector('.c-cart-drawer__title');
        if (drawerTitle) drawerTitle.textContent = _t('cart_title');

        const checkoutBtn = document.querySelector('.c-cart-drawer__checkout-btn');
        if (checkoutBtn) checkoutBtn.textContent = _t('cart_checkout');

        const subtotalLabel = document.querySelector('.c-cart-drawer__subtotal span:first-child');
        if (subtotalLabel) subtotalLabel.textContent = _t('cart_subtotal');

        const cartBody = document.querySelector('.c-cart-drawer__body');
        if (cartBody) {
            if (items.length === 0) {
                cartBody.innerHTML = `
                    <div style="text-align: center; padding: 60px 20px; color: #676986;">
                        <p style="font-size: 16px; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600;">${_t('cart_empty_title')}</p>
                        <button onclick="document.querySelector('.c-cart-drawer').classList.remove('is-open'); document.querySelector('.c-cart-drawer__overlay').classList.remove('is-open'); document.body.style.overflow='';" class="o-btn is-primary" style="margin-top: 20px; padding: 12px 24px; background-color: #2F221A; color: #FAF8F5; border: none; border-radius: 4px; cursor: pointer; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: 13px; letter-spacing: 1px;">${_t('cart_start_shopping')}</button>
                    </div>
                `;
            } else {
                cartBody.innerHTML = items.map(item => {
                    const itemPrice = item.price > 1000 ? (item.price / 100) : item.price;
                    return `
                    <div class="c-cart-drawer__item" data-id="${item.id || item.key}">
                        <img src="${item.image || 'assets/images/s54/robusta_1.jpg'}" alt="${item.title}" class="c-cart-drawer__item-img">
                        <div class="c-cart-drawer__item-details">
                            <h4 class="c-cart-drawer__item-title">${item.title}</h4>
                            <div class="c-cart-drawer__item-price">${formatPrice(itemPrice)}</div>
                            <div class="c-cart-drawer__qty-wrap">
                                <button class="c-cart-drawer__qty-btn" data-action="decrease" data-id="${item.id || item.key}">−</button>
                                <span class="c-cart-drawer__qty-val">${item.quantity}</span>
                                <button class="c-cart-drawer__qty-btn" data-action="increase" data-id="${item.id || item.key}">+</button>
                            </div>
                        </div>
                        <button class="c-cart-drawer__item-remove" data-action="remove" data-id="${item.id || item.key}" aria-label="Xóa">✕</button>
                    </div>`;
                }).join('');
            }
        }

        const freeShippingMsg = document.querySelector('.c-cart-drawer__free-shipping-text');
        const progressFill = document.querySelector('.c-cart-drawer__progress-fill');
        if (freeShippingMsg && progressFill) {
            if (subtotal >= freeShippingThreshold) {
                freeShippingMsg.textContent = _t('cart_freeship_qualified');
                progressFill.style.width = '100%';
            } else {
                const diff = freeShippingThreshold - subtotal;
                freeShippingMsg.textContent = _t('cart_freeship_remaining', { amount: formatPrice(diff) });
                progressFill.style.width = `${Math.min(100, (subtotal / freeShippingThreshold) * 100)}%`;
            }
        }

        const subtotalEl = document.querySelector('.c-cart-drawer__subtotal-amount');
        if (subtotalEl) subtotalEl.textContent = formatPrice(subtotal);
    }

    function ensureCartDrawer() {
        let drawer = document.querySelector('.c-cart-drawer');
        let overlay = document.querySelector('.c-cart-drawer__overlay');

        // Remove conflicting static cart drawer from Shopify template
        const staticDrawer = document.querySelector('.c-cart-drawer.is-empty');
        if (staticDrawer && staticDrawer.classList.contains('aaa')) {
            staticDrawer.remove();
        }

        if (!drawer || drawer.classList.contains('aaa')) {
            if (drawer) drawer.remove();
            
            overlay = document.createElement('div');
            overlay.className = 'c-cart-drawer__overlay';
            overlay.addEventListener('click', closeCartDrawer);

            drawer = document.createElement('div');
            drawer.className = 'c-cart-drawer';
            drawer.innerHTML = `
                <div class="c-cart-drawer__header">
                    <h3 class="c-cart-drawer__title">${_t('cart_title')}</h3>
                    <button class="c-cart-drawer__close" aria-label="Close">✕</button>
                </div>
                <div class="c-cart-drawer__free-shipping">
                    <div class="c-cart-drawer__free-shipping-text">${_t('cart_freeship_remaining', { amount: '$25.00' })}</div>
                    <div class="c-cart-drawer__progress-bar">
                        <div class="c-cart-drawer__progress-fill"></div>
                    </div>
                </div>
                <div class="c-cart-drawer__body"></div>
                <div class="c-cart-drawer__footer">
                    <div class="c-cart-drawer__subtotal">
                        <span>${_t('cart_subtotal')}</span>
                        <span class="c-cart-drawer__subtotal-amount">0₫</span>
                    </div>
                    <button class="c-cart-drawer__checkout-btn">${_t('cart_checkout')}</button>
                </div>
            `;

            document.body.appendChild(overlay);
            document.body.appendChild(drawer);

            drawer.querySelector('.c-cart-drawer__close').addEventListener('click', closeCartDrawer);
            drawer.querySelector('.c-cart-drawer__checkout-btn').addEventListener('click', () => {
                alert(_t('cart_proceed_checkout'));
            });

            drawer.addEventListener('click', (e) => {
                const action = e.target.dataset.action;
                const id = e.target.dataset.id;
                if (!action || !id) return;
                const cart = getCart();
                const item = (cart.items || []).find(i => String(i.id) === String(id) || String(i.key) === String(id));
                if (!item) return;
                if (window.S54Cart) {
                    const key = item.key || item.id;
                    if (action === 'increase') window.S54Cart.updateQuantity(key, item.quantity + 1);
                    else if (action === 'decrease') window.S54Cart.updateQuantity(key, item.quantity - 1);
                    else if (action === 'remove') window.S54Cart.updateQuantity(key, 0);
                }
                updateCartUI();
            });
        }
    }

    function openCartDrawer() {
        ensureCartDrawer();
        const drawer = document.querySelector('.c-cart-drawer');
        const overlay = document.querySelector('.c-cart-drawer__overlay');
        if (drawer) drawer.classList.add('is-open');
        if (overlay) overlay.classList.add('is-open');
        document.body.style.overflow = 'hidden';
        updateCartUI();
    }

    function closeCartDrawer() {
        const drawer = document.querySelector('.c-cart-drawer');
        const overlay = document.querySelector('.c-cart-drawer__overlay');
        if (drawer) drawer.classList.remove('is-open');
        if (overlay) overlay.classList.remove('is-open');
        document.body.style.overflow = '';
    }

    function showToast(message) {
        let toast = document.querySelector('.c-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.className = 'c-toast';
            document.body.appendChild(toast);
        }
        toast.textContent = message;
        toast.classList.add('is-active');
        setTimeout(() => toast.classList.remove('is-active'), 2500);
    }

    window.openCartDrawer = openCartDrawer;
    window.closeCartDrawer = closeCartDrawer;
    window.showToast = showToast;

    window.addEventListener('cart:updated', updateCartUI);
    window.addEventListener('language:changed', updateCartUI);

    /* =====================================================================
       DOM Ready
       ===================================================================== */
    document.addEventListener('DOMContentLoaded', () => {
        console.log('S54 COFFEE Storefront initialized.');
        ensureCartDrawer();
        updateCartUI();

        // Lazy image fallback
        document.querySelectorAll('img[data-src]').forEach(img => {
            if (img.dataset.src && (!img.src || img.src.includes('data:image'))) img.src = img.dataset.src;
        });

        /* ----- Mobile Menu Toggle ----- */
        const menuToggle = document.querySelector('[data-menu-toggle]');
        const mainMenu = document.querySelector('[data-main-menu]');
        const menuClose = document.querySelector('[data-menu-close]');
        const menuBack = document.querySelector('[data-submenu-back]');

        if (menuToggle && mainMenu) {
            menuToggle.addEventListener('click', (e) => {
                e.preventDefault();
                mainMenu.classList.toggle('is-open');
                document.body.classList.toggle('menu-is-open');
            });
        }
        if (menuClose) {
            menuClose.addEventListener('click', () => {
                if (mainMenu) mainMenu.classList.remove('is-open');
                document.body.classList.remove('menu-is-open');
            });
        }
        if (menuBack) {
            menuBack.addEventListener('click', () => {
                const openSubmenu = mainMenu && mainMenu.querySelector('.c-main-menu__submenu.is-open');
                if (openSubmenu) openSubmenu.classList.remove('is-open');
            });
        }

        /* ----- Sticky Header Shrink ----- */
        const header = document.querySelector('.c-header, [data-header]');
        let lastScroll = 0;
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            if (header) {
                header.classList.toggle('is-scrolled', scrollY > 50);
            }
            lastScroll = scrollY;
        }, { passive: true });

        /* ----- Scroll-to-Top Button ----- */
        const scrollTopBtn = document.getElementById('scrollTopBtn');
        if (scrollTopBtn) {
            window.addEventListener('scroll', () => {
                scrollTopBtn.classList.toggle('is-visible', window.scrollY > 400);
            }, { passive: true });
            scrollTopBtn.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        /* ----- Global Click Delegation & Mutex Protection ----- */
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
                    if (titleEl) title = titleEl.textContent.trim().replace(/\s+/g, ' ');
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
            }

            // Close Orbe modal
            if (e.target.closest('#md-btn__form__onSubmit, .md-app-modal__close-button, .md-app-modal-overlay')) {
                e.preventDefault();
                e.stopPropagation();
                document.querySelectorAll('.md-app-modal, .md-app-modal-overlay, #md-app-modal').forEach(el => el.remove());
                document.body.style.overflow = '';
                return;
            }
        });

        /* ----- Carousel Navigation ----- */
        document.querySelectorAll('[data-carousel]').forEach(carousel => {
            const container = carousel.closest('.c-product-carousel, .c-article-feed, .c-featured-collections, .shopify-section') || carousel.parentElement;
            const nextBtn = container.querySelector('[data-carousel-next], .c-product-carousel__arrow--next, .c-collection-carousel__control--next, .c-article-feed__control--next');
            const prevBtn = container.querySelector('[data-carousel-prev], .c-product-carousel__arrow--prev, .c-collection-carousel__control--prev, .c-article-feed__control--prev');
            const scrollTarget = carousel;
            const scrollAmount = Math.min(340, window.innerWidth * 0.8);

            if (nextBtn) nextBtn.addEventListener('click', (e) => { e.preventDefault(); scrollTarget.scrollBy({ left: scrollAmount, behavior: 'smooth' }); });
            if (prevBtn) prevBtn.addEventListener('click', (e) => { e.preventDefault(); scrollTarget.scrollBy({ left: -scrollAmount, behavior: 'smooth' }); });
        });

        /* ----- Video Controller ----- */
        document.querySelectorAll('[data-play], .c-featured-video__button-play').forEach(btn => {
            btn.addEventListener('click', () => {
                const container = btn.closest('.c-featured-video__media-container') || btn.parentElement;
                const video = container.querySelector('video');
                if (video) {
                    if (video.paused) { video.play(); btn.style.opacity = '0'; }
                    else { video.pause(); btn.style.opacity = '1'; }
                }
            });
        });

        /* ----- Newsletter Form ----- */
        document.querySelectorAll('form[action*="contact"], .c-newsletter-form').forEach(form => {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const input = form.querySelector('input[type="email"]');
                if (input && input.value) {
                    showToast(_t('home_newsletter_success', { email: input.value }));
                    input.value = '';
                }
            });
        });

        // Init
        ensureCartDrawer();
        updateCartUI();
    });
})();
