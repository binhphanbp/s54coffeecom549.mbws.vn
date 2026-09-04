import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php

code = """
$logFile = 'storage/logs/laravel.log';
if (file_exists($logFile)) {
    $content = file_get_contents($logFile);
    echo "LOG SIZE: " . strlen($content) . PHP_EOL;
    echo substr($content, -3000) . PHP_EOL;
} else {
    echo "NO LOG FILE: " . $logFile . PHP_EOL;
    echo "FILES IN storage/logs: " . implode(', ', scandir('storage/logs')) . PHP_EOL;
}
"""

print(run_remote_php(code, "read_laravel_log.php"))
