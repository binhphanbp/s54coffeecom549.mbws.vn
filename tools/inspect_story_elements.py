import re
import sys

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

with open('our-story.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all headings, paragraphs, and story titles
titles = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', html, re.DOTALL)
paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)

print("=== HEADINGS IN OUR-STORY ===")
for t in titles:
    clean_t = re.sub(r'<[^>]+>', '', t).strip()
    if clean_t:
        print("H:", clean_t)

print("\n=== PARAGRAPHS IN OUR-STORY ===")
for p in paras[:30]:
    clean_p = re.sub(r'<[^>]+>', '', p).strip()
    if len(clean_p) > 20:
        print("P:", clean_p[:120])
