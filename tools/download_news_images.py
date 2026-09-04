import csv
import re
import urllib.request
from pathlib import Path
import json
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '_', text)[:40]

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / 'assets' / 'images' / 's54' / 'news'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with open(BASE_DIR / 'drive_data' / 'Tin_Tuc.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f))

articles = []
for row in reader[1:]:
    if len(row) > 1 and row[1].strip():
        item_id = row[0].strip()
        title = row[1].strip()
        category = row[2].strip()
        content = row[3].strip()
        img_url = row[4].strip()
        sub_img = row[5].strip() if len(row) > 5 else ''
        note = row[6].strip() if len(row) > 6 else ''
        
        slug = slugify(title)
        filename = f"news_{item_id}_{slug}"
        
        articles.append({
            'id': item_id,
            'title': title,
            'category': category,
            'content': content,
            'img_url': img_url,
            'sub_img': sub_img,
            'note': note,
            'slug': slug,
            'base_filename': filename
        })

print(f"Total articles: {len(articles)}")

downloaded_map = {}

for art in articles:
    url = art['img_url']
    if not url:
        continue
    
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    if not match:
        print(f"Skipping {art['id']}, no drive ID: {url}")
        continue
    
    file_id = match.group(1)
    
    if file_id in downloaded_map:
        art['local_image'] = downloaded_map[file_id]
        print(f"Article {art['id']} reuses {art['local_image']}")
        continue
        
    dl_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    req = urllib.request.Request(dl_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            c_type = resp.headers.get('Content-Type', '')
            ext = '.jpg'
            if 'png' in c_type:
                ext = '.png'
            elif 'webp' in c_type:
                ext = '.webp'
            elif 'jpeg' in c_type or 'jpg' in c_type:
                ext = '.jpg'
            
            filepath = OUTPUT_DIR / f"{art['base_filename']}{ext}"
            filepath.write_bytes(data)
            local_rel = f"assets/images/s54/news/{art['base_filename']}{ext}"
            art['local_image'] = local_rel
            downloaded_map[file_id] = local_rel
            print(f"Downloaded {art['id']}: {local_rel} ({len(data)} bytes, {c_type})")
    except Exception as e:
        print(f"Error downloading for {art['id']}: {e}")
        art['local_image'] = 'assets/images/s54/blog_cup.jpg'

json_path = BASE_DIR / 'drive_data' / 'news_articles.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"Saved JSON data to {json_path}")
