import re

with open('scraped_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]+class=["\']([^"\']+)["\']', html)
print('--- Sections ---')
for s in sections:
    print(s)

print('\n--- Product cards structure snippet ---')
oro_idx = html.find('Cinque Stelle')
if oro_idx == -1:
    oro_idx = html.find('Oro')
print(f'Oro index: {oro_idx}')
if oro_idx != -1:
    print(html[oro_idx-500 : oro_idx+1500])
