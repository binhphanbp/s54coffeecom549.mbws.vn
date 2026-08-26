#!/usr/bin/env python3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
i18n_path = BASE_DIR / 'assets/js/i18n.js'
txt = i18n_path.read_text(encoding='utf-8')

extra_pairs = '''
        // HERO BANNERS (STORY & WHOLESALE)
        ["Câu Chuyện Thương Hiệu S54", "S54 Brand Story & Heritage"],
        ["Hành trình hơn 12 năm kiến tạo giá trị từ Công ty TNHH Giải Pháp Tốt (Good Solutions), chuẩn hóa nguồn cà phê sạch nguyên chất từ vùng đất đỏ Tây Nguyên và lan tỏa tinh hoa cà phê Việt.", "Over 12 years journey by Good Solutions Co., Ltd, standardizing pure clean coffee from Central Highlands red soil and spreading the essence of Vietnamese coffee."],
        ["HÀNH TRÌNH 12+ NĂM DI SẢN (2012 - 2026)", "12+ YEARS HERITAGE JOURNEY (2012 - 2026)"],
        ["Cung Ứng B2B & Đại Lý S54", "S54 B2B & Wholesale Supply"],
        ["Đối tác chiến lược cung ứng nguồn cà phê sạch nguyên chất, thiết bị máy pha chuyên nghiệp và chuyển giao kỹ thuật pha chế cho hơn 500+ chuỗi nhà hàng, khách sạn & quán cafe.", "Strategic partner supplying pure roasted coffee, commercial espresso machines, and brewing technology transfer for over 500+ restaurants, hotels & cafes."],
        ["GIẢI PHÁP CUNG ỨNG B2B TOÀN DIỆN", "COMPREHENSIVE B2B COFFEE SOLUTIONS"],
        ["🌱 Vùng Trồng Đắk Lắk & Cầu Đất", "🌱 Dak Lak & Cau Dat Origins"],
        ["🔥 Công Nghệ Rang Hot-Air Hiện Đại", "🔥 Advanced Hot-Air Artisan Roasting"],
        ["🤝 Đồng Hành Cùng Nông Dân Việt", "🤝 Supporting Vietnamese Farmers"],
        ["☕ Chiết Khấu Đại Lý Tới 35%", "☕ Wholesale Margin Up To 35%"],
        ["📦 Gia Công OEM/ODM Xuất Khẩu", "📦 Private Label OEM/ODM Export"],
        ["🎓 Đào Tạo Barista Chuyên Nghiệp", "🎓 Professional Barista Training"],
'''

idx = txt.find('// 8. OUR STORY')
if idx != -1:
    txt = txt[:idx] + extra_pairs + txt[idx:]
    i18n_path.write_text(txt, encoding='utf-8')
    print("✓ Added new hero translation pairs to i18n.js")
else:
    print("ℹ Could not find index, appending before closing array")
