import sys
import os
import urllib.request
import ssl

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php, ctx

setup_code = """
if (!is_dir('test_82')) {
    mkdir('test_82', 0755, true);
}
file_put_contents('test_82/.htaccess', '<FilesMatch "\\.php$">' . "\\n" . 'SetHandler "proxy:unix:///run/plesk/plesk-php82-fpm.sock|fcgi://localhost"' . "\\n" . '</FilesMatch>' . "\\n");
file_put_contents('test_82/index.php', '<?php echo "HANDLER_OUTPUT_VERSION=" . PHP_VERSION;');
echo "SETUP COMPLETED";
"""

print(run_remote_php(setup_code, "setup_test.php"))

url = "https://s54coffeecom549.mbws.vn/test_82/index.php"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        print("RESULT FROM test_82/index.php:", resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}:", e.read().decode("utf-8", errors="ignore"))
except Exception as e:
    print("Error:", e)

clean_code = """
@unlink('test_82/.htaccess');
@unlink('test_82/index.php');
@rmdir('test_82');
echo "CLEANED UP";
"""
print(run_remote_php(clean_code, "clean_test.php"))
