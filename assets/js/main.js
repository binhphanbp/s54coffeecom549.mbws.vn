/**
 * Main Interactive Controller for Vittoria Coffee Clone
 * Fully integrated with window.VittoriaCart
 */
(function() {
    'use strict';

    const freeShippingThreshold = 69.00;

    function formatPrice(amount) {
        if (typeof amount !== 'number') {
            amount = parseFloat(amount) || 0;
        }
        return '$' + amount.toFixed(2);
    }

    function getCart() {
        if (window.VittoriaCart && typeof window.VittoriaCart.getCart === 'function') {
            return window.VittoriaCart.getCart();
        }
        return window.__vittoriaMockCart || { items: [], total_price: 0, item_count: 0 };
    }

    function updateCartUI() {
        const cart = getCart();
        const items = cart.items || [];
        const totalItems = cart.item_count !== undefined ? cart.item_count : items.reduce((sum, item) => sum + item.quantity, 0);
        const subtotal = (cart.total_price !== undefined ? cart.total_price / 100 : items.reduce((sum, item) => sum + ((item.price / 100 || item.price) * item.quantity), 0));

        // Update badge in header
        document.querySelectorAll('.c-header__cart-count, [data-cart-count], .c-icon-cart__count, .c-cart-count').forEach(badge => {
            badge.textContent = totalItems;
            badge.style.display = totalItems > 0 ? 'inline-flex' : 'none';
        });

        // Update items inside drawer
        const cartBody = document.querySelector('.c-cart-drawer__body');
        if (cartBody) {
            if (items.length === 0) {
                cartBody.innerHTML = `
                    <div style="text-align: center; padding: 60px 20px; color: #676986;">
                        <p style="font-size: 16px; font-family: 'neutraface-demi', sans-serif;">Your bag is currently empty.</p>
                        <button onclick="document.querySelector('.c-cart-drawer').classList.remove('is-open'); document.querySelector('.c-cart-drawer__overlay').classList.remove('is-open');" class="o-btn is-primary" style="margin-top: 20px; padding: 12px 24px; background-color: #2F221A; color: #FAF8F5;">Start Shopping</button>
                    </div>
                `;
            } else {
                cartBody.innerHTML = items.map(item => {
                    const itemPrice = item.price > 1000 ? (item.price / 100) : item.price;
                    return `
                    <div class="c-cart-drawer__item" data-id="${item.id || item.key}" style="display: flex; gap: 16px; padding: 16px 0; border-bottom: 1px solid #ECE7E1; align-items: center;">
                        <img src="${item.image || 'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png'}" alt="${item.title}" class="c-cart-drawer__item-img" style="width: 70px; height: 70px; object-fit: contain; background: #FAF8F5; border-radius: 4px; padding: 4px;">
                        <div class="c-cart-drawer__item-info" style="flex: 1;">
                            <h4 class="c-cart-drawer__item-title" style="margin: 0 0 6px; font-size: 14px; font-family: 'neutraface-demi', sans-serif; color: #2F221A;">${item.title}</h4>
                            <div class="c-cart-drawer__item-price" style="font-size: 13px; color: #676986; margin-bottom: 8px;">${formatPrice(itemPrice)}</div>
                            <div class="c-cart-drawer__qty-control" style="display: inline-flex; align-items: center; border: 1px solid #D9D2C9; border-radius: 20px; padding: 2px 8px; background: #FFF;">
                                <button class="c-cart-drawer__qty-btn" data-action="decrease" data-id="${item.id || item.key}" style="background: none; border: none; font-size: 16px; cursor: pointer; padding: 2px 8px; color: #2F221A;">-</button>
                                <span class="c-cart-drawer__qty-num" style="padding: 0 8px; font-size: 13px; font-weight: 600;">${item.quantity}</span>
                                <button class="c-cart-drawer__qty-btn" data-action="increase" data-id="${item.id || item.key}" style="background: none; border: none; font-size: 16px; cursor: pointer; padding: 2px 8px; color: #2F221A;">+</button>
                            </div>
                        </div>
                        <button style="background: none; border: none; color: #999; font-size: 18px; cursor: pointer; align-self: flex-start; padding: 4px;" data-action="remove" data-id="${item.id || item.key}" title="Remove item">✕</button>
                    </div>
                `;
                }).join('');
            }
        }

        // Update free shipping bar
        const freeShippingMsg = document.querySelector('.c-cart-drawer__free-shipping-text');
        const progressFill = document.querySelector('.c-cart-drawer__progress-fill');
        if (freeShippingMsg && progressFill) {
            if (subtotal >= freeShippingThreshold) {
                freeShippingMsg.textContent = '🎉 You qualify for FREE Delivery!';
                progressFill.style.width = '100%';
            } else {
                const diff = freeShippingThreshold - subtotal;
                freeShippingMsg.textContent = `You're ${formatPrice(diff)} away from FREE shipping!`;
                const pct = Math.min(100, (subtotal / freeShippingThreshold) * 100);
                progressFill.style.width = `${pct}%`;
            }
        }

        // Update subtotal
        const subtotalEl = document.querySelector('.c-cart-drawer__subtotal-amount');
        if (subtotalEl) {
            subtotalEl.textContent = formatPrice(subtotal);
        }
    }

    function ensureCartDrawer() {
        let drawer = document.querySelector('.c-cart-drawer');
        let overlay = document.querySelector('.c-cart-drawer__overlay');

        if (!drawer) {
            overlay = document.createElement('div');
            overlay.className = 'c-cart-drawer__overlay';
            overlay.addEventListener('click', closeCartDrawer);

            drawer = document.createElement('div');
            drawer.className = 'c-cart-drawer';
            drawer.innerHTML = `
                <div class="c-cart-drawer__header">
                    <h3 class="c-cart-drawer__title">Your Bag</h3>
                    <button class="c-cart-drawer__close" aria-label="Close">✕</button>
                </div>
                <div class="c-cart-drawer__free-shipping">
                    <div class="c-cart-drawer__free-shipping-text">You're $25.00 away from FREE shipping!</div>
                    <div class="c-cart-drawer__progress-bar">
                        <div class="c-cart-drawer__progress-fill"></div>
                    </div>
                </div>
                <div class="c-cart-drawer__body"></div>
                <div class="c-cart-drawer__footer">
                    <div class="c-cart-drawer__subtotal">
                        <span>Subtotal</span>
                        <span class="c-cart-drawer__subtotal-amount">$44.00</span>
                    </div>
                    <button class="c-cart-drawer__checkout-btn" onclick="alert('Proceeding to Secure Checkout...');">CHECKOUT</button>
                </div>
            `;

            document.body.appendChild(overlay);
            document.body.appendChild(drawer);

            drawer.querySelector('.c-cart-drawer__close').addEventListener('click', closeCartDrawer);

            // Cart item controls (+, -, remove)
            drawer.addEventListener('click', (e) => {
                const action = e.target.dataset.action;
                const id = e.target.dataset.id;
                if (!action || !id) return;

                const cart = getCart();
                const item = (cart.items || []).find(i => String(i.id) === String(id) || String(i.key) === String(id));
                if (!item) return;

                if (action === 'increase') {
                    if (window.VittoriaCart) {
                        window.VittoriaCart.updateQuantity(item.key || item.id, item.quantity + 1);
                    }
                } else if (action === 'decrease') {
                    if (window.VittoriaCart) {
                        window.VittoriaCart.updateQuantity(item.key || item.id, item.quantity - 1);
                    }
                } else if (action === 'remove') {
                    if (window.VittoriaCart) {
                        window.VittoriaCart.updateQuantity(item.key || item.id, 0);
                    }
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
        setTimeout(() => {
            toast.classList.remove('is-active');
        }, 2500);
    }

    // Expose drawer methods globally
    window.openCartDrawer = openCartDrawer;
    window.closeCartDrawer = closeCartDrawer;
    window.showToast = showToast;

    // Listen for cart state update events
    window.addEventListener('cart:updated', () => {
        updateCartUI();
    });

    document.addEventListener('DOMContentLoaded', () => {
        console.log('Vittoria Coffee Clone initialized successfully.');

        // Lazy image fallback
        document.querySelectorAll('img[data-src]').forEach(img => {
            if (img.dataset.src && (!img.src || img.src.includes('data:image'))) {
                img.src = img.dataset.src;
            }
        });

        // Global Event Delegation for clicks
        document.addEventListener('click', (e) => {
            // 1. Cart Icon Click
            if (e.target.closest('[data-cart-drawer-toggle], .c-header__cart, a[href*="/cart"], .c-icon-cart, [data-cart-trigger], .c-header__icon--cart')) {
                e.preventDefault();
                openCartDrawer();
                return;
            }

            // 2. Add To Bag Button Click
            const addBtn = e.target.closest('button[data-add-to-cart], .c-product-card__button, .c-product-card__add-to-cart, button.is-add-to-cart, [data-action="add-to-cart"], .o-product-thumbnail__add-btn, [data-product-form-add]');
            if (addBtn) {
                e.preventDefault();
                e.stopPropagation();

                const card = addBtn.closest('.o-product-thumbnail') || addBtn.closest('.c-product-card') || addBtn.closest('[data-product-card]') || addBtn.closest('.c-product-carousel__item') || addBtn.closest('.shopify-section');

                let title = 'Cinque Stelle Special Bar Beans';
                let price = 4400; // in cents
                let img = 'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png';
                let id = Date.now();

                if (card) {
                    const titleEl = card.querySelector('.o-product-thumbnail__title, .c-product-card__title, h2, h3, h4, .o-heading');
                    if (titleEl) title = titleEl.textContent.trim().replace(/\s+/g, ' ');

                    const priceEl = card.querySelector('.o-product-thumbnail__price, [data-product-money], .c-product-card__price, .price');
                    if (priceEl) {
                        const parsed = parseFloat(priceEl.textContent.replace(/[^0-9.]/g, ''));
                        if (!isNaN(parsed) && parsed > 0) price = Math.round(parsed * 100);
                    }

                    const imgEl = card.querySelector('img');
                    if (imgEl && (imgEl.src || imgEl.dataset.src)) {
                        img = imgEl.src || imgEl.dataset.src;
                    }
                }

                if (window.VittoriaCart) {
                    window.VittoriaCart.addItem({
                        id: id,
                        variant_id: id,
                        title: title,
                        price: price,
                        original_price: price,
                        final_price: price,
                        line_price: price,
                        quantity: 1,
                        image: img,
                        url: 'product-detail.html'
                    });
                }

                const originalText = addBtn.textContent;
                addBtn.textContent = 'ADDED!';
                addBtn.style.backgroundColor = '#2F221A';
                addBtn.style.color = '#FFFFFF';
                setTimeout(() => {
                    addBtn.textContent = originalText;
                    addBtn.style.backgroundColor = '';
                    addBtn.style.color = '';
                }, 1200);

                showToast(`✓ Added "${title}" to your Bag`);
                openCartDrawer();
                return;
            }

            // 3. Close Geolocation Modal if still present
            if (e.target.closest('#md-btn__form__onSubmit, .md-app-modal__close-button, .md-app-modal-overlay')) {
                e.preventDefault();
                e.stopPropagation();
                document.querySelectorAll('.md-app-modal, .md-app-modal-overlay, #md-app-modal').forEach(el => el.remove());
                document.body.style.overflow = '';
                return;
            }
        });

        // Product Carousel Arrows
        document.querySelectorAll('.c-collection-carousel, .c-product-carousel, [data-carousel], .c-product-carousel__slider').forEach(carousel => {
            const container = carousel.parentElement || carousel;
            const nextBtn = container.querySelector('[data-carousel-next], .c-product-carousel__arrow--next, .c-collection-carousel__control--next');
            const prevBtn = container.querySelector('[data-carousel-prev], .c-product-carousel__arrow--prev, .c-collection-carousel__control--prev');

            const scrollTarget = carousel.querySelector('.c-collection-carousel__products-list, .c-product-carousel__slider') || carousel;

            if (nextBtn) {
                nextBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    scrollTarget.scrollBy({ left: 340, behavior: 'smooth' });
                });
            }
            if (prevBtn) {
                prevBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    scrollTarget.scrollBy({ left: -340, behavior: 'smooth' });
                });
            }
        });

        // Video Controller
        document.querySelectorAll('[data-play], .c-featured-video__button-play').forEach(btn => {
            btn.addEventListener('click', () => {
                const container = btn.closest('.c-featured-video__media-container') || btn.parentElement;
                const video = container.querySelector('video');
                if (video) {
                    if (video.paused) {
                        video.play();
                        btn.style.opacity = '0';
                    } else {
                        video.pause();
                        btn.style.opacity = '1';
                    }
                }
            });
        });

        // Newsletter form
        document.querySelectorAll('form[action*="contact"], .c-newsletter-form').forEach(form => {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const input = form.querySelector('input[type="email"]');
                if (input && input.value) {
                    showToast(`Thank you! 10% discount code sent to ${input.value}`);
                    input.value = '';
                }
            });
        });

        // Initialize Cart Drawer markup & UI
        ensureCartDrawer();
        updateCartUI();
    });
})();
