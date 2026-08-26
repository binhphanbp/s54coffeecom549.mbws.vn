#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
coll_path = BASE_DIR / 'collections-coffee.html'
coll_html = coll_path.read_text(encoding='utf-8')

replacements = [
    ('>All Filters<', '>Bộ Lọc Chi Tiết<'),
    ('data-open-filters-button>\n        <svg fill="none" class="c-collection-template__faceted-nav__open-icon"', 'data-open-filters-button>\n        <svg fill="none" class="c-collection-template__faceted-nav__open-icon"'),
    ('All Filters</button>', 'Bộ Lọc</button>'),
    ('>type\n<svg', '>Loại Sản Phẩm\n<svg'),
    ('>machine compatibility\n<svg', '>Phương Pháp Pha Chế\n<svg'),
    ('>roast profile\n<svg', '>Mức Độ Rang\n<svg'),
    ('Shop premium specialty blends and online exclusives not available in supermarkets. Freshly roasted in Sydney. Proudly Australian family owned and operated.', 'Khám phá các dòng cà phê hạt Robusta & Arabica nguyên chất thượng hạng S54. Tuyển chọn từ Tây Nguyên, rang mộc 100% không tẩm ướp.'),
    ('† Free Shipping offer applies to Australian addresses only.', '† Miễn phí vận chuyển toàn quốc cho đơn hàng từ 599.000₫.')
]

for o, n in replacements:
    coll_html = coll_html.replace(o, n)

coll_path.write_text(coll_html, encoding='utf-8')
print("✓ Translated collection filter tags and drawer titles in collections-coffee.html")
