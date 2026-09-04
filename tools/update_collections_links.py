from pathlib import Path
import re

p = Path('collections-coffee.html')
text = p.read_text(encoding='utf-8')

for i in range(1, 13):
    pid = 200000 + i
    vid = 100000 + i
    pattern = rf'(data-variant-id="{vid}"[\s\S]*?<a\s+href=")product-detail\.html(")'
    replacement = rf'\g<1>product-detail.html?id={pid}\2'
    text = re.sub(pattern, replacement, text)

p.write_text(text, encoding='utf-8')
print("Updated collections-coffee.html product links with ?id=20000X")
