import re
import os

html_files = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

for hf in html_files:
    if not os.path.exists(hf):
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update hamburger icon stroke
    html = html.replace('stroke="#2F221A" stroke-width="2"', 'stroke="#FAF6F1" stroke-width="2"')
    
    # Update cart icon stroke
    html = html.replace('stroke="#2F221A" stroke-width="1.8"', 'stroke="#FAF6F1" stroke-width="1.8"')

    # In mobile menu, close icon should be white
    html = html.replace('class="c-main-menu__close" data-menu-close aria-label="Close Menu">✕</button>', 'class="c-main-menu__close" data-menu-close aria-label="Close Menu" style="color: #FAF6F1; background: none; border: none; font-size: 24px; cursor: pointer;">✕</button>')

    with open(hf, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated header icon markup in {hf}")

print("All HTML header icon markup updated successfully.")
