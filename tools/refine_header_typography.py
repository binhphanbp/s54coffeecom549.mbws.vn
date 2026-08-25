import re
import os

font_link = '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">'

html_files = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

for hf in html_files:
    if not os.path.exists(hf):
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Google Fonts link to include Be Vietnam Pro
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Cormorant\+Garamond[^"]*" rel="stylesheet">',
        font_link,
        html
    )

    # Convert uppercase topbar message to elegant title/sentence case
    html = html.replace(
        'MIỄN PHÍ VẬN CHUYỂN TOÀN QUỐC CHO ĐƠN TỪ 599.000₫ • HOTLINE: 0383.707.578',
        'Miễn phí vận chuyển toàn quốc cho đơn từ 599.000₫ • Hotline: 0383.707.578'
    )

    # Convert uppercase menu links to Title Case
    html = html.replace('>TẤT CẢ SẢN PHẨM<', '>Tất Cả Sản Phẩm<')
    html = html.replace('>CÀ PHÊ HẠT & RANG MỘC<', '>Cà Phê Hạt & Rang Mộc<')
    html = html.replace('>HÒA TAN & SẤY LẠNH<', '>Hòa Tan & Sấy Lạnh<')
    html = html.replace('>CÂU CHUYỆN S54<', '>Câu Chuyện S54<')
    html = html.replace('>B2B & ĐẠI LÝ<', '>B2B & Đại Lý<')

    with open(hf, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated header typography in {hf}")

print("All HTML files updated with Be Vietnam Pro and elegant Title Case.")
