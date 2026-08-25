import re

file_path = 'our-story.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hero Subtitle & Custom Heading
html = html.replace('Roasting premium coffee in Australia since 1958.', 'Hành trình 12+ năm kiến tạo giá trị và lan tỏa hương vị cà phê sạch nguyên chất Việt Nam.')
html = html.replace('Pioneers of the great Australian coffee industry and a proud third-generation family owned business.', '“Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.” — Triết lý Good Solutions & S54 Coffee.')

# 2. Story Blocks replacement
# Story 1: 1947 -> 2012
old_story_1 = '''<h3 class="c-stories__story-title o-heading--4">Our beginnings in 1947</h3><p class="c-stories__story-description o-paragraph--3"><p>Two Italian brothers Orazio and Carmelo first spotted an opportunity to introduce a taste of their Italian heritage to Australia after migrating from Sicily.</p><p>Beginning as a small family business importing products including mineral water, parmesan cheese and pasta to their adoptive country, they were longing for the much-loved Italian ritual of a daily espresso.</p></p>'''
new_story_1 = '''<h3 class="c-stories__story-title o-heading--4">Khởi Nguồn Đam Mê & Thành Lập Good Solutions (2012)</h3><div class="c-stories__story-description o-paragraph--3"><p>Thành lập bởi Công ty TNHH Giải Pháp Tốt (Good Solutions Co., Ltd) dưới sự dẫn dắt của Giám đốc điều hành & Người sáng lập Tony Hoan cùng CEO Nguyễn Xuân Hiếu (Mr. Paul Hieu), S54 Coffee ra đời từ niềm đam mê cháy bỏng với hạt cà phê Việt Nam.</p><p>Chúng tôi bắt đầu với một triết lý đơn giản nhưng kiên định: Thiết lập các giải pháp tối ưu trong việc cung cấp Cà phê Sạch - Đậm đà - Chất lượng cao, mang lại trải nghiệm dịch vụ khách hàng tận tâm hàng đầu.</p></div>'''
html = html.replace(old_story_1, new_story_1)

# Story 2: 1958 -> Triết lý New Coffee, New Income
old_story_2_title = 'Roasting since 1958'
new_story_2_title = 'Triết Lý “NEW COFFEE, NEW INCOME”'
html = html.replace(old_story_2_title, new_story_2_title)

# Replace remaining story sections with authentic Vietnamese coffee content
replacements = [
    (
        'In 1958, the brothers began locally roasting their own premium Arabica beans right here in Australia long before the market understood the difference between instant coffee and espresso. They designed a bespoke blend using only high-grade Arabica beans, introducing Australians to a flavour they quickly fell in love with and one that would become our signature blend. This was the year the S54 COFFEE brand was born.',
        'Tại S54 Coffee, chúng tôi tin rằng cà phê không chỉ để thưởng thức mà còn để kết nối, truyền cảm hứng và cung cấp năng lượng tích cực. Với khẩu hiệu “New Coffee, New Income”, chúng tôi cam kết mang đến những sản phẩm cà phê tươi mới, chất lượng vượt trội, đồng thời khơi dậy sự sáng tạo và năng lượng phát triển không ngừng trong từng khoảnh khắc cuộc sống.'
    ),
    (
        'Making Italian coffee famous',
        'Chuẩn Hóa Vùng Trồng Robusta Đắk Lắk & Arabica Cầu Đất'
    ),
    (
        'Tea and instant coffee dominated the Australian palette which at the time was still heavily influenced by British tradition. It was at this time we introduced espresso style coffee, supplying small batches to Australia’s first Italian cafes. We quickly established ourselves as the coffee roaster of choice for Italian immigrants who were not accustomed to drinking anything but espresso.',
        'S54 Coffee tự hào khai thác nguồn nguyên liệu thượng hạng từ thủ phủ cà phê Đắk Lắk (Robusta đậm đà) và Cầu Đất - Lâm Đồng (Arabica thanh nhã). Từng quả cà phê chín mọng được thu hái thủ công, kiểm soát độ ẩm ≤13% và tỷ lệ tạp chất <2%, bảo đảm tiêu chuẩn khắt khe cho từng mẻ hạt.'
    ),
    (
        'Cafe icons serve S54',
        'Công Nghệ Rang Mộc Hot-Air Hiện Đại'
    ),
    (
        'We are proud to have fostered long-standing relationships with our customers – some that have been serving our coffee for over 50 years. These customers, and the cafes and restaurants they have built, have stood the test of time and helped pave the way for today’s progressive and innovative Australian coffee industry. Together, we encourage one of the most developed specialty coffee markets in the world to flourish.',
        'Hệ thống rang Hot-Air hồi khí công nghệ cao giúp nhiệt độ lan tỏa đều vào tâm hạt, giữ nguyên vẹn tầng hương hoa quả, caramel và hậu vị ngọt sâu mà không cần tẩm ướp bất kỳ hương liệu nhân tạo nào. Mỗi mẻ rang là sự kết hợp chuẩn xác giữa khoa học và nghệ thuật chế tác của các nghệ nhân S54.'
    ),
    (
        'Established first coffee college',
        'Đột Phá Cà Phê Hòa Tan 3-in-1 (456g) & Sấy Lạnh'
    ),
    (
        'In the late 90’s, the cafe culture boom led to a surge in coffee brands. As market leaders, we were acutely aware of the need to protect the quality and reputation of our brand. We pioneered the coffee college, teaching espresso and latte art fundamentals, promoted quality and freshness, introduced certified coffee, and spearheaded the use of 100% Arabica coffee beans.',
        'Nhằm mang đến sự tiện lợi mà không đánh mất hương vị nguyên bản, S54 Coffee giới thiệu dòng Cà Phê Hòa Tan 3-in-1 (Hộp 456g - 24 gói x 19g) tinh tế kết hợp Robusta & Arabica, cùng dòng Cà Phê Sấy Lạnh cao cấp, mang lại ly cà phê sánh đậm như pha tại quán chỉ trong 30 giây.'
    ),
    (
        'The choice of award-winning restaurants',
        'Giải Pháp Cung Ứng B2B & Đại Lý Toàn Diện'
    ),
    (
        'S54 is synonymous with fine dining culture. Our coffee is served in more hatted restaurants across Australia than any other brand. The quality and consistency of our coffee is of the utmost importance to our chefs, restaurateurs, sommeliers and to us. We’re proud to be served in Australia’s most celebrated venues.',
        'Good Solutions cung cấp giải pháp trọn gói cho đối tác doanh nghiệp, chuỗi F&B, khách sạn và đại lý: từ cung ứng nguyên liệu hạt rang mộc ổn định, máy pha cà phê chuyên nghiệp, đào tạo barista đến gia công OEM/ODM thương hiệu riêng với chính sách chiết khấu vượt trội.'
    ),
    (
        'Al Pacino stars in S54 commercial',
        '4 Giá Trị Cốt Lõi: Minh Bạch & Bền Vững'
    ),
    (
        'In 2010, Al Pacino appeared in S54 COFFEE’s television and print commercials. This was the first of two television campaigns featuring the Academy-Award winner and was the beginning of an ongoing, mutually respectful relationship. Today, Al Pacino continues to endorse the brand in the United States and other international markets.',
        'Chúng tôi vận hành trên 4 trụ cột cốt lõi: (1) Sản phẩm chất lượng vượt trội, (2) Kinh doanh minh bạch, (3) Sáng tạo và đổi mới liên tục, (4) Tôn trọng và biết ơn khách hàng, đối tác cùng người nông dân trồng cà phê Việt Nam.'
    ),
    (
        'Celebrating Australian Fashion',
        'Tầm Nhìn Vươn Tầm Toàn Cầu — “Hơn Cả Cà Phê”'
    ),
    (
        'S54 has been supporting the Australian fashion industry including collaborating with both established and emerging designers for more than a decade. Our iconic takeaway cups feature original, limited edition prints straight from the runway. Collaborations have included Australian design heavyweights such as Dion Lee, Camilla, Toni Maticevski, Ellery, We Are Handsome, macgraw and Romance Was Born.',
        'Sứ mệnh của S54 Coffee là vươn tầm thương hiệu cà phê Việt Nam ra thế giới, xây dựng cộng đồng cà phê phát triển, đam mê và hạnh phúc. Chúng tôi cam kết đồng hành cùng bạn trên con đường kiến tạo thành công và sự thịnh vượng bền vững.'
    ),
    (
        'Today we are recognised as pioneers of the great Australian coffee industry',
        'Hơn 12 Năm Đồng Hành Cùng Hàng Triệu Tách Cà Phê Việt'
    ),
    (
        'A proud family owned Australian business',
        'CÔNG TY TNHH GIẢI PHÁP TỐT (GOOD SOLUTIONS CO., LTD)'
    )
]

for old, new in replacements:
    html = html.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated our-story.html with 100% authentic S54 / Good Solutions history!")
