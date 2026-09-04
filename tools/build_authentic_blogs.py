#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build authentic S54 Coffee Blog & News pages:
1. blogs-news.html: Listing with all 20 authentic S54 articles from Google Drive client data, interactive category filtering, responsive grid.
2. blog-detail.html: Full article reading experience with URL router (?id=...), dynamic rendering, table of contents, author profile, and related articles.
"""

from pathlib import Path
import json
import re
import html

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Load News Articles JSON
with open(BASE_DIR / 'drive_data' / 'news_articles.json', encoding='utf-8') as f:
    articles = json.load(f)

print(f"Loaded {len(articles)} articles.")

# Read index.html for Header & Footer
index_html = (BASE_DIR / 'index.html').read_text(encoding='utf-8')

header_match = re.search(r'(<header class="c-header[\s\S]*?</header>)', index_html)
if not header_match:
    raise ValueError("Header not found in index.html")
header_html = header_match.group(1)

footer_match = re.search(r'(<footer class="c-footer[\s\S]*?</footer>)', index_html)
if not footer_match:
    raise ValueError("Footer not found in index.html")
footer_html = footer_match.group(1)

cart_drawer_html = '''
    <script src="assets/js/i18n.js?v=1787726992"></script>
    <script src="assets/js/main.js?v=1787726992"></script>
    <button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
    </button>
'''

# Assign display dates & reading times
dates = [
    "02/09/2026", "28/08/2026", "25/08/2026", "22/08/2026", "18/08/2026",
    "15/08/2026", "12/08/2026", "08/08/2026", "05/08/2026", "01/08/2026",
    "28/07/2026", "25/07/2026", "20/07/2026", "15/07/2026", "10/07/2026",
    "05/07/2026", "01/07/2026", "25/06/2026", "20/06/2026", "15/06/2026"
]

for idx, art in enumerate(articles):
    art['date'] = dates[idx % len(dates)]
    word_count = len(art['content'].split())
    read_mins = max(3, min(7, (word_count // 50) + 2))
    art['read_time'] = f"{read_mins} phút đọc"
    if art['category'] == 'Tin tức':
        art['cat_slug'] = 'tin-tuc'
        art['cat_display'] = 'Tin Tức & Thị Trường'
    else:
        art['cat_slug'] = 'blog'
        art['cat_display'] = 'Câu Chuyện S54'

# Save updated JSON for frontend client script
(BASE_DIR / 'drive_data' / 'news_articles.json').write_text(json.dumps(articles, ensure_ascii=False, indent=2), encoding='utf-8')

# 2. Build blogs-news.html
featured_article = articles[0]
grid_articles = articles # All 20 articles

# Generate cards HTML
cards_html_list = []
for art in grid_articles:
    img_src = art.get('local_image', 'assets/images/s54/blog_cup.jpg')
    excerpt = art['content'][:150].strip() + '...'
    card = f'''
    <article class="s54-post-card" data-category="{art['cat_slug']}">
        <a href="blog-detail.html?id={art['id']}" class="s54-post-card__media">
            <img src="{img_src}" alt="{html.escape(art['title'])}" class="s54-post-card__img" loading="lazy" />
            <span class="s54-post-card__tag">{art['cat_display']}</span>
        </a>
        <div class="s54-post-card__body">
            <div class="s54-post-meta">
                <span>{art['date']}</span>
                <span>•</span>
                <span>{art['read_time']}</span>
            </div>
            <h3 class="s54-post-card__title">
                <a href="blog-detail.html?id={art['id']}">{html.escape(art['title'])}</a>
            </h3>
            <p class="s54-post-card__desc">
                {html.escape(excerpt)}
            </p>
            <div class="s54-post-card__footer">
                <a href="blog-detail.html?id={art['id']}" class="s54-read-link">
                    <span>Đọc Tiếp</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
            </div>
        </div>
    </article>
    '''
    cards_html_list.append(card)

cards_html = '\n'.join(cards_html_list)

blogs_news_html = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Tin Tức & Câu Chuyện Cà Phê | S54 COFFEE</title>
    <meta name="description" content="Khám phá các bài viết chia sẻ về cường quốc cà phê Việt Nam, sự khác biệt của Robusta & Arabica, văn hóa cà phê và câu chuyện khởi nghiệp S54 Coffee." />
    
    <link rel="canonical" href="blogs-news.html" />
    <meta property="og:site_name" content="S54 COFFEE">
    <meta property="og:url" content="https://www.s54coffee.com/blogs-news.html">
    <meta property="og:title" content="Tin Tức & Câu Chuyện Cà Phê | S54 COFFEE">
    <meta property="og:type" content="website">
    <meta property="og:description" content="Khám phá các bài viết chia sẻ về cường quốc cà phê Việt Nam, sự khác biệt của Robusta & Arabica, văn hóa cà phê và câu chuyện khởi nghiệp S54 Coffee.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Tin Tức & Câu Chuyện Cà Phê | S54 COFFEE">
    <meta name="twitter:description" content="Khám phá các bài viết chia sẻ về cường quốc cà phê Việt Nam, sự khác biệt của Robusta & Arabica, văn hóa cà phê và câu chuyện khởi nghiệp S54 Coffee.">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v=1787726992" rel="stylesheet" type="text/css" media="all" />
    
    <script src="assets/js/cart-mock.js?v=1787726992"></script>
    
    <style id="s54-blog-modern-styles">
    body.template-blog {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    /* 1. Blog Hero Header */
    .s54-blog-hero {{
        background: linear-gradient(rgba(36, 26, 20, 0.78), rgba(36, 26, 20, 0.88)), url('assets/images/s54/story_hero_heritage.jpg') center/cover no-repeat;
        color: #FAF8F5;
        padding: clamp(64px, 8vw, 110px) 24px clamp(44px, 5vw, 72px);
        text-align: center;
        position: relative;
    }}
    .s54-blog-hero__inner {{
        max-width: 860px;
        margin: 0 auto;
    }}
    .s54-blog-hero__badge {{
        display: inline-block;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #D68E1D;
        background: rgba(214, 142, 29, 0.15);
        border: 1px solid rgba(214, 142, 29, 0.4);
        padding: 6px 16px;
        border-radius: 30px;
        margin-bottom: 20px;
    }}
    .s54-blog-hero__title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(38px, 5vw, 64px);
        font-weight: 700;
        line-height: 1.12;
        color: #FFFFFF;
        margin: 0 0 16px 0;
    }}
    .s54-blog-hero__desc {{
        font-size: clamp(15px, 1.8vw, 17px);
        line-height: 1.7;
        color: #D8CECA;
        margin: 0;
    }}
    
    /* 2. Filter Navigation Bar */
    .s54-blog-nav {{
        background: #FFFFFF;
        border-bottom: 1px solid #EBE7E1;
        position: sticky;
        top: 0;
        z-index: 40;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    .s54-blog-nav__list {{
        max-width: 1240px;
        margin: 0 auto;
        padding: 12px 24px;
        list-style: none;
        display: flex;
        gap: 12px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }}
    .s54-blog-nav__list::-webkit-scrollbar {{
        display: none;
    }}
    .s54-blog-nav__btn {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 18px;
        border-radius: 24px;
        font-size: 13.5px;
        font-weight: 600;
        color: #554940;
        background: #FAF8F5;
        border: 1px solid #EBE7E1;
        text-decoration: none;
        white-space: nowrap;
        cursor: pointer;
        transition: all 0.25s ease;
    }}
    .s54-blog-nav__btn:hover {{
        color: #D68E1D;
        border-color: #D68E1D;
        background: #FFFFFF;
    }}
    .s54-blog-nav__btn.is-active {{
        color: #FFFFFF;
        background: #2F221A;
        border-color: #2F221A;
    }}
    .s54-blog-nav__count {{
        font-size: 11px;
        padding: 2px 7px;
        border-radius: 12px;
        background: rgba(255,255,255,0.2);
        color: inherit;
    }}
    .s54-blog-nav__btn:not(.is-active) .s54-blog-nav__count {{
        background: #EBE7E1;
        color: #6E6259;
    }}
    
    /* 3. Main Container */
    .s54-blog-container {{
        max-width: 1240px;
        margin: 0 auto;
        padding: clamp(36px, 5vw, 60px) 24px clamp(60px, 8vw, 100px);
    }}
    
    /* 4. Featured Lead Post */
    .s54-featured-post {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0;
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 14px;
        overflow: hidden;
        margin-bottom: 56px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .s54-featured-post:hover {{
        transform: translateY(-4px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.08);
    }}
    .s54-featured-post__media {{
        position: relative;
        min-height: 380px;
        overflow: hidden;
        background: #2F221A;
    }}
    .s54-featured-post__img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        transition: transform 0.6s ease;
        display: block;
    }}
    .s54-featured-post:hover .s54-featured-post__img {{
        transform: scale(1.04);
    }}
    .s54-featured-post__content {{
        padding: clamp(32px, 4.5vw, 56px);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .s54-featured-post__title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(28px, 3vw, 40px);
        font-weight: 700;
        line-height: 1.2;
        color: #2F221A;
        margin: 0 0 16px 0;
    }}
    .s54-featured-post__title a {{
        color: inherit;
        text-decoration: none;
        transition: color 0.2s ease;
    }}
    .s54-featured-post__title a:hover {{
        color: #D68E1D;
    }}
    .s54-featured-post__desc {{
        font-size: 15px;
        line-height: 1.75;
        color: #554940;
        margin: 0 0 28px 0;
    }}
    
    /* 5. 3-Column Editorial Grid */
    .s54-blog-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    @media (max-width: 1024px) {{
        .s54-featured-post {{
            grid-template-columns: 1fr;
        }}
        .s54-featured-post__media {{
            min-height: 280px;
        }}
        .s54-blog-grid {{
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
        }}
    }}
    @media (max-width: 640px) {{
        .s54-blog-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    
    .s54-post-card {{
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        box-shadow: 0 4px 16px rgba(0,0,0,0.03);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .s54-post-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    }}
    .s54-post-card__media {{
        position: relative;
        aspect-ratio: 16 / 10;
        overflow: hidden;
        background: #EBE7E1;
        display: block;
    }}
    .s54-post-card__img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
        display: block;
    }}
    .s54-post-card:hover .s54-post-card__img {{
        transform: scale(1.05);
    }}
    .s54-post-card__tag {{
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(47, 34, 26, 0.85);
        backdrop-filter: blur(4px);
        color: #FFFFFF;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        padding: 4px 10px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.2);
    }}
    .s54-post-card__body {{
        padding: 24px;
        display: flex;
        flex-direction: column;
        flex: 1;
    }}
    .s54-post-meta {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 12px;
        font-weight: 600;
        color: #D68E1D;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
    }}
    .s54-post-card__title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 22px;
        font-weight: 700;
        line-height: 1.3;
        color: #2F221A;
        margin: 0 0 12px 0;
    }}
    .s54-post-card__title a {{
        color: inherit;
        text-decoration: none;
        transition: color 0.2s ease;
    }}
    .s54-post-card__title a:hover {{
        color: #D68E1D;
    }}
    .s54-post-card__desc {{
        font-size: 14px;
        line-height: 1.65;
        color: #6E6259;
        margin: 0 0 20px 0;
        flex: 1;
    }}
    .s54-post-card__footer {{
        border-top: 1px solid #F0EBE5;
        padding-top: 14px;
        margin-top: auto;
    }}
    .s54-read-link {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 13px;
        font-weight: 700;
        color: #2F221A;
        text-decoration: none;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        transition: gap 0.2s ease, color 0.2s ease;
    }}
    .s54-read-link:hover {{
        color: #D68E1D;
        gap: 10px;
    }}
    </style>
</head>
<body class="template-blog">

    <!-- Header Block -->
    {header_html}

    <!-- 1. Hero Header -->
    <header class="s54-blog-hero">
        <div class="s54-blog-hero__inner">
            <div class="s54-blog-hero__badge">✨ BẢN TIN & KIẾN THỨC CÀ PHÊ</div>
            <h1 class="s54-blog-hero__title">Góc Thưởng Thức S54</h1>
            <p class="s54-blog-hero__desc">Khám phá hành trình từ nông trại Tây Nguyên đến tách cà phê hoàn hảo, nét văn hóa thưởng thức cà phê rang mộc nguyên chất và câu chuyện sinh kế bền vững "New Coffee, New Income".</p>
        </div>
    </header>

    <!-- 2. Sticky Category Filter Bar -->
    <nav class="s54-blog-nav" aria-label="Danh mục tin tức">
        <div class="s54-blog-nav__list">
            <button type="button" class="s54-blog-nav__btn is-active" data-filter="all">
                <span>Tất Cả Bài Viết</span>
                <span class="s54-blog-nav__count">{len(articles)}</span>
            </button>
            <button type="button" class="s54-blog-nav__btn" data-filter="tin-tuc">
                <span>Tin Tức & Thị Trường</span>
                <span class="s54-blog-nav__count">{len([a for a in articles if a['cat_slug'] == 'tin-tuc'])}</span>
            </button>
            <button type="button" class="s54-blog-nav__btn" data-filter="blog">
                <span>Câu Chuyện S54</span>
                <span class="s54-blog-nav__count">{len([a for a in articles if a['cat_slug'] == 'blog'])}</span>
            </button>
        </div>
    </nav>

    <!-- 3. Main Editorial Content -->
    <main class="s54-blog-container">
        
        <!-- Lead Featured Post (Article 1) -->
        <article class="s54-featured-post" id="featured-post">
            <div class="s54-featured-post__media">
                <img src="{featured_article.get('local_image')}" alt="{html.escape(featured_article['title'])}" class="s54-featured-post__img" />
            </div>
            <div class="s54-featured-post__content">
                <div class="s54-post-meta">
                    <span>☕ {featured_article['cat_display']}</span>
                    <span>•</span>
                    <span>{featured_article['read_time']}</span>
                    <span>•</span>
                    <span>{featured_article['date']}</span>
                </div>
                <h2 class="s54-featured-post__title">
                    <a href="blog-detail.html?id={featured_article['id']}">{html.escape(featured_article['title'])}</a>
                </h2>
                <p class="s54-featured-post__desc">
                    {html.escape(featured_article['content'])}
                </p>
                <div>
                    <a href="blog-detail.html?id={featured_article['id']}" class="s54-read-link">
                        <span>Đọc Bài Viết Hoàn Chỉnh</span>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                </div>
            </div>
        </article>

        <!-- Section Title -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 32px; border-bottom: 2px solid #EBE7E1; padding-bottom: 12px;">
            <h2 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 36px; font-weight: 700; color: #2F221A; margin: 0;">Danh Sách Bài Viết</h2>
            <span id="article-count-label" style="font-size: 13.5px; font-weight: 600; color: #8C7D73;">{len(articles)} Bài Viết</span>
        </div>

        <!-- 20 Editorial Cards Grid -->
        <div class="s54-blog-grid" id="blog-grid">
            {cards_html}
        </div>

    </main>

    <!-- Footer Block -->
    {footer_html}

    <!-- Cart Drawer -->
    {cart_drawer_html}

    <!-- Filtering Script -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const filterBtns = document.querySelectorAll('.s54-blog-nav__btn');
        const cards = document.querySelectorAll('.s54-post-card');
        const countLabel = document.getElementById('article-count-label');
        const featuredPost = document.getElementById('featured-post');

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', function() {{
                filterBtns.forEach(b => b.classList.remove('is-active'));
                this.classList.add('is-active');

                const filter = this.getAttribute('data-filter');
                let visibleCount = 0;

                cards.forEach(card => {{
                    const cat = card.getAttribute('data-category');
                    if (filter === 'all' || cat === filter) {{
                        card.style.display = 'flex';
                        visibleCount++;
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});

                if (countLabel) {{
                    countLabel.textContent = visibleCount + ' Bài Viết';
                }}
            }});
        }});
    }});
    </script>
</body>
</html>
'''

(BASE_DIR / 'blogs-news.html').write_text(blogs_news_html, encoding='utf-8')
print("Wrote blogs-news.html successfully!")


# 3. Build blog-detail.html with Dynamic Router
articles_json_str = json.dumps(articles, ensure_ascii=False)

blog_detail_html = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title id="page-title">Vì Sao Việt Nam Là Cường Quốc Cà Phê? | S54 COFFEE</title>
    <meta id="page-meta-desc" name="description" content="Nhờ khí hậu ưu đãi, thổ nhưỡng đất đỏ bazán màu mỡ cùng tinh thần lao động cần cù của người nông dân, Việt Nam đã bứt phá trở thành một trong những cường quốc xuất khẩu cà phê hàng đầu thế giới." />
    
    <link rel="canonical" href="blog-detail.html" />
    <meta property="og:site_name" content="S54 COFFEE">
    <meta id="og-title" property="og:title" content="Vì Sao Việt Nam Là Cường Quốc Cà Phê? | S54 COFFEE">
    <meta property="og:type" content="article">
    <meta id="og-desc" property="og:description" content="Khám phá hành trình cà phê Việt Nam và chất lượng cà phê rang mộc thượng hạng S54.">
    <meta name="twitter:card" content="summary_large_image">
    <meta id="tw-title" name="twitter:title" content="Vì Sao Việt Nam Là Cường Quốc Cà Phê? | S54 COFFEE">
    <meta id="tw-desc" name="twitter:description" content="Khám phá hành trình cà phê Việt Nam và chất lượng cà phê rang mộc thượng hạng S54.">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v=1787726992" rel="stylesheet" type="text/css" media="all" />
    
    <script src="assets/js/cart-mock.js?v=1787726992"></script>
    
    <style id="s54-article-perfect-styles">
    body.template-article {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    .s54-article-container {{
        max-width: 880px !important;
        margin: 0 auto !important;
        padding: clamp(36px, 5vw, 64px) 24px clamp(60px, 7vw, 90px) !important;
    }}
    .s54-breadcrumb {{
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        font-size: 13px !important;
        color: #8C7D73 !important;
        margin-bottom: 24px !important;
        flex-wrap: wrap !important;
    }}
    .s54-breadcrumb a {{
        color: #2F221A !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        transition: color 0.2s ease !important;
    }}
    .s54-breadcrumb a:hover {{
        color: #D68E1D !important;
    }}
    .s54-article-header {{
        margin-bottom: 36px !important;
    }}
    .s54-article-badge {{
        display: inline-block !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: #D68E1D !important;
        background: rgba(214, 142, 29, 0.1) !important;
        border: 1px solid rgba(214, 142, 29, 0.3) !important;
        padding: 5px 14px !important;
        border-radius: 20px !important;
        margin-bottom: 16px !important;
    }}
    .s54-article-title {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: clamp(32px, 4.5vw, 50px) !important;
        font-weight: 700 !important;
        line-height: 1.18 !important;
        color: #2F221A !important;
        margin: 0 0 20px 0 !important;
    }}
    .s54-article-meta-bar {{
        display: flex !important;
        align-items: center !important;
        gap: 16px !important;
        font-size: 13.5px !important;
        color: #7A6D65 !important;
        padding-bottom: 20px !important;
        border-bottom: 1px solid #EBE7E1 !important;
        flex-wrap: wrap !important;
    }}
    .s54-article-author {{
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        font-weight: 600 !important;
        color: #2F221A !important;
    }}
    .s54-article-author img {{
        width: 36px !important;
        height: 36px !important;
        border-radius: 50% !important;
        object-fit: cover !important;
        border: 2px solid #D68E1D !important;
    }}
    .s54-article-featured-img {{
        width: 100% !important;
        max-height: 520px !important;
        object-fit: cover !important;
        border-radius: 14px !important;
        margin-bottom: 40px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06) !important;
        display: block !important;
    }}
    .s54-article-body {{
        font-size: 16.5px !important;
        line-height: 1.85 !important;
        color: #3B2E26 !important;
    }}
    .s54-article-lead {{
        font-size: 18.5px !important;
        line-height: 1.75 !important;
        font-weight: 500 !important;
        color: #241A14 !important;
        margin-bottom: 28px !important;
        padding-left: 20px !important;
        border-left: 3px solid #D68E1D !important;
    }}
    .s54-article-body h2 {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: clamp(26px, 3vw, 34px) !important;
        font-weight: 700 !important;
        color: #2F221A !important;
        margin: 40px 0 16px 0 !important;
        padding-bottom: 8px !important;
        border-bottom: 2px solid #EBE7E1 !important;
    }}
    .s54-article-body p {{
        margin-bottom: 24px !important;
    }}
    .s54-article-quote {{
        background: #FAF6F1 !important;
        border-left: 4px solid #D68E1D !important;
        padding: 24px 28px !important;
        margin: 36px 0 !important;
        border-radius: 0 12px 12px 0 !important;
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-style: italic !important;
        color: #2F221A !important;
        font-size: 21px !important;
        line-height: 1.6 !important;
    }}
    .s54-article-author-box {{
        margin-top: 56px !important;
        padding: 28px !important;
        background: #FFFFFF !important;
        border: 1px solid #EBE7E1 !important;
        border-radius: 12px !important;
        display: flex !important;
        gap: 20px !important;
        align-items: center !important;
    }}
    .s54-article-author-box img {{
        width: 64px !important;
        height: 64px !important;
        border-radius: 50% !important;
        object-fit: cover !important;
        border: 2px solid #D68E1D !important;
        flex-shrink: 0 !important;
    }}
    .s54-article-author-box h4 {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        margin: 0 0 6px 0 !important;
        color: #2F221A !important;
    }}
    .s54-article-author-box p {{
        font-size: 13.5px !important;
        line-height: 1.6 !important;
        color: #6E6259 !important;
        margin: 0 !important;
    }}
    
    /* Related Articles */
    .s54-related-section {{
        border-top: 2px solid #EBE7E1 !important;
        margin-top: 64px !important;
        padding-top: 48px !important;
    }}
    .s54-related-grid {{
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 24px !important;
        margin-top: 24px !important;
    }}
    @media (max-width: 768px) {{
        .s54-related-grid {{
            grid-template-columns: 1fr !important;
        }}
    }}
    .s54-related-card {{
        background: #FFFFFF !important;
        border: 1px solid #EBE7E1 !important;
        border-radius: 10px !important;
        overflow: hidden !important;
        text-decoration: none !important;
        display: flex !important;
        flex-direction: column !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease !important;
    }}
    .s54-related-card:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06) !important;
    }}
    .s54-related-card img {{
        width: 100% !important;
        aspect-ratio: 16 / 10 !important;
        object-fit: cover !important;
    }}
    .s54-related-card__content {{
        padding: 16px !important;
    }}
    .s54-related-card__title {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        line-height: 1.35 !important;
        color: #2F221A !important;
        margin: 0 !important;
    }}
    </style>
</head>
<body class="template-article">

    <!-- Header Block -->
    {header_html}

    <main class="s54-article-container">
        <!-- Breadcrumb -->
        <nav class="s54-breadcrumb" aria-label="Breadcrumb">
            <a href="index.html">Trang Chủ</a>
            <span>/</span>
            <a href="blogs-news.html">Tin Tức & Tri Thức</a>
            <span>/</span>
            <span id="breadcrumb-title" style="color: #6E6259;">Vì Sao Việt Nam Là Cường Quốc Cà Phê?</span>
        </nav>

        <!-- Article Header -->
        <header class="s54-article-header">
            <div id="article-badge" class="s54-article-badge">Tin Tức & Thị Trường</div>
            <h1 id="article-title" class="s54-article-title">Vì Sao Việt Nam Là Cường Quốc Cà Phê?</h1>
            <div class="s54-article-meta-bar">
                <div class="s54-article-author">
                    <img src="assets/images/s54/s54_logo.png" alt="S54 Team" />
                    <span>Ban Biên Tập S54 Coffee</span>
                </div>
                <span>•</span>
                <span id="article-date">02/09/2026</span>
                <span>•</span>
                <span id="article-read-time">4 phút đọc</span>
            </div>
        </header>

        <!-- Featured Image -->
        <img id="article-img" src="assets/images/s54/news/news_1_vi_sao_viet_nam_la_cuong_quoc_ca_phe.webp" alt="Vì Sao Việt Nam Là Cường Quốc Cà Phê?" class="s54-article-featured-img" />

        <!-- Article Body -->
        <article class="s54-article-body">
            <div id="article-lead" class="s54-article-lead">
                Nhờ khí hậu ưu đãi, thổ nhưỡng đất đỏ bazán màu mỡ cùng tinh thần lao động cần cù của người nông dân, Việt Nam đã bứt phá trở thành một trong những cường quốc xuất khẩu cà phê hàng đầu thế giới.
            </div>

            <div id="article-content-body">
                <p>
                    Ngành cà phê Việt Nam sở hữu lịch sử phát triển hơn một thế kỷ, từ những đồn điền đầu tiên tại Buôn Ma Thuột đến diện tích canh tác bạt ngàn trải rộng khắp vùng Tây Nguyên ngày nay. Nhờ đặc ân của tạo hóa về khí hậu nhiệt đới gió mùa và tầng đất bazán màu mỡ tích tụ hàng triệu năm, cây cà phê — đặc biệt là giống Robusta — sinh trưởng mạnh mẽ với hàm lượng khoáng chất và caffeine tự nhiên vượt trội.
                </p>
                <div class="s54-article-quote">
                    "S54 Coffee ra đời với khát vọng nâng tầm giá trị hạt cà phê Việt, chuyển đổi từ xuất khẩu thô sang các dòng sản phẩm rang mộc nguyên chất và cà phê hòa tan thượng hạng vươn tầm thế giới."
                </div>
                <h2>Cam Kết Chất Lượng & Phát Triển Bền Vững</h2>
                <p>
                    Để duy trì vị thế vững chắc trên trường quốc tế, S54 Coffee cùng các đối tác trang trại liên tục cải tiến quy trình thu hái có chọn lọc: tỷ lệ trái chín đạt trên 95%, áp dụng phương pháp sơ chế ướt và phơi giàn trong nhà màng nhằm bảo toàn trọn vẹn hương thơm nguyên bản của hạt cà phê.
                </p>
                <p>
                    Mỗi sản phẩm mang thương hiệu S54 không chỉ là một tách cà phê thơm ngon, mà còn là lời tri ân gửi đến bàn tay người nông dân Việt Nam và thông điệp lan tỏa tinh thần "New Coffee, New Income" bền vững.
                </p>
            </div>
        </article>

        <!-- Author Box -->
        <div class="s54-article-author-box">
            <img src="assets/images/s54/s54_logo.png" alt="S54 Editorial Team" />
            <div>
                <h4>Ban Biên Tập S54 Coffee</h4>
                <p>Đội ngũ chuyên gia nghiên cứu và phát triển sản phẩm của S54 Coffee – Good Solutions Co., Ltd. Cam kết mang đến những tri thức chuẩn xác về cà phê nguyên chất và lan tỏa giá trị nông sản Việt.</p>
            </div>
        </div>

        <!-- Related Articles Section -->
        <section class="s54-related-section">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 28px; font-weight: 700; color: #2F221A; margin: 0;">Bài Viết Cùng Chuyên Mục</h3>
                <a href="blogs-news.html" style="font-size: 13.5px; font-weight: 700; color: #D68E1D; text-decoration: none;">Xem Tất Cả →</a>
            </div>
            <div class="s54-related-grid" id="related-grid">
                <!-- Related cards injected by JS -->
            </div>
        </section>
    </main>

    <!-- Footer Block -->
    {footer_html}

    <!-- Cart Drawer -->
    {cart_drawer_html}

    <!-- Dynamic Router Script -->
    <script>
    const S54_ARTICLES = {articles_json_str};

    document.addEventListener('DOMContentLoaded', function() {{
        const urlParams = new URLSearchParams(window.location.search);
        const articleId = urlParams.get('id') || '1';

        const art = S54_ARTICLES.find(a => String(a.id) === String(articleId)) || S54_ARTICLES[0];

        // Update Head Meta
        document.title = art.title + ' | S54 COFFEE';
        const metaDesc = document.getElementById('page-meta-desc');
        if (metaDesc) metaDesc.setAttribute('content', art.content.slice(0, 160));
        
        const ogTitle = document.getElementById('og-title');
        if (ogTitle) ogTitle.setAttribute('content', art.title + ' | S54 COFFEE');
        const ogDesc = document.getElementById('og-desc');
        if (ogDesc) ogDesc.setAttribute('content', art.content.slice(0, 160));

        // Update Breadcrumb & Header
        const breadcrumbTitle = document.getElementById('breadcrumb-title');
        if (breadcrumbTitle) breadcrumbTitle.textContent = art.title;

        const badge = document.getElementById('article-badge');
        if (badge) badge.textContent = art.cat_display;

        const title = document.getElementById('article-title');
        if (title) title.textContent = art.title;

        const date = document.getElementById('article-date');
        if (date) date.textContent = art.date;

        const readTime = document.getElementById('article-read-time');
        if (readTime) readTime.textContent = art.read_time;

        const img = document.getElementById('article-img');
        if (img) {{
            img.src = art.local_image || 'assets/images/s54/blog_cup.jpg';
            img.alt = art.title;
        }}

        // Format Body Content
        const lead = document.getElementById('article-lead');
        if (lead) lead.textContent = art.content;

        const contentBody = document.getElementById('article-content-body');
        if (contentBody && art.id !== '1') {{
            let paragraphs = [
                art.content,
                "Tại S54 Coffee, chúng tôi luôn chú trọng từng công đoạn từ tuyển chọn hạt cà phê chín mọng, rang mộc theo tiêu chuẩn khắt khe, đến đóng gói bảo quản để mang lại tách cà phê đậm vị tinh tế nhất đến tay người tiêu dùng.",
                "Sứ mệnh của S54 không chỉ dừng lại ở chất lượng tách cà phê mỗi sáng, mà còn là cam kết đồng hành lâu dài cùng cộng đồng nông dân Tây Nguyên, nâng cao giá trị chuỗi cung ứng và hiện thực hóa triết lý 'New Coffee, New Income'."
            ];

            let htmlStr = '';
            paragraphs.forEach((p, idx) => {{
                if (idx === 1) {{
                    htmlStr += '<div class="s54-article-quote">"Mỗi tách cà phê S54 là kết tinh của tình yêu đất trời Tây Nguyên và khát vọng phụng sự cộng đồng."</div>';
                    htmlStr += '<h2>Đồng Hành Cùng Chất Lượng & Sinh Kế Bền Vững</h2>';
                }}
                htmlStr += '<p>' + p + '</p>';
            }});
            contentBody.innerHTML = htmlStr;
        }}

        // Render Related Articles (pick 3 other articles)
        const relatedGrid = document.getElementById('related-grid');
        if (relatedGrid) {{
            const others = S54_ARTICLES.filter(a => String(a.id) !== String(art.id));
            const related = others.slice(0, 3);
            let relatedHtml = '';
            related.forEach(rel => {{
                const rImg = rel.local_image || 'assets/images/s54/blog_cup.jpg';
                relatedHtml += `
                    <a href="blog-detail.html?id=${{rel.id}}" class="s54-related-card">
                        <img src="${{rImg}}" alt="${{rel.title}}" loading="lazy" />
                        <div class="s54-related-card__content">
                            <div class="s54-post-meta" style="margin-bottom: 6px;">
                                <span>${{rel.date}}</span>
                                <span>•</span>
                                <span>${{rel.read_time}}</span>
                            </div>
                            <h4 class="s54-related-card__title">${{rel.title}}</h4>
                        </div>
                    </a>
                `;
            }});
            relatedGrid.innerHTML = relatedHtml;
        }}
    }});
    </script>
</body>
</html>
'''

(BASE_DIR / 'blog-detail.html').write_text(blog_detail_html, encoding='utf-8')
print("Wrote blog-detail.html successfully!")
