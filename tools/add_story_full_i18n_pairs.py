#!/usr/bin/env python3
"""
Add all authentic our-story.html translation pairs to assets/js/i18n.js
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
i18n_path = BASE_DIR / 'assets/js/i18n.js'
txt = i18n_path.read_text(encoding='utf-8')

story_pairs = '''
        // AUTHENTIC S54 STORY TIMELINE & PHILOSOPHY
        ["“Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.” — Triết lý Good Solutions & S54 Coffee.", "“To establish good solutions in providing quality coffee with unmatched levels of service.” — Philosophy of Good Solutions & S54 Coffee."],
        ["Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.", "To establish good solutions in providing quality coffee with unmatched levels of service."],
        ["Triết lý Good Solutions & S54 Coffee.", "Philosophy of Good Solutions & S54 Coffee."],
        ["GIAI ĐOẠN 2012 - KHỞI NGUỒN ĐAM MÊ", "2012 - OUR PASSION & FOUNDING"],
        ["Thành Lập Good Solutions & Khát Vọng Cà Phê Sạch", "Founding of Good Solutions & Pure Clean Coffee Vision"],
        ["Năm 2012, Công ty TNHH Giải Pháp Tốt (Good Solutions) chính thức được thành lập với mục tiêu thiết lập những chuẩn mực mới cho ngành cà phê Việt Nam. Chứng kiến thực trạng cà phê pha tạp bắp đậu trên thị trường, những người sáng lập S54 đã quyết tâm xây dựng thương hiệu cà phê rang mộc 100% nguyên chất, minh bạch từ nguồn gốc nông trại đến từng tách cà phê trao tay người tiêu dùng.", "In 2012, Good Solutions Co., Ltd was established to set new standards for Vietnamese coffee. Witnessing widespread adulterated coffee on the market, S54 founders committed to building a 100% pure roasted coffee brand, transparent from farm origins to every cup served."],
        ["VÙNG TRỒNG NGUYÊN LIỆU", "COFFEE FARMING ORIGINS"],
        ["Liên Kết Nông Trại Đắk Lắk & Cầu Đất (Lâm Đồng)", "Partnering with Dak Lak & Cau Dat (Lam Dong) Farms"],
        ["S54 Coffee trực tiếp liên kết và bao tiêu sản lượng tại các nông trại thổ nhưỡng bazan màu mỡ ở Buôn Ma Thuột (Đắk Lắk) và Cầu Đất (Lâm Đồng) ở độ cao lý tưởng từ 800m - 1.500m. Chúng tôi kiên định quy chuẩn thu hái quả chín mọng trên cây đạt tỷ lệ trên 95%, áp dụng phương pháp sơ chế ướt (Full Washed) và phơi giàn kính tự nhiên để bảo tồn tối đa hương vị nguyên bản của thổ nhưỡng Việt Nam.", "S54 Coffee directly partners and secures harvest with fertile basalt soil farms in Buon Ma Thuot (Dak Lak) and Cau Dat (Lam Dong) at altitudes from 800m - 1,500m. We adhere to harvesting >95% ripe cherries, applying full-washed processing and natural greenhouse raised beds to preserve authentic Vietnamese terroir."],
        ["CÔNG NGHỆ SẢN XUẤT", "ROASTING TECHNOLOGY"],
        ["Công Nghệ Rang Hot-Air Chuẩn HACCP & ISO", "Hot-Air Roasting Technology with HACCP & ISO Standards"],
        ["Đầu tư nhà máy rang hiện đại với công nghệ khí nóng Hot-Air hồi lưu, S54 kiểm soát chính xác từng profile nhiệt độ và thời gian rang cho từng mẻ hạt. Công nghệ này giúp hạt cà phê chín đều từ lõi ra vỏ, không cháy cạnh, triệt tiêu vị khét và làm nổi bật các nốt hương sô cô la, caramel, thảo mộc tự nhiên cùng hậu vị ngọt thanh êm dịu.", "Investing in modern roasting facilities with recirculating Hot-Air convection, S54 precisely controls temperature profiles and roasting time. This ensures beans roast evenly from core to surface without burnt edges, highlighting notes of dark chocolate, caramel, and sweet smooth aftertaste."],
        ["ĐỔI MỚI SẢN PHẨM", "PRODUCT INNOVATION"],
        ["Đột Phá Hòa Tan 3-in-1 (456g) & Sấy Lạnh Cao Cấp", "Breakthrough 3-in-1 Instant (456g) & Premium Freeze-Dried Coffee"],
        ["Đáp ứng nhịp sống hiện đại mà vẫn giữ vững chuẩn mực gu thưởng thức, S54 Coffee phát triển thành công dòng cà phê hòa tan 3-in-1 hộp 456g đậm đà và cà phê sấy lạnh thăng hoa cao cấp. Quy trình trích ly và sấy ở nhiệt độ âm giúp giữ lại hơn 99% hợp chất hương thơm tự nhiên của hạt Robusta & Arabica thượng hạng.", "Meeting modern lifestyles while preserving authentic taste, S54 Coffee developed rich 3-in-1 instant coffee (456g box) and premium freeze-dried coffee. Sub-zero extraction and freeze-drying retain over 99% of the natural aromatic compounds of premium Robusta & Arabica beans."],
        ["ĐỒNG HÀNH & PHÁT TRIỂN", "COMMUNITY & GROWTH"],
        ["Đào Tạo Barista & Cung Ứng B2B Toàn Diện", "Barista Training & Comprehensive B2B Supply"],
        ["Không chỉ là nhà cung cấp nguyên liệu, S54 Coffee là đối tác chiến lược đồng hành cùng hơn 500+ nhà hàng, khách sạn và quán cà phê. Chúng tôi đào tạo kỹ năng Barista chuyên sâu, chuyển giao công thức pha chế độc quyền, setup quầy bar và cung cấp các dòng máy pha espresso công nghiệp tiêu chuẩn quốc tế.", "More than an ingredient supplier, S54 Coffee is a strategic partner accompanying 500+ restaurants, hotels, and cafes. We provide in-depth Barista training, exclusive brewing recipes, bar setup, and commercial espresso machinery."],
'''

idx = txt.find('// 8. OUR STORY')
if idx != -1:
    txt = txt[:idx] + story_pairs + txt[idx:]
    i18n_path.write_text(txt, encoding='utf-8')
    print("✓ Added full authentic story translation pairs to i18n.js")
else:
    print("❌ Could not find // 8. OUR STORY marker in i18n.js")
