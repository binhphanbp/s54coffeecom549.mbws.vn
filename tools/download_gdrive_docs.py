#!/usr/bin/env python3
import urllib.request
import os

docs_to_download = [
    {
        'name': 'Tong_hop_va_goi_y_thay_doi_noi_dung_web.xlsx',
        'url': 'https://docs.google.com/spreadsheets/d/186rxa5XAICsRjv7EhsQR59lewAl5_PcX/export?format=xlsx'
    },
    {
        'name': 'San_Pham.csv',
        'url': 'https://docs.google.com/spreadsheets/d/1NJV03zhjPohFvG7NEqgrYpassNFrmg3hE4TATB4YM_M/export?format=csv'
    },
    {
        'name': 'Tin_Tuc.csv',
        'url': 'https://docs.google.com/spreadsheets/d/1z9UtNSwC52VOLpDdxL58Z6bI4EUkI4yfb2AIZzcJl-w/export?format=csv'
    }
]

os.makedirs('drive_data', exist_ok=True)

for doc in docs_to_download:
    print(f"Downloading {doc['name']}...")
    try:
        req = urllib.request.Request(doc['url'], headers={'User-Agent': 'Mozilla/5.0'})
        content = urllib.request.urlopen(req).read()
        dest = os.path.join('drive_data', doc['name'])
        with open(dest, 'wb') as f:
            f.write(content)
        print(f"✓ Saved {dest} ({len(content)} bytes)")
    except Exception as e:
        print(f"❌ Failed to download {doc['name']}: {e}")

