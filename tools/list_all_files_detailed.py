#!/usr/bin/env python3
from parse_gdrive_tree import fetch_folder_items, root_id

for top_folder in fetch_folder_items(root_id):
    print(f"\n📂 Top folder: {top_folder['name']} (ID: {top_folder['id']})")
    subs = fetch_folder_items(top_folder['id'])
    for s in subs:
        if s['is_folder']:
            print(f"   📁 Subfolder: {s['name']} (ID: {s['id']})")
            files = fetch_folder_items(s['id'])
            for f in files:
                print(f"      📄 File: {f['name']} ({f['mimeType']}) [ID: {f['id']}]")
        else:
            print(f"   📄 File: {s['name']} ({s['mimeType']}) [ID: {s['id']}]")
