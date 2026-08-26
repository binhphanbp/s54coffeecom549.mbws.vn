#!/usr/bin/env python3
import re
from pathlib import Path

i18n_path = Path('assets/js/i18n.js')
c = i18n_path.read_text(encoding='utf-8')

footer_pairs = """
        // Footer & Legal
        ["CÔNG TY TNHH GIẢI PHÁP TỐT", "GOOD SOLUTIONS COMPANY LIMITED"],
        ["Sản Phẩm S54", "S54 Products"],
        ["Về S54 & Dịch Vụ", "About S54 & Services"],
        ["Đăng Ký Nhận Ưu Đãi", "Subscribe for Offers"],
        ["Nhận ngay voucher ưu đãi 15% cho đơn hàng đầu tiên cùng cẩm nang pha chế độc quyền từ S54 Coffee.", "Get 15% off your first order plus an exclusive brewing guide from S54 Coffee."],
        ["Nhập địa chỉ email của bạn...", "Enter your email address..."],
        ["Kết Nối Với Chúng Tôi:", "Connect With Us:"],
        ["Chính Sách Đổi Trả & Bảo Mật", "Returns & Privacy Policy"],
        ["Liên Hệ Hợp Tác", "Partner Contact"],
        ["Nông Trại & Công Nghệ Rang", "Smart Farming & Roasting"],
        ["Gia Công OEM/ODM Xuất Khẩu", "Private Label OEM/ODM Export"],
        ["Chuyển Khoản", "Bank Transfer"],
        ["Giữ toàn quyền bản quyền.", "All rights reserved."],
"""

if '["Sản Phẩm S54"' not in c:
    c = c.replace('const translationPairs = [', 'const translationPairs = [' + footer_pairs)
    i18n_path.write_text(c, encoding='utf-8')
    print("✓ Added footer translation pairs to i18n.js")
else:
    print("ℹ Footer translation pairs already present")
