import os

html_files = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

old_btn = '<button type="button" class="c-header__link is-cart" data-cart-drawer-toggle aria-label="Cart" style="position: relative; background: none; border: none; cursor: pointer; padding: 6px;">'
new_btn = '<button type="button" class="c-header__link is-cart" data-cart-drawer-toggle aria-label="Cart">'

for hf in html_files:
    if not os.path.exists(hf):
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(old_btn, new_btn)
    with open(hf, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Cleaned cart button inline style in {hf}")

print("All HTML files cleaned.")
