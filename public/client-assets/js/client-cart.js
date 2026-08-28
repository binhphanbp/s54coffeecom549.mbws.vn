/**
 * S54 Coffee Client Cart Engine
 * Seamlessly connects Cart Drawer & Quick Add buttons to /api/public/cart endpoints.
 */
(function() {
    'use strict';

    var CART_STORAGE_KEY = 's54_cart_items_v2';

    function getLocalCart() {
        try {
            return JSON.parse(localStorage.getItem(CART_STORAGE_KEY)) || [];
        } catch(e) {
            return [];
        }
    }

    function saveLocalCart(items) {
        localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(items));
        updateCartUI();
    }

    function updateCartUI() {
        var items = getLocalCart();
        var totalQty = 0;
        var subtotal = 0;

        items.forEach(function(it) {
            totalQty += (it.quantity || 1);
            subtotal += (it.price || 0) * (it.quantity || 1);
        });

        // Update badge
        var badge = document.getElementById('s54-cart-badge');
        if (badge) badge.textContent = totalQty;

        var drawerCount = document.getElementById('s54-drawer-count');
        if (drawerCount) drawerCount.textContent = totalQty;

        var subtotalEl = document.getElementById('s54-drawer-subtotal');
        if (subtotalEl) {
            subtotalEl.textContent = new Intl.NumberFormat('vi-VN').format(subtotal) + '₫';
        }

        // Render drawer items
        var emptyState = document.getElementById('s54-cart-empty-state');
        var itemsList = document.getElementById('s54-cart-items-list');

        if (!itemsList) return;

        if (items.length === 0) {
            if (emptyState) emptyState.style.display = 'block';
            itemsList.style.display = 'none';
            itemsList.innerHTML = '';
        } else {
            if (emptyState) emptyState.style.display = 'none';
            itemsList.style.display = 'block';
            
            var html = '';
            items.forEach(function(it, idx) {
                var itemTotal = (it.price || 0) * (it.quantity || 1);
                html += `
                    <div style="display: flex; gap: 14px; padding: 14px 0; border-bottom: 1px solid #EBE7E1; align-items: center;">
                        <img src="${it.image || 'client-assets/images/s54/robusta_1.jpg'}" style="width: 60px; height: 60px; object-fit: contain; background: #FFFFFF; border-radius: 4px; padding: 4px; border: 1px solid #EBE7E1;">
                        <div style="flex: 1;">
                            <h4 style="margin: 0 0 4px 0; font-size: 13.5px; font-weight: 700; color: #2F221A;">${it.name}</h4>
                            <p style="margin: 0 0 6px 0; font-size: 13px; font-weight: 700; color: #D68E1D;">${new Intl.NumberFormat('vi-VN').format(it.price)}₫</p>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <button type="button" class="s54-cart-qty-btn" data-action="dec" data-index="${idx}" style="width: 24px; height: 24px; border: 1px solid #D0C8C0; background: #FFFFFF; border-radius: 3px; cursor: pointer;">-</button>
                                <span style="font-size: 13px; font-weight: 700; min-width: 16px; text-align: center;">${it.quantity}</span>
                                <button type="button" class="s54-cart-qty-btn" data-action="inc" data-index="${idx}" style="width: 24px; height: 24px; border: 1px solid #D0C8C0; background: #FFFFFF; border-radius: 3px; cursor: pointer;">+</button>
                                <button type="button" class="s54-cart-remove-btn" data-index="${idx}" style="background: none; border: none; color: #A08D80; font-size: 12px; cursor: pointer; margin-left: 8px;">Xóa</button>
                            </div>
                        </div>
                    </div>
                `;
            });
            itemsList.innerHTML = html;
        }
    }

    function openDrawer() {
        var drawer = document.getElementById('s54-cart-drawer');
        var overlay = document.getElementById('s54-cart-overlay');
        if (drawer) drawer.style.right = '0';
        if (overlay) overlay.style.display = 'block';
    }

    function closeDrawer() {
        var drawer = document.getElementById('s54-cart-drawer');
        var overlay = document.getElementById('s54-cart-overlay');
        if (drawer) drawer.style.right = '-450px';
        if (overlay) overlay.style.display = 'none';
    }

    function addToCart(product) {
        var items = getLocalCart();
        var existing = items.find(function(it) {
            return it.id === product.id && it.variantId === product.variantId;
        });

        if (existing) {
            existing.quantity += (product.quantity || 1);
        } else {
            items.push({
                id: product.id,
                variantId: product.variantId,
                name: product.name,
                price: product.price,
                image: product.image,
                quantity: product.quantity || 1
            });
        }

        saveLocalCart(items);
        openDrawer();
    }

    // Attach DOM Events
    document.addEventListener('DOMContentLoaded', function() {
        updateCartUI();

        // Cart trigger button
        var trigger = document.getElementById('s54-cart-trigger');
        if (trigger) {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                openDrawer();
            });
        }

        // Close button & overlay
        var closeBtn = document.getElementById('s54-cart-close');
        var overlay = document.getElementById('s54-cart-overlay');
        if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
        if (overlay) overlay.addEventListener('click', closeDrawer);

        // Quick add buttons
        document.addEventListener('click', function(e) {
            var btn = e.target.closest('.s54-quick-add-btn');
            if (btn) {
                e.preventDefault();
                addToCart({
                    id: btn.dataset.productId,
                    variantId: btn.dataset.variantId || btn.dataset.productId,
                    name: btn.dataset.productName,
                    price: parseFloat(btn.dataset.productPrice) || 145000,
                    image: btn.dataset.productImage,
                    quantity: 1
                });
            }

            // Detail add button
            var detailBtn = e.target.closest('#s54-detail-add-btn');
            if (detailBtn) {
                e.preventDefault();
                var qtyInput = document.getElementById('s54-qty-input');
                var qty = qtyInput ? parseInt(qtyInput.value) || 1 : 1;
                addToCart({
                    id: detailBtn.dataset.productId,
                    variantId: detailBtn.dataset.variantId || detailBtn.dataset.productId,
                    name: detailBtn.dataset.productName,
                    price: parseFloat(detailBtn.dataset.productPrice) || 145000,
                    image: detailBtn.dataset.productImage,
                    quantity: qty
                });
            }

            // Qty buttons in drawer
            var qtyBtn = e.target.closest('.s54-cart-qty-btn');
            if (qtyBtn) {
                var idx = parseInt(qtyBtn.dataset.index);
                var action = qtyBtn.dataset.action;
                var items = getLocalCart();
                if (items[idx]) {
                    if (action === 'inc') items[idx].quantity += 1;
                    else if (action === 'dec') {
                        items[idx].quantity -= 1;
                        if (items[idx].quantity <= 0) items.splice(idx, 1);
                    }
                    saveLocalCart(items);
                }
            }

            // Remove button in drawer
            var removeBtn = e.target.closest('.s54-cart-remove-btn');
            if (removeBtn) {
                var idx = parseInt(removeBtn.dataset.index);
                var items = getLocalCart();
                items.splice(idx, 1);
                saveLocalCart(items);
            }

            // Detail quantity plus/minus
            if (e.target.closest('#s54-qty-plus')) {
                var qi = document.getElementById('s54-qty-input');
                if (qi) qi.value = parseInt(qi.value || 1) + 1;
            }
            if (e.target.closest('#s54-qty-minus')) {
                var qi = document.getElementById('s54-qty-input');
                if (qi && parseInt(qi.value) > 1) qi.value = parseInt(qi.value) - 1;
            }

            // Variant selector buttons on product detail
            var varBtn = e.target.closest('.s54-variant-btn');
            if (varBtn) {
                document.querySelectorAll('.s54-variant-btn').forEach(function(b) {
                    b.classList.remove('is-selected');
                    b.style.background = '#FFFFFF';
                    b.style.color = '#2F221A';
                    b.style.borderColor = '#D0C8C0';
                });
                varBtn.classList.add('is-selected');
                varBtn.style.background = '#2F221A';
                varBtn.style.color = '#FAF6F1';
                varBtn.style.borderColor = '#2F221A';

                var priceDisplay = document.getElementById('s54-product-price-display');
                if (priceDisplay && varBtn.dataset.variantPriceFormatted) {
                    priceDisplay.textContent = varBtn.dataset.variantPriceFormatted;
                }
                var addBtn = document.getElementById('s54-detail-add-btn');
                if (addBtn) {
                    addBtn.dataset.variantId = varBtn.dataset.variantId;
                    addBtn.dataset.productPrice = varBtn.dataset.variantPrice;
                }
            }
        });
    });
})();
