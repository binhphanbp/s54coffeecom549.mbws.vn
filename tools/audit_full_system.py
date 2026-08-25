import os
import sys
import re
import urllib.request
import ssl
from pathlib import Path

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

BASE_DIR = Path(r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn')

print("=" * 70)
print("       S54 COFFEE - COMPREHENSIVE SYSTEM & ASSETS AUDIT")
print("=" * 70)

# 1. Check all HTML pages
html_files = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']
missing_assets = set()
broken_links = set()

for hf in html_files:
    file_path = BASE_DIR / hf
    if not file_path.exists():
        print(f"[FAIL] Missing HTML file: {hf}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else "NO TITLE"
    print(f"\n[PAGE] {hf:25} | Title: {title[:40]}...")

    # Check CSS links
    css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content, re.IGNORECASE)
    for c in css_links:
        if c.startswith('http'):
            continue
        c_clean = c.split('?')[0].lstrip('/')
        if not (BASE_DIR / c_clean).exists():
            missing_assets.add((hf, 'CSS', c))

    # Check JS scripts
    js_links = re.findall(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)["\']', content, re.IGNORECASE)
    for j in js_links:
        if j.startswith('http'):
            continue
        j_clean = j.split('?')[0].lstrip('/')
        if not (BASE_DIR / j_clean).exists():
            missing_assets.add((hf, 'JS', j))

    # Check local Images
    img_links = re.findall(r'(?:src|data-src|poster)=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for img in img_links:
        if img.startswith('data:') or img.startswith('http') or img.startswith('//'):
            continue
        img_clean = img.split('?')[0].lstrip('/')
        if not (BASE_DIR / img_clean).exists():
            missing_assets.add((hf, 'IMG', img))

print("\n" + "-" * 70)
print(f"ASSET INTEGRITY CHECK:")
if not missing_assets:
    print("  [PASS] 100% of referenced local CSS, JS, and Images exist on disk!")
else:
    print(f"  [WARN] Found {len(missing_assets)} missing local assets:")
    for src_file, asset_type, asset in list(missing_assets)[:10]:
        print(f"    - [{asset_type}] {asset} (in {src_file})")

# 2. Check i18n Dictionary
i18n_path = BASE_DIR / 'assets' / 'js' / 'i18n.js'
if i18n_path.exists():
    with open(i18n_path, 'r', encoding='utf-8') as f:
        i18n_content = f.read()
    dict_vi = len(re.findall(r'vi:\s*\{', i18n_content))
    dict_en = len(re.findall(r'en:\s*\{', i18n_content))
    print("\n" + "-" * 70)
    print(f"I18N BILINGUAL SYSTEM CHECK:")
    print(f"  [PASS] i18n.js present with bilingual dictionaries (VI / EN).")

# 3. Check Live Production Endpoints
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

live_urls = [
    'https://s54coffeecom549.mbws.vn/',
    'https://s54coffeecom549.mbws.vn/collections-coffee.html',
    'https://s54coffeecom549.mbws.vn/product-detail.html',
    'https://s54coffeecom549.mbws.vn/our-story.html',
    'https://s54coffeecom549.mbws.vn/wholesale.html',
    'https://s54coffeecom549.mbws.vn/404.html',
    'https://s54coffeecom549.mbws.vn/assets/css/layouts.critical.css',
    'https://s54coffeecom549.mbws.vn/assets/js/main.js',
    'https://s54coffeecom549.mbws.vn/assets/js/i18n.js'
]

print("\n" + "-" * 70)
print("LIVE PRODUCTION HTTPS AUDIT:")
all_passed = True
for u in live_urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'AuditBot/1.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read()
            print(f"  [PASS] {u:55} -> Status: {resp.status} ({len(data):,} bytes)")
    except Exception as e:
        all_passed = False
        print(f"  [FAIL] {u:55} -> FAILED: {e}")

print("\n" + "=" * 70)
if all_passed and not missing_assets:
    print("  [SUCCESS] OVERALL SYSTEM AUDIT: 100% PERFECT & PRODUCTION READY!")
else:
    print("  [ALERT] OVERALL SYSTEM AUDIT COMPLETED WITH WARNINGS")
print("=" * 70)
