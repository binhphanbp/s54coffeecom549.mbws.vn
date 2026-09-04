import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php

setup_env_code = """
// 1. Create necessary directories and set permissions
$dirs = [
    'bootstrap/cache',
    'storage/framework/cache/data',
    'storage/framework/sessions',
    'storage/framework/views',
    'storage/logs',
    'storage/app/public'
];
foreach ($dirs as $d) {
    if (!is_dir($d)) {
        mkdir($d, 0777, true);
    }
    @chmod($d, 0777);
}
@chmod('bootstrap/cache', 0777);
@chmod('storage', 0777);

echo "DIRECTORIES CREATED & PERMISSIONS APPLIED" . PHP_EOL;

// 2. Generate .env file
$envContent = <<<EOD
APP_NAME="S54 COFFEE"
APP_ENV=production
APP_KEY=
APP_DEBUG=false
APP_URL=https://s54coffeecom549.mbws.vn

TRUSTED_PROXIES=*

APP_LOCALE=vi
APP_FALLBACK_LOCALE=en
MULTILINGUAL_ENABLED=true
MULTILINGUAL_MODE=manual
CONTENT_DEFAULT_LOCALE=vi
CONTENT_FALLBACK_LOCALE=vi
TRANSLATION_PROVIDER=google
APP_FAKER_LOCALE=vi_VN

ADMIN_NAME="S54 Admin"
ADMIN_EMAIL=admin@s54coffee.com
ADMIN_PASSWORD=S54Coffee@2026!Secure

APP_MAINTENANCE_DRIVER=file
BCRYPT_ROUNDS=12

LOG_CHANNEL=stack
LOG_STACK=single
LOG_LEVEL=error

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=db_c3c66f76
DB_USERNAME=db_c3c66f76
DB_PASSWORD="oVkoa?B0p_t9ePk6"

SESSION_DRIVER=file
SESSION_LIFETIME=120
SESSION_ENCRYPT=false
SESSION_PATH=/
SESSION_DOMAIN=null
SESSION_SECURE_COOKIE=true
SESSION_HTTP_ONLY=true
SESSION_SAME_SITE=lax

CACHE_STORE=file
QUEUE_CONNECTION=sync
MAIL_MAILER=log
EOD;

file_put_contents('.env', $envContent);
echo ".ENV CREATED" . PHP_EOL;

// 3. Generate APP_KEY
echo shell_exec('/opt/plesk/php/8.2/bin/php artisan key:generate --force 2>&1') . PHP_EOL;

// 4. Run package:discover
echo shell_exec('/opt/plesk/php/8.2/bin/php artisan package:discover --ansi 2>&1') . PHP_EOL;
"""

print(run_remote_php(setup_env_code, "setup_laravel_env.php"))
