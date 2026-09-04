import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php

trigger_code = """
set_time_limit(300);
$cmd = '/opt/plesk/php/8.2/bin/php -d memory_limit=1024M composer.phar install --no-dev --prefer-dist --optimize-autoloader --no-interaction > composer_build.log 2>&1 &';
exec($cmd);
echo "COMPOSER_STARTED";
"""

print("Triggering composer install on server...")
res = run_remote_php(trigger_code, "run_composer.php")
print("Response:", res)

# Monitor log
check_code = """
if (file_exists('composer_build.log')) {
    echo file_get_contents('composer_build.log');
} else {
    echo "NO_LOG_YET";
}
"""

for i in range(25):
    time.sleep(4)
    log_output = run_remote_php(check_code, "check_composer_log.php")
    print(f"--- Check {i+1} (Elapsed { (i+1)*4 }s) ---")
    lines = log_output.strip().split('\n')
    for l in lines[-8:]:
        print(l)
    if "Generating optimized autoload files" in log_output or "Generated optimized autoload" in log_output:
        print("\n>>> COMPOSER INSTALL SUCCESSFUL! <<<")
        break
    if "Script @php" in log_output or "No lockfile found" in log_output or "killed" in log_output.lower():
        print("\n>>> COMPOSER FINISHED OR STOPPED <<<")
        break
