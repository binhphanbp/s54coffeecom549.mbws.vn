import re
import urllib.parse

with open('scraped_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find css
css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content, re.IGNORECASE)
print('--- CSS links count ---', len(css_links))
for l in sorted(list(set(css_links))):
    print('CSS:', l)

# find scripts
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
print('--- Scripts count ---', len(scripts))
for s in sorted(list(set(scripts))):
    print('JS:', s)

# find images
images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
data_srcs = re.findall(r'data-src=["\']([^"\']+)["\']', content, re.IGNORECASE)
data_srcsets = re.findall(r'data-srcset=["\']([^"\']+)["\']', content, re.IGNORECASE)
srcsets = re.findall(r'srcset=["\']([^"\']+)["\']', content, re.IGNORECASE)

all_imgs = set(images + data_srcs)
print('--- Images count (src + data-src) ---', len(all_imgs))
for img in list(all_imgs)[:15]:
    print('IMG:', img)

# find section elements
sections = re.findall(r'id=["\'](shopify-section-[^"\']+)["\']', content)
print('--- Shopify sections count ---', len(sections))
for sec in sections:
    print('Section:', sec)
