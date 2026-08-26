#!/usr/bin/env python3
"""
Generate complete luxury Blog & News pages for S54 Coffee:
1. blogs-news.html (Catalog listing with filter tabs, featured hero post, article cards, pagination)
2. blog-detail.html (Full editorial article with rich typography, table of contents, author box, related posts)
"""

from pathlib import Path
import re
import time

BASE_DIR = Path(__file__).resolve().parent.parent

# Read index.html header & footer to keep 100% brand consistency
index_html = (BASE_DIR / 'index.html').read_text(encoding='utf-8')

# Extract Header Block
header_match = re.search(r'(<div class="c-announcement-bar">[\s\S]*?</header>\s*</div>)', index_html)
header_html = header_match.group(1) if header_match else ''

# Extract Footer Block
footer_match = re.search(r'(<div id="shopify-section-footer"[\s\S]*?</footer>\s*</div>)', index_html)
footer_html = footer_match.group(1) if footer_match else ''

BLOG_LIST_HTML = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Tin Tức & Kiến Thức Cà Phê | S54 COFFEE</title>
    <meta name="description" content="Khám phá các bài viết chia sẻ kiến thức cà phê sạch rang mộc nguyên chất, hướng dẫn pha chế và câu chuyện thương hiệu S54 Coffee - Good Solutions." />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v={int(time.time())}" rel="stylesheet" type="text/css" media="all" />
    
    <style id="s54-direct-typography-override">
    @media (min-width: 768px) {{
        h1, .o-heading--1, .s54-hero-title, .c-hero-banner__title, .c-hero-banner__title span {{
            font-size: 68px !important;
            line-height: 1.08 !important;
        }}
        h2, .o-heading--2, .c-blog-heading, .s54-section-title {{
            font-size: 56px !important;
            line-height: 1.12 !important;
        }}
    }}
    
    /* Blog Specific Luxury Styles */
    .s54-blog-hero {{
        background: linear-gradient(rgba(36, 26, 20, 0.75), rgba(36, 26, 20, 0.85)), url('assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg') center/cover no-repeat;
        color: #FAF8F5;
        padding: clamp(60px, 8vw, 110px) 24px clamp(40px, 5vw, 70px);
        text-align: center;
    }}
    .s54-blog-hero__badge {{
        display: inline-block;
        padding: 6px 16px;
        background: rgba(214, 142, 29, 0.2);
        border: 1px solid #D68E1D;
        border-radius: 50px;
        color: #E8C17F;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 16px;
    }}
    .s54-blog-hero__title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(36px, 5vw, 64px);
        font-weight: 700;
        margin: 0 0 16px;
        color: #FFFFFF;
    }}
    .s54-blog-hero__desc {{
        max-width: 680px;
        margin: 0 auto;
        font-size: clamp(14px, 1.2vw, 16px);
        line-height: 1.6;
        color: #D8CEBE;
    }}
    
    /* Category Filter Tabs */
    .s54-blog-nav {{
        background: #FAF8F5;
        border-bottom: 1px solid #EBE7E1;
        position: sticky;
        top: 60px;
        z-index: 20;
        padding: 12px 24px;
    }}
    .s54-blog-nav__list {{
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        gap: 12px;
        overflow-x: auto;
        padding-bottom: 4px;
        scrollbar-width: none;
        list-style: none;
        padding-left: 0;
    }}
    .s54-blog-nav__list::-webkit-scrollbar {{ display: none; }}
    .s54-blog-nav__btn {{
        padding: 8px 18px;
        border-radius: 30px;
        border: 1px solid #D8CEBE;
        background: #FFFFFF;
        color: #2F221A;
        font-size: 13px;
        font-weight: 600;
        text-decoration: none;
        white-space: nowrap;
        transition: all 0.25s ease;
        cursor: pointer;
    }}
    .s54-blog-nav__btn:hover, .s54-blog-nav__btn.is-active {{
        background: #2F221A;
        color: #FAF8F5;
        border-color: #2F221A;
    }}
    
    /* Blog Content Layout */
    .s54-blog-container {{
        max-width: 1280px;
        margin: 0 auto;
        padding: clamp(40px, 5vw, 70px) 24px;
    }}
    
    /* Featured Article Card */
    .s54-featured-post {{
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: clamp(24px, 4vw, 48px);
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 56px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .s54-featured-post:hover {{
        transform: translateY(-4px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.08);
    }}
    .s54-featured-post__img {{
        width: 100%;
        height: 100%;
        min-height: 340px;
        object-fit: cover;
        display: block;
    }}
    .s54-featured-post__content {{
        padding: clamp(24px, 4vw, 44px);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .s54-post-meta {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 12px;
        font-weight: 600;
        color: #D68E1D;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }}
    .s54-post-title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(24px, 2.5vw, 36px);
        font-weight: 700;
        line-height: 1.2;
        color: #2F221A;
        margin: 0 0 14px;
    }}
    .s54-post-excerpt {{
        font-size: 14px;
        line-height: 1.65;
        color: #6E6259;
        margin: 0 0 24px;
    }}
    .s54-read-btn {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #2F221A;
        text-decoration: none;
        transition: color 0.2s ease, transform 0.2s ease;
    }}
    .s54-read-btn:hover {{
        color: #D68E1D;
        transform: translateX(4px);
    }}
    
    /* Blog Grid */
    .s54-blog-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
        gap: 32px;
    }}
    .s54-post-card {{
        background: #FFFFFF;
        border: 1px solid #EBE7E1;
        border-radius: 8px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .s54-post-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.06);
    }}
    .s54-post-card__img-wrap {{
        position: relative;
        padding-bottom: 60%;
        overflow: hidden;
    }}
    .s54-post-card__img {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .s54-post-card:hover .s54-post-card__img {{
        transform: scale(1.05);
    }}
    .s54-post-card__body {{
        padding: 24px;
        display: flex;
        flex-direction: column;
        flex: 1;
    }}
    .s54-post-card__title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 22px;
        font-weight: 700;
        line-height: 1.3;
        color: #2F221A;
        margin: 0 0 10px;
    }}
    .s54-post-card__title a {{
        color: inherit;
        text-decoration: none;
        transition: color 0.2s ease;
    }}
    .s54-post-card__title a:hover {{
        color: #D68E1D;
    }}
    
    @media (max-width: 768px) {{
        .s54-featured-post {{
            grid-template-columns: 1fr;
        }}
        .s54-blog-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
</head>
<body class="template-blog">

    {header_html}

    <!-- Blog Hero -->
    <header class="s54-blog-hero">
        <div class="s54-blog-hero__badge">✨ BẢN TIN & KIẾN THỨC CÀ PHÊ</div>
        <h1 class="s54-blog-hero__title">Góc Thưởng Thức S54</h1>
        <p class="s54-blog-hero__desc">Khám phá hành trình từ nông trại đến tách cà phê hoàn hảo, văn hóa thưởng thức cà phê rang mộc nguyên chất và câu chuyện sinh kế bền vững "New Coffee, New Income".</p>
    </header>

    <!-- Category Filter Bar -->
    <nav class="s54-blog-nav" aria-label="Danh mục tin tức">
        <ul class="s54-blog-nav__list">
            <li><a href="blogs-news.html" class="s54-blog-nav__btn is-active">Tất Cả Bài Viết</a></li>
            <li><a href="blogs-news.html" class="s54-blog-nav__btn">Kiến Thức Cà Phê</a></li>
            <li><a href="blogs-news.html" class="s54-blog-nav__btn">Câu Chuyện S54</a></li>
            <li><a href="blogs-news.html" class="s54-blog-nav__btn">Hướng Dẫn Pha Chế</a></li>
            <li><a href="blogs-news.html" class="s54-blog-nav__btn">Bản Tin Extracts</a></li>
        </ul>
    </nav>

    <!-- Main Blog Container -->
    <main class="s54-blog-container">
        
        <!-- Featured Post -->
        <article class="s54-featured-post">
            <img src="assets/images/s54/blog_cup.jpg" alt="5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê" class="s54-featured-post__img" />
            <div class="s54-featured-post__content">
                <div class="s54-post-meta">
                    <span>☕ Kiến Thức Cà Phê</span>
                    <span>•</span>
                    <span>5 phút đọc</span>
                    <span>•</span>
                    <span>26/08/2026</span>
                </div>
                <h2 class="s54-post-title">
                    <a href="blog-detail.html" style="color: inherit; text-decoration: none;">5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết</a>
                </h2>
                <p class="s54-post-excerpt">
                    Mỗi tách cà phê rang mộc nguyên chất chứa hàm lượng chất chống oxy hóa polyphenol dồi dào, giúp kích hoạt cơ thể, tăng cường nhận thức, đẩy lùi cơn đau đầu và đốt cháy chất béo tự nhiên. Khám phá ngay cùng chuyên gia S54 Coffee!
                </p>
                <a href="blog-detail.html" class="s54-read-btn">
                    <span>Đọc Bài Viết</span>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
            </div>
        </article>

        <h2 class="s54-section-title" style="margin-bottom: 32px; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 38px; color: #2F221A;">Các Bài Viết Mới Nhất</h2>

        <!-- Blog Grid -->
        <div class="s54-blog-grid">
            
            <!-- Card 1 -->
            <article class="s54-post-card">
                <div class="s54-post-card__img-wrap">
                    <img src="assets/images/s54/robusta_1.jpg" alt="Bí Quyết Phân Biệt Cà Phê Rang Mộc" class="s54-post-card__img" />
                </div>
                <div class="s54-post-card__body">
                    <div class="s54-post-meta">
                        <span>Phân Biệt Cà Phê</span>
                        <span>•</span>
                        <span>4 phút đọc</span>
                    </div>
                    <h3 class="s54-post-card__title">
                        <a href="blog-detail.html">Bí Quyết Phân Biệt Cà Phê Rang Mộc Nguyên Chất & Cà Phê Pha Tạp</a>
                    </h3>
                    <p class="s54-post-excerpt">
                        Cách nhận biết bột cà phê thật qua màu sắc nâu cánh gián, độ xốp nở khi gặp nước sôi và hậu vị thanh ngọt lưu lại nơi cuống họng.
                    </p>
                    <div style="margin-top: auto;">
                        <a href="blog-detail.html" class="s54-read-btn">Đọc Tiếp →</a>
                    </div>
                </div>
            </article>

            <!-- Card 2 -->
            <article class="s54-post-card">
                <div class="s54-post-card__img-wrap">
                    <img src="assets/images/s54/roasting_facility.png" alt="Triết Lý New Coffee, New Income" class="s54-post-card__img" />
                </div>
                <div class="s54-post-card__body">
                    <div class="s54-post-meta">
                        <span>Câu Chuyện S54</span>
                        <span>•</span>
                        <span>6 phút đọc</span>
                    </div>
                    <h3 class="s54-post-card__title">
                        <a href="our-story.html">Triết Lý “NEW COFFEE, NEW INCOME” & Hơn Cả Cà Phê</a>
                    </h3>
                    <p class="s54-post-excerpt">
                        Hành trình hơn 12 năm của Good Solutions và Founder Tony Hoan & Paul Hieu trong việc xây dựng chuỗi cung ứng minh bạch, nâng cao giá trị hạt cà phê Việt.
                    </p>
                    <div style="margin-top: auto;">
                        <a href="our-story.html" class="s54-read-btn">Đọc Tiếp →</a>
                    </div>
                </div>
            </article>

            <!-- Card 3 -->
            <article class="s54-post-card">
                <div class="s54-post-card__img-wrap">
                    <img src="assets/images/s54/espresso_brewtorial_desktop.jpg" alt="Nghệ Thuật Chiết Xuất Espresso" class="s54-post-card__img" />
                </div>
                <div class="s54-post-card__body">
                    <div class="s54-post-meta">
                        <span>Pha Chế</span>
                        <span>•</span>
                        <span>5 phút đọc</span>
                    </div>
                    <h3 class="s54-post-card__title">
                        <a href="blog-detail.html">Nghệ Thuật Chiết Xuất Tách Espresso & Cà Phê Phin Đậm Đà</a>
                    </h3>
                    <p class="s54-post-excerpt">
                        Tỷ lệ vàng giữa bột cà phê và nhiệt độ nước 92°C - 96°C để tạo nên lớp crema vàng óng cùng hương thơm ngào ngạt đánh thức mọi giác quan.
                    </p>
                    <div style="margin-top: auto;">
                        <a href="blog-detail.html" class="s54-read-btn">Đọc Tiếp →</a>
                    </div>
                </div>
            </article>

            <!-- Card 4 -->
            <article class="s54-post-card">
                <div class="s54-post-card__img-wrap">
                    <img src="assets/images/s54/instant_3in1_1.jpg" alt="Cà Phê Sấy Lạnh S54" class="s54-post-card__img" />
                </div>
                <div class="s54-post-card__body">
                    <div class="s54-post-meta">
                        <span>Công Nghệ Rang</span>
                        <span>•</span>
                        <span>3 phút đọc</span>
                    </div>
                    <h3 class="s54-post-card__title">
                        <a href="collections-coffee.html">Công Nghệ Cà Phê Sấy Lạnh Giữ Trọn 99% Hương Thơm Nguyên Bản</a>
                    </h3>
                    <p class="s54-post-excerpt">
                        Giải pháp tiện lợi cho cuộc sống bận rộn mà vẫn đảm bảo tiêu chuẩn chất lượng khắt khe của dòng cà phê đặc sản S54 Coffee.
                    </p>
                    <div style="margin-top: auto;">
                        <a href="collections-coffee.html" class="s54-read-btn">Đọc Tiếp →</a>
                    </div>
                </div>
            </article>

            <!-- Card 5 -->
            <article class="s54-post-card">
                <div class="s54-post-card__img-wrap">
                    <img src="assets/images/s54/arabica_beans.jpg" alt="Vùng Nguyên Liệu Cầu Đất" class="s54-post-card__img" />
                </div>
                <div class="s54-post-card__body">
                    <div class="s54-post-meta">
                        <span>Nông Trại</span>
                        <span>•</span>
                        <span>5 phút đọc</span>
                    </div>
                    <h3 class="s54-post-card__title">
                        <a href="our-story.html">Tại Sao Hạt Arabica Cầu Đất Được Gọi Là "Nữ Hoàng Cà Phê Việt"?</a>
                    </h3>
                    <p class="s54-post-excerpt">
                        Khám phá độ cao 1.600m và khí hậu ôn đới đặc thù đã tạo nên nốt hương hoa quả chua thanh tao nhã cho dòng S54 Arabica Thượng Hạng.
                    </p>
                    <div style="margin-top: auto;">
                        <a href="our-story.html" class="s54-read-btn">Đọc Tiếp →</a>
                    </div>
                </div>
            </article>

            <!-- Card 6 -->
            <article class="s54-post-card">
                <div class="s54-post-card__img-wrap">
                    <img src="assets/images/s54/instant_box.png" alt="Bản Tin S54 Extracts" class="s54-post-card__img" />
                </div>
                <div class="s54-post-card__body">
                    <div class="s54-post-meta">
                        <span>Bản Tin</span>
                        <span>•</span>
                        <span>3 phút đọc</span>
                    </div>
                    <h3 class="s54-post-card__title">
                        <a href="wholesale.html">Bản Tin S54 Extracts: Cơ Hội Hợp Tác B2B Cung Ứng & Gia Công OEM 2026</a>
                    </h3>
                    <p class="s54-post-excerpt">
                        Chính sách chiết khấu tận xưởng, hỗ trợ thiết kế bao bì thương hiệu riêng và giải pháp cà phê toàn diện cho chuỗi nhà hàng khách sạn.
                    </p>
                    <div style="margin-top: auto;">
                        <a href="wholesale.html" class="s54-read-btn">Đọc Tiếp →</a>
                    </div>
                </div>
            </article>

        </div>

    </main>

    {footer_html}

    <script src="assets/js/i18n.js"></script>
    <script src="assets/js/main.js"></script>
    <button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
    </button>
</body>
</html>'''

# Write blogs-news.html
(BASE_DIR / 'blogs-news.html').write_text(BLOG_LIST_HTML, encoding='utf-8')
print("✓ Generated blogs-news.html")

# Write blog-detail.html
BLOG_DETAIL_HTML = f'''<!DOCTYPE HTML>
<html class="js-unavailable" lang="vi" data-country="Vietnam">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết | S54 COFFEE</title>
    <meta name="description" content="Khám phá 5 lợi ích bất ngờ cho sức khỏe từ ly cà phê sạch rang mộc nguyên chất mỗi sáng: chống oxy hóa, đẩy lùi cơn đau đầu, hỗ trợ vận động viên và giảm mệt mỏi." />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <link href="assets/css/layouts.critical.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/layouts.theme.css" rel="stylesheet" type="text/css" media="all" />
    <link href="assets/css/custom.css?v={int(time.time())}" rel="stylesheet" type="text/css" media="all" />
    
    <style id="s54-direct-typography-override">
    @media (min-width: 768px) {{
        h1, .o-heading--1, .s54-hero-title, .c-hero-banner__title, .c-hero-banner__title span {{
            font-size: 56px !important;
            line-height: 1.15 !important;
        }}
    }}
    
    .s54-article-container {{
        max-width: 860px;
        margin: 0 auto;
        padding: clamp(36px, 5vw, 64px) 24px;
    }}
    .s54-article-header {{
        margin-bottom: 36px;
        text-align: center;
    }}
    .s54-article-title {{
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(32px, 4.5vw, 48px);
        font-weight: 700;
        line-height: 1.2;
        color: #2F221A;
        margin: 16px 0 20px;
    }}
    .s54-article-featured-img {{
        width: 100%;
        border-radius: 12px;
        margin-bottom: 40px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.06);
    }}
    .s54-article-body {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 16px;
        line-height: 1.8;
        color: #3B2E26;
    }}
    .s54-article-body h2 {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 32px !important;
        color: #2F221A !important;
        margin: 36px 0 16px !important;
        padding-bottom: 8px;
        border-bottom: 2px solid #EBE7E1;
    }}
    .s54-article-body p {{
        margin-bottom: 20px;
    }}
    .s54-article-quote {{
        background: #FAF8F5;
        border-left: 4px solid #D68E1D;
        padding: 20px 24px;
        margin: 28px 0;
        border-radius: 0 8px 8px 0;
        font-style: italic;
        color: #2F221A;
        font-size: 17px;
    }}
    .s54-article-author-box {{
        margin-top: 50px;
        padding: 24px;
        background: #FAF8F5;
        border: 1px solid #EBE7E1;
        border-radius: 8px;
        display: flex;
        gap: 20px;
        align-items: center;
    }}
    .s54-author-avatar {{
        width: 64px;
        height: 64px;
        border-radius: 50%;
        background: #2F221A;
        color: #D68E1D;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 700;
        flex-shrink: 0;
    }}
    </style>
</head>
<body class="template-article">

    {header_html}

    <main class="s54-article-container">
        
        <!-- Article Header -->
        <header class="s54-article-header">
            <div class="s54-post-meta" style="justify-content: center;">
                <a href="blogs-news.html" style="color: #D68E1D; text-decoration: none;">← Quay lại Tin Tức</a>
                <span>•</span>
                <span>Kiến Thức Cà Phê</span>
                <span>•</span>
                <span>26/08/2026</span>
            </div>
            <h1 class="s54-article-title">5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết</h1>
            <p style="font-size: 16px; color: #6E6259; line-height: 1.6;">
                Tác giả: <strong>Ban Biên Tập S54 COFFEE</strong> • Cố vấn chuyên môn: <strong>Good Solutions Co., Ltd</strong>
            </p>
        </header>

        <img src="assets/images/s54/blog_cup.jpg" alt="5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê" class="s54-article-featured-img" />

        <!-- Article Body Content from Authentic Client Source -->
        <div class="s54-article-body">
            <p>
                Có nhiều cách để khởi động ngày mới năng động như hít thở, thư giãn và luyện tập thể dục thể thao; trong đó, hoạt động uống cà phê là thói quen khá phổ biến. Tuy nhiên, không phải ai cũng biết được những lợi ích từ ly cà phê sáng mang lại. 
            </p>
            <p>
                Các nghiên cứu khoa học đã chỉ ra rằng, dù là cà phê pha phin truyền thống hay cà phê hòa tan 100% nguyên chất, với một lượng vừa phải mỗi ngày, cà phê sẽ mang lại những lợi ích tuyệt vời cho sức khoẻ như cải thiện tập trung, giảm mệt mỏi, hỗ trợ giảm đau đầu và ngăn ngừa nhiều nguy cơ bệnh tật.
            </p>

            <blockquote class="s54-article-quote">
                “Các sản phẩm S54 COFFEE được sản xuất từ 100% hạt cà phê đạt chuẩn Tây Nguyên, mang tới cho bạn những ly cà phê nguyên chất, góp phần vào cuộc sống vui khoẻ của người Việt.”
            </blockquote>

            <h2>1. Nguồn Chất Chống Oxy Hóa Dồi Dào Bảo Vệ Tế Bào</h2>
            <p>
                Lợi ích lớn nhất mà cà phê nguyên chất mang lại là nguồn chất chống oxy hoá dồi dào, đặc biệt là trong hạt cà phê Robusta và Arabica chưa qua tẩm ướp hóa chất. Mỗi tách cà phê chứa hàm lượng polyphenol cao, hoạt động cùng với các khoáng chất vi lượng để giúp cơ thể và các tế bào hoạt động tối ưu, ngăn ngừa lão hóa và duy trì sức khỏe tổng thể.
            </p>

            <h2>2. Kích Hoạt Trí Nhớ & Tăng Cường Sự Tập Trung Tột Đỉnh</h2>
            <p>
                Cà phê rất giàu caffeine tự nhiên – thành phần kích hoạt hệ thần kinh trung ương, giúp cải thiện chức năng nhận thức, phản xạ và trí nhớ ngắn hạn. Thưởng thức một ly cà phê đen hoặc cà phê sữa ít đường vào đầu giờ làm việc sẽ giúp bạn nhanh chóng nạp lại năng lượng và làm việc hiệu quả gấp bội.
            </p>

            <h2>3. Đẩy Lùi Cơn Đau Đầu Nhờ Tác Động Giãn Mạch Tự Nhiên</h2>
            <p>
                Caffeine là một chất làm giãn mạch tự nhiên, có khả năng hỗ trợ điều hòa áp lực máu bằng cách ngăn chặn các cơ trong tĩnh mạch căng lên và thu hẹp lại. Do đó, một lượng cà phê vừa phải (1-2 ly/ngày) sẽ giúp xoa dịu những cơn đau đầu do căng thẳng làm việc.
            </p>

            <h2>4. Tăng Cường Hiệu Suất Thể Chất Cho Người Luyện Tập</h2>
            <p>
                Đối với những người thường xuyên tập thể thao, gym hay vận động viên, một tách cà phê nguyên chất trước buổi tập 30 phút sẽ kích thích giải phóng adrenaline, giúp xoa dịu cảm giác mệt mỏi và nâng cao sức bền vận động rõ rệt.
            </p>

            <h2>5. Hỗ Trợ Đốt Cháy Mỡ Thừa Qua Cơ Chế Sinh Nhiệt Tự Nhiên</h2>
            <p>
                Caffeine từ lâu đã được chứng minh có khả năng thúc đẩy quá trình "sinh nhiệt" (thermogenesis) – cơ chế đốt cháy calo và mỡ thừa tự nhiên của cơ thể. Để đạt hiệu quả tối ưu, bạn nên kết hợp uống cà phê rang mộc không đường với chế độ dinh dưỡng lành mạnh và uống đủ nước mỗi ngày.
            </p>

            <!-- Author Box -->
            <div class="s54-article-author-box">
                <div class="s54-author-avatar">S54</div>
                <div>
                    <h4 style="margin: 0 0 4px; font-size: 16px; color: #2F221A;">S54 Coffee Editorial Team</h4>
                    <p style="margin: 0; font-size: 13px; color: #6E6259; line-height: 1.5;">
                        Đội ngũ nghiên cứu & phát triển sản phẩm của Công ty TNHH Giải Pháp Tốt (Good Solutions Co., Ltd). Sứ mệnh mang tinh hoa cà phê Việt sạch nguyên chất đến hàng triệu người tiêu dùng.
                    </p>
                </div>
            </div>

            <!-- CTA Back & Shop -->
            <div style="margin-top: 40px; text-align: center; display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                <a href="blogs-news.html" class="s54-btn s54-btn--secondary" style="padding: 12px 24px; border: 1px solid #2F221A; color: #2F221A; text-decoration: none; border-radius: 4px; font-weight: 700; font-size: 13px;">← Xem Tất Cả Bài Viết</a>
                <a href="collections-coffee.html" class="s54-btn s54-btn--primary" style="padding: 12px 24px; background: #D68E1D; color: #FFFFFF; text-decoration: none; border-radius: 4px; font-weight: 700; font-size: 13px;">Khám Phá Cà Phê S54 →</a>
            </div>

        </div>

    </main>

    {footer_html}

    <script src="assets/js/i18n.js"></script>
    <script src="assets/js/main.js"></script>
    <button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
    </button>
</body>
</html>'''

(BASE_DIR / 'blog-detail.html').write_text(BLOG_DETAIL_HTML, encoding='utf-8')
print("✓ Generated blog-detail.html")

print("\n✅ All blog pages successfully built!")
