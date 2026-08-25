#!/usr/bin/env python3
import re
from pathlib import Path

i18n_path = Path('assets/js/i18n.js')
c = i18n_path.read_text(encoding='utf-8')

# Add S54 specific translation pairs
s54_pairs = """
        // S54 Coffee Specifics
        ["MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578", "FREE NATIONWIDE SHIPPING ON ORDERS OVER 599,000₫ • HOTLINE: (+84) 383 707 578"],
        ["S54 COFFEE - Tinh Hoa Cà Phê Việt®", "S54 COFFEE - The Essence of Vietnamese Coffee®"],
        ["Khám Phá Dòng Cà Phê S54", "Discover S54 Coffee Range"],
        ["“S54 Coffee mang đến giải pháp cà phê sạch nguyên chất, đậm đà vị truyền thống và phong cách hiện đại cho hàng triệu người tiêu dùng.”", "“S54 Coffee delivers pure, clean coffee solutions with authentic rich flavor and modern style to millions of consumers.”"],
        ["Mr. Paul Hieu (CEO) & Tony Hoan (Founder)", "Mr. Paul Hieu (CEO) & Tony Hoan (Founder)"],
        ["Hơn 12 Năm Kinh Nghiệm & Đam Mê Cà Phê Sạch", "Over 12 Years of Clean Coffee Passion & Expertise"],
        ["Thành lập từ năm 2012 bởi Công ty TNHH Giải Pháp Tốt (Good Solutions), S54 Coffee tự hào kế thừa tinh hoa cà phê Robusta & Arabica từ vùng đất đỏ bazan Tây Nguyên (Đắk Lắk, Lâm Đồng). Chúng tôi áp dụng quy trình kiểm soát nghiêm ngặt từ hạt giống, nông trại thông minh đến công nghệ rang mộc hiện đại, lưu giữ trọn vẹn hương thơm tự nhiên và hậu vị sâu lắng đặc trưng của cà phê Việt.", "Established in 2012 by Good Solutions Co., Ltd, S54 Coffee inherits the finest Robusta & Arabica beans from the Central Highlands (Dak Lak, Lam Dong). We employ rigorous quality control from smart farming to modern artisan roasting."],
        ["Nghệ Thuật Pha Chế & Thưởng Thức Cà Phê S54 Chuẩn Vị", "The Art of Brewing & Enjoying Authentic S54 Coffee"],
        ["Cùng chuyên gia S54 Coffee khám phá bí quyết chiết xuất tách Espresso thơm ngậy với lớp crema dày sánh mịn hoặc pha phin truyền thống đậm đà khó quên.", "Join S54 Coffee experts to discover the secrets of brewing rich Espresso with golden crema or traditional Vietnamese drip coffee."],
        ["S54 Robusta Rang Mộc Nguyên Chất", "S54 Pure Roasted Robusta Beans"],
        ["S54 Arabica Cầu Đất Thượng Hạng", "S54 Premium Cau Dat Arabica"],
        ["S54 Hòa Tan 3-in-1 Hộp 456g", "S54 Instant Coffee 3-in-1 (456g)"],
        ["S54 Cà Phê Sấy Lạnh Cao Cấp", "S54 Premium Freeze-Dried Blend"],
        ["S54 Cà Phê Túi Lọc Drip Bag", "S54 Drip Bag Coffee Sachets"],
        ["S54 Robusta Xay Pha Phin", "S54 Traditional Ground Robusta"],
        ["5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Mỗi Ngày Cho Sức Khỏe", "5 Amazing Health Benefits of Drinking Coffee Daily"],
        ["Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp", "How to Distinguish Pure Artisan Roasted Coffee from Mixed Coffee"],
        ["So Sánh Hương Vị Đậm Đà Của S54 Robusta Và Chua Thanh Của S54 Arabica", "Comparing the Bold Flavor of S54 Robusta with the Crisp Acidity of S54 Arabica"],
        ["Kết Nối Cùng S54 Coffee Trên Mạng Xã Hội", "Connect with S54 Coffee on Social Media"],
        ["Đăng Ký Nhận Ưu Đãi & Tin Tức Cà Phê Mới Nhất", "Subscribe for Exclusive Offers & Coffee News"],
        ["Nhận ngay voucher giảm 15% cho đơn hàng đầu tiên cùng cẩm nang pha chế cà phê độc quyền từ S54 Coffee.", "Get 15% off your first order plus an exclusive brewing guide from S54 Coffee."],
        ["CÔNG TY TNHH GIẢI PHÁP TỐT (GOOD SOLUTIONS CO., LTD)", "GOOD SOLUTIONS COMPANY LIMITED (S54 COFFEE)"],
        ["Số 35, Đường T8, Manhattan, Vinhomes Grand Park, P. Long Bình, TP. Thủ Đức, TP. Hồ Chí Minh", "No. 35, T8 Street, Manhattan, Vinhomes Grand Park, Long Binh Ward, Thu Duc City, HCMC, Vietnam"],
        ["Chính Sách Đại Lý & Cung Ứng B2B", "Wholesale & B2B Supply Policy"],
        ["Dịch Vụ Cung Ứng Cà Phê B2B & Gia Công OEM/ODM", "B2B Coffee Supply & Private Label OEM/ODM Services"],
"""

c = c.replace('const translationPairs = [', 'const translationPairs = [' + s54_pairs)
i18n_path.write_text(c, encoding='utf-8')
print("✓ Enhanced i18n.js with S54 Coffee translation pairs")
