import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('scraped_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content, re.IGNORECASE)

font_urls = set()
bg_urls = set()

for href in css_links:
    if href.startswith('//'):
        url = 'https:' + href
    elif href.startswith('/'):
        url = 'https://www.vittoriacoffee.com' + href
    else:
        url = href
    print(f'Fetching CSS: {url}')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            css_text = res.read().decode('utf-8', errors='ignore')
            # find fonts
            fonts = re.findall(r'url\(["\']?([^)"\']+\.(?:woff2?|ttf|eot|otf)[^)"\']*)["\']?\)', css_text)
            font_urls.update(fonts)
            # find bg images
            bgs = re.findall(r'url\(["\']?([^)"\']+\.(?:png|jpg|jpeg|svg|webp|gif)[^)"\']*)["\']?\)', css_text)
            bg_urls.update(bgs)
    except Exception as e:
        print(f'Error fetching {url}: {e}')

print(f'Found {len(font_urls)} fonts:')
for f in sorted(list(font_urls)):
    print('FONT:', f)

print(f'Found {len(bg_urls)} background images:')
for b in sorted(list(bg_urls))[:20]:
    print('BG:', b)
