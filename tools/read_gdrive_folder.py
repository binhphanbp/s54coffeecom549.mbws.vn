#!/usr/bin/env python3
import urllib.request
import re
import json

folder_id = '1jIrSz7F7_Ruc8myLEJOE6seOlIOMBNtL'
url = f'https://drive.google.com/drive/folders/{folder_id}'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Search for file names and IDs in the Drive payload
print("Title matches:")
for m in re.finditer(r'<title>(.*?)</title>', html):
    print(" ", m.group(1))

# Search for JS data items
items = re.findall(r'\["([a-zA-Z0-9_-]{25,})",\["([^"]+)"', html)
print(f"Found {len(items)} possible drive items:")
for item_id, item_name in items[:20]:
    print(f" - ID: {item_id}, Name: {item_name}")

# Also search for files/items JSON blob
matches = re.findall(r'(\[[^\]]*"(?:docx?|pdf|xlsx?|txt|png|jpe?g)"[^\]]*\])', html, re.IGNORECASE)
print(f"Found {len(matches)} extension matches:")
for m in matches[:10]:
    print(" ", m[:120])
