import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0'}
BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')
IMAGES_DIR = BASE_DIR / 'assets' / 'images'
MEDIA_DIR = BASE_DIR / 'assets' / 'media'
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

files_to_download = [
    ('espresso_brew_desktop.mp4', 'https://cdn.shopify.com/videos/c/o/v/f171588186f142b58fa906ebfc87625a.mp4', MEDIA_DIR),
    ('espresso_brew_mobile.mp4', 'https://cdn.shopify.com/videos/c/o/v/0ca8f326fcd745a899531df5f011eb66.mp4', MEDIA_DIR),
    ('bag_20pack_esp_f_V2_500x.png', 'https://www.vittoriacoffee.com/cdn/shop/files/bag_20pack_esp_f_V2_500x.png?v=1743550925', IMAGES_DIR)
]

for fname, url, folder in files_to_download:
    dest = folder / fname
    print(f'Downloading {fname} from {url}...')
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
            print(f'Saved {fname} ({len(data)} bytes)')
    except Exception as e:
        print(f'Error downloading {fname}: {e}')

print('Done downloading remaining media!')
