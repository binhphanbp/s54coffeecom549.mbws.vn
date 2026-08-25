import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace existing hero container and strip with pure, authentic luxury Vittoria-style hero
pattern = r'<section class="c-hero-banner is-large is-homepage s54-hero-container">[\s\S]*?<!-- S54 Value Highlights Strip -->[\s\S]*?<\/div>\s*<\/div>'

clean_hero_html = """<section class="c-hero-banner is-large is-homepage">
  <div class="c-hero-banner__media-container o-media-container">
    <picture>
      <source media="(max-width:750px)" srcset="assets/images/016_vit-homepage-banner-mobile-2_750x.jpg">
      <source media="(min-width:751px)" srcset="assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg">
      <img src="assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg" alt="S54 Coffee Hero Banner" class="c-hero-banner__media o-media has-mobile" />
    </picture>
    <div class="c-hero-banner__overlay is-narrow is-vertical-bottom s-overlay--left is-colour-light--mobile is-colour-dark--desktop">
      <h1 class="c-hero-banner__title o-heading--1">Tinh Hoa<br/>Cà Phê Việt®</h1>
      <p class="c-hero-banner__subtitle is-size--large">100% Cà phê rang mộc nguyên chất từ vùng đất đỏ Tây Nguyên</p>
      <a href="collections-coffee.html" class="c-hero-banner__button has-margin-top-small o-btn is-primary is-dark has-arrow">
        MUA SẮM NGAY
        <svg fill="none" class="o-btn__arrow" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><g clip-rule="evenodd" fill="#2f221a" fill-rule="evenodd"><path d="m.146118 12c0-.2761.223858-.5.5-.5h22.054082c.2761 0 .5.2239.5.5s-.2239.5-.5.5h-22.054082c-.276142 0-.5-.2239-.5-.5z"/><path d="m17.3776 6.1973c.198-.19257.5145-.18823.7071.00969l5.2973 5.44441c.1888.1941.1888.5033 0 .6974l-5.2973 5.4444c-.1926.1979-.5091.2023-.7071.0097-.1979-.1926-.2022-.5091-.0096-.707l4.958-5.0958-4.958-5.09576c-.1926-.19792-.1883-.51447.0096-.70704z"/></g></svg>
      </a>
    </div>
  </div>
</section>"""

if re.search(pattern, html):
    html = re.sub(pattern, clean_hero_html, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced with authentic, pure luxury Vittoria hero layout.")
else:
    # Try alternative matching
    pattern_alt = r'<section class="c-hero-banner[^>]*>[\s\S]*?<\/section>'
    match = re.search(pattern_alt, html)
    if match:
        # Also remove strip if present
        html = re.sub(r'<div class="s54-features-strip">[\s\S]*?<\/div>\s*<\/div>', '', html)
        html = re.sub(pattern_alt, clean_hero_html, html, count=1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Replaced via alternative pattern.")

