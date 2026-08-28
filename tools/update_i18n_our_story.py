#!/usr/bin/env python3
"""
Add bilingual dictionary entries for the updated Giới Thiệu (Our Story) page
"""

from pathlib import Path

BASE_DIR = Path('/home/binhphan/matbao-ws/clients/s54coffeecom549.mbws.vn')

our_story_pairs = '''
        // 8. OUR STORY (GIỚI THIỆU S54 COFFEE)
        ["S54 COFFEE • VIETNAMESE COFFEE. MADE FOR THE WORLD.", "S54 COFFEE • VIETNAMESE COFFEE. MADE FOR THE WORLD."],
        ["Hành Trình Tinh Hoa Cà Phê Việt & Sứ Mệnh 54 Dân Tộc", "The Vietnamese Coffee Heritage & 54 Ethnic Unity"],
        ["Tự hào mang tên gọi kết hợp giữa hình ảnh dải đất hình chữ S và 54 dân tộc anh em, S54 Coffee ra đời với sứ mệnh nâng tầm hạt cà phê Robusta và Arabica từ thủ phủ Tây Nguyên vươn tầm quốc tế theo phương châm \\"New Coffee, New Income\\".", "Named after the S-shaped Vietnamese land and 54 brotherly ethnic groups, S54 Coffee elevates Central Highlands Robusta & Arabica globally under the motto \\"New Coffee, New Income\\"."],
        ["GIỚI THIỆU CHUNG", "ABOUT S54 COFFEE"],
        ["Cà Phê Nguyên Bản Cho Năng Lượng & Giá Trị Bền Vững", "Pure Vietnamese Coffee For Energy & Sustainable Growth"],
        ["S54 Coffee mang đến những trải nghiệm cà phê nguyên bản, đậm đà—từ các dòng cà phê hòa tan 3in1 tiện lợi đến cà phê hạt rang chất lượng cao, lưu giữ trọn vẹn hương vị mộc mạc của đất trời Tây Nguyên.", "S54 Coffee delivers authentic, rich coffee experiences—from convenient 3-in-1 instant blends to premium roasted whole beans that preserve the true spirit of Central Highlands."],
        ["Với phương châm \\"New Coffee, New Income\\", S54 Coffee không chỉ cung cấp nguồn năng lượng tỉnh táo, sáng tạo mỗi ngày mà còn hướng tới xây dựng giá trị phát triển bền vững và cơ hội thu nhập cho cộng đồng.", "With our core motto \\"New Coffee, New Income\\", S54 Coffee empowers daily creative energy while creating sustainable economic opportunities for our farming community."],
        ["ĐỊNH HƯỚNG CHIẾN LƯỢC", "STRATEGIC PILLARS"],
        ["Tầm Nhìn • Sứ Mệnh • Giá Trị Cốt Lõi", "Vision • Mission • Core Values"],
        ["Tầm Nhìn", "Our Vision"],
        ["Trở thành thương hiệu cà phê Việt uy tín, vươn tầm quốc tế với các dòng sản phẩm chất lượng cao và sáng tạo.", "To become a globally prestigious Vietnamese coffee brand renowned for quality and innovation."],
        ["Sứ Mệnh", "Our Mission"],
        ["Mang đến tách cà phê chuẩn vị, truyền năng lượng tích cực và tạo dựng thu nhập bền vững cho cộng đồng (New Coffee, New Income).", "Delivering authentic coffee, inspiring positive energy, and creating sustainable incomes."],
        ["Giá Trị Cốt Lõi", "Core Values"],
        ["Trung thực: Minh bạch nguồn gốc và chất lượng.", "Honesty: Transparent origin and quality."],
        ["Chất lượng: Chuẩn vị nguyên bản từng mẻ rang.", "Quality: Authentic taste in every batch."],
        ["Cải tiến: Ứng dụng công nghệ hiện đại.", "Innovation: Modern roasting technology."],
        ["Đồng hành: Cùng phát triển bền vững.", "Partnership: Growing sustainably together."],
        ["HÀNH TRÌNH PHÁT TRIỂN", "OUR DEVELOPMENT MILESTONES"],
        ["Các Cột Mốc Đột Phá Của S54 Coffee", "Key Breakthrough Milestones"],
        ["Cột Mốc 1", "Milestone 1"],
        ["Nghiên Cứu & Phát Triển Chuẩn Vị Tây Nguyên", "R&D and Authentic Taste Formulation"],
        ["Nghiên cứu và phát triển thành công dòng sản phẩm cà phê hòa tan 3in1 tiện lợi & cà phê hạt rang chất lượng cao chuẩn vị thủ phủ Tây Nguyên.", "Successfully formulated authentic instant 3-in-1 and premium roasted whole beans from Central Highlands."],
        ["Cột Mốc 2", "Milestone 2"],
        ["Mở Rộng Hệ Thống Phân Phối & Lan Tỏa Thương Hiệu", "Expanding Distribution & Brand Outreach"],
        ["Mở rộng hệ thống phân phối, phát triển chuỗi cửa hàng trải nghiệm và định hình thông điệp thương hiệu S54 Coffee \\"New Coffee, New Income\\".", "Expanded commercial distribution networks and established the brand message \\"New Coffee, New Income\\"."],
        ["Cột Mốc 3", "Milestone 3"],
        ["Số Hóa Thương Hiệu & Nền Tảng Đa Kênh Hiện Đại", "Digital Transformation & Omnichannel Commerce"],
        ["Số hóa toàn diện thương hiệu, hoàn thiện website bán hàng chuyên nghiệp, tích hợp Core Admin quản trị hiện đại và mở rộng kết nối đối tác quốc tế.", "Fully digitized brand operations with a professional e-commerce platform and modern Core Admin backend."],
        ["HỆ THỐNG VĂN PHÒNG & CỬA HÀNG THỰC TẾ", "OUR OFFICES & COFFEE SHOPS"],
        ["Không Gian Trải Nghiệm S54 Coffee", "Experience S54 Coffee Spaces"],
        ["Văn Phòng S54 Coffee", "S54 Coffee Office"],
        ["The Manhattan, Vinhomes Grand Park, TP. Thủ Đức", "The Manhattan, Vinhomes Grand Park, Thu Duc City"],
        ["Trụ Sở Điều Hành", "Executive Headquarters"],
        ["Không gian làm việc sáng tạo & đào tạo barista", "Creative workspace and barista training center"],
        ["Quán Cafe S54 Coffee", "S54 Coffee Shop"],
        ["Điểm trải nghiệm cà phê nguyên bản tại Nhà Bè, TP.HCM", "Artisan coffee experience destination in Nha Be, HCMC"],
'''

for target_file in [BASE_DIR / 'assets/js/i18n.js', BASE_DIR / 'public/client-assets/js/i18n.js']:
    if not target_file.exists():
        continue
    content = target_file.read_text(encoding='utf-8')
    # Replace the existing section 8 if present
    if '// 8. OUR STORY' in content:
        # replace from '// 8. OUR STORY' to next section or end
        import re
        content = re.sub(r'// 8\. OUR STORY[\s\S]*?(?=// 9|\n\s*\];)', our_story_pairs.strip() + '\n        ', content)
    else:
        # insert before closing bracket
        idx = content.rfind('];')
        if idx != -1:
            content = content[:idx] + our_story_pairs + content[idx:]
    target_file.write_text(content, encoding='utf-8')
    print(f"✓ Updated i18n file: {target_file}")

print("✅ Updated i18n for Our Story successfully!")
