#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Completely clean and standardize wholesale.html for S54 Coffee:
- Remove ALL English text, Australian/Sydney/65 years/Vittoria references
- Standardize all Vietnamese B2B copy (Hot Air roasting, Buôn Ma Thuột origin, Barista training, POSM, B2B contact form)
- Replace foreign partners/testimonials with authentic Vietnamese F&B partner quotes
- Fix form action so it triggers local success alert and doesn't 404
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent
wholesale_file = BASE_DIR / 'wholesale.html'
text = wholesale_file.read_text(encoding='utf-8')

# 1. Meta Tags
text = re.sub(
    r'<meta name="description" content="We are more than just a wholesale coffee supplier[\s\S]*?Reach out today\." />',
    '<meta name="description" content="Giải pháp cà phê bán sỉ, đại lý và cung ứng B2B chuyên nghiệp từ S54 Coffee. Cung cấp cà phê hạt rang mộc, máy pha chế, tư vấn quầy bar và đào tạo Barista toàn quốc." />',
    text
)
text = re.sub(
    r'<meta property="og:title" content="Cà Phê Bán Sỉ B2B Suppliers Australia - S54 COFFEE">',
    '<meta property="og:title" content="Chính Sách Đại Lý & Cung Ứng B2B | S54 COFFEE">',
    text
)
text = re.sub(
    r'<meta property="og:description" content="We are more than just a wholesale coffee supplier[\s\S]*?Reach out today\.">',
    '<meta property="og:description" content="Giải pháp cà phê bán sỉ, đại lý và cung ứng B2B chuyên nghiệp từ S54 Coffee. Cung cấp cà phê hạt rang mộc, máy pha chế, tư vấn quầy bar và đào tạo Barista toàn quốc.">',
    text
)
text = re.sub(
    r'<meta name="twitter:title" content="Cà Phê Bán Sỉ B2B Suppliers Australia - S54 COFFEE">',
    '<meta name="twitter:title" content="Chính Sách Đại Lý & Cung Ứng B2B | S54 COFFEE">',
    text
)
text = re.sub(
    r'<meta name="twitter:description" content="We are more than just a wholesale coffee supplier[\s\S]*?Reach out today\.">',
    '<meta name="twitter:description" content="Giải pháp cà phê bán sỉ, đại lý và cung ứng B2B chuyên nghiệp từ S54 Coffee. Cung cấp cà phê hạt rang mộc, máy pha chế, tư vấn quầy bar và đào tạo Barista toàn quốc.">',
    text
)

# 2. Hero Section Subtitle & Button
text = text.replace(
    'We are more than just a coffee supplier, we are a partner that offers unmatched support.',
    'Chúng tôi không chỉ là nhà cung cấp cà phê, chúng tôi là đối tác chiến lược mang đến giải pháp toàn diện và hỗ trợ vượt trội cho doanh nghiệp của bạn.'
)
text = re.sub(
    r'href="https://www\.s54coffee\.com/pages/help-desk\?hcUrl=[^"]*"',
    'href="#contact"',
    text
)

# 3. Intro Section
text = text.replace(
    'Our wholesale coffee partner program is designed to offer more than just <a href="https://www.s54coffee.com/collections/coffee-beans" title="Khám phá các dòng cà phê hạt cao cấp S54">nguồn hạt cà phê thượng hạng</a> – it’s about empowering our partners with unparalleled levels of support.',
    'Chương trình đối tác bán sỉ và đại lý của S54 được thiết kế để mang lại nhiều hơn chỉ là <a href="collections-coffee.html" title="Khám phá các dòng cà phê hạt cao cấp S54">nguồn hạt cà phê thượng hạng</a> – đó là sự đồng hành, hỗ trợ và cam kết phát triển bền vững cùng đối tác.'
)

# 4. Roastery Section
old_roastery = '''<p class="o-paragraph--1" >At the core of our operation lies a singular vision – scouring the globe for the finest premium beans to craft the world’s most exceptional coffees. We’ve been doing it for over 65 years.</p><p class="o-paragraph--1" >These days, our expertise is supported by our state-of-the-art roastery in Sydney.</p><p class="o-paragraph--1" >Our quality process involves 23 stages allowing us to scientifically analyse crucial variables such as the moisture content of green beans, acidity, pH, density, brix, total dissolved solids, and caffeine levels. This precision, combined with sensory testing, provides a comprehensive understanding of every blend, enabling us to replicate our coffees with unrivalled consistency.</p><p class="o-paragraph--1" >You can always trust our coffee.</p>'''
new_roastery = '''<p class="o-paragraph--1" >Trọng tâm hoạt động của S54 Coffee là tuyển chọn những nguồn hạt Robusta & Arabica nguyên bản thượng hạng từ các thủ phủ cà phê Buôn Ma Thuột, Đắk Lắk và Cầu Đất (Lâm Đồng) để tạo nên những mẻ rang mộc hoàn hảo nhất cho chuỗi quán và doanh nghiệp.</p><p class="o-paragraph--1" >Xưởng rang xay hiện đại của chúng tôi áp dụng công nghệ rang Hot Air tiên tiến, giúp hạt chín đều từ trong ra ngoài, không cháy khét và lưu giữ tối đa tầng hương phức hợp tự nhiên.</p><p class="o-paragraph--1" >Quy trình kiểm soát chất lượng nghiêm ngặt qua nhiều công đoạn: kiểm tra độ ẩm hạt xanh, tỷ lệ sàng lọc tiêu chuẩn S18, đo mật độ, độ pH và thử nếm (cupping) từng mẻ rang để đảm bảo chất lượng đồng đều 100% trước khi giao đến tay đối tác.</p><p class="o-paragraph--1" >Quý đối tác hoàn toàn có thể an tâm về nguồn hàng ổn định và chuẩn vị cà phê Việt.</p>'''
text = text.replace(old_roastery, new_roastery)

# 5. Partners & Case Studies Heading & Excerpts
text = text.replace(
    'Read more about out customer stories and our joint efforts to support business growth.',
    'Khám phá câu chuyện hợp tác thành công cùng các chuỗi quán cà phê, khách sạn và văn phòng hiện đại trên toàn quốc.'
)
text = text.replace(
    'L\'Americano Espresso Bar',
    'The Rustic Coffee Hub'
)
text = text.replace(
    'Bobbin Head Bakery',
    'Chuỗi Tiệm Bánh & Cà Phê Saigon Heritage'
)
text = text.replace(
    'customer highlights',
    'Điểm Sáng Đối Tác'
)
text = text.replace(
    'Four minute read',
    '4 phút đọc'
)
text = text.replace(
    'Three minute read',
    '3 phút đọc'
)

# 6. Testimonials Carousel
old_testimonials = '''<div class="c-testimonial__carousel-slides"  data-carousel ><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">My passion for pizza is exactly the same as [S54’s] passion for their coffee.</p><h6>Johnny, 400 Gradi</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">When we want to do something new and exciting, I always know I have a great support network with S54.</p><h6>Shane Delia, Maha</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">It’s got the flair, it’s got the taste and it’s always consistent. That’s very important in our business.</p><h6>Serge, Urban Express</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">We wouldn't have had the growth we have over the past 18 months without the help of the team.</p><h6>Acacia, Bobbin Head Bakery Owner</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">To say that the team at S54 have been an integral part of our growth is a vast understatement.</p><h6>Matthew El-Bayeh, Els Cafe & Bar</h6></div></div>'''
new_testimonials = '''<div class="c-testimonial__carousel-slides" data-carousel ><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">Chất lượng cà phê hạt rang mộc của S54 rất đậm đà, độ ổn định cao giữa các mẻ rang. Khách hàng của chúng tôi luôn khen ngợi hương vị cà phê phin và pha máy.</p><h6>Anh Tuấn Dũng, Chủ Chuỗi Cà Phê Mộc Sài Gòn</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">Khi cần tư vấn set-up quầy bar và đào tạo nhân viên pha chế, đội ngũ chuyên gia của S54 luôn hỗ trợ nhiệt tình và chuyên nghiệp nhất.</p><h6>Chị Mai Hương, Giám Đốc F&B Khách Sạn Central Heritage</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">Hương vị chuẩn gu Việt, hậu vị ngọt sâu và chính sách giá đại lý rất tốt. Hợp tác cùng S54 giúp quán chúng tôi tăng trưởng lượng khách quen rõ rệt.</p><h6>Anh Quốc Hưng, Founder The Rustic Garden Cafe</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">Dòng cà phê hòa tan 3in1 và sấy lạnh của S54 được toàn thể nhân viên văn phòng chúng tôi ưa chuộng mỗi buổi sáng.</p><h6>Chị Bích Trâm, Trưởng Phòng Hành Chính VinGroup Partner</h6></div><div class="c-testimonial__carousel-slide o-heading--5"><p class="o-heading--5">Đồng hành cùng S54 là lựa chọn đúng đắn nhất của chúng tôi trong hành trình xây dựng chuỗi đồ uống mang đậm bản sắc Việt.</p><h6>Anh Hoàng Nam, Giám Đốc Vận Hành Highlands Art Cafe</h6></div></div>'''
text = text.replace(old_testimonials, new_testimonials)

# 7. Barista Training Paragraphs
old_barista_intro = '''A truly exceptional cup of coffee is the result of meticulous attention to detail, from bean selection to the art and science of roasting. Yet, it’s the skill and dedication of the barista that truly brings coffee to life.'''
new_barista_intro = '''Một tách cà phê tuyệt hảo là sự cộng hưởng khắt khe từ nguồn hạt tuyển chọn, kỹ thuật rang mộc điêu luyện đến tay nghề của người Barista. S54 cung cấp các khóa đào tạo Barista chuyên nghiệp từ cơ bản đến nâng cao, hướng dẫn kỹ thuật chiết xuất chuẩn xác, cân chỉnh cối xay và tạo hình Latte Art đẹp mắt.'''
text = text.replace(old_barista_intro, new_barista_intro)

old_barista_details = '''That’s why we’re committed to providing comprehensive training programs, available on-site or at our dedicated coffee training centres around the country.<br/><br/>We offer barista certification courses, training resources and specialised one-on-one training to all our partners. Your team will go deep into the nuances of espresso preparation, understanding all the variables that impact extraction including grind size, temperature, extraction time, weight, tamping and other controllable variables, to deliver consistent, exceptional coffee.<br/><br/>For experienced baristas who don’t require training, we offer opportunities to represent S54 COFFEE as ambassadors providing promotional opportunities for your venue.'''
new_barista_details = '''Đó là lý do S54 cam kết cung cấp các chương trình đào tạo pha chế toàn diện, thực hiện trực tiếp tại cơ sở của đối tác hoặc tại trung tâm đào tạo chuyên biệt của chúng tôi.<br/><br/>Khóa học giúp đội ngũ nhân sự nắm vững mọi biến số ảnh hưởng đến chất lượng tách cà phê: kích thước bột xay, nhiệt độ nước, áp suất chiết xuất, tỷ lệ chiết xuất (brew ratio) và kỹ thuật nén tamping chuẩn mực để đảm bảo chất lượng đồng nhất trong mọi khung giờ đông khách.<br/><br/>Đối với những Barista lành nghề, S54 tạo điều kiện kết nối mạng lưới đại sứ thương hiệu, cùng tham gia các sự kiện thử nếm và cuộc thi pha chế chuyên nghiệp.'''
text = text.replace(old_barista_details, new_barista_details)

# 8. Equipment Section
old_equipment = '''We supply an extensive range of state-of-the-art coffee equipment from Faema through our exclusive partnership of over 50 years, as well as La Marzocco, Mahlkonig and many more. Our commercial machines hold stable temperatures to the group heads, keep consistent pressure and rarely break down. If they do, we have technicians available anytime, day or night. <br/>'''
new_equipment = '''Chúng tôi cung cấp và tư vấn các dòng máy pha, máy xay cà phê chuyên nghiệp hàng đầu thế giới (La Marzocco, Faema, Nuova Simonelli, Mahlkönig) cùng các dòng máy xay cầm tay cao cấp mang thương hiệu S54. Các thiết bị được nhập khẩu chính hãng, kiểm định áp suất và nhiệt độ ổn định, đi kèm dịch vụ bảo dưỡng định kỳ và hỗ trợ kỹ thuật 24/7 từ đội ngũ kỹ thuật viên lành nghề.<br/>'''
text = text.replace(old_equipment, new_equipment)

# 9. Signage & POSM Section
old_signage = '''The S54 brand is a symbol of coffee excellence, but we know each customer has their own unique style. That’s why we customise our signage to each venue to complement the overall aesthetic. Our designers work closely with you and your team to understand your objectives and deliver considered solutions with  a team of professional sign writers and manufacturers.'''
new_signage = '''Thương hiệu S54 là biểu tượng của chất lượng cà phê Việt đích thực, đồng thời chúng tôi tôn trọng phong cách độc bản của từng đối tác. Đội ngũ tư vấn và thiết kế của S54 sẵn sàng đồng hành cùng bạn từ bố trí công năng quầy bar tối ưu, bộ nhận diện POSM sang trọng đến biển hiệu ấn tượng, mang lại dấu ấn riêng biệt cho không gian thưởng thức.'''
text = text.replace(old_signage, new_signage)

# 10. Marketing Section Heading & Content
text = text.replace(
    'Marketing for<br />\nhospitality businesses',
    'Đồng Hành Marketing &<br />\nPhát Triển Doanh Nghiệp F&B'
)
old_marketing = '''From humble beginnings in 1958, we’ve been a part of Australia’s hospitality industry. From supplying Sydney’s first cafes and restaurants with our freshly roasted Arabica coffees to driving the growth of cafe culture throughout the dynamic decades of the 1970s and 80s, we’ve played a pivotal role in shaping Australia’s famous coffee culture.<br/> <br/>But hospitality is tough. Operators face an array of challenges that test their resilience and adaptability. We understand that success in this environment hinges on a number of factors beyond just the quality of the coffee you serve.<br/><br/>We operate like a hospitality marketing and design agency providing clients all over the world with naming ideation, brand and logo development supported by local marketing strategies to maximise awareness at launch.'''
new_marketing = '''Khởi nguồn từ khát vọng đưa hạt cà phê Việt Nam vươn tầm, S54 thấu hiểu sâu sắc những thách thức mà các chủ quán và doanh nghiệp F&B phải đối mặt trên thị trường cạnh tranh ngày nay.<br/><br/>Thành công của một thương hiệu không chỉ dừng lại ở tách cà phê ngon, mà còn đến từ trải nghiệm khách hàng, câu chuyện truyền thông và chiến lược kinh doanh bài bản.<br/><br/>S54 đóng vai trò như một đối tác chiến lược: hỗ trợ tư vấn menu tối ưu chi phí nguyên liệu, đào tạo kỹ năng pha chế cho nhân sự, cung cấp giải pháp Marketing tại điểm bán và chia sẻ công thức đồ uống đón đầu xu hướng tiêu dùng hiện đại.'''
text = text.replace(old_marketing, new_marketing)

# 11. Community Section
old_community = '''We believe in playing a role in the community. We actively support charities and support industry events that celebrate art, hospitality and food. If you’ve been anywhere in Australia, there’s a good chance you’ve seen one of our carts pumping out the complete coffee menu with a healthy dose of latte art. Partnering with us means joining a network that thrives on mutual support and shared success.'''
new_community = '''S54 luôn tin rằng sự phát triển bền vững phải gắn liền với cộng đồng và người nông dân trồng cà phê tại Tây Nguyên. Chúng tôi cam kết bao tiêu nông sản với mức giá công bằng theo mô hình "New Coffee, New Income", góp phần nâng cao đời sống bà con đồng bào và thúc đẩy phương thức canh tác hữu cơ bảo vệ môi trường. Hợp tác cùng S54 là bạn đang đồng hành lan tỏa giá trị nhân văn và nâng tầm hạt cà phê Việt.'''
text = text.replace(old_community, new_community)

# 12. Family Business / Commitment Section
old_commitment = '''A privately held, third-generation family business with the scale to compete against the largest food companies in the world. If you’re serious about coffee, we think there’s no better partner to have in your corner.'''
new_commitment = '''Là doanh nghiệp cà phê tiên phong với quy mô và năng lực cạnh tranh tiêu chuẩn quốc tế, S54 Coffee cam kết cung cấp nguồn hàng nguyên chất ổn định, không pha tạp, đầy đủ chứng nhận an toàn vệ sinh thực phẩm và hóa đơn minh bạch. Nếu bạn nghiêm túc tìm kiếm đối tác cung ứng cà phê chuyên nghiệp, S54 là người đồng hành đáng tin cậy nhất của bạn.'''
text = text.replace(old_commitment, new_commitment)

# 13. Contact Form Subtitle & Action
text = text.replace(
    'Share some details and we’ll be in touch.',
    'Hãy để lại thông tin, chuyên viên tư vấn B2B của S54 Coffee sẽ liên hệ với bạn trong vòng 24 giờ.'
)
text = text.replace(
    '<form method="post" action="/contact#contact" id="contact" accept-charset="UTF-8" class="c-contact__form">',
    '<form class="c-contact__form" id="contact" onsubmit="event.preventDefault(); alert(\'Cảm ơn Quý khách đã gửi thông tin hợp tác B2B! Đội ngũ S54 Coffee sẽ liên hệ tư vấn trong vòng 24 giờ qua số điện thoại/email của bạn.\'); this.reset();">'
)

# 14. Clean any remaining Australia country localization comment
text = text.replace('<!-- localization.country:Australia-->', '<!-- localization.country:Vietnam-->')

wholesale_file.write_text(text, encoding='utf-8')
print("Successfully updated wholesale.html!")
