import os
import sys
from html.parser import HTMLParser

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style', 'nav', 'header', 'footer']:
            self.in_script = True

    def handle_endtag(self, tag):
        if tag in ['script', 'style', 'nav', 'header', 'footer']:
            self.in_script = False

    def handle_data(self, data):
        if not self.in_script:
            t = data.strip()
            if t:
                self.result.append(t)

def parse_file(fname):
    p = os.path.join('tools', 'old_site', fname)
    if not os.path.exists(p):
        return
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    parser = TextExtractor()
    parser.feed(c)
    print("=" * 60)
    print(f"FILE: {fname}")
    print("=" * 60)
    for line in parser.result:
        if len(line) > 20 and not any(k in line.lower() for k in ['đăng nhập', 'giỏ hàng', 'google', 'facebook', 'tài khoản']):
            print("-", line)

parse_file('http___goodsolutions_com_vn_ve-chung-toi.html')
parse_file('http___goodsolutions_com_vn_5-loi-ich-tuyet-voi-cua-viec-uong-ca-phe-co-the-ban-chua-biet.html')
