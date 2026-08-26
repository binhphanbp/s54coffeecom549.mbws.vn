#!/usr/bin/env python3
import re
from pathlib import Path

i18n_path = Path('assets/js/i18n.js')
c = i18n_path.read_text(encoding='utf-8')

blog_pairs = """
        // Blog & News
        ["Tin Tức & Kiến Thức Cà Phê", "News & Coffee Insights"],
        ["Góc Thưởng Thức S54", "S54 Coffee Journal"],
        ["Tất Cả Bài Viết", "All Articles"],
        ["Kiến Thức Cà Phê", "Coffee Insights"],
        ["Câu Chuyện S54", "S54 Stories"],
        ["Hướng Dẫn Pha Chế", "Brewing Guides"],
        ["Bản Tin Extracts", "Extracts Newsletter"],
        ["Các Bài Viết Mới Nhất", "Latest Articles"],
        ["Đọc Bài Viết", "Read Article"],
        ["Đọc Tiếp →", "Read More →"],
        ["5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết", "5 Amazing Benefits of Drinking Coffee You Might Not Know"],
        ["Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp", "How to Distinguish Pure Roasted Coffee vs Adulterated Coffee"],
        ["← Quay lại Tin Tức", "← Back to News"],
        ["← Xem Tất Cả Bài Viết", "← View All Articles"],
"""

if '["Góc Thưởng Thức S54"' not in c:
    c = c.replace('const translationPairs = [', 'const translationPairs = [' + blog_pairs)
    i18n_path.write_text(c, encoding='utf-8')
    print("✓ Added blog translation pairs to i18n.js")
else:
    print("ℹ Blog pairs already exist in i18n.js")
