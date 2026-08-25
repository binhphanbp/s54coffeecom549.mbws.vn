import re
from pathlib import Path

content = Path('index.html').read_text(encoding='utf-8')

# Find all section IDs and titles
sections = re.findall(r'(<div id="shopify-section-[^"]*" class="shopify-section[^"]*">[\s\S]*?)(?=<div id="shopify-section-|\Z)', content)
print(f"Total sections found: {len(sections)}")

for idx, sec in enumerate(sections):
    sec_id = re.search(r'id="([^"]*)"', sec)
    sec_class = re.search(r'class="([^"]*)"', sec)
    heading = re.search(r'<h[1-6][^>]*>(.*?)</h[1-6]>', sec)
    h_text = re.sub(r'<[^>]+>', '', heading.group(1)).strip() if heading else 'No heading'
    print(f"\n[{idx+1}] ID: {sec_id.group(1) if sec_id else 'N/A'}")
    print(f"    Class: {sec_class.group(1) if sec_class else 'N/A'}")
    print(f"    Heading: {h_text}")
    
    # Check images inside section
    imgs = re.findall(r'<img[^>]+src="([^"]*)"', sec)
    print(f"    Images ({len(imgs)}): {imgs[:3]}")

