import os
import re
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
IMAGES_DIR = BASE_DIR / 'assets' / 'images'
MEDIA_DIR = BASE_DIR / 'assets' / 'media'
CSS_DIR = BASE_DIR / 'assets' / 'css'
JS_DIR = BASE_DIR / 'assets' / 'js'

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
      "url": "product-detail.html",
      "featured_image": {
        "aspect_ratio": 1.0,
        "alt": "Cinque Stelle Oro Beans",
        "height": 1000,
        "url": "assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png",
        "width": 1000
      },
      "image": "assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png",
      "handle": "cinque-stelle-beans-1kg",
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

def clean_filename(url):
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        filename = 'image_' + str(abs(hash(url))) + '.jpg'
    filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    return filename

local_imgs = os.listdir(IMAGES_DIR)

pages = [
    ('scraped_raw.html', 'index.html'),
    ('collections_coffee_raw.html', 'collections-coffee.html'),
    ('our_story_raw.html', 'our-story.html'),
    ('wholesale_raw.html', 'wholesale.html'),
    ('product_detail_raw.html', 'product-detail.html')
]

for raw_file, out_file in pages:
    if not (BASE_DIR / raw_file).exists():
        continue
    with open(BASE_DIR / raw_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Map image URLs
    for u in re.findall(r'(?:src|data-src|poster|data-background|data-bg)=["\']([^"\']+)["\']', html, re.IGNORECASE):
        if not u.endswith('.js') and not u.endswith('.css'):
            base = clean_filename(u)
            for lf in local_imgs:
                if lf.endswith('_' + base) or lf == base or base in lf:
                    html = html.replace(u, f'assets/images/{lf}')
                    break

    # Map videos
    html = html.replace('https://cdn.shopify.com/videos/c/o/v/f171588186f142b58fa906ebfc87625a.mp4', 'assets/media/espresso_brew_desktop.mp4')
    html = html.replace('https://cdn.shopify.com/videos/c/o/v/0ca8f326fcd745a899531df5f011eb66.mp4', 'assets/media/espresso_brew_mobile.mp4')

    # Map CSS files
    for css_file in os.listdir(CSS_DIR):
        if css_file.endswith('.css'):
            pattern = rf'href=["\'][^"\']*{re.escape(css_file)}[^"\']*["\']'
            html = re.sub(pattern, f'href="assets/css/{css_file}"', html)

    # Map JS files
    for js_file in os.listdir(JS_DIR):
        if js_file.endswith('.js'):
            pattern = rf'src=["\'][^"\']*{re.escape(js_file)}[^"\']*["\']'
            html = re.sub(pattern, f'src="assets/js/{js_file}"', html)

    # Remove trackers & third party scripts
    for p in patterns_to_remove:
        html = re.sub(p, '', html, flags=re.DOTALL | re.IGNORECASE)

    # Link navigation menu & internal links to generated subpages
    html = re.sub(r'href=["\'](?:https?://(?:www\.)?vittoriacoffee\.com)?/collections/coffee["\']', 'href="collections-coffee.html"', html)
    html = re.sub(r'href=["\'](?:https?://(?:www\.)?vittoriacoffee\.com)?/pages/our-story["\']', 'href="our-story.html"', html)
    html = re.sub(r'href=["\'](?:https?://(?:www\.)?vittoriacoffee\.com)?/pages/wholesale["\']', 'href="wholesale.html"', html)
    html = re.sub(r'href=["\'](?:https?://(?:www\.)?vittoriacoffee\.com)?/products/[^"\']+["\']', 'href="product-detail.html"', html)
    html = re.sub(r'href=["\'](?:https?://(?:www\.)?vittoriacoffee\.com)?/["\']', 'href="index.html"', html)

    # Add early script in head
    html = re.sub(r'<head[^>]*>', f'<head>\n{early_script}', html, flags=re.IGNORECASE)

    # Add footer
    if '</footer' in html:
        html = html.replace('</footer>', f'{footer_bottom_html}\n</footer>')

    # Custom CSS & JS injection
    if 'assets/css/custom.css' not in html:
        html = html.replace('</head>', '    <link rel="stylesheet" href="assets/css/custom.css">\n</head>')

    if 'assets/js/main.js' not in html:
        custom_scripts = '''
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="assets/js/main.js"></script>
        '''
        html = html.replace('</body>', f'{custom_scripts}\n</body>')

    with open(BASE_DIR / out_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Compiled {out_file} successfully!')

print('Fast compilation complete!')
