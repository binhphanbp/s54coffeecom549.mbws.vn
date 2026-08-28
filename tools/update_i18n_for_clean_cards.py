#!/usr/bin/env python3
"""
Add bilingual pairs for the cleaned products in i18n.js
"""

from pathlib import Path

BASE_DIR = Path('/home/binhphan/matbao-ws/clients/s54coffeecom549.mbws.vn')

for p in [BASE_DIR / 'assets/js/i18n.js', BASE_DIR / 'public/client-assets/js/i18n.js']:
    if not p.exists():
        continue
    txt = p.read_text(encoding='utf-8')
    
    new_pairs = '''
        // CLEANED CARD TITLES & EXCERPTS
        ["S54 Cà Phê Khử Caffeine (Decaf)", "S54 Decaffeinated Blend"],
        ["Dòng blend nguyên bản tạo nên danh tiếng S54 Coffee", "Our signature blend created for coffee lovers"],
        ["Dòng blend đậm đà chuẩn vị cà phê Espresso Ý", "Authentic Italian-style espresso blend"],
        ["Hương vị phong phú, thanh tao từ vùng cao nguyên Cầu Đất", "Rich and delicate flavours from Cau Dat highlands"],
        ["Cà phê espresso Ý nguyên bản, được khử caffeine tự nhiên", "Authentic Italian espresso, naturally decaffeinated"],
'''
    if 'CLEANED CARD TITLES & EXCERPTS' not in txt:
        idx = txt.find('// 8. OUR STORY')
        if idx != -1:
            txt = txt[:idx] + new_pairs + txt[idx:]
            p.write_text(txt, encoding='utf-8')
            print(f"✓ Updated {p}")

print("✅ Updated i18n dictionaries successfully!")
