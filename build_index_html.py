import os
import re
import urllib.parse
from pathlib import Path

BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')
IMAGES_DIR = BASE_DIR / 'assets' / 'images'
MEDIA_DIR = BASE_DIR / 'assets' / 'media'
CSS_DIR = BASE_DIR / 'assets' / 'css'
JS_DIR = BASE_DIR / 'assets' / 'js'

# Read raw html
with open(BASE_DIR / 'scraped_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

local_images = os.listdir(IMAGES_DIR)

def clean_filename(url):
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        filename = 'image_' + str(abs(hash(url))) + '.jpg'
    filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    return filename

# Find all image URLs
all_matches = set()
for m in re.findall(r'(?:src|data-src|poster|data-background|data-bg)=["\']([^"\']+)["\']', html, re.IGNORECASE):
    if not m.endswith('.js') and not m.endswith('.css'):
        all_matches.add(m)
for m in re.findall(r'(?:srcset|data-srcset)=["\']([^"\']+)["\']', html, re.IGNORECASE):
    for part in m.split(','):
        u = part.strip().split(' ')[0]
        if u and not u.endswith('.js') and not u.endswith('.css'):
            all_matches.add(u)
for m in re.findall(r'url\(["\']?([^)"\']+\.(?:png|jpg|jpeg|svg|webp|gif)[^)"\']*)["\']?\)', html, re.IGNORECASE):
    all_matches.add(m)

url_to_local = {}
for u in all_matches:
    base = clean_filename(u)
    matched = None
    for lf in local_images:
        if lf.endswith('_' + base) or lf == base or base in lf:
            matched = lf
            break
    if matched:
        url_to_local[u] = f'assets/images/{matched}'

# Replace image URLs
for u, local_path in url_to_local.items():
    html = html.replace(u, local_path)

# Map videos to local assets/media/
html = html.replace('https://cdn.shopify.com/videos/c/o/v/f171588186f142b58fa906ebfc87625a.mp4', 'assets/media/espresso_brew_desktop.mp4')
html = html.replace('https://cdn.shopify.com/videos/c/o/v/0ca8f326fcd745a899531df5f011eb66.mp4', 'assets/media/espresso_brew_mobile.mp4')
html = html.replace('//www.vittoriacoffee.com/cdn/shop/files/bag_20pack_esp_f_V2_500x.png?v=1743550925', 'assets/images/bag_20pack_esp_f_V2_500x.png')

# Map CSS
css_files = [
    'layouts.critical.css',
    'layouts.theme.css',
    'sections.subscription-bar.css',
    'sections.hero-banner.css',
    'sections.product-carousel.css',
    'sections.featured-collections.css',
    'sections.text-and-image.css',
    'sections.featured-video.css',
    'sections.article-feed.css',
    'sections.instagram-feed.css',
    'sections.cart-drawer.css'
]

for css in css_files:
    pattern = rf'href=["\'][^"\']*{re.escape(css)}[^"\']*["\']'
    html = re.sub(pattern, f'href="assets/css/{css}"', html)

# Map JS
js_files = [
    'vendor.js',
    'layouts.theme.js',
    'sections.hero-banner.js',
    'sections.product-carousel.js',
    'sections.featured-collections.js',
    'sections.featured-video.js',
    'sections.article-feed.js',
    'sections.cart-section.js',
    'sections.promotions.js',
    'sections.subscription-bar.js'
]

for js in js_files:
    pattern = rf'src=["\'][^"\']*{re.escape(js)}[^"\']*["\']'
    html = re.sub(pattern, f'src="assets/js/{js}"', html)

# Remove third party external tracking, blocking scripts and geolocation redirect popup
patterns_to_remove = [
    r'<script[^>]*data-locksmith[^>]*>.*?</script>',
    r'<script[^>]*application/vnd\.locksmith\+json[^>]*>.*?</script>',
    r'<script[^>]*data-gorgias[^>]*>.*?</script>',
    r'<script[^>]*klaviyo[^>]*>.*?</script>',
    r'<script[^>]*bat\.bing\.com[^>]*>.*?</script>',
    r'<script[^>]*googletagmanager\.com[^>]*>.*?</script>',
    r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->',
    r'<!-- BING -->.*?<!-- End BING -->',
    r'<script[^>]*okendo-reviews\.js[^>]*></script>',
    r'<script[^>]*shopify-origin-trials[^>]*></script>',
    r'<script[^>]*webmcp[^>]*></script>',
    r'<script[^>]*storefront/load_feature[^>]*></script>',
    r'<script[^>]*redirect-app\.js[^>]*></script>',
    r'<script[^>]*weglot_script_tag\.js[^>]*></script>',
    r'<script[^>]*pushowl-shopify\.js[^>]*></script>',
    r'<script[^>]*reconvert-cdn\.com[^>]*></script>',
    r'<script[^>]*shop\.app/checkouts[^>]*></script>',
    r'<script[^>]*t\.cfjump\.com[^>]*></script>',
    r'<script[^>]*webyze\.com[^>]*></script>',
    r'<script[^>]*yotpo\.com[^>]*></script>',
    r'<script[^>]*portable-wallets\.en\.js[^>]*></script>',
    r'<script[^>]*orbe[^>]*></script>',
    r'<link[^>]*orbe-geolocation[^>]*>'
]

for p in patterns_to_remove:
    html = re.sub(p, '', html, flags=re.DOTALL | re.IGNORECASE)

# Early Mock Script injected at the very top of <head>
early_script = '''
<script>
window.__vittoriaMockCart = {
  "token": "d7480a82b992167389148d53efd67db9",
  "note": null,
  "attributes": {},
  "original_total_price": 4400,
  "total_price": 4400,
  "total_discount": 0,
  "total_weight": 1000.0,
  "item_count": 1,
  "items": [
    {
      "id": 401234567890,
      "properties": { "_bundle_item": false, "_is_subscription": false },
      "quantity": 1,
      "variant_id": 401234567890,
      "key": "401234567890:1",
      "title": "Cinque Stelle Oro - 1kg Beans",
      "price": 4400,
      "original_price": 4400,
      "discounted_price": 4400,
      "line_price": 4400,
      "original_line_price": 4400,
      "total_discount": 0,
      "discounts": [],
      "sku": "VIT-ORO-1KG",
      "grams": 1000,
      "vendor": "Vittoria Coffee",
      "taxable": false,
      "product_id": 6718616502447,
      "product_has_only_default_variant": false,
      "gift_card": false,
      "final_price": 4400,
      "final_line_price": 4400,
      "url": "#",
      "featured_image": {
        "aspect_ratio": 1.0,
        "alt": "Cinque Stelle Oro Beans",
        "height": 1000,
        "url": "assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png",
        "width": 1000
      },
      "image": "assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png",
      "handle": "cinque-stelle-beans",
      "requires_shipping": true,
      "product_type": "Beans",
      "product_title": "Cinque Stelle",
      "product_description": "Australia's favourite premium blend",
      "variant_title": "1kg Beans",
      "variant_options": ["1kg Beans"],
      "options_with_values": [{ "name": "Size", "value": "1kg Beans" }],
      "line_level_discount_allocations": []
    }
  ],
  "requires_shipping": true,
  "currency": "AUD",
  "items_subtotal_price": 4400,
  "cart_level_discount_applications": []
};

// Global Fetch Interceptor
(function() {
  var origFetch = window.fetch;
  window.fetch = function(url, opts) {
    var u = (typeof url === 'string') ? url : (url && url.url) || '';
    if (u.indexOf('/cart') !== -1 || u.indexOf('cart.js') !== -1) {
      return Promise.resolve(new Response(JSON.stringify(window.__vittoriaMockCart), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      }));
    }
    if (u.indexOf('/localization') !== -1) {
      return Promise.resolve(new Response(JSON.stringify({ success: true }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      }));
    }
    return origFetch ? origFetch.apply(this, arguments) : Promise.resolve(new Response('{}', { status: 200 }));
  };
})();
</script>
'''

html = re.sub(r'<head[^>]*>', f'<head>\n{early_script}', html, flags=re.IGNORECASE)

# Footer bottom bar with copyright and payment badges
footer_bottom_html = '''
<div class="c-footer__bottom-bar">
  <div class="c-footer__copyright">
    &copy; 2026 Vittoria Coffee. All rights reserved. Family owned & operated.
  </div>
  <div class="c-footer__payment-icons">
    <span class="c-footer__payment-badge">VISA</span>
    <span class="c-footer__payment-badge">Mastercard</span>
    <span class="c-footer__payment-badge">AMEX</span>
    <span class="c-footer__payment-badge">Apple Pay</span>
    <span class="c-footer__payment-badge">Google Pay</span>
    <span class="c-footer__payment-badge">PayPal</span>
    <span class="c-footer__payment-badge">Afterpay</span>
    <span class="c-footer__payment-badge">Zip</span>
  </div>
</div>
'''

if '</footer' in html:
    html = html.replace('</footer>', f'{footer_bottom_html}\n</footer>')

# Insert custom CSS & JS
if 'assets/css/custom.css' not in html:
    html = html.replace('</head>', '    <link rel="stylesheet" href="assets/css/custom.css">\n</head>')

if 'assets/js/main.js' not in html:
    custom_scripts = '''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="assets/js/main.js"></script>
    '''
    html = html.replace('</body>', f'{custom_scripts}\n</body>')

with open(BASE_DIR / 'index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Compiled updated index.html successfully without Orbe blocker!')
