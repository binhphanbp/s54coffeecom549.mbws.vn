import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    'https://s54coffeecom549.mbws.vn/api/public/health',
    'https://s54coffeecom549.mbws.vn/api/public/settings',
    'https://s54coffeecom549.mbws.vn/api/public/products',
    'https://s54coffeecom549.mbws.vn/api/public/categories',
    'https://s54coffeecom549.mbws.vn/api/public/posts'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read()
            parsed = json.loads(data)
            print(f"200 OK: {u}")
            preview = str(parsed)[:100]
            print(f"   Response: {preview}...")
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')[:150]
        print(f"HTTP {e.code}: {u} -> {body}")
    except Exception as e:
        print(f"ERR {u}: {e}")
