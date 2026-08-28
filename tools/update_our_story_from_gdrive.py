#!/usr/bin/env python3
"""
Update our-story.html, theme/our-story.html, and resources/views/client/pages/our-story.blade.php
with exact client content and real photos from Google Drive.
"""

from pathlib import Path
import re

BASE_DIR = Path('/home/binhphan/matbao-ws/clients/s54coffeecom549.mbws.vn')

# 1. Update resources/views/client/pages/our-story.blade.php
blade_content = '''@extends('client.layouts.app')

@php
    $locale = app()->getLocale();
@endphp

@section('title', ($locale === 'vi' ? 'Câu Chuyện S54 Coffee — Tinh Hoa Cà Phê Việt & Hành Trình Vươn Tầm' : 'Our Story — S54 Coffee Heritage & Vision'))

@section('content')
{{-- Hero Banner --}}
<section class="s54-page-hero" style="background: radial-gradient(circle at center, rgba(47,34,26,0.85) 0%, rgba(26,18,14,0.96) 100%), url('{{ asset('client-assets/images/s54/story_hero_heritage.jpg') }}') center/cover no-repeat; padding: 100px 20px 80px; text-align: center; color: #FAF6F1;">
    <div class="o-wrapper" style="max-width: 960px; margin: 0 auto;">
        <span style="display: inline-block; background: rgba(214,142,29,0.25); border: 1px solid #D68E1D; color: #F7D08A; padding: 6px 18px; border-radius: 20px; font-size: 11.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 20px;">
            {{ $locale === 'vi' ? 'S54 COFFEE • VIETNAMESE COFFEE. MADE FOR THE WORLD.' : 'S54 COFFEE • VIETNAMESE COFFEE. MADE FOR THE WORLD.' }}
        </span>
        <h1 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(36px, 5.5vw, 56px); font-weight: 700; line-height: 1.2; margin-bottom: 22px; color: #FFFFFF;">
            {{ $locale === 'vi' ? 'Hành Trình Tinh Hoa Cà Phê Việt & Sứ Mệnh 54 Dân Tộc' : 'The Vietnamese Coffee Heritage & 54 Ethnic Unity' }}
        </h1>
        <p style="font-size: clamp(15px, 2vw, 17.5px); line-height: 1.7; color: #E5DDD5; max-width: 780px; margin: 0 auto; font-weight: 400;">
            {{ $locale === 'vi' 
                ? 'Tự hào mang tên gọi kết hợp giữa hình ảnh dải đất hình chữ S và 54 dân tộc anh em, S54 Coffee ra đời với sứ mệnh nâng tầm hạt cà phê Robusta và Arabica từ thủ phủ Tây Nguyên vươn tầm quốc tế theo phương châm "New Coffee, New Income".' 
                : 'Named after the S-shaped Vietnamese land and 54 brotherly ethnic groups, S54 Coffee elevates Central Highlands Robusta & Arabica globally under the motto "New Coffee, New Income".' }}
        </p>
    </div>
</section>

{{-- Brand Introduction & Official Video --}}
<section style="background-color: #FAF8F5; padding: 80px 20px;">
    <div class="o-wrapper" style="max-width: 1200px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 48px; align-items: center;">
            <div>
                <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; display: block; margin-bottom: 10px;">
                    {{ $locale === 'vi' ? 'GIỚI THIỆU CHUNG' : 'ABOUT S54 COFFEE' }}
                </span>
                <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(28px, 4vw, 38px); font-weight: 700; color: #2F221A; margin-bottom: 20px; line-height: 1.25;">
                    {{ $locale === 'vi' ? 'Cà Phê Nguyên Bản Cho Năng Lượng & Giá Trị Bền Vững' : 'Pure Vietnamese Coffee For Energy & Sustainable Growth' }}
                </h2>
                <p style="color: #5C4A3E; font-size: 15.5px; line-height: 1.8; margin-bottom: 18px;">
                    {{ $locale === 'vi' 
                        ? 'S54 Coffee mang đến những trải nghiệm cà phê nguyên bản, đậm đà—từ các dòng cà phê hòa tan 3in1 tiện lợi đến cà phê hạt rang chất lượng cao, lưu giữ trọn vẹn hương vị mộc mạc của đất trời Tây Nguyên.' 
                        : 'S54 Coffee delivers authentic, rich coffee experiences—from convenient 3-in-1 instant blends to premium roasted whole beans that preserve the true spirit of Central Highlands.' }}
                </p>
                <p style="color: #5C4A3E; font-size: 15.5px; line-height: 1.8; margin-bottom: 28px;">
                    {{ $locale === 'vi' 
                        ? 'Với phương châm "New Coffee, New Income", S54 Coffee không chỉ cung cấp nguồn năng lượng tỉnh táo, sáng tạo mỗi ngày mà còn hướng tới xây dựng giá trị phát triển bền vững và cơ hội thu nhập cho cộng đồng.' 
                        : 'With our core motto "New Coffee, New Income", S54 Coffee empowers daily creative energy while creating sustainable economic opportunities for our farming community.' }}
                </p>
                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <a href="{{ route('client.catalog.index', ['locale' => $locale]) }}" style="background-color: #2F221A; color: #FAF6F1; padding: 12px 28px; border-radius: 4px; font-size: 12.5px; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: 1px;">
                        {{ $locale === 'vi' ? 'Khám Phá Sản Phẩm' : 'Explore Products' }}
                    </a>
                </div>
            </div>

            {{-- Video Frame --}}
            <div style="background: #FFFFFF; padding: 12px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
                    <iframe src="https://www.youtube.com/embed/7PB6Tn2pyE8" title="S54 Coffee Introduction" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
</section>

{{-- Vision, Mission, Core Values Section --}}
<section style="background-color: #241A14; color: #FAF6F1; padding: 90px 20px;">
    <div class="o-wrapper" style="max-width: 1200px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 12px;">
                {{ $locale === 'vi' ? 'ĐỊNH HƯỚNG CHIẾN LƯỢC' : 'STRATEGIC PILLARS' }}
            </span>
            <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(32px, 4.5vw, 44px); font-weight: 700; color: #FFFFFF;">
                {{ $locale === 'vi' ? 'Tầm Nhìn • Sứ Mệnh • Giá Trị Cốt Lõi' : 'Vision • Mission • Core Values' }}
            </h2>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px;">
            {{-- Vision Card --}}
            <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(214,142,29,0.3); border-radius: 12px; padding: 36px 28px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="width: 50px; height: 50px; background: rgba(214,142,29,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #D68E1D; font-size: 22px; margin-bottom: 20px;">
                        👁️
                    </div>
                    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #FAF6F1; margin-bottom: 14px;">
                        {{ $locale === 'vi' ? 'Tầm Nhìn' : 'Our Vision' }}
                    </h3>
                    <p style="color: #D6C7BC; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
                        {{ $locale === 'vi' 
                            ? 'Trở thành thương hiệu cà phê Việt uy tín, vươn tầm quốc tế với các dòng sản phẩm chất lượng cao và sáng tạo.' 
                            : 'To become a globally prestigious Vietnamese coffee brand renowned for quality and innovation.' }}
                    </p>
                </div>
                <div style="border-radius: 8px; overflow: hidden; position: relative; padding-bottom: 56.25%; height: 0;">
                    <iframe src="https://www.youtube.com/embed/8nVnuZSauE8" title="S54 Vision" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
                </div>
            </div>

            {{-- Mission Card --}}
            <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(214,142,29,0.3); border-radius: 12px; padding: 36px 28px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="width: 50px; height: 50px; background: rgba(214,142,29,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #D68E1D; font-size: 22px; margin-bottom: 20px;">
                        🚀
                    </div>
                    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #FAF6F1; margin-bottom: 14px;">
                        {{ $locale === 'vi' ? 'Sứ Mệnh' : 'Our Mission' }}
                    </h3>
                    <p style="color: #D6C7BC; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
                        {{ $locale === 'vi' 
                            ? 'Mang đến tách cà phê chuẩn vị, truyền năng lượng tích cực và tạo dựng thu nhập bền vững cho cộng đồng (New Coffee, New Income).' 
                            : 'Delivering authentic coffee, inspiring positive energy, and creating sustainable incomes.' }}
                    </p>
                </div>
                <div style="border-radius: 8px; overflow: hidden; position: relative; padding-bottom: 56.25%; height: 0;">
                    <iframe src="https://www.youtube.com/embed/bIC2_Dko3xk" title="S54 Mission" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
                </div>
            </div>

            {{-- Core Values Card --}}
            <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(214,142,29,0.3); border-radius: 12px; padding: 36px 28px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="width: 50px; height: 50px; background: rgba(214,142,29,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #D68E1D; font-size: 22px; margin-bottom: 20px;">
                        💎
                    </div>
                    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #FAF6F1; margin-bottom: 14px;">
                        {{ $locale === 'vi' ? 'Giá Trị Cốt Lõi' : 'Core Values' }}
                    </h3>
                    <p style="color: #D6C7BC; font-size: 15px; line-height: 1.8; margin-bottom: 24px;">
                        <strong style="color: #F7D08A;">• Trung thực:</strong> {{ $locale === 'vi' ? 'Minh bạch nguồn gốc và chất lượng.' : 'Transparent origin & quality.' }}<br>
                        <strong style="color: #F7D08A;">• Chất lượng:</strong> {{ $locale === 'vi' ? 'Chuẩn vị nguyên bản từng mẻ rang.' : 'Authentic taste in every batch.' }}<br>
                        <strong style="color: #F7D08A;">• Cải tiến:</strong> {{ $locale === 'vi' ? 'Ứng dụng công nghệ hiện đại.' : 'Continuous product innovation.' }}<br>
                        <strong style="color: #F7D08A;">• Đồng hành:</strong> {{ $locale === 'vi' ? 'Cùng phát triển bền vững.' : 'Growing together with community.' }}
                    </p>
                </div>
                <div style="border-radius: 8px; overflow: hidden; position: relative; padding-bottom: 56.25%; height: 0;">
                    <iframe src="https://www.youtube.com/embed/T8MfqRZlsFo" title="S54 Core Values" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
</section>

{{-- Milestones Journey Section --}}
<section class="c-stories" style="background-color: #FAF8F5; padding: 90px 20px;">
    <div class="o-wrapper" style="max-width: 1100px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 12px;">
                {{ $locale === 'vi' ? 'HÀNH TRÌNH PHÁT TRIỂN' : 'OUR DEVELOPMENT MILESTONES' }}
            </span>
            <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(32px, 4.5vw, 44px); font-weight: 700; color: #2F221A;">
                {{ $locale === 'vi' ? 'Các Cột Mốc Đột Phá Của S54 Coffee' : 'Key Breakthrough Milestones' }}
            </h2>
        </div>

        <div class="c-stories__story">
            {{-- Milestone 1 --}}
            <div class="c-stories__story-block">
                <div class="c-stories__story-block-image">
                    <img src="{{ asset('client-assets/images/s54/story_farm_origin.jpg') }}" alt="Nghiên cứu & phát triển cà phê S54" loading="lazy" style="border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
                </div>
                <div class="c-stories__story-block-text">
                    <div class="c-stories__story-block-year">Cột Mốc 1</div>
                    <h3 class="c-stories__story-block-title">
                        {{ $locale === 'vi' ? 'Nghiên Cứu & Phát Triển Chuẩn Vị Tây Nguyên' : 'R&D and Authentic Taste Formulation' }}
                    </h3>
                    <p class="c-stories__story-block-body">
                        {{ $locale === 'vi' 
                            ? 'Nghiên cứu và phát triển thành công dòng sản phẩm cà phê hòa tan 3in1 tiện lợi & cà phê hạt rang chất lượng cao chuẩn vị thủ phủ Tây Nguyên.' 
                            : 'Successfully formulated authentic instant 3-in-1 and premium roasted whole beans from Central Highlands.' }}
                    </p>
                </div>
            </div>

            {{-- Milestone 2 --}}
            <div class="c-stories__story-block is-reversed">
                <div class="c-stories__story-block-image">
                    <img src="{{ asset('client-assets/images/s54/s54_cafe_nhabe_1.jpg') }}" alt="Mở rộng hệ thống phân phối S54 Coffee" loading="lazy" style="border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
                </div>
                <div class="c-stories__story-block-text">
                    <div class="c-stories__story-block-year">Cột Mốc 2</div>
                    <h3 class="c-stories__story-block-title">
                        {{ $locale === 'vi' ? 'Mở Rộng Hệ Thống Phân Phối & Lan Tỏa Thương Hiệu' : 'Expanding Distribution & Brand Outreach' }}
                    </h3>
                    <p class="c-stories__story-block-body">
                        {{ $locale === 'vi' 
                            ? 'Mở rộng hệ thống phân phối, phát triển chuỗi cửa hàng trải nghiệm và định hình thông điệp thương hiệu S54 Coffee "New Coffee, New Income".' 
                            : 'Expanded commercial distribution networks and established the brand message "New Coffee, New Income".' }}
                    </p>
                </div>
            </div>

            {{-- Milestone 3 --}}
            <div class="c-stories__story-block">
                <div class="c-stories__story-block-image">
                    <img src="{{ asset('client-assets/images/s54/s54_office_vinhome_2.jpg') }}" alt="Số hóa thương hiệu S54 Coffee" loading="lazy" style="border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
                </div>
                <div class="c-stories__story-block-text">
                    <div class="c-stories__story-block-year">Cột Mốc 3</div>
                    <h3 class="c-stories__story-block-title">
                        {{ $locale === 'vi' ? 'Số Hóa Thương Hiệu & Nền Tảng Đa Kênh Hiện Đại' : 'Digital Transformation & Omnichannel Commerce' }}
                    </h3>
                    <p class="c-stories__story-block-body">
                        {{ $locale === 'vi' 
                            ? 'Số hóa toàn diện thương hiệu, hoàn thiện website bán hàng chuyên nghiệp, tích hợp Core Admin quản trị hiện đại và mở rộng kết nối đối tác quốc tế.' 
                            : 'Fully digitized brand operations with a professional e-commerce platform and modern Core Admin backend.' }}
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

{{-- Real Office & Coffee Shop Gallery --}}
<section style="background-color: #F3EEE8; padding: 80px 20px;">
    <div class="o-wrapper" style="max-width: 1200px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 48px;">
            <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 10px;">
                {{ $locale === 'vi' ? 'HỆ THỐNG VĂN PHÒNG & CỬA HÀNG THỰC TẾ' : 'OUR OFFICES & COFFEE SHOPS' }}
            </span>
            <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(28px, 4vw, 38px); font-weight: 700; color: #2F221A;">
                {{ $locale === 'vi' ? 'Không Gian Trải Nghiệm S54 Coffee' : 'Experience S54 Coffee Spaces' }}
            </h2>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
            <div style="background: #FFFFFF; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
                <img src="{{ asset('client-assets/images/s54/s54_office_vinhome_1.jpg') }}" alt="Văn phòng S54 Coffee Vinhomes Grand Park" style="width: 100%; height: 240px; object-fit: cover;">
                <div style="padding: 16px 20px;">
                    <strong style="color: #2F221A; font-size: 14.5px; display: block; margin-bottom: 4px;">Văn Phòng S54 Coffee</strong>
                    <span style="color: #8A7B70; font-size: 13px;">The Manhattan, Vinhomes Grand Park, TP. Thủ Đức</span>
                </div>
            </div>

            <div style="background: #FFFFFF; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
                <img src="{{ asset('client-assets/images/s54/s54_office_vinhome_3.jpg') }}" alt="Khu làm việc S54 Coffee" style="width: 100%; height: 240px; object-fit: cover;">
                <div style="padding: 16px 20px;">
                    <strong style="color: #2F221A; font-size: 14.5px; display: block; margin-bottom: 4px;">Trụ Sở Điều Hành</strong>
                    <span style="color: #8A7B70; font-size: 13px;">Không gian làm việc sáng tạo & đào tạo barista</span>
                </div>
            </div>

            <div style="background: #FFFFFF; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
                <img src="{{ asset('client-assets/images/s54/s54_cafe_nhabe_2.jpg') }}" alt="Quán Cafe S54 tại Nhà Bè" style="width: 100%; height: 240px; object-fit: cover;">
                <div style="padding: 16px 20px;">
                    <strong style="color: #2F221A; font-size: 14.5px; display: block; margin-bottom: 4px;">Quán Cafe S54 Coffee</strong>
                    <span style="color: #8A7B70; font-size: 13px;">Điểm trải nghiệm cà phê nguyên bản tại Nhà Bè, TP.HCM</span>
                </div>
            </div>
        </div>
    </div>
</section>

{{-- Final Quote & CTA --}}
<section style="background-color: #241A14; color: #FAF6F1; padding: 80px 20px; text-align: center;">
    <div class="o-wrapper" style="max-width: 860px; margin: 0 auto;">
        <span style="color: #D68E1D; font-size: 42px; font-family: 'Cormorant Garamond', serif; display: block; line-height: 1;">“</span>
        <blockquote style="font-family: 'Cormorant Garamond', serif; font-size: clamp(22px, 3.5vw, 32px); font-style: italic; line-height: 1.4; color: #FAF6F1; margin: 0 0 20px 0;">
            {{ $locale === 'vi' 
                ? 'Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.' 
                : 'Establishing premier solutions in delivering Quality Coffee with unparalleled standards of service.' }}
        </blockquote>
        <cite style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #D68E1D; font-style: normal; display: block; margin-bottom: 36px;">
            — {{ $locale === 'vi' ? 'Triết lý Good Solutions & S54 Coffee' : 'Good Solutions & S54 Coffee Philosophy' }}
        </cite>
        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
            <a href="{{ route('client.catalog.index', ['locale' => $locale]) }}" style="background-color: #D68E1D; color: #FFFFFF; padding: 14px 32px; border-radius: 4px; font-size: 13px; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: 1px;">
                {{ $locale === 'vi' ? 'Mua Cà Phê Ngay' : 'Shop Coffee' }}
            </a>
            <a href="{{ route('client.pages.show', ['locale' => $locale, 'slug' => 'wholesale']) }}" style="background: transparent; color: #FAF6F1; border: 1.5px solid #FAF6F1; padding: 14px 32px; border-radius: 4px; font-size: 13px; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: 1px;">
                {{ $locale === 'vi' ? 'Hợp Tác Doanh Nghiệp' : 'Wholesale Inquiry' }}
            </a>
        </div>
    </div>
</section>
@endsection
'''

(BASE_DIR / 'resources/views/client/pages/our-story.blade.php').write_text(blade_content, encoding='utf-8')
print("✓ Updated resources/views/client/pages/our-story.blade.php")

# 2. Update our-story.html and theme/our-story.html for static rendering
# Let's read the static template header and footer from our-story.html and replace its main content
our_story_path = BASE_DIR / 'our-story.html'
html = our_story_path.read_text(encoding='utf-8')

# Replace the inner story content in our-story.html
# We construct the exact modern static section for our-story.html
static_main_content = '''
<main id="MainContent" class="content-for-layout focus-none" role="main" tabindex="-1">
  
  <!-- HERO BANNER -->
  <section class="s54-page-hero" style="background: radial-gradient(circle at center, rgba(47,34,26,0.85) 0%, rgba(26,18,14,0.96) 100%), url('assets/images/s54/story_hero_heritage.jpg') center/cover no-repeat; padding: 100px 20px 80px; text-align: center; color: #FAF6F1;">
    <div class="o-wrapper" style="max-width: 960px; margin: 0 auto;">
      <span style="display: inline-block; background: rgba(214,142,29,0.25); border: 1px solid #D68E1D; color: #F7D08A; padding: 6px 18px; border-radius: 20px; font-size: 11.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 20px;">
        S54 COFFEE • VIETNAMESE COFFEE. MADE FOR THE WORLD.
      </span>
      <h1 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(36px, 5.5vw, 56px); font-weight: 700; line-height: 1.2; margin-bottom: 22px; color: #FFFFFF;">
        Hành Trình Tinh Hoa Cà Phê Việt & Sứ Mệnh 54 Dân Tộc
      </h1>
      <p style="font-size: clamp(15px, 2vw, 17.5px); line-height: 1.7; color: #E5DDD5; max-width: 780px; margin: 0 auto; font-weight: 400;">
        Tự hào mang tên gọi kết hợp giữa hình ảnh dải đất hình chữ S và 54 dân tộc anh em, S54 Coffee ra đời với sứ mệnh nâng tầm hạt cà phê Robusta và Arabica từ thủ phủ Tây Nguyên vươn tầm quốc tế theo phương châm "New Coffee, New Income".
      </p>
    </div>
  </section>

  <!-- GIỚI THIỆU CHUNG & VIDEO -->
  <section style="background-color: #FAF8F5; padding: 80px 20px;">
    <div class="o-wrapper" style="max-width: 1200px; margin: 0 auto;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 48px; align-items: center;">
        <div>
          <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; display: block; margin-bottom: 10px;">GIỚI THIỆU CHUNG</span>
          <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(28px, 4vw, 38px); font-weight: 700; color: #2F221A; margin-bottom: 20px; line-height: 1.25;">
            Cà Phê Nguyên Bản Cho Năng Lượng & Giá Trị Bền Vững
          </h2>
          <p style="color: #5C4A3E; font-size: 15.5px; line-height: 1.8; margin-bottom: 18px;">
            S54 Coffee mang đến những trải nghiệm cà phê nguyên bản, đậm đà—từ các dòng cà phê hòa tan 3in1 tiện lợi đến cà phê hạt rang chất lượng cao, lưu giữ trọn vẹn hương vị mộc mạc của đất trời Tây Nguyên.
          </p>
          <p style="color: #5C4A3E; font-size: 15.5px; line-height: 1.8; margin-bottom: 28px;">
            Với phương châm "New Coffee, New Income", S54 Coffee không chỉ cung cấp nguồn năng lượng tỉnh táo, sáng tạo mỗi ngày mà còn hướng tới xây dựng giá trị phát triển bền vững và cơ hội thu nhập cho cộng đồng.
          </p>
          <div>
            <a href="collections-coffee.html" style="background-color: #2F221A; color: #FAF6F1; padding: 12px 28px; border-radius: 4px; font-size: 12.5px; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: 1px; display: inline-block;">
              Khám Phá Sản Phẩm
            </a>
          </div>
        </div>
        <div style="background: #FFFFFF; padding: 12px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
          <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
            <iframe src="https://www.youtube.com/embed/7PB6Tn2pyE8" title="S54 Coffee Introduction" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- TẦM NHÌN, SỨ MỆNH, GIÁ TRỊ CỐT LÕI -->
  <section style="background-color: #241A14; color: #FAF6F1; padding: 90px 20px;">
    <div class="o-wrapper" style="max-width: 1200px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 60px;">
        <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 12px;">ĐỊNH HƯỚNG CHIẾN LƯỢC</span>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(32px, 4.5vw, 44px); font-weight: 700; color: #FFFFFF;">
          Tầm Nhìn • Sứ Mệnh • Giá Trị Cốt Lõi
        </h2>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px;">
        <!-- Vision -->
        <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(214,142,29,0.3); border-radius: 12px; padding: 36px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="width: 50px; height: 50px; background: rgba(214,142,29,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #D68E1D; font-size: 22px; margin-bottom: 20px;">👁️</div>
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #FAF6F1; margin-bottom: 14px;">Tầm Nhìn</h3>
            <p style="color: #D6C7BC; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              Trở thành thương hiệu cà phê Việt uy tín, vươn tầm quốc tế với các dòng sản phẩm chất lượng cao và sáng tạo.
            </p>
          </div>
          <div style="border-radius: 8px; overflow: hidden; position: relative; padding-bottom: 56.25%; height: 0;">
            <iframe src="https://www.youtube.com/embed/8nVnuZSauE8" title="S54 Vision" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
          </div>
        </div>

        <!-- Mission -->
        <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(214,142,29,0.3); border-radius: 12px; padding: 36px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="width: 50px; height: 50px; background: rgba(214,142,29,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #D68E1D; font-size: 22px; margin-bottom: 20px;">🚀</div>
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #FAF6F1; margin-bottom: 14px;">Sứ Mệnh</h3>
            <p style="color: #D6C7BC; font-size: 15px; line-height: 1.7; margin-bottom: 24px;">
              Mang đến tách cà phê chuẩn vị, truyền năng lượng tích cực và tạo dựng thu nhập bền vững cho cộng đồng (New Coffee, New Income).
            </p>
          </div>
          <div style="border-radius: 8px; overflow: hidden; position: relative; padding-bottom: 56.25%; height: 0;">
            <iframe src="https://www.youtube.com/embed/bIC2_Dko3xk" title="S54 Mission" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
          </div>
        </div>

        <!-- Core Values -->
        <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(214,142,29,0.3); border-radius: 12px; padding: 36px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="width: 50px; height: 50px; background: rgba(214,142,29,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #D68E1D; font-size: 22px; margin-bottom: 20px;">💎</div>
            <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 700; color: #FAF6F1; margin-bottom: 14px;">Giá Trị Cốt Lõi</h3>
            <p style="color: #D6C7BC; font-size: 15px; line-height: 1.8; margin-bottom: 24px;">
              <strong style="color: #F7D08A;">• Trung thực:</strong> Minh bạch nguồn gốc và chất lượng.<br>
              <strong style="color: #F7D08A;">• Chất lượng:</strong> Chuẩn vị nguyên bản từng mẻ rang.<br>
              <strong style="color: #F7D08A;">• Cải tiến:</strong> Ứng dụng công nghệ hiện đại.<br>
              <strong style="color: #F7D08A;">• Đồng hành:</strong> Cùng phát triển bền vững.
            </p>
          </div>
          <div style="border-radius: 8px; overflow: hidden; position: relative; padding-bottom: 56.25%; height: 0;">
            <iframe src="https://www.youtube.com/embed/T8MfqRZlsFo" title="S54 Core Values" style="position: absolute; top:0; left:0; width: 100%; height: 100%; border:0;" allowfullscreen></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HÀNH TRÌNH PHÁT TRIỂN (3 CỘT MỐC) -->
  <section class="c-stories" style="background-color: #FAF8F5; padding: 90px 20px;">
    <div class="o-wrapper" style="max-width: 1100px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 60px;">
        <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 12px;">HÀNH TRÌNH PHÁT TRIỂN</span>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(32px, 4.5vw, 44px); font-weight: 700; color: #2F221A;">
          Các Cột Mốc Đột Phá Của S54 Coffee
        </h2>
      </div>

      <div class="c-stories__story">
        <!-- Milestone 1 -->
        <div class="c-stories__story-block">
          <div class="c-stories__story-block-image">
            <img src="assets/images/s54/story_farm_origin.jpg" alt="Nghiên cứu & phát triển cà phê S54" loading="lazy" style="border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
          </div>
          <div class="c-stories__story-block-text">
            <div class="c-stories__story-block-year">Cột Mốc 1</div>
            <h3 class="c-stories__story-block-title">Nghiên Cứu & Phát Triển Chuẩn Vị Tây Nguyên</h3>
            <p class="c-stories__story-block-body">
              Nghiên cứu và phát triển thành công dòng sản phẩm cà phê hòa tan 3in1 tiện lợi & cà phê hạt rang chất lượng cao chuẩn vị thủ phủ Tây Nguyên.
            </p>
          </div>
        </div>

        <!-- Milestone 2 -->
        <div class="c-stories__story-block is-reversed">
          <div class="c-stories__story-block-image">
            <img src="assets/images/s54/s54_cafe_nhabe_1.jpg" alt="Mở rộng hệ thống phân phối S54 Coffee" loading="lazy" style="border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
          </div>
          <div class="c-stories__story-block-text">
            <div class="c-stories__story-block-year">Cột Mốc 2</div>
            <h3 class="c-stories__story-block-title">Mở Rộng Hệ Thống Phân Phối & Lan Tỏa Thương Hiệu</h3>
            <p class="c-stories__story-block-body">
              Mở rộng hệ thống phân phối, phát triển chuỗi cửa hàng trải nghiệm và định hình thông điệp thương hiệu S54 Coffee "New Coffee, New Income".
            </p>
          </div>
        </div>

        <!-- Milestone 3 -->
        <div class="c-stories__story-block">
          <div class="c-stories__story-block-image">
            <img src="assets/images/s54/s54_office_vinhome_2.jpg" alt="Số hóa thương hiệu S54 Coffee" loading="lazy" style="border-radius: 8px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">
          </div>
          <div class="c-stories__story-block-text">
            <div class="c-stories__story-block-year">Cột Mốc 3</div>
            <h3 class="c-stories__story-block-title">Số Hóa Thương Hiệu & Nền Tảng Đa Kênh Hiện Đại</h3>
            <p class="c-stories__story-block-body">
              Số hóa toàn diện thương hiệu, hoàn thiện website bán hàng chuyên nghiệp, tích hợp Core Admin quản trị hiện đại và mở rộng kết nối đối tác quốc tế.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- HỆ THỐNG VĂN PHÒNG & QUÁN THỰC TẾ -->
  <section style="background-color: #F3EEE8; padding: 80px 20px;">
    <div class="o-wrapper" style="max-width: 1200px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: 48px;">
        <span style="color: #D68E1D; font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 10px;">HỆ THỐNG VĂN PHÒNG & CỬA HÀNG THỰC TẾ</span>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(28px, 4vw, 38px); font-weight: 700; color: #2F221A;">Không Gian Trải Nghiệm S54 Coffee</h2>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
        <div style="background: #FFFFFF; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
          <img src="assets/images/s54/s54_office_vinhome_1.jpg" alt="Văn phòng S54 Coffee Vinhomes Grand Park" style="width: 100%; height: 240px; object-fit: cover;">
          <div style="padding: 16px 20px;">
            <strong style="color: #2F221A; font-size: 14.5px; display: block; margin-bottom: 4px;">Văn Phòng S54 Coffee</strong>
            <span style="color: #8A7B70; font-size: 13px;">The Manhattan, Vinhomes Grand Park, TP. Thủ Đức</span>
          </div>
        </div>

        <div style="background: #FFFFFF; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
          <img src="assets/images/s54/s54_office_vinhome_3.jpg" alt="Khu làm việc S54 Coffee" style="width: 100%; height: 240px; object-fit: cover;">
          <div style="padding: 16px 20px;">
            <strong style="color: #2F221A; font-size: 14.5px; display: block; margin-bottom: 4px;">Trụ Sở Điều Hành</strong>
            <span style="color: #8A7B70; font-size: 13px;">Không gian làm việc sáng tạo & đào tạo barista</span>
          </div>
        </div>

        <div style="background: #FFFFFF; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
          <img src="assets/images/s54/s54_cafe_nhabe_2.jpg" alt="Quán Cafe S54 tại Nhà Bè" style="width: 100%; height: 240px; object-fit: cover;">
          <div style="padding: 16px 20px;">
            <strong style="color: #2F221A; font-size: 14.5px; display: block; margin-bottom: 4px;">Quán Cafe S54 Coffee</strong>
            <span style="color: #8A7B70; font-size: 13px;">Điểm trải nghiệm cà phê nguyên bản tại Nhà Bè, TP.HCM</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- QUOTE & CTA -->
  <section style="background-color: #241A14; color: #FAF6F1; padding: 80px 20px; text-align: center;">
    <div class="o-wrapper" style="max-width: 860px; margin: 0 auto;">
      <span style="color: #D68E1D; font-size: 42px; font-family: 'Cormorant Garamond', serif; display: block; line-height: 1;">“</span>
      <blockquote style="font-family: 'Cormorant Garamond', serif; font-size: clamp(22px, 3.5vw, 32px); font-style: italic; line-height: 1.4; color: #FAF6F1; margin: 0 0 20px 0;">
        Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.
      </blockquote>
      <cite style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #D68E1D; font-style: normal; display: block; margin-bottom: 36px;">
        — Triết lý Good Solutions & S54 Coffee
      </cite>
      <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
        <a href="collections-coffee.html" style="background-color: #D68E1D; color: #FFFFFF; padding: 14px 32px; border-radius: 4px; font-size: 13px; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: 1px;">
          Mua Cà Phê Ngay
        </a>
        <a href="wholesale.html" style="background: transparent; color: #FAF6F1; border: 1.5px solid #FAF6F1; padding: 14px 32px; border-radius: 4px; font-size: 13px; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: 1px;">
          Hợp Tác Doanh Nghiệp
        </a>
      </div>
    </div>
  </section>
</main>
'''

# Replace <main id="MainContent" ... </main> in our-story.html
new_html = re.sub(
    r'<main id="MainContent"[\s\S]*?</main>',
    static_main_content.strip(),
    html
)

our_story_path.write_text(new_html, encoding='utf-8')
(BASE_DIR / 'theme/our-story.html').write_text(new_html, encoding='utf-8')
print("✓ Updated our-story.html and theme/our-story.html")

