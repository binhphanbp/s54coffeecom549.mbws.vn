import http.server
import socketserver
import urllib.parse
import json
import os
import sys

PORT = 3000
DIRECTORY = r'd:\Workspace\matbao-ws\s54coffeecom549.mbws.vn'
os.chdir(DIRECTORY)

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

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip('/')
        
        # Shopify Cart JSON API
        if path.endswith('/cart.js') or path == '/cart' or path.endswith('/cart.json'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(mock_cart).encode('utf-8'))
            return
            
        # Clean URL Routing to HTML Subpages
        if path == '/collections/coffee' or path == '/collections':
            self.path = '/collections-coffee.html'
        elif path.startswith('/products/'):
            self.path = '/product-detail.html'
        elif path == '/pages/our-story':
            self.path = '/our-story.html'
        elif path == '/pages/wholesale':
            self.path = '/wholesale.html'
        elif path == '' or path == '/':
            self.path = '/index.html'
        else:
            self.path = parsed.path

        return super().do_GET()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(mock_cart).encode('utf-8'))

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == '__main__':
    with ThreadedServer(('0.0.0.0', PORT), CustomHandler) as httpd:
        print(f"Serving at http://127.0.0.1:{PORT} and http://localhost:{PORT}")
        sys.stdout.flush()
        httpd.serve_forever()
