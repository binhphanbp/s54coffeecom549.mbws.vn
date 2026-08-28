#!/usr/bin/env python3
import urllib.request
import re
import json

def decode_js_hex(s):
    def replace_hex(match):
        return chr(int(match.group(1), 16))
    return re.sub(r'\\x([0-9a-fA-F]{2})', replace_hex, s)

def fetch_folder_items(folder_id):
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

    raw_str = m.group(1)
    decoded_str = decode_js_hex(raw_str)
    try:
        data = json.loads(decoded_str)
    except Exception as e:
        print(f"Error parsing json for {folder_id}: {e}")
        return []

    items = []
    # data is a list of items: [[id, parents, name, mimeType, ...], ...]
    for entry in data:
        if isinstance(entry, list) and len(entry) >= 4 and isinstance(entry[0], str):
            item_id = entry[0]
            item_name = entry[2]
            mime_type = entry[3]
            items.append({
                'id': item_id,
                'name': item_name,
                'mimeType': mime_type,
                'is_folder': mime_type == 'application/vnd.google-apps.folder'
            })
    return items

def print_tree(folder_id, folder_name="Root", indent=0):
    print("  " * indent + f"📁 {folder_name} (ID: {folder_id})")
    items = fetch_folder_items(folder_id)
    for it in items:
        if it['is_folder']:
            print_tree(it['id'], it['name'], indent + 1)
        else:
            print("  " * (indent + 1) + f"📄 {it['name']} (ID: {it['id']}, type: {it['mimeType']})")

root_id = '1jIrSz7F7_Ruc8myLEJOE6seOlIOMBNtL'
print("=== GOOGLE DRIVE FOLDER TREE ===")
print_tree(root_id, "Thông tin trang web (S54 Coffee)")
