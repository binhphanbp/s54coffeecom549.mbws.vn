#!/usr/bin/env python3
"""
Phase 1: Fix CRITICAL structural issues across all HTML pages.
1. Fix collections-coffee.html "of" -> "trên" corruption
2. Fix product-detail.html corrupted class names
3. Fix wholesale.html hidden form
4. Clean duplicate jQuery, Orbe junk, duplicate footer elements
5. Inject proper header/footer lang switchers
6. Add scroll-to-top button
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

print("=" * 70)
print("  UX FIX Phase 1: Critical HTML Structure Fixes")
print("=" * 70)

# =====================================================================
# FIX 1: collections-coffee.html — Reverse "of" → "trên" corruption
# =====================================================================
coll_path = BASE_DIR / 'collections-coffee.html'
if coll_path.exists():
    content = coll_path.read_text(encoding='utf-8')
    
    # Reverse the systematic corruption
    replacements = [
        ('typetrên', 'typeof'),
        ('instancetrên', 'instanceof'),
        ('trênfset', 'offset'),
        ('trênfee', 'offee'),
        ('wtrênf', 'woff'),
        ('nth-trên-type', 'nth-of-type'),
        ('prtrênile', 'profile'),
        ('trêntTeams', 'oftTeams'),
        ('MicrostrêntTeams', 'MicrosoftTeams'),
        ('ctrênfee', 'coffee'),
        ('Ctrênfee', 'Coffee'),
        ('roast-prtrênile', 'roast-profile'),
        ('trênfering', 'offering'),
        ('for...trên', 'for...of'),
        # Fix "for(const [a,s] trên new" patterns
    ]
    
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ collections-coffee.html: Fixed '{old}' → '{new}' ({count} instances)")
    
    # Fix remaining "trên" that should be "of" in JS contexts
    # Pattern: ) trên  or  trên new FormData  or  trên this
    content = re.sub(r'\)\s+trên\s+', ') of ', content)
    content = re.sub(r'trên new\b', 'of new', content)
    
    # Fix doubled words like "Hữu Cơ Hữu Cơ"
    content = content.replace('Hữu Cơ Hữu Cơ', 'Hữu Cơ')
    
    coll_path.write_text(content, encoding='utf-8')
    print(f"  ✓ collections-coffee.html: All 'trên' corruption reversed")

# =====================================================================
# FIX 2: product-detail.html — Fix corrupted class names
# =====================================================================
pd_path = BASE_DIR / 'product-detail.html'
if pd_path.exists():
    content = pd_path.read_text(encoding='utf-8')
    
    # Fix corrupted Okendo review class
    content = content.replace('okeĐánh Giá Của Khách Hàng', 'okeReviews')
    
    # Fix inline CSS syntax error (missing ; and })
    content = re.sub(
        r'text-transform: capitalize\s*</style>',
        'text-transform: capitalize; }</style>',
        content
    )
    
    # Fix montserrat references
    content = content.replace("font-family: montserrat;", "font-family: 'Plus Jakarta Sans', sans-serif;")
    
    pd_path.write_text(content, encoding='utf-8')
    print(f"  ✓ product-detail.html: Fixed corrupted classes and CSS syntax")

# =====================================================================
# FIX 3: wholesale.html — Unhide the contact form
# =====================================================================
ws_path = BASE_DIR / 'wholesale.html'
if ws_path.exists():
    content = ws_path.read_text(encoding='utf-8')
    
    # Remove the display:none rules hiding the form
    content = re.sub(
        r'\.c-contact__form-input\s*\{\s*display:\s*none\s*;?\s*\}',
        '.c-contact__form-input { display: block; }',
        content
    )
    content = re.sub(
        r'\.c-contact__form-label\s*\{\s*display:\s*none\s*;?\s*\}',
        '.c-contact__form-label { display: block; }',
        content
    )
    content = re.sub(
        r'\.c-contact__form-pill\s*\{\s*display:\s*none\s*;?\s*\}',
        '.c-contact__form-pill { display: inline-block; }',
        content
    )
    content = re.sub(
        r'\.c-contact__form-label--inline\s*\{\s*display:\s*none\s*;?\s*\}',
        '.c-contact__form-label--inline { display: inline-block; }',
        content
    )
    content = re.sub(
        r'\.contact-day\s*\{\s*display:\s*none\s*;?\s*\}',
        '.contact-day { display: block; }',
        content
    )
    
    # Fix montserrat references
    content = content.replace("font-family: montserrat;", "font-family: 'Plus Jakarta Sans', sans-serif;")
    
    ws_path.write_text(content, encoding='utf-8')
    print(f"  ✓ wholesale.html: Unhid contact form fields")

# =====================================================================
# FIX 4: Fix montserrat references in ALL files
# =====================================================================
for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    if 'montserrat' in content:
        content = content.replace("font-family: montserrat;", "font-family: 'Plus Jakarta Sans', sans-serif;")
        content = content.replace("font-family: montserrat", "font-family: 'Plus Jakarta Sans', sans-serif")
        fpath.write_text(content, encoding='utf-8')
        print(f"  ✓ {page}: Fixed montserrat → Plus Jakarta Sans")

# =====================================================================
# FIX 5: Remove duplicate jQuery in ALL files
# =====================================================================
for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    
    # Find all jQuery script tags
    jquery_pattern = r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/jquery/3\.5\.1/jquery\.min\.js"></script>'
    matches = list(re.finditer(jquery_pattern, content))
    
    if len(matches) > 1:
        # Remove all but the first
        for match in reversed(matches[1:]):
            content = content[:match.start()] + content[match.end():]
        fpath.write_text(content, encoding='utf-8')
        print(f"  ✓ {page}: Removed {len(matches)-1} duplicate jQuery tag(s)")

# =====================================================================
# FIX 6: Remove ALL Orbe junk scripts/styles from ALL files
# =====================================================================
for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    original_len = len(content)
    
    # Remove Orbe script blocks
    content = re.sub(r'<script>\s*var orbitoMK[\s\S]*?</script>', '', content)
    content = re.sub(r'<script>\s*if\s*\(\s*document\.getElementById\([\'"]md-footer-selector-block[\'"]\)[\s\S]*?</script>', '', content)
    content = re.sub(r'<script>\s*function initializeCountrySelector[\s\S]*?</script>', '', content)
    content = re.sub(r'<script>\s*initializeCountrySelector[\s\S]*?</script>', '', content)
    
    # Remove Orbe style/CSS blocks
    content = re.sub(r'<style data-orbe-flags[^>]*>[\s\S]*?</style>', '', content)
    content = re.sub(r'<script type="application/json" id="orbe-flag-css-meta"[^>]*>[\s\S]*?</script>', '', content)
    
    saved = original_len - len(content)
    if saved > 0:
        fpath.write_text(content, encoding='utf-8')
        print(f"  ✓ {page}: Removed {saved:,} bytes of Orbe junk")

# =====================================================================
# FIX 7: Remove ALL existing lang switchers, then inject clean ones
# =====================================================================
HEADER_SWITCHER = '''<div class="c-lang-switcher c-lang-switcher--header" data-lang-switcher>
        <button type="button" class="c-lang-btn is-active" data-lang="vi" aria-label="Tiếng Việt">🇻🇳 VI</button>
        <span class="c-lang-divider">|</span>
        <button type="button" class="c-lang-btn" data-lang="en" aria-label="English">🇬🇧 EN</button>
    </div>'''

FOOTER_SWITCHER = '''<div class="c-lang-switcher c-lang-switcher--footer" data-lang-switcher>
        <span class="c-lang-label">Ngôn ngữ / Language:</span>
        <button type="button" class="c-lang-btn is-active" data-lang="vi" aria-label="Tiếng Việt">🇻🇳 Tiếng Việt</button>
        <span class="c-lang-divider">|</span>
        <button type="button" class="c-lang-btn" data-lang="en" aria-label="English">🇬🇧 English</button>
    </div>'''

SCROLL_TOP = '''<button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
</button>'''

for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    
    # Remove ALL existing lang switchers
    content = re.sub(
        r'<div class="c-lang-switcher[^"]*"[^>]*data-lang-switcher[^>]*>[\s\S]*?</div>\s*',
        '',
        content
    )
    
    # Inject header switcher into topbar (after topbar-messages closing div)
    topbar_match = re.search(r'(class="c-header__topbar-message[^"]*"[^>]*>[^<]*</a>)(</div>)', content)
    if topbar_match:
        insert_pos = topbar_match.end(1)
        content = content[:insert_pos] + '\n    ' + HEADER_SWITCHER + '\n    ' + content[insert_pos:]
        print(f"  ✓ {page}: Injected header lang switcher")
    
    # Inject footer switcher before last </footer>
    footer_close = content.rfind('</footer>')
    if footer_close != -1:
        content = content[:footer_close] + '\n' + FOOTER_SWITCHER + '\n' + content[footer_close:]
        print(f"  ✓ {page}: Injected footer lang switcher")
    
    # Add scroll-to-top button before </body>
    if 'c-scroll-top' not in content:
        body_close = content.rfind('</body>')
        if body_close != -1:
            content = content[:body_close] + SCROLL_TOP + '\n' + content[body_close:]
    
    # Clean excessive whitespace
    content = re.sub(r'\n{4,}', '\n\n', content)
    
    fpath.write_text(content, encoding='utf-8')

# =====================================================================
# FIX 8: Remove duplicate footer bottom-bars
# =====================================================================
for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    
    bottom_bars = list(re.finditer(r'<div class="c-footer__bottom-bar">[\s\S]*?</div>\s*</div>', content))
    if len(bottom_bars) > 1:
        for match in reversed(bottom_bars[:-1]):
            content = content[:match.start()] + content[match.end():]
        fpath.write_text(content, encoding='utf-8')
        print(f"  ✓ {page}: Removed {len(bottom_bars)-1} duplicate footer bottom-bar(s)")

print("\n✅ Phase 1 complete: All critical HTML fixes applied.")
