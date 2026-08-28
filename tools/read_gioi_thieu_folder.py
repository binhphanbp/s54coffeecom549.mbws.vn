#!/usr/bin/env python3
import urllib.request
import re
import json
import os

from parse_gdrive_tree import decode_js_hex

def get_items(folder_id):
    url = f'https://drive.google.com/drive/folders/{folder_id}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
        return []

    m = re.search(r"window\['_DRIVE_ivd'\]\s*=\s*'([^']+)'", html)
    if not m:
        return []

    decoded = decode_js_hex(m.group(1))
    parsed = json.loads(decoded)
    items = []
    if isinstance(parsed, list) and len(parsed) > 0 and isinstance(parsed[0], list):
        for sub in parsed[0]:
            if isinstance(sub, list) and len(sub) > 3 and isinstance(sub[0], str):
                items.append({
                    'id': sub[0],
                    'name': sub[2],
                    'mimeType': sub[3],
                    'is_folder': sub[3] == 'application/vnd.google-apps.folder'
                })
    return items

gioi_thieu_id = '1dGbKIpaLnh4YXUuq6RlioInSCxOwKv-h'
print("=== FILES IN '2. Giới thiệu' ===")
items = get_items(gioi_thieu_id)
for it in items:
    print(f"- {it['name']} ({it['mimeType']}) [ID: {it['id']}]")

