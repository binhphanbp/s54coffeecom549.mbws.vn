import sys
import re

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', html, re.DOTALL)
print("=== HEADINGS IN INDEX.HTML ===")
for h in headings:
    ch = re.sub(r'<[^>]+>', '', h).strip()
    if ch and len(ch) > 3:
        print("H:", ch)
