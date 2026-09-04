import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    'https://s54coffeecom549.mbws.vn/up',
    'https://s54coffeecom549.mbws.vn/admin',
    'https://s54coffeecom549.mbws.vn/vi/admin',
    'https://s54coffeecom549.mbws.vn/vi/admin/login'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            print(f"{resp.status} {u} -> Final: {resp.geturl()}")
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')[:300]
        print(f"HTTP {e.code} {u} -> {body}")
    except Exception as e:
        print(f"ERR {u}: {e}")
