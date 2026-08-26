#!/usr/bin/env python3
import re
from pathlib import Path

css_path = Path('assets/css/custom.css')
c = css_path.read_text(encoding='utf-8')

old_nav_block = r'\.c-main-menu__link\.is-level-1\s*\{[\s\S]*?\.c-main-menu__link\.is-level-1:hover:after\s*\{[^}]*\}'

new_nav_block = '''.c-main-menu__link.is-level-1 {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: #FAF6F1 !important;
    text-decoration: none !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
    text-transform: none !important;
    white-space: nowrap !important;
    padding: 8px 12px !important;
    border-radius: 0 !important;
    position: relative !important;
    background: transparent !important;
    transition: color 0.25s ease !important;
    display: inline-flex !important;
    align-items: center !important;
}

.c-main-menu__link.is-level-1 .c-main-menu__link-title {
    color: inherit !important;
    transition: color 0.25s ease !important;
}

.c-main-menu__link.is-level-1:after {
    content: '' !important;
    position: absolute !important;
    bottom: 2px !important;
    left: 12px !important;
    right: 12px !important;
    height: 2px !important;
    background-color: #D68E1D !important;
    transform: scaleX(0) !important;
    transform-origin: center !important;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: none !important;
}

.c-main-menu__link.is-level-1:hover {
    color: #D68E1D !important;
    background: transparent !important;
    text-shadow: none !important;
}

.c-main-menu__link.is-level-1:hover .c-main-menu__link-title {
    color: #D68E1D !important;
}

.c-main-menu__link.is-level-1:hover:after {
    transform: scaleX(1) !important;
}'''

c = re.sub(old_nav_block, new_nav_block, c)
css_path.write_text(c, encoding='utf-8')
print("✓ Successfully replaced navigation hover with clean luxury gold amber underline & text transition")
