#!/usr/bin/env python3
import urllib.request
import os

images_to_download = [
    {
        'id': '15EHOuSuynN-nOkOnB5WlOs55hWZc9mb4',
        'name': 's54_office_vinhome_1.jpg'
    },
    {
        'id': '16nS-Qg0pQp3q_XwkRlV4awb_IaEsqho1',
        'name': 's54_office_vinhome_2.jpg'
    },
    {
        'id': '1ZL30kFOzBqxYD-HDUr8V4NbiMuxrih-k',
        'name': 's54_office_vinhome_3.jpg'
    },
    {
        'id': '1b3N0Mi6oiFMzpE5LdFjdU4vdsmDibDQS',
        'name': 's54_cafe_nhabe_1.jpg'
    },
    {
        'id': '1w9yo3CK9TA7pjoHtF9kAd8QBzS0EqpVC',
        'name': 's54_cafe_nhabe_2.jpg'
    },
    {
        'id': '1Q7kxg2e5g0TizQ9-k3Yxyo2F3oodbbpX',
        'name': 's54_cafe_nhabe_3.jpg'
    }
]

dest_dirs = [
    'assets/images/s54',
    'public/client-assets/images/s54',
    'theme/assets/images/s54'
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

for img in images_to_download:
    url = f"https://drive.google.com/uc?export=download&id={img['id']}"
    print(f"Downloading {img['name']} from ID {img['id']}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        content = urllib.request.urlopen(req).read()
        for d in dest_dirs:
            p = os.path.join(d, img['name'])
            with open(p, 'wb') as f:
                f.write(content)
        print(f"✓ Saved {img['name']} ({len(content)} bytes)")
    except Exception as e:
        print(f"❌ Error downloading {img['name']}: {e}")

