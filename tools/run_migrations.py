import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from tools.remote_probe import run_remote_php

migration_code = """
set_time_limit(300);
echo "=== RUNNING MIGRATION ===" . PHP_EOL;
echo shell_exec('/opt/plesk/php/8.2/bin/php artisan migrate:fresh --force 2>&1') . PHP_EOL;

echo "=== RUNNING SEEDER ===" . PHP_EOL;
echo shell_exec('/opt/plesk/php/8.2/bin/php artisan db:seed --force 2>&1') . PHP_EOL;

echo "=== VERIFYING DATABASE TABLES & RECORDS ===" . PHP_EOL;
try {
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=db_c3c66f76;charset=utf8mb4', 'db_c3c66f76', 'oVkoa?B0p_t9ePk6');
    $tables = $pdo->query("SHOW TABLES")->fetchAll(PDO::FETCH_COLUMN);
    echo "Total tables in DB: " . count($tables) . PHP_EOL;
    echo "Tables: " . implode(', ', $tables) . PHP_EOL;
    
    $userCount = $pdo->query("SELECT count(*) FROM users")->fetchColumn();
    $prodCount = $pdo->query("SELECT count(*) FROM products")->fetchColumn();
    $catCount = $pdo->query("SELECT count(*) FROM categories")->fetchColumn();
    $postCount = $pdo->query("SELECT count(*) FROM posts")->fetchColumn();
    echo "Records summary: Users={$userCount}, Products={$prodCount}, Categories={$catCount}, Posts={$postCount}" . PHP_EOL;
} catch (Exception $e) {
    echo "DB Query Error: " . $e->getMessage() . PHP_EOL;
}
"""

print(run_remote_php(migration_code, "run_db_migrate.php"))
