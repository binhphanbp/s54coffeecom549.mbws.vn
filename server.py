#!/usr/bin/env python3
"""
Vittoria Coffee Local Development & Preview Server
- Cross-platform (Linux, Windows, macOS)
- Clean URL Routing & Shopify Cart Mock API
- Robust asset routing for subpaths (/collections/..., /products/..., /pages/...)
- Accurate MIME types for Fonts (WOFF/WOFF2), SVG, MP4, and Static Assets
"""

import http.server
import socketserver
import urllib.parse
import json
import os
import sys
from pathlib import Path

PORT = int(os.environ.get('PORT', 3000))
BASE_DIR = Path(__file__).resolve().parent
os.chdir(str(BASE_DIR))

# Initial Cart State
mock_cart = {
    "token": "d7480a82b992167389148d53efd67db9",
    "note": None,
    "attributes": {},
    "original_total_price": 4400,
    "total_price": 4400,
    "total_discount": 0,
    "total_weight": 1000.0,
    "item_count": 1,
    "items": [
        {
            "id": 401234567890,
            "properties": {
                "_bundle_item": False,
                "_is_subscription": False
            },
            "quantity": 1,
            "variant_id": 401234567890,
            "key": "401234567890:1",
            "title": "Cinque Stelle Oro - 1kg Beans",
            "price": 4400,
            "original_price": 4400,
            "discounted_price": 4400,
            "line_price": 4400,
            "original_line_price": 4400,
            "total_discount": 0,
            "discounts": [],
            "sku": "VIT-ORO-1KG",
            "grams": 1000,
            "vendor": "Vittoria Coffee",
            "taxable": False,
            "product_id": 6718616502447,
            "product_has_only_default_variant": False,
            "gift_card": False,
            "final_price": 4400,
            "final_line_price": 4400,
            "url": "/product-detail.html",
            "featured_image": {
                "aspect_ratio": 1.0,
                "alt": "Cinque Stelle Oro Beans",
                "height": 1000,
                "url": "assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png",
                "width": 1000
            },
            "image": "assets/images/000_sb_beans_1kg_oro_f_V2_HOMEPAGE_500x_4_120x_2x.png",
            "handle": "cinque-stelle-beans-1kg",
            "requires_shipping": True,
            "product_type": "Beans",
            "product_title": "Cinque Stelle",
            "product_description": "Australia's favourite premium blend",
            "variant_title": "1kg Beans",
            "variant_options": ["1kg Beans"],
            "options_with_values": [
                {
                    "name": "Size",
                    "value": "1kg Beans"
                }
            ],
            "line_level_discount_allocations": []
        }
    ],
    "requires_shipping": True,
    "currency": "AUD",
    "items_subtotal_price": 4400,
    "cart_level_discount_applications": []
}

def recalculate_cart():
    count = sum(item.get('quantity', 1) for item in mock_cart['items'])
    total = sum(item.get('price', 0) * item.get('quantity', 1) for item in mock_cart['items'])
    mock_cart['item_count'] = count
    mock_cart['total_price'] = total
    mock_cart['original_total_price'] = total
    mock_cart['items_subtotal_price'] = total


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.woff': 'font/woff',
        '.woff2': 'font/woff2',
        '.ttf': 'font/ttf',
        '.svg': 'image/svg+xml',
        '.mp4': 'video/mp4',
        '.webp': 'image/webp',
        '.json': 'application/json',
        '.js': 'application/javascript',
        '.css': 'text/css',
    }

    def send_json_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip('/')

        # 1. PRIORITY: Asset Requests (Must come BEFORE clean URL routing!)
        # Check if the URL contains '/assets/' regardless of subpath (/collections/assets/...)
        if '/assets/' in parsed.path:
            asset_subpath = parsed.path[parsed.path.index('/assets/'):]
            self.path = asset_subpath
            return super().do_GET()

        # Check for static assets requested directly
        static_exts = ('.css', '.js', '.woff', '.woff2', '.ttf', '.svg', '.png', '.jpg', '.jpeg', '.webp', '.mp4', '.gif', '.ico')
        if parsed.path.lower().endswith(static_exts):
            clean_name = os.path.basename(parsed.path)
            # Check if file exists directly
            direct_file = BASE_DIR / parsed.path.lstrip('/')
            if direct_file.exists() and direct_file.is_file():
                self.path = parsed.path
                return super().do_GET()
            # Search within assets
            for sub in ['css', 'js', 'fonts', 'images', 'icons', 'media']:
                candidate = BASE_DIR / 'assets' / sub / clean_name
                if candidate.exists():
                    self.path = f'/assets/{sub}/{clean_name}'
                    return super().do_GET()

        # 2. Shopify Mock Cart JSON API
        if path.endswith('/cart.js') or path == '/cart' or path.endswith('/cart.json'):
            return self.send_json_response(mock_cart)

        if path.endswith('/localization') or path.endswith('/localization.json'):
            return self.send_json_response({"success": True})

        # 3. Clean URL Routing to HTML Pages
        if path == '' or path == '/' or path == '/index.html' or path == '/index':
            self.path = '/index.html'
        elif path.startswith('/collections'):
            self.path = '/collections-coffee.html'
        elif path.startswith('/products') or path.startswith('/product-detail'):
            self.path = '/product-detail.html'
        elif path.startswith('/pages/our-story') or path == '/our-story' or path.startswith('/pages/roasting') or path.startswith('/pages/community') or path.startswith('/pages/brewing') or path.startswith('/pages/news') or path.startswith('/pages/subscriptions'):
            self.path = '/our-story.html'
        elif path.startswith('/pages/wholesale') or path == '/wholesale' or path.startswith('/pages/business') or path == '/business' or path.startswith('/pages/contact') or path == '/contact':
            self.path = '/wholesale.html'
        elif path.startswith('/search'):
            self.path = '/collections-coffee.html'
        elif (BASE_DIR / path.lstrip('/')).is_file():
            self.path = path
        elif (BASE_DIR / (path.lstrip('/') + '.html')).is_file():
            self.path = path + '.html'
        else:
            self.path = '/404.html'

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip('/')

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'

        try:
            body = json.loads(post_data)
        except Exception:
            body = urllib.parse.parse_qs(post_data)

        if path.endswith('/cart/add.js') or path.endswith('/cart/add'):
            recalculate_cart()
            return self.send_json_response(mock_cart['items'][0] if mock_cart['items'] else {})

        if path.endswith('/cart/change.js') or path.endswith('/cart/update.js') or path.endswith('/cart/update'):
            recalculate_cart()
            return self.send_json_response(mock_cart)

        if path.endswith('/cart/clear.js') or path.endswith('/cart/clear'):
            mock_cart['items'] = []
            recalculate_cart()
            return self.send_json_response(mock_cart)

        return self.send_json_response(mock_cart)


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == '__main__':
    with ThreadedServer(('0.0.0.0', PORT), CustomHandler) as httpd:
        print(f"==================================================")
        print(f"  Vittoria Coffee Storefront Server Active")
        print(f"  Local Preview:  http://localhost:{PORT}/")
        print(f"  Network Access: http://127.0.0.1:{PORT}/")
        print(f"  Root Directory: {BASE_DIR}")
        print(f"==================================================")
        sys.stdout.flush()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down.")
            httpd.shutdown()
