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

p = os.path.join('tools', 'old_site', 'http___goodsolutions_com_vn_ve-chung-toi.html')
with open(p, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

parser = TextExtractor()
parser.feed(c)
print("=== ABOUT US COMPLETE CONTENT ===")
for line in parser.result:
    if len(line) > 15 and not any(k in line.lower() for k in ['javascript', 'function', 'giỏ hàng', 'google', 'facebook']):
        print("•", line)
