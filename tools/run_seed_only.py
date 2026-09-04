import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php

seed_code = """
set_time_limit(180);
echo "=== SEEDING ===" . PHP_EOL;
echo shell_exec('/opt/plesk/php/8.2/bin/php artisan db:seed --force 2>&1') . PHP_EOL;
try {
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=db_c3c66f76;charset=utf8mb4', 'db_c3c66f76', 'oVkoa?B0p_t9ePk6');
    $userCount = $pdo->query('SELECT count(*) FROM users')->fetchColumn();
    $prodCount = $pdo->query('SELECT count(*) FROM products')->fetchColumn();
    $catCount = $pdo->query('SELECT count(*) FROM categories')->fetchColumn();
    $postCount = $pdo->query('SELECT count(*) FROM posts')->fetchColumn();
    echo "SEED RESULT: Users={$userCount}, Products={$prodCount}, Categories={$catCount}, Posts={$postCount}" . PHP_EOL;
} catch (Exception $e) {
    echo "DB Error: " . $e->getMessage() . PHP_EOL;
}
"""

print(run_remote_php(seed_code, "run_seed_only.php"))
