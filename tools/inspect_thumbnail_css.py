import re

for css_file in ['assets/css/layouts.theme.css', 'assets/css/sections.product-carousel.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = re.findall(r'(\.o-product-thumbnail[^{]*\{[^}]+\})', content)
    print(f'=== {css_file} rules ({len(rules)}) ===')
    for r in rules:
        if 'hover' in r or 'price' in r or 'content' in r or 'title' in r:
            print(r)
