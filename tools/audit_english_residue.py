#!/usr/bin/env python3
"""
Comprehensive Audit of English residues across all 8 HTML files.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

pages = ['index.html', 'collections-coffee.html', 'product-detail.html', 'our-story.html', 'wholesale.html', 'blogs-news.html', 'blog-detail.html', '404.html']

common_english_patterns = [
    r'\bSubscribe\b', r'\bSave\b', r'\bOnline Exclusive\b', r'\bSpecial Bar\b',
    r'\bSelect Size\b', r'\bSize:\b', r'\bQuantity\b', r'\bAdd to Bag\b', r'\bAdd to Cart\b',
    r'\bQuick Add\b', r'\bView Product\b', r'\bShop Now\b', r'\bLearn More\b',
    r'\bDescription\b', r'\bOrigins\b', r'\bExtraction Parameters\b', r'\bRoast Profile\b',
    r'\bReviews\b', r'\bCustomer Reviews\b', r'\bWrite a review\b', r'\bRelated Products\b',
    r'\bYou may also like\b', r'\bFilter\b', r'\bSort by\b', r'\bFeatured\b',
    r'\bBest Sellers\b', r'\bNew Arrivals\b', r'\bIn Stock\b', r'\bOut of Stock\b',
    r'\bSold Out\b', r'\bRead More\b', r'\bBack to\b', r'\bShare\b',
    r'\bSubtotal\b', r'\bCheckout\b', r'\bFree Shipping\b', r'\bYour Bag\b'
]

print("=== S54 I18N ENGLISH RESIDUE AUDIT ===")
for p in pages:
    fpath = BASE_DIR / p
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding='utf-8')
    matches_found = []
    for pat in common_english_patterns:
        found = re.findall(pat, c, re.IGNORECASE)
        if found:
            matches_found.append(f"{pat} ({len(found)})")
    print(f"\n📄 {p}:")
    print("   Matches: " + (", ".join(matches_found) if matches_found else "None"))

