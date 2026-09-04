import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php

code = """
echo "RUNNING COMPOSER CHECK ON SERVER:" . PHP_EOL;
echo shell_exec('/opt/plesk/php/8.2/bin/php composer.phar -V 2>&1') . PHP_EOL;
"""

print(run_remote_php(code, "test_composer.php"))
