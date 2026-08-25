#!/usr/bin/env python3
"""
Complete Installer for Frontend UI/UX Skills:
1. ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill)
2. ui-design (mblode/agent-skills/skills/ui-design)
3. ui-animation (mblode/agent-skills/skills/ui-animation)
4. typography-audit (mblode/agent-skills/skills/typography-audit)
5. responsive-design (mblode/agent-skills/skills/responsive-design)
6. impeccable-design (pbakaus/impeccable/plugin/skills/impeccable)
7. web-quality-audit (addyosmani/web-quality-skills/skills/web-quality-audit)
8. accessibility-audit (addyosmani/web-quality-skills/skills/accessibility)
"""

import os
import shutil
import urllib.request
import json
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
LOCAL_SKILLS_DIR = WORKSPACE_ROOT / '.agents' / 'skills'
GLOBAL_SKILLS_DIR = Path.home() / '.gemini' / 'antigravity' / 'skills'

LOCAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
GLOBAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

def download_file(url, target_path):
    target_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
        target_path.write_bytes(content)

def install_skill_tree(owner_repo, branch, src_prefix, local_skill_name):
    print(f"📦 Installing: {local_skill_name} from {owner_repo}:{src_prefix}...")
    api_url = f"https://api.github.com/repos/{owner_repo}/git/trees/{branch}?recursive=1"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  ✗ Failed tree for {owner_repo}: {e}")
        return False

    tree = data.get('tree', [])
    skill_files = [item['path'] for item in tree if item['path'].startswith(src_prefix) and item['type'] == 'blob']
    
    dest_dir = LOCAL_SKILLS_DIR / local_skill_name
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for path in skill_files:
        rel_subpath = path[len(src_prefix):].lstrip('/')
        target_file = dest_dir / rel_subpath
        raw_url = f"https://raw.githubusercontent.com/{owner_repo}/{branch}/{path}"
        try:
            download_file(raw_url, target_file)
            count += 1
        except Exception as e:
            print(f"    ✗ Failed {path}: {e}")
            
    print(f"  ✓ {local_skill_name}: Installed {count} files")
    
    # Sync to global
    global_dest = GLOBAL_SKILLS_DIR / local_skill_name
    if global_dest.exists():
        shutil.rmtree(global_dest)
    shutil.copytree(dest_dir, global_dest)
    return True

skills = [
    ('mblode/agent-skills', 'main', 'skills/ui-design', 'ui-design'),
    ('mblode/agent-skills', 'main', 'skills/ui-animation', 'ui-animation'),
    ('mblode/agent-skills', 'main', 'skills/typography-audit', 'typography-audit'),
    ('mblode/agent-skills', 'main', 'skills/responsive-design', 'responsive-design'),
    ('pbakaus/impeccable', 'main', 'plugin/skills/impeccable', 'impeccable-design'),
    ('addyosmani/web-quality-skills', 'main', 'skills/web-quality-audit', 'web-quality-audit'),
    ('addyosmani/web-quality-skills', 'main', 'skills/accessibility', 'accessibility-audit'),
    ('nextlevelbuilder/ui-ux-pro-max-skill', 'main', 'src/ui-ux-pro-max', 'ui-ux-pro-max')
]

for repo, branch, prefix, name in skills:
    install_skill_tree(repo, branch, prefix, name)

print("\n✨ All skills successfully downloaded and synced to:")
print(f"  1. Workspace : {LOCAL_SKILLS_DIR}")
print(f"  2. Global AGY: {GLOBAL_SKILLS_DIR}")

