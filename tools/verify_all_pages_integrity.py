#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent.parent
html_files = sorted(list(BASE_DIR.glob('*.html')))

print(f"Checking {len(html_files)} HTML files:")

for f in html_files:
    text = f.read_text(encoding='utf-8')
    m_title = re.search(r'<title[^>]*>(.*?)</title>', text)
    title = m_title.group(1).strip() if m_title else 'NO TITLE'
    
    links = re.findall(r'href=["\']([a-zA-Z0-9_\-\./]+\.html(?:\?[^"\']*)?)["\']', text)
    missing = []
    for l in set(links):
        clean_l = l.split('?')[0].split('#')[0]
        if not clean_l.startswith('http') and clean_l != '':
            target = BASE_DIR / clean_l
            if not target.exists():
                missing.append(clean_l)
                
    status = f"MISSING: {missing}" if missing else "ALL LINKS OK"
    print(f"  {f.name:<25} | Title: {title[:45]:<45} | {status}")
