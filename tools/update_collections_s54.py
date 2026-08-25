#!/usr/bin/env python3
import re
from pathlib import Path

coll_file = Path('collections-coffee.html')
c = coll_file.read_text(encoding='utf-8')

# Replace product names
c = re.sub(r'Cinque Stelle Special Bar Beans', 'S54 Robusta Cà Phê Rang Mộc', c)
c = re.sub(r'Oro Coffee Beans', 'S54 Arabica Cầu Đất Thượng Hạng', c)
c = re.sub(r'Organic Coffee Beans', 'S54 Cà Phê Hòa Tan 3-in-1 Đậm Vị', c)
c = re.sub(r'Black Valley Beans', 'S54 Cà Phê Sấy Lạnh Cao Cấp', c)
c = re.sub(r'Espresso Coffee Beans', 'S54 Cà Phê Túi Lọc Drip Bag', c)
c = re.sub(r'Mountain Grown Beans', 'S54 Cà Phê Xay Pha Phin Chuẩn Vị', c)

# Replace product images
c = re.sub(r'assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_.*?\.png', 'assets/images/s54/robusta_1.jpg', c)
c = re.sub(r'assets/images/049_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_.*?\.png', 'assets/images/s54/arabica_beans.jpg', c)
c = re.sub(r'assets/images/091_MicrosoftTeams-image_279_.*?\.png', 'assets/images/s54/instant_3in1_1.jpg', c)
c = re.sub(r'assets/images/151_ground_1kg_esp_f_R_Car_3_.*?\.png', 'assets/images/s54/freeze_dried_blend.jpg', c)
c = re.sub(r'assets/images/014_inst_100g_clas_f_V2_d7df202b-71d9-4a81-a29d-9af211d42e34_.*?\.png', 'assets/images/s54/instant_box.png', c)
c = re.sub(r'assets/images/247_bag_20pack_esp_f_V2_.*?\.png', 'assets/images/s54/robusta_2.jpg', c)

# Replace prices
c = re.sub(r'\$60\.50 AUD', '150.000₫', c)
c = re.sub(r'\$44\.00 AUD', '185.000₫', c)
c = re.sub(r'\$48\.50 AUD', '125.000₫', c)
c = re.sub(r'\$42\.00 AUD', '195.000₫', c)
c = re.sub(r'\$38\.00 AUD', '135.000₫', c)
c = re.sub(r'\$36\.00 AUD', '150.000₫', c)

coll_file.write_text(c, encoding='utf-8')
print("✓ Updated collections-coffee.html with authentic S54 product listings")
