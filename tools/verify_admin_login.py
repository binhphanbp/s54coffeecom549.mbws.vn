import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cj),
    urllib.request.HTTPSHandler(context=ctx)
)

print("1. Fetching login page to obtain CSRF token...")
login_url = "https://s54coffeecom549.mbws.vn/vi/admin/login"
req = urllib.request.Request(login_url, headers={"User-Agent": "Mozilla/5.0"})
resp = opener.open(req)
html = resp.read().decode('utf-8')
print("   Page loaded, status:", resp.status)

# Extract _token
csrf_match = re.search(r'name="_token"\s+value="([^"]+)"', html)
if not csrf_match:
    csrf_match = re.search(r'value="([^"]+)"\s+name="_token"', html)

if csrf_match:
    token = csrf_match.group(1)
    print("   CSRF token extracted:", token[:15] + "...")
else:
    print("   CSRF token not found in form, cookies:", [c.name for c in cj])
    token = ""

print("\n2. Submitting login credentials...")
post_data = urllib.parse.urlencode({
    '_token': token,
    'email': 'admin@s54coffee.com',
    'password': 'S54Coffee@2026!Secure'
}).encode('utf-8')

post_req = urllib.request.Request(
    login_url,
    data=post_data,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": login_url,
        "Origin": "https://s54coffeecom549.mbws.vn"
    }
)

try:
    post_resp = opener.open(post_req)
    final_url = post_resp.geturl()
    body = post_resp.read().decode('utf-8', errors='ignore')
    print("   Post response status:", post_resp.status)
    print("   Redirected to:", final_url)
    if "admin" in final_url and "login" not in final_url:
        print(">>> LOGIN SUCCESSFUL! Redirected to Admin Dashboard! <<<")
    elif "dashboard" in final_url:
        print(">>> LOGIN SUCCESSFUL! Redirected to Dashboard! <<<")
    else:
        print("   Current URL after POST:", final_url)
        # Check error message if any
        errs = re.findall(r'class="[^"]*alert[^"]*"[^>]*>(.*?)</div>', body, re.DOTALL)
        if errs:
            print("   Alert message:", errs)
except urllib.error.HTTPError as e:
    print("HTTP error during login:", e.code)
    print(e.read().decode('utf-8', errors='ignore')[:300])
