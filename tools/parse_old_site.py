import os
import sys
import re
from html.parser import HTMLParser

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style']:
            self.in_script = True

    def handle_endtag(self, tag):
        if tag in ['script', 'style']:
            self.in_script = False

    def handle_data(self, data):
        if not self.in_script:
            t = data.strip()
            if t:
                self.result.append(t)

def get_text_from_html(filename):
    path = os.path.join('tools', 'old_site', filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    parser = HTMLTextExtractor()
    parser.feed(content)
    return parser.result

print("=" * 70)
print("     AUTHENTIC S54 COFFEE / GOOD SOLUTIONS DATA SUMMARY")
print("=" * 70)

# 1. About Us
about_texts = get_text_from_html('http___goodsolutions_com_vn_ve-chung-toi.html')
print("\n--- [1. VỀ CHÚNG TÔI / ABOUT US] ---")
for t in about_texts[:40]:
    if len(t) > 25 and not any(k in t.lower() for k in ['javascript', 'function', 'menu', 'đăng nhập', 'header', 'footer']):
        print(" >", t)

# 2. Products
print("\n--- [2. SẢN PHẨM / PRODUCTS] ---")
product_files = [
    ('arabica-coffee-beans.html', 'Arabica Coffee Beans'),
    ('robusta-coffee-beans.html', 'Robusta Coffee Beans'),
    ('ca-phe-hoa-tan-3-in-1-456-gram-s54-coffee.html', 'Cà Phê Hòa Tan 3in1 456g'),
    ('s54-robusta-ca-phe-rang-nguyen-chat.html', 'S54 Robusta Rang Mộc')
]
for pf, label in product_files:
    texts = get_text_from_html(pf)
    print(f"\n[PRODUCT: {label}]")
    for t in texts:
        if any(k in t.lower() for k in ['thành phần', 'khối lượng', 'hạn sử dụng', 'xuất xứ', 'giá', 'hương vị', 'đặc điểm', 'pha chế', 'gram', 'vnđ', 'đ', 'gu']):
            print("  *", t)

# 3. Blog
print("\n--- [3. BÀI VIẾT / BLOG POSTS] ---")
blog_texts = get_text_from_html('coffee-blog.html')
for t in blog_texts:
    if any(k in t.lower() for k in ['lợi ích', 'bí quyết', 'nguồn gốc', 'cà phê', 'pha', 'thưởng thức', 'cách']) and len(t) > 30:
        print("  - Article:", t)

# 4. Contact
print("\n--- [4. LIÊN HỆ / CONTACT & LEGAL] ---")
contact_texts = get_text_from_html('lien-he.html')
for t in contact_texts:
    if any(k in t.lower() for k in ['địa chỉ', 'hotline', 'email', 'mst', 'điện thoại', 'thủ đức', 't8', 'manhattan', 'vinhomes', 'long bình', 'phường', 'công ty']):
        print("  #", t)
