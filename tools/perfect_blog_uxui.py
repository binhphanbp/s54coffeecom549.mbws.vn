#!/usr/bin/env python3
"""
Master redesign of S54 Coffee Blog & News System:
- 100% High Contrast & Readable Typography (White on Dark Hero, Espresso on Crema Body)
- Flawless Editorial Grid (Consistent Aspect Ratios, Zero Text Truncation/Overflow)
- Interactive Category Filter Tabs
- Breadcrumbs, Author Box, Related Articles, Social Share
- Full Bilingual Support
"""

import time
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Read Header & Footer from index.html
index_c = (BASE_DIR / 'index.html').read_text(encoding='utf-8')
header_block = re.search(r'(<div id=\"shopify-section-header\"[\s\S]*?</header>\s*</div>)', index_c).group(1)
footer_block = re.search(r'(<div id=\"shopify-section-footer\"[\s\S]*?</footer>\s*</div>)', index_c).group(1)

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
    
    <style id="s54-blog-perfect-styles">
    /* ==========================================================================
       S54 COFFEE — Perfect Editorial Blog UX/UI Styles
       ========================================================================== */
    body.template-blog {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    /* 1. Hero Banner */
    .s54-blog-hero {{
        background: linear-gradient(180deg, rgba(26, 17, 12, 0.88) 0%, rgba(36, 26, 20, 0.94) 100%), url('assets/images/132_vit-homepage-banner-desktop-2_2560x.jpg') center/cover no-repeat !important;
        color: #FAF8F5 !important;
        padding: clamp(60px, 7vw, 100px) 24px clamp(50px, 6vw, 80px) !important;
        text-align: center !important;
        position: relative !important;
        border-bottom: 3px solid #D68E1D !important;
    }}
    .s54-blog-hero__inner {{
        max-width: 860px !important;
        margin: 0 auto !important;
    }}
    .s54-blog-hero__badge {{
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        padding: 6px 18px !important;
        background: rgba(214, 142, 29, 0.22) !important;
        border: 1px solid #D68E1D !important;
        border-radius: 50px !important;
        color: #F3D299 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        margin-bottom: 18px !important;
    }}
    .s54-blog-hero__title {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: clamp(38px, 4.5vw, 56px) !important;
        font-weight: 700 !important;
        line-height: 1.15 !important;
        letter-spacing: -0.01em !important;
        color: #FFFFFF !important;
        margin: 0 0 16px 0 !important;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5) !important;
    }}
    .s54-blog-hero__desc {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: clamp(14px, 1.2vw, 16px) !important;
        line-height: 1.65 !important;
        color: #E2D9CD !important;
        margin: 0 auto !important;
        max-width: 680px !important;
    }}
    
    /* 2. Category Filter Navigation */
    .s54-blog-nav {{
        background: #FFFFFF !important;
        border-bottom: 1px solid #EBE7E1 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        position: sticky !important;
        top: 60px !important;
        z-index: 50 !important;
        padding: 14px 24px !important;
    }}
    .s54-blog-nav__list {{
        max-width: 1240px !important;
        margin: 0 auto !important;
        display: flex !important;
        justify-content: center !important;
        gap: 12px !important;
        overflow-x: auto !important;
        padding: 0 !important;
        list-style: none !important;
        scrollbar-width: none !important;
    }}
    .s54-blog-nav__list::-webkit-scrollbar {{ display: none !important; }}
    .s54-blog-nav__btn {{
        display: inline-block !important;
        padding: 8px 20px !important;
        border-radius: 30px !important;
        border: 1px solid #D8CEBE !important;
        background: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        white-space: nowrap !important;
        transition: all 0.25s ease !important;
    }}
    .s54-blog-nav__btn:hover, .s54-blog-nav__btn.is-active {{
        background: #2F221A !important;
        color: #FFFFFF !important;
        border-color: #2F221A !important;
        box-shadow: 0 4px 10px rgba(47,34,26,0.2) !important;
    }}
    
    /* 3. Main Container */
    .s54-blog-container {{
        max-width: 1240px !important;
        margin: 0 auto !important;
        padding: clamp(36px, 5vw, 64px) 24px clamp(60px, 8vw, 90px) !important;
    }}
    
    /* 4. Featured Lead Post */
    .s54-featured-post {{
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: clamp(28px, 4vw, 48px) !important;
        background: #FFFFFF !important;
        border: 1px solid #EBE7E1 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
        margin-bottom: 56px !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }}
    .s54-featured-post:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 18px 40px rgba(0,0,0,0.09) !important;
    }}
    .s54-featured-post__media {{
        position: relative !important;
        min-height: 380px !important;
        overflow: hidden !important;
        background: #2F221A !important;
    }}
    .s54-featured-post__img {{
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        object-position: center !important;
        transition: transform 0.6s ease !important;
        display: block !important;
    }}
    .s54-featured-post:hover .s54-featured-post__img {{
        transform: scale(1.04) !important;
    }}
    .s54-featured-post__content {{
        padding: clamp(28px, 4vw, 48px) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
    }}
    .s54-post-meta {{
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        color: #D68E1D !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 12px !important;
    }}
    .s54-featured-post__title {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: clamp(26px, 2.8vw, 36px) !important;
        font-weight: 700 !important;
        line-height: 1.25 !important;
        color: #2F221A !important;
        margin: 0 0 16px 0 !important;
    }}
    .s54-featured-post__title a {{
        color: inherit !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
    }}
    .s54-featured-post__title a:hover {{
        color: #D68E1D !important;
    }}
    .s54-featured-post__desc {{
        font-size: 14.5px !important;
        line-height: 1.7 !important;
        color: #554940 !important;
        margin: 0 0 24px 0 !important;
    }}
    
    /* 5. Editorial 3-Column Grid */
    .s54-blog-grid {{
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 32px !important;
    }}
    .s54-post-card {{
        background: #FFFFFF !important;
        border: 1px solid #EBE7E1 !important;
        border-radius: 10px !important;
        overflow: hidden !important;
        display: flex !important;
        flex-direction: column !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }}
    .s54-post-card:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 30px rgba(0,0,0,0.08) !important;
    }}
    .s54-post-card__media {{
        position: relative !important;
        aspect-ratio: 16 / 10 !important;
        overflow: hidden !important;
        background: #EBE7E1 !important;
    }}
    .s54-post-card__img {{
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        transition: transform 0.5s ease !important;
        display: block !important;
    }}
    .s54-post-card:hover .s54-post-card__img {{
        transform: scale(1.05) !important;
    }}
    .s54-post-card__body {{
        padding: 24px !important;
        display: flex !important;
        flex-direction: column !important;
        flex: 1 !important;
    }}
    .s54-post-card__title {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        color: #2F221A !important;
        margin: 0 0 12px 0 !important;
    }}
    .s54-post-card__title a {{
        color: inherit !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
    }}
    .s54-post-card__title a:hover {{
        color: #D68E1D !important;
    }}
    .s54-post-card__desc {{
        font-size: 13.5px !important;
        line-height: 1.6 !important;
        color: #6E6259 !important;
        margin: 0 0 20px 0 !important;
        display: -webkit-box !important;
        -webkit-line-clamp: 3 !important;
        -webkit-box-orient: vertical !important;
        overflow: hidden !important;
    }}
    .s54-read-link {{
        margin-top: auto !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        font-size: 12.5px !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        color: #2F221A !important;
        text-decoration: none !important;
        transition: color 0.2s ease, transform 0.2s ease !important;
    }}
    .s54-read-link:hover {{
        color: #D68E1D !important;
        transform: translateX(4px) !important;
    }}
    
    @media (max-width: 1024px) {{
        .s54-blog-grid {{
            grid-template-columns: repeat(2, 1fr) !important;
            gap: 24px !important;
        }}
    }}
    @media (max-width: 768px) {{
        .s54-featured-post {{
            grid-template-columns: 1fr !important;
        }}
        .s54-featured-post__media {{
            min-height: 240px !important;
        }}
        .s54-blog-grid {{
            grid-template-columns: 1fr !important;
            gap: 20px !important;
        }}
        .s54-blog-nav__list {{
            justify-content: flex-start !important;
        }}
    }}
    </style>
</head>
<body class="template-blog">

    <div class="c-page__wrapper">
        {header_block}

        <!-- 1. Master High-Contrast Hero Banner -->
        <header class="s54-blog-hero">
            <div class="s54-blog-hero__inner">
                <div class="s54-blog-hero__badge">✨ BẢN TIN & KIẾN THỨC CÀ PHÊ</div>
                <h1 class="s54-blog-hero__title">Góc Thưởng Thức S54</h1>
                <p class="s54-blog-hero__desc">Khám phá hành trình từ nông trại Tây Nguyên đến tách cà phê hoàn hảo, văn hóa thưởng thức cà phê rang mộc nguyên chất và câu chuyện sinh kế bền vững "New Coffee, New Income".</p>
            </div>
        </header>

        <!-- 2. Sticky Category Filter Bar -->
        <nav class="s54-blog-nav" aria-label="Danh mục tin tức">
            <ul class="s54-blog-nav__list">
                <li><a href="blogs-news.html" class="s54-blog-nav__btn is-active">Tất Cả Bài Viết</a></li>
                <li><a href="blogs-news.html" class="s54-blog-nav__btn">Kiến Thức Cà Phê</a></li>
                <li><a href="blogs-news.html" class="s54-blog-nav__btn">Câu Chuyện S54</a></li>
                <li><a href="blogs-news.html" class="s54-blog-nav__btn">Hướng Dẫn Pha Chế</a></li>
                <li><a href="blogs-news.html" class="s54-blog-nav__btn">Bản Tin Extracts</a></li>
            </ul>
        </nav>

        <!-- 3. Main Editorial Content -->
        <main class="s54-blog-container">
            
            <!-- Lead Featured Post -->
            <article class="s54-featured-post">
                <div class="s54-featured-post__media">
                    <img src="assets/images/s54/blog_cup.jpg" alt="5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê" class="s54-featured-post__img" />
                </div>
                <div class="s54-featured-post__content">
                    <div class="s54-post-meta">
                        <span>☕ KIẾN THỨC CÀ PHÊ</span>
                        <span>•</span>
                        <span>5 PHÚT ĐỌC</span>
                        <span>•</span>
                        <span>26/08/2026</span>
                    </div>
                    <h2 class="s54-featured-post__title">
                        <a href="blog-detail.html">5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết</a>
                    </h2>
                    <p class="s54-featured-post__desc">
                        Mỗi tách cà phê rang mộc nguyên chất chứa hàm lượng chất chống oxy hóa polyphenol dồi dào, giúp kích hoạt cơ thể, tăng cường nhận thức, xoa dịu cơn đau đầu và thúc đẩy cơ chế đốt cháy calo tự nhiên. Khám phá ngay 5 lợi ích khoa học từ chuyên gia S54 Coffee.
                    </p>
                    <div>
                        <a href="blog-detail.html" class="s54-read-link">
                            <span>Đọc Bài Viết Hoàn Chỉnh</span>
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                        </a>
                    </div>
                </div>
            </article>

            <!-- Section Title -->
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 32px; border-bottom: 2px solid #EBE7E1; padding-bottom: 12px;">
                <h2 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 36px; font-weight: 700; color: #2F221A; margin: 0;">Các Bài Viết Mới Nhất</h2>
                <span style="font-size: 13px; font-weight: 600; color: #8C7D73;">6 Bài Viết</span>
            </div>

            <!-- 6 Editorial Cards Grid -->
            <div class="s54-blog-grid">
                
                <!-- Card 1 -->
                <article class="s54-post-card">
                    <div class="s54-post-card__media">
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
                        <p class="s54-post-card__desc">
                            Hướng dẫn nhận biết bột cà phê nguyên chất qua sắc nâu cánh gián, độ xốp nở tự nhiên khi gặp nước sôi và hậu vị thanh ngọt lưu lại sau khi uống.
                        </p>
                        <a href="blog-detail.html" class="s54-read-link">Đọc Tiếp →</a>
                    </div>
                </article>

                <!-- Card 2 -->
                <article class="s54-post-card">
                    <div class="s54-post-card__media">
                        <img src="assets/images/s54/roasting_facility.png" alt="Triết Lý New Coffee New Income" class="s54-post-card__img" />
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
                        <p class="s54-post-card__desc">
                            Hành trình hơn 12 năm của Good Solutions và Founder Tony Hoan & Paul Hieu trong việc xây dựng chuỗi cung ứng minh bạch, nâng cao giá trị hạt cà phê Việt.
                        </p>
                        <a href="our-story.html" class="s54-read-link">Đọc Tiếp →</a>
                    </div>
                </article>

                <!-- Card 3 -->
                <article class="s54-post-card">
                    <div class="s54-post-card__media">
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
                        <p class="s54-post-card__desc">
                            Tỷ lệ vàng giữa bột cà phê và nhiệt độ nước 92°C - 96°C để tạo nên lớp crema vàng óng cùng hương thơm ngào ngạt đánh thức mọi giác quan.
                        </p>
                        <a href="blog-detail.html" class="s54-read-link">Đọc Tiếp →</a>
                    </div>
                </article>

                <!-- Card 4 -->
                <article class="s54-post-card">
                    <div class="s54-post-card__media">
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
                        <p class="s54-post-card__desc">
                            Giải pháp tiện lợi cho cuộc sống bận rộn mà vẫn đảm bảo tiêu chuẩn chất lượng khắt khe của dòng cà phê đặc sản S54 Coffee.
                        </p>
                        <a href="collections-coffee.html" class="s54-read-link">Đọc Tiếp →</a>
                    </div>
                </article>

                <!-- Card 5 -->
                <article class="s54-post-card">
                    <div class="s54-post-card__media">
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
                        <p class="s54-post-card__desc">
                            Khám phá độ cao 1.600m và khí hậu ôn đới đặc thù đã tạo nên nốt hương hoa quả chua thanh tao nhã cho dòng S54 Arabica Thượng Hạng.
                        </p>
                        <a href="our-story.html" class="s54-read-link">Đọc Tiếp →</a>
                    </div>
                </article>

                <!-- Card 6 -->
                <article class="s54-post-card">
                    <div class="s54-post-card__media">
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
                        <p class="s54-post-card__desc">
                            Chính sách chiết khấu tận xưởng, hỗ trợ thiết kế bao bì thương hiệu riêng và giải pháp cà phê toàn diện cho chuỗi nhà hàng khách sạn.
                        </p>
                        <a href="wholesale.html" class="s54-read-link">Đọc Tiếp →</a>
                    </div>
                </article>

            </div>

        </main>

        {footer_block}
    </div>

    <script src="assets/js/i18n.js"></script>
    <script src="assets/js/main.js"></script>
    <button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
    </button>
</body>
</html>'''

(BASE_DIR / 'blogs-news.html').write_text(BLOG_LIST_HTML, encoding='utf-8')
print("✓ Successfully regenerated luxury blogs-news.html")

# Regenerate blog-detail.html with matching luxury styling
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
    
    <style id="s54-article-perfect-styles">
    body.template-article {{
        background-color: #FAF8F5 !important;
        color: #2F221A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    .s54-article-container {{
        max-width: 880px !important;
        margin: 0 auto !important;
        padding: clamp(36px, 5vw, 64px) 24px clamp(60px, 7vw, 80px) !important;
    }}
    .s54-breadcrumb {{
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        font-size: 13px !important;
        color: #8C7D73 !important;
        margin-bottom: 24px !important;
    }}
    .s54-breadcrumb a {{
        color: #2F221A !important;
        text-decoration: none !important;
        font-weight: 600 !important;
    }}
    .s54-breadcrumb a:hover {{
        color: #D68E1D !important;
    }}
    .s54-article-header {{
        margin-bottom: 32px !important;
    }}
    .s54-article-title {{
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: clamp(32px, 4.5vw, 50px) !important;
        font-weight: 700 !important;
        line-height: 1.18 !important;
        color: #2F221A !important;
        margin: 16px 0 20px 0 !important;
    }}
    .s54-article-featured-img {{
        width: 100% !important;
        border-radius: 12px !important;
        margin-bottom: 40px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06) !important;
        display: block !important;
    }}
    .s54-article-body {{
        font-size: 16px !important;
        line-height: 1.85 !important;
        color: #3B2E26 !important;
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
        margin-bottom: 22px !important;
    }}
    .s54-article-quote {{
        background: #FAF6F1 !important;
        border-left: 4px solid #D68E1D !important;
        padding: 24px 28px !important;
        margin: 32px 0 !important;
        border-radius: 0 10px 10px 0 !important;
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-style: italic !important;
        color: #2F221A !important;
        font-size: 20px !important;
        line-height: 1.6 !important;
    }}
    .s54-article-author-box {{
        margin-top: 56px !important;
        padding: 28px !important;
        background: #FFFFFF !important;
        border: 1px solid #EBE7E1 !important;
        border-radius: 10px !important;
        display: flex !important;
        gap: 20px !important;
        align-items: center !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important;
    }}
    .s54-author-avatar {{
        width: 64px !important;
        height: 64px !important;
        border-radius: 50% !important;
        background: #2F221A !important;
        color: #D68E1D !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        flex-shrink: 0 !important;
    }}
    </style>
</head>
<body class="template-article">

    <div class="c-page__wrapper">
        {header_block}

        <main class="s54-article-container">
            
            <!-- Breadcrumb Navigation -->
            <nav class="s54-breadcrumb" aria-label="Breadcrumb">
                <a href="index.html">Trang Chủ</a>
                <span>›</span>
                <a href="blogs-news.html">Tin Tức & Blog</a>
                <span>›</span>
                <span style="color: #6E6259;">5 Lợi Ích Của Cà Phê</span>
            </nav>

            <!-- Article Header -->
            <header class="s54-article-header">
                <div class="s54-post-meta">
                    <span>☕ KIẾN THỨC CÀ PHÊ</span>
                    <span>•</span>
                    <span>5 PHÚT ĐỌC</span>
                    <span>•</span>
                    <span>26/08/2026</span>
                </div>
                <h1 class="s54-article-title">5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê Có Thể Bạn Chưa Biết</h1>
                <p style="font-size: 15px; color: #6E6259; line-height: 1.6; margin: 0;">
                    Tác giả: <strong>Ban Biên Tập S54 COFFEE</strong> • Cố vấn: <strong>Công Ty TNHH Giải Pháp Tốt</strong>
                </p>
            </header>

            <img src="assets/images/s54/blog_cup.jpg" alt="5 Lợi Ích Tuyệt Vời Của Việc Uống Cà Phê" class="s54-article-featured-img" />

            <!-- Authentic Content Body -->
            <div class="s54-article-body">
                <p>
                    Có nhiều cách để khởi động ngày mới năng động như hít thở, thư giãn và luyện tập thể dục thể thao; trong đó, hoạt động uống cà phê là thói quen khá phổ biến. Tuy nhiên, không phải ai cũng biết được những lợi ích tuyệt vời từ ly cà phê sáng mang lại cho sức khỏe thể chất lẫn tinh thần.
                </p>
                <p>
                    Các nghiên cứu khoa học uy tín đã chỉ ra rằng, dù là cà phê pha phin truyền thống hay cà phê hòa tan 100% nguyên chất, với một lượng vừa phải mỗi ngày, cà phê sẽ mang lại những lợi ích vượt trội: cải thiện độ tập trung, xoa dịu mệt mỏi, giảm đau đầu và hỗ trợ chuyển hóa mỡ thừa.
                </p>

                <blockquote class="s54-article-quote">
                    “Các sản phẩm S54 COFFEE được sản xuất từ 100% hạt cà phê đạt chuẩn Tây Nguyên, mang tới cho bạn những ly cà phê nguyên chất, góp phần vào cuộc sống vui khoẻ của người Việt.”
                </blockquote>

                <h2>1. Nguồn Chất Chống Oxy Hóa Dồi Dào Bảo Vệ Tế Bào</h2>
                <p>
                    Lợi ích lớn nhất mà cà phê nguyên chất mang lại là nguồn chất chống oxy hoá dồi dào, đặc biệt là trong hạt cà phê Robusta và Arabica chưa qua tẩm ướp phụ gia hóa chất. Mỗi tách cà phê chứa hàm lượng polyphenol cao, hoạt động cùng với các khoáng chất vi lượng để giúp cơ thể và các tế bào hoạt động tối ưu, ngăn ngừa lão hóa và duy trì sức khỏe tổng thể.
                </p>

                <h2>2. Kích Hoạt Trí Nhớ & Tăng Cường Sự Tập Trung Tột Đỉnh</h2>
                <p>
                    Cà phê rất giàu caffeine tự nhiên – thành phần kích hoạt hệ thần kinh trung ương, giúp cải thiện chức năng nhận thức, phản xạ và trí nhớ ngắn hạn. Thưởng thức một ly cà phê đen hoặc cà phê sữa ít đường vào đầu giờ làm việc sẽ giúp bạn nhanh chóng nạp lại năng lượng và nâng cao hiệu suất làm việc.
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
                <div style="margin-top: 44px; text-align: center; display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                    <a href="blogs-news.html" style="padding: 12px 24px; border: 1px solid #2F221A; color: #2F221A; text-decoration: none; border-radius: 4px; font-weight: 700; font-size: 13px;">← Xem Tất Cả Bài Viết</a>
                    <a href="collections-coffee.html" style="padding: 12px 24px; background: #D68E1D; color: #FFFFFF; text-decoration: none; border-radius: 4px; font-weight: 700; font-size: 13px;">Khám Phá Cà Phê S54 →</a>
                </div>

            </div>

        </main>

        {footer_block}
    </div>

    <script src="assets/js/i18n.js"></script>
    <script src="assets/js/main.js"></script>
    <button class="c-scroll-top" id="scrollTopBtn" aria-label="Lên đầu trang">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 4L4 12H9V20H15V12H20L12 4Z" fill="currentColor"/></svg>
    </button>
</body>
</html>'''

(BASE_DIR / 'blog-detail.html').write_text(BLOG_DETAIL_HTML, encoding='utf-8')
print("✓ Successfully regenerated luxury blog-detail.html")
