import os
import re
import urllib.request
import urllib.parse
import ssl
from pathlib import Path

# Disable SSL verification for asset scraping
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / 'assets'
CSS_DIR = ASSETS_DIR / 'css'
JS_DIR = ASSETS_DIR / 'js'
FONTS_DIR = ASSETS_DIR / 'fonts'
IMAGES_DIR = ASSETS_DIR / 'images'

for d in [CSS_DIR, JS_DIR, FONTS_DIR, IMAGES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def download_file(url, dest_path):
    if not url:
        return None
    if url.startswith('//'):
        url = 'https:' + url
    elif url.startswith('/'):
        url = 'https://www.vittoriacoffee.com' + url
    
    # Remove URL query params for file saving but keep original url for request
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = resp.read()
            with open(dest_path, 'wb') as f:
                f.write(data)
            print(f'Downloaded: {dest_path.name} ({len(data)} bytes)')
            return dest_path
    except Exception as e:
        print(f'Failed to download {url}: {e}')
        return None

print('--- Step 1: Downloading Fonts ---')
fonts = [
    'domaine-regular.woff',
    'domaine-regular.woff2',
    'domainedispnar-regularitalic.woff',
    'domainedispnar-regularitalic.woff2',
    'gilroy-semibold.woff',
    'gilroy-semibold.woff2',
    'neutra2text-book-webfont.woff',
    'neutra2text-book-webfont.woff2',
    'neutra2text-demi-webfont.woff',
    'neutra2text-demi-webfont.woff2'
]

for font in fonts:
    font_url = f'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/{font}'
    download_file(font_url, FONTS_DIR / font)

print('--- Step 2: Downloading CSS files ---')
css_files = [
    ('layouts.critical.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/layouts.critical.css?v=44415648165723515651714627810'),
    ('layouts.theme.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/layouts.theme.css?v=16435976937801593671784015050'),
    ('sections.subscription-bar.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.subscription-bar.css?v=113485404550110677601742818449'),
    ('sections.hero-banner.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.hero-banner.css?v=176642738441974525051778660977'),
    ('sections.product-carousel.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.product-carousel.css?v=181167473110575555081682046513'),
    ('sections.featured-collections.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.featured-collections.css?v=21500882283471994941703198557'),
    ('sections.text-and-image.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.text-and-image.css?v=50475230508705142061709598527'),
    ('sections.featured-video.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.featured-video.css?v=140959852766020445001708494133'),
    ('sections.article-feed.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.article-feed.css?v=179437996688464527541685514086'),
    ('sections.instagram-feed.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.instagram-feed.css?v=126280250909586583061675914984'),
    ('sections.cart-drawer.css', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.cart-drawer.css?v=183113512966747051501685514089')
]

for name, url in css_files:
    download_file(url, CSS_DIR / name)

print('--- Step 3: Downloading JS files ---')
js_files = [
    ('vendor.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/vendor.js?v=53223130924339055331714627833'),
    ('layouts.theme.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/layouts.theme.js?v=9736880247184568211715045613'),
    ('sections.hero-banner.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.hero-banner.js?v=176642738441974525051778660977'),
    ('sections.product-carousel.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.product-carousel.js?v=136883552501562724291715045627'),
    ('sections.featured-collections.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.featured-collections.js?v=140471532124537820231715045623'),
    ('sections.featured-video.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.featured-video.js?v=180558522949887157801715045623'),
    ('sections.article-feed.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.article-feed.js?v=156314781011188315021715045615'),
    ('sections.cart-section.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.cart-section.js?v=68261902306995669921715045617'),
    ('sections.promotions.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.promotions.js?v=119799251174506032681715045629'),
    ('sections.subscription-bar.js', 'https://www.vittoriacoffee.com/cdn/shop/t/196/assets/sections.subscription-bar.js?v=53871669189316170711715045632')
]

for name, url in js_files:
    download_file(url, JS_DIR / name)

print('--- Step 4: Extracting and Downloading All Images in HTML ---')
with open(BASE_DIR / 'scraped_raw.html', 'r', encoding='utf-8') as f:
    raw_html = f.read()

# find all img urls in src, data-src, srcset, data-srcset, poster, data-bg
img_urls = set()

# src and data-src
for match in re.findall(r'(?:src|data-src|poster|data-background|data-bg)=["\']([^"\']+)["\']', raw_html, re.IGNORECASE):
    if any(ext in match.lower() for ext in ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', 'accentuate.io', '/cdn/shop/']):
        img_urls.add(match)

# srcset and data-srcset
for match in re.findall(r'(?:srcset|data-srcset)=["\']([^"\']+)["\']', raw_html, re.IGNORECASE):
    for part in match.split(','):
        u = part.strip().split(' ')[0]
        if u and any(ext in u.lower() for ext in ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', 'accentuate.io', '/cdn/shop/']):
            img_urls.add(u)

# style url(...)
for match in re.findall(r'url\(["\']?([^)"\']+\.(?:png|jpg|jpeg|svg|webp|gif)[^)"\']*)["\']?\)', raw_html, re.IGNORECASE):
    img_urls.add(match)

print(f'Found {len(img_urls)} unique image URLs to download.')

def clean_filename(url):
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        filename = 'image_' + str(abs(hash(url))) + '.jpg'
    # remove special chars
    filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    return filename

url_to_local = {}
for i, u in enumerate(img_urls):
    fname = clean_filename(u)
    # prepend index to prevent duplicate filenames
    local_fname = f'{i:03d}_{fname}'
    local_path = IMAGES_DIR / local_fname
    download_file(u, local_path)
    url_to_local[u] = f'assets/images/{local_fname}'

print('Image download complete!')
