import csv
import json

with open('drive_data/Tin_Tuc.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    headers = reader[0]
    items = []
    for row in reader[1:]:
        if len(row) > 1 and row[1].strip():
            items.append({
                'id': row[0].strip(),
                'title': row[1].strip(),
                'category': row[2].strip(),
                'content_length': len(row[3].strip()),
                'image': row[4].strip(),
                'sub_image': row[5].strip() if len(row) > 5 else '',
                'note': row[6].strip() if len(row) > 6 else ''
            })
    print(f"Total valid items: {len(items)}")
    for it in items:
        print(f"{it['id']}: [{it['category']}] {it['title']} (len: {it['content_length']})")
        if it['image']:
            print(f"   image: {it['image']}")
