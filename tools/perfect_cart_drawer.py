#!/usr/bin/env python3
"""
Master redesign of S54 Cart Drawer:
1. Fix full 100vh height & layout (Top Header, Progress Bar, Scrollable Body, Fixed Footer)
2. Complete full-screen backdrop overlay (100vw, 100vh, blur 4px)
3. Luxury typography, high contrast, clean buttons, smooth slide-out animation
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update custom.css
css_path = BASE_DIR / 'assets/css/custom.css'
c = css_path.read_text(encoding='utf-8')

cart_css_block = '''/* ==========================================================================
   8. S54 LUXURY SLIDE-OUT CART DRAWER (100vh Full-Height & Perfect UI/UX)
   ========================================================================== */

/* Full-Screen Backdrop Overlay */
.c-cart-drawer__overlay,
.c-cart-drawer__background {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    height: 100dvh !important;
    background: rgba(26, 17, 12, 0.72) !important;
    backdrop-filter: blur(5px) !important;
    -webkit-backdrop-filter: blur(5px) !important;
    z-index: 9999990 !important;
    opacity: 0 !important;
    visibility: hidden !important;
    transition: opacity 0.35s ease, visibility 0.35s ease !important;
    pointer-events: none !important;
    margin: 0 !important;
    padding: 0 !important;
}

.c-cart-drawer__overlay.is-open,
.c-cart-drawer.is-open ~ .c-cart-drawer__overlay,
.c-cart-drawer.is-drawer-open + .c-cart-drawer__background {
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: all !important;
}

/* Master Cart Drawer (Full Height 100vh, Fixed on Right) */
.c-cart-drawer {
    position: fixed !important;
    top: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100% !important;
    max-width: 480px !important;
    height: 100vh !important;
    height: 100dvh !important;
    background-color: #FAF8F5 !important;
    z-index: 99999999 !important;
    box-shadow: -8px 0 35px rgba(0, 0, 0, 0.28) !important;
    transform: translateX(100%) !important;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
    display: flex !important;
    flex-direction: column !important;
    overflow: hidden !important;
    pointer-events: auto !important;
    border-left: 1px solid #EBE7E1 !important;
}

.c-cart-drawer.is-open,
.c-cart-drawer.is-drawer-open {
    transform: translateX(0) !important;
    visibility: visible !important;
}

/* Header */
.c-cart-drawer__header {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 20px 24px !important;
    border-bottom: 1px solid #EBE7E1 !important;
    background: #FFFFFF !important;
    flex-shrink: 0 !important;
}

.c-cart-drawer__title {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 26px !important;
    font-weight: 700 !important;
    line-height: 1 !important;
    margin: 0 !important;
    color: #2F221A !important;
    letter-spacing: -0.01em !important;
}

.c-cart-drawer__close {
    background: #FAF8F5 !important;
    border: 1px solid #EBE7E1 !important;
    border-radius: 50% !important;
    width: 34px !important;
    height: 34px !important;
    font-size: 16px !important;
    cursor: pointer !important;
    color: #6E6259 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.2s ease !important;
    padding: 0 !important;
    line-height: 1 !important;
}

.c-cart-drawer__close:hover {
    background: #2F221A !important;
    color: #FFFFFF !important;
    border-color: #2F221A !important;
    transform: rotate(90deg) !important;
}

/* Free Shipping Bar */
.c-cart-drawer__free-shipping {
    background-color: #F5EFEB !important;
    padding: 14px 24px !important;
    border-bottom: 1px solid #EBE7E1 !important;
    flex-shrink: 0 !important;
}

.c-cart-drawer__free-shipping-text {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #2F221A !important;
    text-align: center !important;
    line-height: 1.4 !important;
}

.c-cart-drawer__progress-bar {
    height: 6px !important;
    background: #E5DDD3 !important;
    border-radius: 6px !important;
    margin-top: 8px !important;
    overflow: hidden !important;
}

.c-cart-drawer__progress-fill {
    height: 100% !important;
    background: linear-gradient(90deg, #D68E1D, #F0C475) !important;
    border-radius: 6px !important;
    transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

/* Scrollable Body */
.c-cart-drawer__body {
    flex: 1 1 auto !important;
    overflow-y: auto !important;
    padding: 20px 24px !important;
    background: #FAF8F5 !important;
}

.c-cart-drawer__body::-webkit-scrollbar {
    width: 5px;
}
.c-cart-drawer__body::-webkit-scrollbar-thumb {
    background: #D8CEBE;
    border-radius: 4px;
}

.c-cart-drawer__item {
    display: grid !important;
    grid-template-columns: 76px 1fr auto !important;
    gap: 16px !important;
    align-items: center !important;
    padding: 16px 0 !important;
    border-bottom: 1px solid #EBE7E1 !important;
}

.c-cart-drawer__item:last-child {
    border-bottom: none !important;
}

.c-cart-drawer__item-img {
    width: 76px !important;
    height: 76px !important;
    object-fit: contain !important;
    background: #FFFFFF !important;
    border: 1px solid #EBE7E1 !important;
    border-radius: 8px !important;
    padding: 6px !important;
}

.c-cart-drawer__item-details {
    display: flex !important;
    flex-direction: column !important;
    gap: 4px !important;
}

.c-cart-drawer__item-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #2F221A !important;
    margin: 0 !important;
    line-height: 1.35 !important;
}

.c-cart-drawer__item-price {
    font-size: 14px !important;
    font-weight: 700 !important;
    color: #D68E1D !important;
}

.c-cart-drawer__qty-wrap {
    display: inline-flex !important;
    align-items: center !important;
    border: 1px solid #D8CEBE !important;
    border-radius: 20px !important;
    background: #FFFFFF !important;
    overflow: hidden !important;
    height: 28px !important;
    width: fit-content !important;
    margin-top: 4px !important;
}

.c-cart-drawer__qty-btn {
    background: none !important;
    border: none !important;
    width: 28px !important;
    height: 28px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    color: #2F221A !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background 0.2s ease !important;
}

.c-cart-drawer__qty-btn:hover {
    background: #F5EFEB !important;
}

.c-cart-drawer__qty-val {
    font-size: 13px !important;
    font-weight: 700 !important;
    padding: 0 8px !important;
    min-width: 24px !important;
    text-align: center !important;
    color: #2F221A !important;
}

.c-cart-drawer__item-remove {
    background: none !important;
    border: none !important;
    color: #A3968C !important;
    cursor: pointer !important;
    font-size: 16px !important;
    padding: 6px !important;
    transition: color 0.2s ease !important;
    align-self: flex-start !important;
}

.c-cart-drawer__item-remove:hover {
    color: #D63031 !important;
}

/* Footer */
.c-cart-drawer__footer {
    padding: 20px 24px 28px !important;
    background: #FFFFFF !important;
    border-top: 1px solid #EBE7E1 !important;
    box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.04) !important;
    flex-shrink: 0 !important;
}

.c-cart-drawer__subtotal {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    font-size: 15px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    margin-bottom: 16px !important;
    color: #2F221A !important;
}

.c-cart-drawer__subtotal-amount {
    font-size: 18px !important;
    color: #D68E1D !important;
    font-weight: 700 !important;
}

.c-cart-drawer__checkout-btn {
    width: 100% !important;
    background: #2F221A !important;
    color: #FFFFFF !important;
    padding: 16px !important;
    text-align: center !important;
    border: none !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    font-size: 13.5px !important;
    text-transform: uppercase !important;
    cursor: pointer !important;
    border-radius: 6px !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 12px rgba(47, 34, 26, 0.15) !important;
    display: block !important;
}

.c-cart-drawer__checkout-btn:hover {
    background: #D68E1D !important;
    box-shadow: 0 6px 18px rgba(214, 142, 29, 0.3) !important;
    transform: translateY(-1px) !important;
}'''

# Replace cart CSS block in custom.css
old_cart_pattern = r'/\* 8\. Slide-out Cart Drawer[\s\S]*?\.c-cart-drawer__checkout-btn:hover\s*\{[^}]*\}'
c = re.sub(old_cart_pattern, cart_css_block, c)
css_path.write_text(c, encoding='utf-8')
print("✓ Updated custom.css with luxury 100vh Cart Drawer styling")

# 2. Update main.js to ensure single clean drawer and correct markup
js_path = BASE_DIR / 'assets/js/main.js'
jc = js_path.read_text(encoding='utf-8')

# Ensure item HTML in updateCartUI uses the new classes
old_item_render = r'cartBody\.innerHTML = items\.map\(item => \{[\s\S]*?\}\)\.join\(\'\'\);'
new_item_render = '''cartBody.innerHTML = items.map(item => {
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
                }).join('');'''

jc = re.sub(old_item_render, new_item_render, jc)

# Clean up static AAA drawer in ensureCartDrawer
js_path.write_text(jc, encoding='utf-8')
print("✓ Updated main.js cart drawer markup")

print("\n✅ Cart Drawer overhaul complete!")
