#!/usr/bin/env python3
"""
Deployment script for s54coffeecom549.mbws.vn
- Creates optimized zip deployment package
- Uploads via FTP to /httpdocs
- Executes server-side PHP extraction for instantaneous deployment
- Cleans up temporary artifacts and verifies deployment
"""

import os
import sys
import zipfile
import ftplib
import urllib.request
import ssl
import time
from pathlib import Path

# Force UTF-8 on Windows terminal
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

FTP_HOST = "203.205.31.252"
FTP_USER = "u513776f0"
FTP_PASS = "1~dzR0hkLJ0~tlgm"
REMOTE_DIR = "/httpdocs"
DOMAIN = "s54coffeecom549.mbws.vn"

BASE_DIR = Path(__file__).resolve().parent

EXCLUDE_DIRS = {'.git', '.github', '.idea', '.vscode', 'tools', '__pycache__'}
EXCLUDE_FILES = {'deploy.py', 'deploy.zip', 'extractor.php', '.gitignore'}

def print_header():
    print("=" * 65)
    print("      S54 Coffee Storefront - Deployment Pipeline")
    print(f"      Target: https://{DOMAIN}/ ({FTP_HOST})")
    print("=" * 65)

def create_deploy_package(zip_filename="deploy.zip", code_only=False):
    mode_text = "code-only (fast)" if code_only else "full package"
    print(f"[1/4] Building optimized {mode_text} deployment package...")
    zip_path = BASE_DIR / zip_filename
    if zip_path.exists():
        zip_path.unlink()

    file_count = 0
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(BASE_DIR):
            # Exclude unwanted directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            if code_only:
                # In code-only mode, skip large media and image directories (already present on remote server)
                dirs[:] = [d for d in dirs if d not in {'media', 'images'}]
            
            rel_dir = os.path.relpath(root, BASE_DIR)
            if rel_dir == '.':
                rel_dir = ''
                
            for file in files:
                if file in EXCLUDE_FILES or file.endswith('.log') or file.endswith('.tmp'):
                    continue
                if code_only and (file.endswith('.mp4') or file.endswith('.mov') or file.endswith('.webm')):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.join(rel_dir, file) if rel_dir else file
                zipf.write(file_path, arcname)
                file_count += 1

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    print(f"      [OK] Package built: {file_count} files ({size_mb:.2f} MB)")
    return zip_path

def create_extractor_script():
    php_code = """<?php
header('Content-Type: text/plain; charset=utf-8');
set_time_limit(300);

$zipFile = __DIR__ . '/deploy.zip';
if (!file_exists($zipFile)) {
    echo "ERROR: deploy.zip not found.\\n";
    exit(1);
}

if (!class_exists('ZipArchive')) {
    echo "ERROR: ZipArchive extension is missing.\\n";
    exit(1);
}

$zip = new ZipArchive();
if ($zip->open($zipFile) === TRUE) {
    $zip->extractTo(__DIR__);
    $zip->close();
    echo "SUCCESS: Extracted all files successfully.\\n";
    @unlink($zipFile);
    @unlink(__FILE__);
} else {
    echo "ERROR: Failed to open zip file.\\n";
    exit(1);
}
"""
    extractor_path = BASE_DIR / "extractor.php"
    extractor_path.write_text(php_code, encoding='utf-8')
    return extractor_path

def upload_via_ftp(zip_path, extractor_path):
    print(f"[2/4] Uploading package to {FTP_HOST} ({REMOTE_DIR})...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(REMOTE_DIR)

    # Upload deploy.zip with progress
    zip_size = os.path.getsize(zip_path)
    uploaded = 0

    def progress(chunk):
        nonlocal uploaded
        uploaded += len(chunk)
        pct = (uploaded / zip_size) * 100
        print(f"\r      Uploading deploy.zip: {pct:.1f}% ({uploaded / (1024*1024):.2f}/{zip_size / (1024*1024):.2f} MB)", end="", flush=True)

    with open(zip_path, "rb") as f:
        ftp.storbinary("STOR deploy.zip", f, callback=progress)
    print("\n      [OK] deploy.zip uploaded.")

    # Upload extractor.php
    with open(extractor_path, "rb") as f:
        ftp.storbinary("STOR extractor.php", f)
    print("      [OK] extractor.php uploaded.")

    ftp.quit()

def trigger_extraction():
    print("[3/4] Triggering server-side extraction...")
    extractor_url = f"http://{DOMAIN}/extractor.php"
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(extractor_url, headers={'User-Agent': 'Deployer/1.0', 'Host': DOMAIN})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            output = resp.read().decode('utf-8')
            print(f"      Server response: {output.strip()}")
            if "SUCCESS" in output:
                return True
    except Exception as e:
        print(f"      Trying direct IP with Host header: {e}")
        ip_url = f"http://{FTP_HOST}/extractor.php"
        req = urllib.request.Request(ip_url, headers={'User-Agent': 'Deployer/1.0', 'Host': DOMAIN})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            output = resp.read().decode('utf-8')
            print(f"      Server response: {output.strip()}")
            return "SUCCESS" in output

    return False

def verify_deployment():
    print("[4/4] Verifying production deployment...")
    test_urls = [
        f"http://{DOMAIN}/",
        f"http://{DOMAIN}/collections/all-coffee-products",
        f"http://{DOMAIN}/products/cinque-stelle-beans",
        f"http://{DOMAIN}/pages/our-story",
        f"http://{DOMAIN}/pages/wholesale",
        f"http://{DOMAIN}/assets/css/layouts.critical.css",
        f"http://{DOMAIN}/assets/js/cart-mock.js"
    ]
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    for u in test_urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Host': DOMAIN})
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                print(f"      [OK] {u:55} -> Status: {resp.status}")
        except Exception as e:
            print(f"      [FAIL] {u:55} -> Error: {e}")

def cleanup_local(zip_path, extractor_path):
    if zip_path.exists():
        zip_path.unlink()
    if extractor_path.exists():
        extractor_path.unlink()

def main():
    print_header()
    code_only = '--fast' in sys.argv or '--code-only' in sys.argv
    zip_path = create_deploy_package(code_only=code_only)
    extractor_path = create_extractor_script()
    try:
        upload_via_ftp(zip_path, extractor_path)
        if trigger_extraction():
            print("\n" + "=" * 65)
            print("  ✨ DEPLOYMENT COMPLETED SUCCESSFULLY!")
            print(f"  Live Storefront: https://{DOMAIN}/")
            print("=" * 65 + "\n")
            verify_deployment()
        else:
            print("[-] Warning: Extraction trigger did not return SUCCESS.")
    finally:
        cleanup_local(zip_path, extractor_path)

if __name__ == '__main__':
    main()
