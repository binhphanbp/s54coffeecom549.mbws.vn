#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create checkout.html, cart.html, contact.html, and policy pages for S54 Coffee.
Ensures 100% brand consistency, header/footer parity, and fixes broken 404 links.
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

index_html = (BASE_DIR / 'index.html').read_text(encoding='utf-8')

header_match = re.search(r'(<header class="c-header[\s\S]*?</header>)', index_html)
header_html = header_match.group(1) if header_match else ''

footer_match = re.search(r'(<footer class="c-footer[\s\S]*?</footer>)', index_html)
footer_html = footer_match.group(1) if footer_match else ''

# Fix footer links in footer_html for all pages
footer_html = footer_html.replace('href="wholesale.html">Chính Sách Vận Chuyển</a>', 'href="policy-shipping.html">Chính Sách Vận Chuyển</a>')
footer_html = footer_html.replace('href="wholesale.html">Chính Sách Đổi Trả & Bảo Mật</a>', 'href="policy-returns.html">Chính Sách Đổi Trả & Bảo Mật</a>')
footer_html = footer_html.replace('href="wholesale.html">Liên Hệ Hợp Tác</a>', 'href="contact.html">Liên Hệ Hợp Tác</a>')

scripts_tail = '''
    <script src="assets/js/i18n.js?v=1787726992"></script>
    <script src="assets/js/main.js?v=1787726992"></script>
    <button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
    </button>
'''

# 1. CHECKOUT.HTML
checkout_html = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Thanh Toán Đơn Hàng | S54 COFFEE</title>
    <meta name="description" content="Thanh toán an toàn, bảo mật và nhanh chóng tại S54 Coffee. Miễn phí vận chuyển toàn quốc cho đơn hàng từ 599.000₫." />
    
    <link rel="canonical" href="checkout.html" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v=1787726992" rel="stylesheet" type="text/css" media="all" />
    
    <script src="assets/js/cart-mock.js?v=1787726992"></script>
    
    <style>
    body.template-checkout {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    .s54-checkout-wrapper {{
        max-width: 1140px;
        margin: 0 auto;
        padding: clamp(36px, 4vw, 56px) 24px clamp(60px, 6vw, 90px);
    }}
    .s54-checkout-grid {{
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 40px;
        align-items: flex-start;
    }}
    @media (max-width: 900px) {{
        .s54-checkout-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    .s54-checkout-card {{
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        padding: 32px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .s54-checkout-title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 26px;
        font-weight: 700;
        color: #2F221A;
        margin: 0 0 20px 0;
        padding-bottom: 12px;
        border-bottom: 1px solid #F0EBE5;
    }}
    .s54-form-group {{
        margin-bottom: 18px;
    }}
    .s54-form-label {{
        display: block;
        font-size: 13px;
        font-weight: 600;
        color: #554940;
        margin-bottom: 6px;
    }}
    .s54-form-input {{
        width: 100%;
        padding: 12px 14px;
        border: 1px solid #D8CECA;
        border-radius: 6px;
        font-size: 14.5px;
        font-family: inherit;
        background: #FAF8F5;
        transition: border-color 0.2s;
    }}
    .s54-form-input:focus {{
        outline: none;
        border-color: #D68E1D;
        background: #FFFFFF;
    }}
    .s54-form-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
    }}
    .s54-order-item {{
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 12px 0;
        border-bottom: 1px solid #F0EBE5;
    }}
    .s54-order-item img {{
        width: 56px;
        height: 56px;
        object-fit: cover;
        border-radius: 6px;
        border: 1px solid #EBE7E1;
    }}
    .s54-order-item-info {{
        flex: 1;
    }}
    .s54-order-item-title {{
        font-size: 14px;
        font-weight: 600;
        color: #2F221A;
        margin: 0 0 4px 0;
    }}
    .s54-order-item-qty {{
        font-size: 12.5px;
        color: #7A6D65;
    }}
    .s54-order-item-price {{
        font-size: 14.5px;
        font-weight: 700;
        color: #2F221A;
    }}
    .s54-summary-row {{
        display: flex;
        justify-content: space-between;
        font-size: 14.5px;
        padding: 10px 0;
        color: #554940;
    }}
    .s54-summary-total {{
        display: flex;
        justify-content: space-between;
        font-size: 19px;
        font-weight: 700;
        color: #2F221A;
        padding-top: 14px;
        border-top: 2px solid #EBE7E1;
        margin-top: 10px;
    }}
    .s54-pay-option {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px;
        border: 1px solid #EBE7E1;
        border-radius: 8px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: all 0.2s;
    }}
    .s54-pay-option:hover, .s54-pay-option.is-selected {{
        border-color: #D68E1D;
        background: #FFFDF9;
    }}
    .s54-btn-submit {{
        width: 100%;
        padding: 16px;
        background: #2F221A;
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        cursor: pointer;
        margin-top: 20px;
        transition: background 0.2s;
    }}
    .s54-btn-submit:hover {{
        background: #D68E1D;
    }}
    </style>
</head>
<body class="template-checkout">

    <!-- Header Block -->
    {header_html}

    <main class="s54-checkout-wrapper">
        <h1 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(32px, 4vw, 44px); font-weight: 700; margin: 0 0 28px 0;">Thanh Toán Đơn Hàng</h1>
        
        <div class="s54-checkout-grid">
            <!-- Col 1: Customer Form & Payment -->
            <form id="checkout-form" class="s54-checkout-card" onsubmit="event.preventDefault(); handlePlaceOrder();">
                <h2 class="s54-checkout-title">1. Thông Tin Giao Hàng</h2>
                
                <div class="s54-form-row">
                    <div class="s54-form-group">
                        <label class="s54-form-label">Họ và tên *</label>
                        <input type="text" class="s54-form-input" required placeholder="Nguyễn Văn A" id="cust-name" />
                    </div>
                    <div class="s54-form-group">
                        <label class="s54-form-label">Số điện thoại *</label>
                        <input type="tel" class="s54-form-input" required placeholder="0901 234 567" id="cust-phone" />
                    </div>
                </div>

                <div class="s54-form-group">
                    <label class="s54-form-label">Địa chỉ email *</label>
                    <input type="email" class="s54-form-input" required placeholder="email@domain.com" id="cust-email" />
                </div>

                <div class="s54-form-group">
                    <label class="s54-form-label">Địa chỉ nhận hàng chi tiết *</label>
                    <input type="text" class="s54-form-input" required placeholder="Số nhà, tên đường, phường/xã..." id="cust-address" />
                </div>

                <div class="s54-form-row">
                    <div class="s54-form-group">
                        <label class="s54-form-label">Tỉnh / Thành phố *</label>
                        <input type="text" class="s54-form-input" required placeholder="TP. Hồ Chí Minh" id="cust-city" />
                    </div>
                    <div class="s54-form-group">
                        <label class="s54-form-label">Quận / Huyện *</label>
                        <input type="text" class="s54-form-input" required placeholder="TP. Thủ Đức" id="cust-district" />
                    </div>
                </div>

                <div class="s54-form-group">
                    <label class="s54-form-label">Ghi chú đơn hàng (tuỳ chọn)</label>
                    <textarea class="s54-form-input" rows="2" placeholder="Ghi chú thêm về thời gian nhận hàng hoặc yêu cầu xay cà phê..." id="cust-note"></textarea>
                </div>

                <h2 class="s54-checkout-title" style="margin-top: 36px;">2. Phương Thức Thanh Toán</h2>
                
                <label class="s54-pay-option is-selected">
                    <input type="radio" name="payment_method" value="cod" checked />
                    <div>
                        <strong>Thanh toán khi nhận hàng (COD)</strong>
                        <div style="font-size: 13px; color: #7A6D65;">Kiểm tra hàng trước khi thanh toán tiền mặt cho nhân viên giao hàng.</div>
                    </div>
                </label>

                <label class="s54-pay-option">
                    <input type="radio" name="payment_method" value="bank_transfer" />
                    <div>
                        <strong>Chuyển khoản Ngân hàng (VietQR)</strong>
                        <div style="font-size: 13px; color: #7A6D65;">Quét mã QR chuyển khoản tức thì 24/7 không cần nhập thông tin.</div>
                    </div>
                </label>

                <label class="s54-pay-option">
                    <input type="radio" name="payment_method" value="vnpay" />
                    <div>
                        <strong>Cổng thanh toán VNPAY / Momo / Thẻ Quốc Tế</strong>
                        <div style="font-size: 13px; color: #7A6D65;">Hỗ trợ thẻ ATM, Visa, MasterCard, JCB và ví điện tử.</div>
                    </div>
                </label>

                <button type="submit" class="s54-btn-submit">XÁC NHẬN ĐẶT HÀNG</button>
            </form>

            <!-- Col 2: Order Summary -->
            <div class="s54-checkout-card">
                <h2 class="s54-checkout-title">Đơn Hàng Của Bạn</h2>
                <div id="checkout-items-list">
                    <!-- Items rendered by JS -->
                </div>

                <div style="margin-top: 20px;">
                    <div class="s54-summary-row">
                        <span>Tạm tính:</span>
                        <span id="summary-subtotal">0₫</span>
                    </div>
                    <div class="s54-summary-row">
                        <span>Phí vận chuyển:</span>
                        <span id="summary-shipping" style="color: #2E7D32; font-weight: 600;">Miễn phí</span>
                    </div>
                    <div class="s54-summary-total">
                        <span>Tổng thanh toán:</span>
                        <span id="summary-total" style="color: #D68E1D;">0₫</span>
                    </div>
                </div>

                <div style="margin-top: 24px; padding: 16px; background: #FAF8F5; border-radius: 8px; font-size: 13px; color: #6E6259; line-height: 1.6;">
                    🔒 <strong>Cam kết bảo mật:</strong> Mọi thông tin đặt hàng của Quý khách được mã hóa an toàn theo tiêu chuẩn SSL. Cần hỗ trợ nhanh? Gọi ngay Hotline: <a href="tel:0383707578" style="color: #2F221A; font-weight: 700;">0383.707.578</a>.
                </div>
            </div>
        </div>
    </main>

    <!-- Footer Block -->
    {footer_html}
    {scripts_tail}

    <script>
    function renderCheckoutSummary() {{
        const cart = window.S54Cart ? window.S54Cart.getCart() : {{ items: [], total_price: 0 }};
        const items = cart.items || [];
        const container = document.getElementById('checkout-items-list');
        let subtotal = 0;

        if (items.length === 0) {{
            container.innerHTML = '<p style="color: #7A6D65; text-align: center; padding: 24px 0;">Giỏ hàng của bạn đang trống. <a href="collections-coffee.html" style="color: #D68E1D; font-weight: 600;">Tiếp tục mua sắm</a></p>';
            document.getElementById('summary-subtotal').textContent = '0₫';
            document.getElementById('summary-total').textContent = '0₫';
            return;
        }}

        let html = '';
        items.forEach(item => {{
            const price = item.price || 0;
            const linePrice = price * item.quantity;
            subtotal += linePrice;
            html += `
                <div class="s54-order-item">
                    <img src="${{item.image || 'assets/images/s54/products/tui_3in1_456g.jpg'}}" alt="${{item.title}}" />
                    <div class="s54-order-item-info">
                        <h4 class="s54-order-item-title">${{item.title}}</h4>
                        <div class="s54-order-item-qty">Số lượng: ${{item.quantity}}</div>
                    </div>
                    <div class="s54-order-item-price">${{linePrice.toLocaleString('vi-VN')}}₫</div>
                </div>
            `;
        }});
        container.innerHTML = html;

        const shipping = subtotal >= 599000 ? 0 : 30000;
        document.getElementById('summary-subtotal').textContent = subtotal.toLocaleString('vi-VN') + '₫';
        document.getElementById('summary-shipping').textContent = shipping === 0 ? 'Miễn phí (Đơn > 599k)' : '30.000₫';
        document.getElementById('summary-total').textContent = (subtotal + shipping).toLocaleString('vi-VN') + '₫';
    }}

    function handlePlaceOrder() {{
        const name = document.getElementById('cust-name').value;
        const phone = document.getElementById('cust-phone').value;
        const orderId = 'S54-' + Math.floor(100000 + Math.random() * 900000);
        
        alert('Chúc mừng Quý khách ' + name + '!\\n\\nĐơn hàng #' + orderId + ' đã được ghi nhận thành công.\\nChuyên viên S54 Coffee sẽ liên hệ số điện thoại ' + phone + ' để xác nhận và gửi hàng sớm nhất.');
        
        if (window.S54Cart) window.S54Cart.clear();
        window.location.href = 'index.html';
    }}

    document.addEventListener('DOMContentLoaded', renderCheckoutSummary);
    </script>
</body>
</html>
'''

(BASE_DIR / 'checkout.html').write_text(checkout_html, encoding='utf-8')
print("Wrote checkout.html successfully!")


# 2. CART.HTML
cart_html = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Giỏ Hàng Của Bạn | S54 COFFEE</title>
    <meta name="description" content="Xem lại giỏ hàng và tiến hành thanh toán các dòng cà phê nguyên chất thượng hạng S54 Coffee." />
    
    <link rel="canonical" href="cart.html" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v=1787726992" rel="stylesheet" type="text/css" media="all" />
    
    <script src="assets/js/cart-mock.js?v=1787726992"></script>
    
    <style>
    body.template-cart {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    .s54-cart-wrapper {{
        max-width: 1100px;
        margin: 0 auto;
        padding: clamp(36px, 5vw, 60px) 24px clamp(60px, 7vw, 90px);
    }}
    .s54-cart-table {{
        width: 100%;
        border-collapse: collapse;
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }}
    .s54-cart-table th {{
        background: #FAF8F5;
        padding: 16px 20px;
        font-size: 13.5px;
        font-weight: 700;
        color: #554940;
        text-align: left;
        border-bottom: 1px solid #EBE7E1;
    }}
    .s54-cart-table td {{
        padding: 20px;
        border-bottom: 1px solid #F0EBE5;
        vertical-align: middle;
    }}
    .s54-cart-item-info {{
        display: flex;
        align-items: center;
        gap: 16px;
    }}
    .s54-cart-item-img {{
        width: 70px;
        height: 70px;
        object-fit: cover;
        border-radius: 8px;
        border: 1px solid #EBE7E1;
    }}
    .s54-cart-qty-wrap {{
        display: inline-flex;
        align-items: center;
        border: 1px solid #D8CECA;
        border-radius: 6px;
        overflow: hidden;
    }}
    .s54-cart-qty-btn {{
        background: #FAF8F5;
        border: none;
        width: 32px;
        height: 32px;
        font-size: 16px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .s54-cart-qty-val {{
        width: 36px;
        text-align: center;
        font-size: 14px;
        font-weight: 600;
    }}
    .s54-cart-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 32px;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .s54-btn-checkout {{
        display: inline-block;
        padding: 16px 36px;
        background: #2F221A;
        color: #FFFFFF;
        text-decoration: none;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: background 0.2s;
    }}
    .s54-btn-checkout:hover {{
        background: #D68E1D;
    }}
    .s54-btn-continue {{
        color: #6E6259;
        text-decoration: none;
        font-size: 14px;
        font-weight: 600;
    }}
    .s54-btn-continue:hover {{
        color: #D68E1D;
    }}
    </style>
</head>
<body class="template-cart">

    <!-- Header Block -->
    {header_html}

    <main class="s54-cart-wrapper">
        <h1 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(32px, 4vw, 44px); font-weight: 700; margin: 0 0 24px 0;">Giỏ Hàng Của Bạn</h1>

        <div id="full-cart-container">
            <table class="s54-cart-table">
                <thead>
                    <tr>
                        <th>Sản phẩm</th>
                        <th>Đơn giá</th>
                        <th>Số lượng</th>
                        <th>Tổng tiền</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody id="cart-table-body">
                    <!-- Injected by JS -->
                </tbody>
            </table>

            <div class="s54-cart-footer">
                <a href="collections-coffee.html" class="s54-btn-continue">← Tiếp tục mua sắm</a>
                <div style="text-align: right;">
                    <div style="font-size: 15px; color: #6E6259; margin-bottom: 8px;">Tạm tính: <strong id="cart-total-amount" style="font-size: 22px; color: #2F221A;">0₫</strong></div>
                    <div style="font-size: 12.5px; color: #2E7D32; margin-bottom: 16px;">✓ Miễn phí vận chuyển toàn quốc cho đơn từ 599.000₫</div>
                    <a href="checkout.html" class="s54-btn-checkout">TIẾN HÀNH THANH TOÁN</a>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer Block -->
    {footer_html}
    {scripts_tail}

    <script>
    function renderFullCart() {{
        const cart = window.S54Cart ? window.S54Cart.getCart() : {{ items: [] }};
        const items = cart.items || [];
        const tbody = document.getElementById('cart-table-body');
        const container = document.getElementById('full-cart-container');
        let total = 0;

        if (items.length === 0) {{
            container.innerHTML = `
                <div style="background: #FFFFFF; border: 1px solid #EBE7E1; border-radius: 12px; padding: 60px 20px; text-align: center;">
                    <p style="font-size: 18px; color: #6E6259; margin-bottom: 20px;">Giỏ hàng của bạn đang trống</p>
                    <a href="collections-coffee.html" class="s54-btn-checkout" style="display: inline-block;">Khám Phá Sản Phẩm Ngay</a>
                </div>
            `;
            return;
        }}

        let html = '';
        items.forEach(item => {{
            const price = item.price || 0;
            const linePrice = price * item.quantity;
            total += linePrice;

            html += `
                <tr>
                    <td>
                        <div class="s54-cart-item-info">
                            <img src="${{item.image || 'assets/images/s54/products/tui_3in1_456g.jpg'}}" alt="${{item.title}}" class="s54-cart-item-img" />
                            <div>
                                <a href="${{item.url || 'product-detail.html'}}" style="color: #2F221A; font-weight: 700; text-decoration: none;">${{item.title}}</a>
                            </div>
                        </div>
                    </td>
                    <td style="font-weight: 600;">${{price.toLocaleString('vi-VN')}}₫</td>
                    <td>
                        <div class="s54-cart-qty-wrap">
                            <button type="button" class="s54-cart-qty-btn" onclick="updateQty('${{item.key || item.id}}', ${{item.quantity - 1}})">−</button>
                            <span class="s54-cart-qty-val">${{item.quantity}}</span>
                            <button type="button" class="s54-cart-qty-btn" onclick="updateQty('${{item.key || item.id}}', ${{item.quantity + 1}})">+</button>
                        </div>
                    </td>
                    <td style="font-weight: 700; color: #D68E1D;">${{linePrice.toLocaleString('vi-VN')}}₫</td>
                    <td>
                        <button type="button" style="background: none; border: none; color: #A89F91; cursor: pointer; font-size: 18px;" onclick="updateQty('${{item.key || item.id}}', 0)">✕</button>
                    </td>
                </tr>
            `;
        }});

        tbody.innerHTML = html;
        document.getElementById('cart-total-amount').textContent = total.toLocaleString('vi-VN') + '₫';
    }}

    function updateQty(id, qty) {{
        if (window.S54Cart) {{
            window.S54Cart.updateQuantity(id, qty);
            renderFullCart();
        }}
    }}

    document.addEventListener('DOMContentLoaded', renderFullCart);
    </script>
</body>
</html>
'''

(BASE_DIR / 'cart.html').write_text(cart_html, encoding='utf-8')
print("Wrote cart.html successfully!")


# 3. CONTACT.HTML
contact_html = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Liên Hệ Hợp Tác & Showroom | S54 COFFEE</title>
    <meta name="description" content="Liên hệ S54 Coffee – Good Solutions Co., Ltd. Trụ sở tại Vinhomes Grand Park, TP. Thủ Đức, TP. Hồ Chí Minh. Hotline: 0383.707.578." />
    
    <link rel="canonical" href="contact.html" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v=1787726992" rel="stylesheet" type="text/css" media="all" />
    
    <script src="assets/js/cart-mock.js?v=1787726992"></script>
    
    <style>
    body.template-contact {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    .s54-contact-wrapper {{
        max-width: 1140px;
        margin: 0 auto;
        padding: clamp(40px, 5vw, 70px) 24px clamp(60px, 8vw, 100px);
    }}
    .s54-contact-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 48px;
        margin-top: 36px;
    }}
    @media (max-width: 860px) {{
        .s54-contact-grid {{
            grid-template-columns: 1fr;
            gap: 32px;
        }}
    }}
    .s54-contact-info-card {{
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        padding: 36px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .s54-contact-item {{
        display: flex;
        gap: 16px;
        margin-bottom: 24px;
    }}
    .s54-contact-icon {{
        font-size: 24px;
        color: #D68E1D;
    }}
    .s54-contact-item h4 {{
        font-size: 15px;
        font-weight: 700;
        margin: 0 0 6px 0;
        color: #2F221A;
    }}
    .s54-contact-item p {{
        font-size: 14.5px;
        line-height: 1.6;
        color: #6E6259;
        margin: 0;
    }}
    .s54-contact-form {{
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        padding: 36px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    </style>
</head>
<body class="template-contact">

    <!-- Header Block -->
    {header_html}

    <main class="s54-contact-wrapper">
        <div style="text-align: center; max-width: 700px; margin: 0 auto;">
            <div style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: #D68E1D; text-transform: uppercase; margin-bottom: 12px;">KẾT NỐI VỚI S54 COFFEE</div>
            <h1 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(34px, 4.5vw, 54px); font-weight: 700; margin: 0 0 16px 0;">Liên Hệ & Hợp Tác</h1>
            <p style="font-size: 16px; line-height: 1.7; color: #6E6259; margin: 0;">Đội ngũ S54 Coffee luôn sẵn sàng lắng nghe và tư vấn giải pháp cà phê tối ưu nhất cho gia đình và doanh nghiệp của bạn.</p>
        </div>

        <div class="s54-contact-grid">
            <!-- Left Column: Info -->
            <div class="s54-contact-info-card">
                <h3 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 26px; font-weight: 700; margin: 0 0 24px 0;">Thông Tin Liên Hệ</h3>

                <div class="s54-contact-item">
                    <div class="s54-contact-icon">🏢</div>
                    <div>
                        <h4>Công Ty TNHH Giải Pháp Tốt</h4>
                        <p>Thương hiệu cà phê rang mộc thượng hạng S54 Coffee.</p>
                    </div>
                </div>

                <div class="s54-contact-item">
                    <div class="s54-contact-icon">📍</div>
                    <div>
                        <h4>Địa Chỉ Văn Phòng & Showroom</h4>
                        <p>Số 35, Đường T8, Manhattan, Vinhomes Grand Park, P. Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh</p>
                    </div>
                </div>

                <div class="s54-contact-item">
                    <div class="s54-contact-icon">📞</div>
                    <div>
                        <h4>Hotline Tư Vấn 24/7</h4>
                        <p><a href="tel:0383707578" style="color: #D68E1D; font-weight: 700; text-decoration: none;">0383.707.578</a> — <a href="tel:0902873345" style="color: #D68E1D; font-weight: 700; text-decoration: none;">0902.873.345</a></p>
                    </div>
                </div>

                <div class="s54-contact-item">
                    <div class="s54-contact-icon">✉️</div>
                    <div>
                        <h4>Email Hỗ Trợ Khách Hàng</h4>
                        <p><a href="mailto:pm@goodsolutions.com.vn" style="color: #2F221A; text-decoration: none;">pm@goodsolutions.com.vn</a></p>
                    </div>
                </div>

                <div class="s54-contact-item">
                    <div class="s54-contact-icon">🕒</div>
                    <div>
                        <h4>Thời Gian Hoạt Động</h4>
                        <p>Thứ 2 – Thứ 7: 08:00 – 18:00 (Chủ Nhật hỗ trợ qua Hotline/Zalo)</p>
                    </div>
                </div>
            </div>

            <!-- Right Column: Form -->
            <form class="s54-contact-form" onsubmit="event.preventDefault(); alert('Cảm ơn Quý khách đã gửi tin nhắn! S54 Coffee sẽ phản hồi trong vòng 24 giờ.'); this.reset();">
                <h3 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 26px; font-weight: 700; margin: 0 0 24px 0;">Gửi Yêu Cầu Cho Chúng Tôi</h3>

                <div style="margin-bottom: 16px;">
                    <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Họ và tên *</label>
                    <input type="text" required style="width: 100%; padding: 12px 14px; border: 1px solid #D8CECA; border-radius: 6px; font-size: 14.5px;" placeholder="Nguyễn Văn A" />
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
                    <div>
                        <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Số điện thoại *</label>
                        <input type="tel" required style="width: 100%; padding: 12px 14px; border: 1px solid #D8CECA; border-radius: 6px; font-size: 14.5px;" placeholder="0901..." />
                    </div>
                    <div>
                        <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Email *</label>
                        <input type="email" required style="width: 100%; padding: 12px 14px; border: 1px solid #D8CECA; border-radius: 6px; font-size: 14.5px;" placeholder="email@..." />
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px;">Nội dung cần hỗ trợ / Hợp tác *</label>
                    <textarea rows="4" required style="width: 100%; padding: 12px 14px; border: 1px solid #D8CECA; border-radius: 6px; font-size: 14.5px; font-family: inherit;" placeholder="Quý khách vui lòng cho biết nhu cầu: mua lẻ, làm đại lý, mở quán cà phê hoặc cung cấp máy xay..."></textarea>
                </div>

                <button type="submit" style="width: 100%; padding: 16px; background: #2F221A; color: #FFFFFF; border: none; border-radius: 8px; font-size: 14px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer; transition: background 0.2s;">GỬI TIN NHẮN NGAY</button>
            </form>
        </div>
    </main>

    <!-- Footer Block -->
    {footer_html}
    {scripts_tail}
</body>
</html>
'''

(BASE_DIR / 'contact.html').write_text(contact_html, encoding='utf-8')
print("Wrote contact.html successfully!")


# 4. POLICY PAGES (Shipping, Returns, Privacy)
def make_policy_page(filename, title, content_html):
    page_html = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>{title} | S54 COFFEE</title>
    
    <link rel="canonical" href="{filename}" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v=1787726992" rel="stylesheet" type="text/css" media="all" />
    
    <script src="assets/js/cart-mock.js?v=1787726992"></script>
    
    <style>
    body.template-policy {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    .s54-policy-wrapper {{
        max-width: 860px;
        margin: 0 auto;
        padding: clamp(40px, 5vw, 64px) 24px clamp(60px, 7vw, 90px);
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        margin-top: 40px;
        margin-bottom: 60px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .s54-policy-wrapper h1 {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(32px, 4vw, 44px);
        font-weight: 700;
        margin: 0 0 24px 0;
        padding-bottom: 16px;
        border-bottom: 2px solid #EBE7E1;
    }}
    .s54-policy-wrapper h2 {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 24px;
        font-weight: 700;
        margin: 32px 0 12px 0;
        color: #2F221A;
    }}
    .s54-policy-wrapper p, .s54-policy-wrapper li {{
        font-size: 15.5px;
        line-height: 1.8;
        color: #4A3E36;
        margin-bottom: 14px;
    }}
    </style>
</head>
<body class="template-policy">
    {header_html}

    <main class="s54-policy-wrapper">
        <h1>{title}</h1>
        {content_html}
    </main>

    {footer_html}
    {scripts_tail}
</body>
</html>
'''
    (BASE_DIR / filename).write_text(page_html, encoding='utf-8')
    print(f"Wrote {filename} successfully!")

# Shipping Policy
shipping_content = '''
<h2>1. Phạm Vi Giao Hàng</h2>
<p>S54 Coffee áp dụng chính sách giao hàng tận nơi trên toàn quốc, bao gồm tất cả 63 tỉnh thành tại Việt Nam thông qua các đối tác vận chuyển uy tín: Giao Hàng Tiết Kiệm (GHTK), Giao Hàng Nhanh (GHN) và Viettel Post.</p>

<h2>2. Cước Phí Vận Chuyển</h2>
<ul>
    <li><strong>Miễn phí vận chuyển (Freeship):</strong> Áp dụng cho tất cả đơn hàng có tổng giá trị thanh toán từ <strong>599.000 VNĐ</strong> trở lên trên toàn quốc.</li>
    <li><strong>Đơn hàng dưới 599.000 VNĐ:</strong> Cước phí vận chuyển đồng giá 30.000 VNĐ cho khu vực nội thành TP.HCM và 35.000 VNĐ cho các tỉnh thành khác.</li>
</ul>

<h2>3. Thời Gian Giao Hàng</h2>
<ul>
    <li><strong>Khu vực TP. Hồ Chí Minh:</strong> Giao nhanh trong ngày hoặc 1 ngày làm việc tiếp theo. Hỗ trợ giao hỏa tốc 2 giờ qua GrabExpress/Ahamove khi khách hàng yêu cầu.</li>
    <li><strong>Các tỉnh thành miền Nam & miền Trung:</strong> Từ 1 – 3 ngày làm việc.</li>
    <li><strong>Khu vực Hà Nội & các tỉnh phía Bắc:</strong> Từ 2 – 4 ngày làm việc.</li>
</ul>

<h2>4. Kiểm Hàng Khi Nhận (Đồng Kiểm)</h2>
<p>Quý khách hoàn toàn được quyền mở kiện hàng kiểm tra sản phẩm trước khi thanh toán cho nhân viên giao hàng. Nếu sản phẩm bị móp méo, rách bao bì hoặc không đúng mẫu mã, quý khách có quyền từ chối nhận và liên hệ ngay Hotline: <strong>0383.707.578</strong>.</p>
'''
make_policy_page('policy-shipping.html', 'Chính Sách Vận Chuyển & Giao Nhận', shipping_content)

# Returns Policy
returns_content = '''
<h2>1. Điều Kiện Đổi Trả</h2>
<p>S54 Coffee cam kết đổi mới 100% sản phẩm miễn phí trong vòng <strong>7 ngày</strong> kể từ ngày quý khách nhận hàng trong các trường hợp sau:</p>
<ul>
    <li>Sản phẩm giao không đúng chủng loại, mẫu mã hoặc số lượng như đơn đặt hàng.</li>
    <li>Bao bì sản phẩm bị rách hỏng, van 1 chiều bị bung trong quá trình vận chuyển.</li>
    <li>Chất lượng cà phê không đảm bảo (ẩm mốc, có mùi lạ không phải hương vị cà phê mộc).</li>
</ul>

<h2>2. Chính Sách Bảo Hành Máy Xay Cà Phê Cầm Tay</h2>
<ul>
    <li>Bảo hành chính hãng <strong>12 tháng</strong> đối với lỗi kỹ thuật do nhà sản xuất (lõi xay CNC, trục xoay, nắp đậy).</li>
    <li>1 đổi 1 trong vòng 30 ngày đầu tiên nếu máy phát sinh lỗi kỹ thuật.</li>
</ul>

<h2>3. Quy Trình Đổi Trả Đơn Giản</h2>
<p>Bước 1: Chụp ảnh/quay video sản phẩm cần đổi trả.<br/>
Bước 2: Gửi thông tin qua Zalo Hotline <strong>0383.707.578</strong> hoặc email <strong>pm@goodsolutions.com.vn</strong>.<br/>
Bước 3: Nhân viên S54 sẽ gửi sản phẩm mới đến tận nhà đổi cho quý khách, quý khách không cần mang ra bưu điện.</p>
'''
make_policy_page('policy-returns.html', 'Chính Sách Đổi Trả & Bảo Hành', returns_content)

# Privacy Policy
privacy_content = '''
<h2>1. Mục Đích Thu Thập Thông Tin</h2>
<p>S54 Coffee (Công ty TNHH Giải Pháp Tốt) chỉ thu thập các thông tin cần thiết phục vụ cho việc xử lý đơn hàng và chăm sóc khách hàng: Họ tên, Số điện thoại, Địa chỉ giao hàng và Email.</p>

<h2>2. Cam Kết Bảo Mật</h2>
<ul>
    <li>Mọi thông tin cá nhân của Quý khách được lưu trữ bảo mật trên hệ thống máy chủ an toàn.</li>
    <li>Chúng tôi cam kết tuyệt đối <strong>KHÔNG</strong> chia sẻ, bán hoặc trao đổi thông tin khách hàng cho bất kỳ bên thứ ba nào vì mục đích thương mại.</li>
    <li>Quý khách có quyền yêu cầu chỉnh sửa hoặc xóa thông tin cá nhân bất cứ lúc nào bằng cách liên hệ với bộ phận CSKH của S54 Coffee.</li>
</ul>
'''
make_policy_page('policy-privacy.html', 'Chính Sách Bảo Mật Thông Tin', privacy_content)

print("All policy and checkout pages created successfully!")
