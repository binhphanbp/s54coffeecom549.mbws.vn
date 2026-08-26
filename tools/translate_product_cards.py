#!/usr/bin/env python3
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent

p = BASE_DIR / 'collections-coffee.html'
txt = p.read_text(encoding='utf-8')

replacements = [
    ("Our premiere blend, served in leading restaurants", "Dòng cà phê thượng hạng phục vụ tại các nhà hàng & quán cafe cao cấp"),
    ("Our darkest roast offering a bold and intense cup", "Độ rang đậm đà, mang lại hương vị espresso nồng nàn và mạnh mẽ"),
    ("A medium blend with sweet caramel and toasted nut notes", "Hương vị caramel ngọt ngào, thơm bùi hạt rang và hậu vị thanh êm"),
    ("Rich and full-bodied blend with hints of chocolate", "Đậm đà, béo ngậy với nốt hương sô cô la đen nguyên chất"),
    ("Smooth and balanced everyday blend", "Cân bằng, êm dịu, hoàn hảo cho gu thưởng thức mỗi ngày"),
    ("A dark roast blend with intense smoky notes", "Rang đậm truyền thống với nốt hương khói thơm nồng"),
    ("Exclusive Specialty Range", "Dòng Specialty Tuyển Chọn"),
    ("Sold Out", "Hết Hàng"),
    ("SOLD OUT", "HẾT HÀNG")
]

for old_str, new_str in replacements:
    txt = txt.replace(old_str, new_str)

p.write_text(txt, encoding='utf-8')
print("✓ Translated product card descriptions in collections-coffee.html")
