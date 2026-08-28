#!/usr/bin/env python3
import urllib.request
import re
import json

def decode_js_hex(s):
    return re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)

def get_items(folder_id):
    url = f'https://drive.google.com/drive/folders/{folder_id}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {folder_id}: {e}")
        return []

    m = re.search(r"window\['_DRIVE_ivd'\]\s*=\s*'([^']+)'", html)
    if not m:
        return []

    decoded = decode_js_hex(m.group(1))
    try:
        parsed = json.loads(decoded)
    except Exception as e:
        return []

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

def explore(folder_id, folder_name="Root", indent=0):
    print("  " * indent + f"📁 {folder_name}")
    items = get_items(folder_id)
    for it in items:
        if it['is_folder']:
            explore(it['id'], it['name'], indent + 1)
        else:
            print("  " * (indent + 1) + f"📄 {it['name']} ({it['mimeType']}) [ID: {it['id']}]")

root_id = '1jIrSz7F7_Ruc8myLEJOE6seOlIOMBNtL'
print("================================================================")
print("     CÁC TỆP & THƯ MỤC TRONG GOOGLE DRIVE 'Thông tin trang web' ")
print("================================================================")
explore(root_id, "Thông tin trang web (S54 Coffee)")
print("================================================================")
