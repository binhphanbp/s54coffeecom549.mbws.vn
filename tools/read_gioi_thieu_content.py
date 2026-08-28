#!/usr/bin/env python3
import urllib.request
import os
import csv
from read_gioi_thieu_folder import get_items

# 1. Download GIỚI THIỆU spreadsheet as CSV
url = 'https://docs.google.com/spreadsheets/d/1oEWA7t_CouXiIXHLyaTkoctfL0cEHe0Z0JAxKYthi6I/export?format=csv'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    content = urllib.request.urlopen(req).read()
    with open('drive_data/Gioi_Thieu.csv', 'wb') as f:
        f.write(content)
    print("✓ Downloaded drive_data/Gioi_Thieu.csv")
except Exception as e:
    print(f"Error downloading GIỚI THIỆU csv: {e}")

# 2. Print all rows in Gioi_Thieu.csv
print("\n=== NỘI DUNG SHEET 'GIỚI THIỆU' ===")
if os.path.exists('drive_data/Gioi_Thieu.csv'):
    with open('drive_data/Gioi_Thieu.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if any(row):
                print(f"Row {i}:")
                for col_idx, col in enumerate(row):
                    if col.strip():
                        print(f"   Col {col_idx}: {col}")

# 3. List images in 'Ảnh cửa hàng, doanh nghiệp'
img_folder_id = '1Dvg66RQlRMQB-YS_fWwH87zZosulaA3h'
print("\n=== DANH SÁCH ẢNH TRONG 'Ảnh cửa hàng, doanh nghiệp' ===")
img_items = get_items(img_folder_id)
for it in img_items:
    print(f"- {it['name']} (ID: {it['id']})")

