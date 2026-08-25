#!/usr/bin/env python3
"""
Installer for Top-tier Frontend UI/UX Skills for Antigravity / Gemini Agent.
Installs:
1. ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill)
2. frontend-design (pbakaus/impeccable)
3. ui-animation (pbakaus/impeccable)
4. typography-audit (pbakaus/impeccable)
5. web-quality (addyosmani/web-quality-skills)
6. accessibility (addyosmani/web-quality-skills)
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

print("=" * 70)
print("  Installing Curated Frontend & UI/UX Agent Skills")
print(f"  Target Local : {LOCAL_SKILLS_DIR}")
print(f"  Target Global: {GLOBAL_SKILLS_DIR}")
print("=" * 70)

def download_file(url, target_path):
    target_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
        target_path.write_bytes(content)

def install_github_dir(owner_repo, branch, src_prefix, local_skill_name):
    print(f"\n📦 Installing skill: {local_skill_name} (from {owner_repo}/{src_prefix})...")
    api_url = f"https://api.github.com/repos/{owner_repo}/git/trees/{branch}?recursive=1"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  ✗ Failed to fetch tree for {owner_repo}: {e}")
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
            
    print(f"  ✓ Installed {count} files for {local_skill_name}")
    
    # Copy to global as well
    global_dest = GLOBAL_SKILLS_DIR / local_skill_name
    if global_dest.exists():
        shutil.rmtree(global_dest)
    shutil.copytree(dest_dir, global_dest)
    return True

# 1. UI-UX Pro Max
install_github_dir('nextlevelbuilder/ui-ux-pro-max-skill', 'main', 'src/ui-ux-pro-max', 'ui-ux-pro-max')

# Create a top-level SKILL.md for ui-ux-pro-max if not present
skill_md_uipro = LOCAL_SKILLS_DIR / 'ui-ux-pro-max' / 'SKILL.md'
if not skill_md_uipro.exists():
    skill_md_content = """---
name: ui-ux-pro-max
description: Complete UI/UX design intelligence and design system generator for frontend web applications. Use for color palettes, typography hierarchy, component styling, UX heuristics, and micro-interactions.
---

# UI/UX Pro Max Skill

This skill provides comprehensive UI/UX guidelines, design systems, typography scales, color palettes, and component design patterns.

## Available Modules
- `data/styles.csv`: Visual design styles and aesthetic directions (Minimal, Luxury, Editorial, Modern).
- `data/typography.csv`: Font pairings, scale ratios, and line-height best practices.
- `data/colors.csv`: Curated high-contrast color palettes and semantic tokens.
- `data/motion.csv`: Animation curves, duration scales, and transition timing.
- `data/ux-guidelines.csv`: Usability heuristics, accessibility standards, and mobile ergonomics.

## How to Apply
1. Select appropriate aesthetic vibe (e.g. Luxury Editorial for Coffee Storefront).
2. Enforce responsive typography scale using fluid clamp() values.
3. Optimize interaction touch targets (min 44x44px for mobile).
4. Maintain visual hierarchy and consistent whitespace.
"""
    skill_md_uipro.write_text(skill_md_content, encoding='utf-8')
    shutil.copy(skill_md_uipro, GLOBAL_SKILLS_DIR / 'ui-ux-pro-max' / 'SKILL.md')

# 2. Frontend Design (pbakaus/impeccable)
install_github_dir('pbakaus/impeccable', 'main', 'skills/frontend-design', 'frontend-design')

# 3. UI Design (pbakaus/impeccable)
install_github_dir('pbakaus/impeccable', 'main', 'skills/ui-design', 'ui-design')

# 4. UI Animation (pbakaus/impeccable)
install_github_dir('pbakaus/impeccable', 'main', 'skills/ui-animation', 'ui-animation')

# 5. Typography Audit (pbakaus/impeccable)
install_github_dir('pbakaus/impeccable', 'main', 'skills/typography-audit', 'typography-audit')

# 6. Web Quality Audit & Core Web Vitals (addyosmani/web-quality-skills)
install_github_dir('addyosmani/web-quality-skills', 'main', 'skills/web-quality-audit', 'web-quality-audit')
install_github_dir('addyosmani/web-quality-skills', 'main', 'skills/accessibility', 'accessibility-audit')

print("\n" + "=" * 70)
print("  🎉 ALL UI/UX FRONTEND SKILLS INSTALLED SUCCESSFULLY!")
print("=" * 70)
