#!/usr/bin/env python3
"""
Clean UI script:
1. Strips all Orbe Geolocation modal / dropdown junk from footer.
2. Injects exactly one clean Language Switcher in Header Topbar and exactly one in Footer.
3. Fixes CSS so there is zero overlap.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', '404.html']

HEADER_SWITCHER = '''
    <div class="c-lang-switcher" data-lang-switcher>
        <button type="button" class="c-lang-btn is-active" data-lang="vi" title="Tiếng Việt (Chính)">
            <span class="c-lang-flag">🇻🇳</span> Tiếng Việt
        </button>
        <span class="c-lang-divider">|</span>
        <button type="button" class="c-lang-btn" data-lang="en" title="English">
            <span class="c-lang-flag">🇬🇧</span> English
        </button>
    </div>
'''

FOOTER_SWITCHER = '''
    <div class="c-lang-switcher c-lang-switcher--footer" data-lang-switcher style="margin: 20px auto 10px; display: flex; justify-content: center; align-items: center;">
        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-right: 8px; color: #AC8A62; font-weight: 600;">Ngôn ngữ / Language:</span>
        <button type="button" class="c-lang-btn is-active" data-lang="vi">
            🇻🇳 Tiếng Việt (Chính)
        </button>
        <span class="c-lang-divider">|</span>
        <button type="button" class="c-lang-btn" data-lang="en">
            🇬🇧 English
        </button>
    </div>
'''

for page in PAGES:
    fpath = BASE_DIR / page
    if not fpath.exists():
        continue
    content = fpath.read_text(encoding='utf-8')
    
    # 1. Remove all old Orbe / md-footer selector blocks
    content = re.sub(r'<div id=\"md-footer-selector-block\"[\s\S]*?<!-- END app snippet -->', '', content)
    content = re.sub(r'<div class=\"md-footer-selector__container\"[\s\S]*?</md-footer-selector__form>', '', content)
    content = re.sub(r'<div id=\"md-app-modal\"[\s\S]*?</div>\s*</div>\s*</div>', '', content)
    content = re.sub(r'<div class=\"md-app-modal-overlay\"[\s\S]*?</div>', '', content)

    # Remove any existing .c-lang-switcher
    content = re.sub(r'<div class=[\"\']c-lang-switcher[\s\S]*?</div>\s*</div>', '', content)
    content = re.sub(r'<div class=[\"\']c-lang-switcher[^>]*>[\s\S]*?</div>', '', content)

    # 2. Add header switcher into Announcement bar
    def inject_header_switcher(match):
        ann_content = match.group(1).strip()
        # strip any existing switcher
        ann_text = re.sub(r'<div class=[\"\']c-lang-switcher[\s\S]*', '', ann_content).strip()
        return f'<div class="c-announcement-bar"><div class="c-announcement-bar__inner" style="display:flex; justify-content:space-between; align-items:center; width:100%; max-width:1200px; margin:0 auto; padding:0 16px;"><span>{ann_text}</span>{HEADER_SWITCHER}</div></div>'

    content = re.sub(r'<div class=[\"\']c-announcement-bar[\"\']>([\s\S]*?)</div>', inject_header_switcher, content, count=1)

    # 3. Add footer switcher before copyright or before </footer>
    if '<footer' in content:
        # Find where copyright is or insert before </footer>
        if '© 2026 Vittoria Coffee' in content:
            content = content.replace('© 2026 Vittoria Coffee', FOOTER_SWITCHER + '\n<div style="font-size: 11px; color: #AC8A62;">© 2026 Vittoria Coffee')
        else:
            content = content.replace('</footer>', FOOTER_SWITCHER + '\n</footer>')

    fpath.write_text(content, encoding='utf-8')
    print(f"✓ Cleaned UI & properly injected static switchers in {page}")

