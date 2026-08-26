#!/usr/bin/env python3
"""
Add dynamic filter tab translation handler to assets/js/i18n.js
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
i18n_path = BASE_DIR / 'assets/js/i18n.js'
i18n_txt = i18n_path.read_text(encoding='utf-8')

hook_code = '''
    // Dynamic Filter Pills Localizer (collections-coffee.html)
    function localizeFilterPills() {
        var currentLang = getLang();
        var filterBtns = document.querySelectorAll('.c-faceted-nav__filters-featured button, .c-faceted-nav__filters-featured .o-btn, [data-facet-button]');
        var viMap = {
            'ALL': 'TẤT CẢ',
            'ONLINE EXCLUSIVE': 'ĐỘC QUYỀN ONLINE',
            'BEANS': 'CÀ PHÊ HẠT',
            'SPECIALTY CÀ PHÊ HẠT': 'SPECIALTY CAO CẤP',
            'BLENDS': 'CÀ PHÊ BLEND',
            'SINGLE ORIGIN': 'SINGLE ORIGIN',
            'GROUND': 'CÀ PHÊ XAY',
            'FEATURED': 'NỔI BẬT'
        };
        var enMap = {
            'TẤT CẢ': 'ALL',
            'ĐỘC QUYỀN ONLINE': 'ONLINE EXCLUSIVE',
            'CÀ PHÊ HẠT': 'COFFEE BEANS',
            'SPECIALTY CAO CẤP': 'SPECIALTY BEANS',
            'SPECIALTY CÀ PHÊ HẠT': 'SPECIALTY BEANS',
            'CÀ PHÊ BLEND': 'COFFEE BLENDS',
            'CÀ PHÊ XAY': 'GROUND COFFEE',
            'NỔI BẬT': 'FEATURED'
        };

        filterBtns.forEach(function(btn) {
            var txt = (btn.textContent || '').trim();
            if (currentLang === 'vi') {
                if (viMap[txt]) btn.textContent = viMap[txt];
            } else {
                if (enMap[txt]) btn.textContent = enMap[txt];
            }
        });
    }

    // Observe dynamic filter insertion
    var filterNav = document.querySelector('[data-filters-featured]');
    if (filterNav) {
        var obs = new MutationObserver(function() {
            localizeFilterPills();
        });
        obs.observe(filterNav, { childList: true, subtree: true });
        setTimeout(localizeFilterPills, 100);
        setTimeout(localizeFilterPills, 500);
        setTimeout(localizeFilterPills, 1200);
    }
'''

if 'Dynamic Filter Pills Localizer' not in i18n_txt:
    idx = i18n_txt.rfind('})();')
    if idx != -1:
        i18n_txt = i18n_txt[:idx] + hook_code + '\n' + i18n_txt[idx:]
        i18n_path.write_text(i18n_txt, encoding='utf-8')
        print("✓ Injected dynamic filter pills localizer into assets/js/i18n.js")
    else:
        print("❌ Could not find closing tag in i18n.js")
