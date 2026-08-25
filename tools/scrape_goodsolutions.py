import urllib.request
import ssl
import re
import os
import sys

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

os.makedirs('tools/old_site', exist_ok=True)

base_url = 'https://goodsolutions.com.vn'

def fetch_page(url, save_name):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            with open(f'tools/old_site/{save_name}.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fetched {url} -> tools/old_site/{save_name}.html ({len(content)} bytes)")
            return content
    except Exception as e:
        print(f"Failed {url}: {e}")
        return None

home_html = fetch_page(base_url, 'home')
if home_html:
    # Extract links
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', home_html)
    found_urls = set()
    for h in hrefs:
        if h.startswith('#') or h.startswith('javascript:') or h.startswith('mailto:') or h.startswith('tel:'):
            continue
        if h.startswith('/'):
            full_url = base_url + h
        elif 'goodsolutions.com.vn' in h:
            full_url = h
        else:
            continue
        found_urls.add(full_url)
    
    print("\nFound internal URLs on old website:")
    for u in sorted(list(found_urls)):
        print(" -", u)
        name = re.sub(r'[^a-zA-Z0-9_-]', '_', u.replace(base_url, '').strip('/'))
        if not name:
            name = 'index'
        fetch_page(u, name)
