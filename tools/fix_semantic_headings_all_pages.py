#!/usr/bin/env python3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update index.html
index_path = BASE_DIR / 'index.html'
if index_path.exists():
    c = index_path.read_text(encoding='utf-8')
    
    # Carousel title: h3 -> h2
    c = re.sub(r'<h3 class="c-product-carousel__title">([\s\S]*?)</h3>', r'<h2 class="c-product-carousel__title o-heading--2">\1</h2>', c)
    
    # Story title: h2 with o-heading--3 -> o-heading--2
    c = re.sub(r'<h2 class="c-text-and-image__text-title o-heading--3">', r'<h2 class="c-text-and-image__text-title o-heading--2">', c)
    
    # Video title: h3 -> h2
    c = re.sub(r'<h3 class="c-featured-video__title">([\s\S]*?)</h3>', r'<h2 class="c-featured-video__title o-heading--2">\1</h2>', c)
    
    # Best sellers title: h3 -> h2
    c = re.sub(r'<h3 class="c-featured-collections__header-title o-heading--3">([\s\S]*?)</h3>', r'<h2 class="c-featured-collections__header-title o-heading--2">\1</h2>', c)
    
    # Article feed title: h4 -> h2
    c = re.sub(r'<h4 class="c-article-feed__title o-heading--3">([\s\S]*?)</h4>', r'<h2 class="c-article-feed__title o-heading--2">\1</h2>', c)
    
    # Product thumbnails inside grid: h2 -> h3
    c = re.sub(r'<h2 class="o-product-thumbnail__title o-heading--6\s*">([\s\S]*?)</h2>', r'<h3 class="o-product-thumbnail__title o-heading--6">\1</h3>', c)
    
    index_path.write_text(c, encoding='utf-8')
    print("✓ Fixed semantic headings in index.html")

# 2. Update collections-coffee.html
coll_path = BASE_DIR / 'collections-coffee.html'
if coll_path.exists():
    c = coll_path.read_text(encoding='utf-8')
    c = re.sub(r'<h2 class="o-product-thumbnail__title o-heading--6\s*">([\s\S]*?)</h2>', r'<h3 class="o-product-thumbnail__title o-heading--6">\1</h3>', c)
    coll_path.write_text(c, encoding='utf-8')
    print("✓ Fixed semantic headings in collections-coffee.html")

# 3. Update our-story.html
story_path = BASE_DIR / 'our-story.html'
if story_path.exists():
    c = story_path.read_text(encoding='utf-8')
    c = re.sub(r'<h3 class="c-text-and-image__text-title o-heading--3">', r'<h2 class="c-text-and-image__text-title o-heading--2">', c)
    story_path.write_text(c, encoding='utf-8')
    print("✓ Fixed semantic headings in our-story.html")

# 4. Update wholesale.html
ws_path = BASE_DIR / 'wholesale.html'
if ws_path.exists():
    c = ws_path.read_text(encoding='utf-8')
    c = re.sub(r'<h3 class="c-text-and-image__text-title o-heading--3">', r'<h2 class="c-text-and-image__text-title o-heading--2">', c)
    ws_path.write_text(c, encoding='utf-8')
    print("✓ Fixed semantic headings in wholesale.html")

print("\n✅ All pages now have 100% correct semantic H2 section headings!")
