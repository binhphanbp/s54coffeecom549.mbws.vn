#!/usr/bin/env python3
import re
from pathlib import Path

css_path = Path('assets/css/custom.css')
c = css_path.read_text(encoding='utf-8')

old_cart_block = r'/\* 8\. Slide-out Cart Drawer \*/[\s\S]*?\.c-cart-drawer__overlay\.is-open\s*\{[^}]*\}'

new_cart_block = '''/* 8. Slide-out Cart Drawer Master Hierarchy & Zero-Overlay Bug Fix */
.c-cart-drawer,
.c-cart-drawer.is-open,
.c-cart-drawer.is-drawer-open,
.c-cart-template,
.c-cart-contents,
.c-cart-template__inner {
    z-index: 99999999 !important;
    opacity: 1 !important;
}

.c-cart-drawer .c-cart-template {
    background-color: #FAF8F5 !important;
    opacity: 1 !important;
    z-index: 99999999 !important;
}

.c-cart-drawer__overlay,
.c-cart-drawer__background {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    background-color: rgba(36, 26, 20, 0.6) !important;
    backdrop-filter: blur(4px) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    z-index: 9999990 !important;
    transition: opacity 0.3s ease, visibility 0.3s ease !important;
}

.c-cart-drawer__overlay {
    opacity: 0 !important;
    visibility: hidden !important;
}

.c-cart-drawer__overlay.is-open {
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: all !important;
}'''

c = re.sub(old_cart_block, new_cart_block, c)
css_path.write_text(c, encoding='utf-8')
print("✓ Successfully updated Cart Drawer z-index hierarchy in custom.css")
