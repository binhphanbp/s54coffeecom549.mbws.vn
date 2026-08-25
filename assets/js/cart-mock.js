/**
 * S54 COFFEE - Cart Mock & Storefront State Manager
 * Provides offline cart simulation, sessionStorage persistence, and Fetch/XHR interception for Shopify Cart APIs.
 */
(function () {
    'use strict';

    const STORAGE_KEY = 's54_storefront_cart';
    const FREESHIP_THRESHOLD = 599000; // 599.000 VND

    const DEFAULT_CART = {
        token: 'd7480a82b992167389148d53efd67db9',
        note: null,
        attributes: {},
        original_total_price: 4400,
        total_price: 4400,
        total_discount: 0,
        total_weight: 1000.0,
        item_count: 1,
        items: [
            {
                id: 401234567890,
                properties: { _bundle_item: false, _is_subscription: false },
                quantity: 1,
                variant_id: 401234567890,
                key: '401234567890:1',
                title: 'Cinque Stelle Oro - 1kg Beans',
                price: 4400,
                original_price: 4400,
                discounted_price: 4400,
                line_price: 4400,
                original_line_price: 4400,
                total_discount: 0,
                discounts: [],
                sku: 'VIT-ORO-1KG',
                grams: 1000,
                vendor: 'S54 COFFEE',
                taxable: false,
                product_id: 6718616502447,
                product_has_only_default_variant: false,
                gift_card: false,
                final_price: 4400,
                final_line_price: 4400,
                url: 'product-detail.html',
                featured_image: {
                    aspect_ratio: 1.0,
                    alt: 'Cinque Stelle Oro Beans',
                    height: 1000,
                    url: 'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png',
                    width: 1000
                },
                image: 'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png',
                handle: 'cinque-stelle-beans-1kg',
                requires_shipping: true,
                product_type: 'Beans',
                product_title: 'Cinque Stelle',
                product_description: "Australia's favourite premium blend",
                variant_title: '1kg Beans',
                variant_options: ['1kg Beans'],
                options_with_values: [{ name: 'Size', value: '1kg Beans' }],
                line_level_discount_allocations: []
            }
        ],
        requires_shipping: true,
        currency: 'VND',
        items_subtotal_price: 4400,
        cart_level_discount_applications: []
    };

    function loadCart() {
        try {
            const saved = sessionStorage.getItem(STORAGE_KEY);
            if (saved) {
                return JSON.parse(saved);
            }
        } catch (e) {
            console.warn('[CartMock] Failed to read sessionStorage', e);
        }
        return JSON.parse(JSON.stringify(DEFAULT_CART));
    }

    function recalculateTotals(cart) {
        let count = 0;
        let total = 0;
        let weight = 0;

        cart.items.forEach(item => {
            count += item.quantity;
            item.line_price = item.price * item.quantity;
            item.original_line_price = item.original_price * item.quantity;
            item.final_line_price = item.final_price * item.quantity;
            total += item.line_price;
            weight += (item.grams || 0) * item.quantity;
        });

        cart.item_count = count;
        cart.total_price = total;
        cart.original_total_price = total;
        cart.items_subtotal_price = total;
        cart.total_weight = weight;
    }

    function saveCart(cart) {
        recalculateTotals(cart);
        try {
            sessionStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
        } catch (e) {
            console.warn('[CartMock] Failed to save sessionStorage', e);
        }
        window.__s54MockCart = cart;
        window.dispatchEvent(new CustomEvent('cart:updated', { detail: cart }));
        return cart;
    }

    let cartState = loadCart();
    window.__s54MockCart = cartState;

    // Cart public API
    window.S54Cart = {
        getCart: function () {
            return JSON.parse(JSON.stringify(cartState));
        },
        addItem: function (item) {
            const existing = cartState.items.find(i => i.id === item.id || (item.variant_id && i.variant_id === item.variant_id));
            if (existing) {
                existing.quantity += (item.quantity || 1);
            } else {
                const newItem = Object.assign({
                    id: Date.now(),
                    variant_id: Date.now(),
                    key: Date.now() + ':1',
                    title: 'S54 Special Blend',
                    price: 3500,
                    original_price: 3500,
                    final_price: 3500,
                    line_price: 3500,
                    quantity: 1,
                    image: 'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png',
                    url: 'product-detail.html'
                }, item);
                cartState.items.push(newItem);
            }
            return saveCart(cartState);
        },
        updateQuantity: function (keyOrId, quantity) {
            if (quantity <= 0) {
                cartState.items = cartState.items.filter(i => i.key !== keyOrId && i.id !== keyOrId && i.variant_id !== keyOrId);
            } else {
                const item = cartState.items.find(i => i.key === keyOrId || i.id === keyOrId || i.variant_id === keyOrId);
                if (item) {
                    item.quantity = quantity;
                }
            }
            return saveCart(cartState);
        },
        clear: function () {
            cartState.items = [];
            return saveCart(cartState);
        },
        reset: function () {
            cartState = JSON.parse(JSON.stringify(DEFAULT_CART));
            return saveCart(cartState);
        }
    };

    // Intercept fetch requests for Shopify Cart API
    const origFetch = window.fetch;
    window.fetch = function (url, opts) {
        const u = (typeof url === 'string') ? url : (url && url.url) || '';

        if (u.indexOf('/cart/add') !== -1 || u.indexOf('cart/add.js') !== -1) {
            let body = null;
            if (opts && opts.body) {
                try {
                    body = typeof opts.body === 'string' ? JSON.parse(opts.body) : opts.body;
                } catch (e) {
                    body = {};
                }
            }
            const quantity = (body && body.quantity) ? parseInt(body.quantity, 10) : 1;
            const updated = window.S54Cart.addItem({ quantity: quantity });
            return Promise.resolve(new Response(JSON.stringify(updated.items[updated.items.length - 1] || {}), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }));
        }

        if (u.indexOf('/cart/change') !== -1 || u.indexOf('cart/change.js') !== -1 || u.indexOf('/cart/update') !== -1) {
            let body = null;
            if (opts && opts.body) {
                try {
                    body = typeof opts.body === 'string' ? JSON.parse(opts.body) : opts.body;
                } catch (e) {
                    body = {};
                }
            }
            if (body && (body.id || body.line || body.key) !== undefined) {
                const target = body.id || body.key || body.line;
                const qty = parseInt(body.quantity, 10);
                window.S54Cart.updateQuantity(target, isNaN(qty) ? 1 : qty);
            }
            return Promise.resolve(new Response(JSON.stringify(window.S54Cart.getCart()), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }));
        }

        if (u.indexOf('/cart/clear') !== -1 || u.indexOf('cart/clear.js') !== -1) {
            window.S54Cart.clear();
            return Promise.resolve(new Response(JSON.stringify(window.S54Cart.getCart()), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }));
        }

        if (u.indexOf('/cart') !== -1 || u.indexOf('cart.js') !== -1 || u.indexOf('cart.json') !== -1) {
            return Promise.resolve(new Response(JSON.stringify(window.S54Cart.getCart()), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }));
        }

        if (u.indexOf('/localization') !== -1) {
            return Promise.resolve(new Response(JSON.stringify({ success: true }), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }));
        }

        return origFetch ? origFetch.apply(this, arguments) : Promise.resolve(new Response('{}', { status: 200 }));
    };
})();
