@extends('client.layouts.app')

@section('title', 'S54 COFFEE — Tinh Hoa Cà Phê Việt | New Coffee, New Income')

@section('content')
{{-- Hero Banner Section --}}
<section class="s54-page-hero" style="background: radial-gradient(circle at center, rgba(62,42,30,0.85) 0%, rgba(36,26,20,0.96) 100%), url('{{ asset('client-assets/images/s54/story_hero_heritage.jpg') }}') center/cover no-repeat; padding: 100px 20px 80px; text-align: center; color: #FFFFFF;">
    <div class="o-wrapper" style="max-width: 1000px; margin: 0 auto;">
        <span style="display: inline-block; background: rgba(214,142,29,0.25); border: 1px solid #D68E1D; color: #F7D08A; padding: 6px 18px; border-radius: 20px; font-size: 11.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 20px;">
            {{ app()->getLocale() === 'vi' ? 'CÔNG NGHỆ RANG HOT-AIR ĐỨC • 100% NGUYÊN CHẤT' : 'GERMAN HOT-AIR ROASTING • 100% ARTISAN' }}
        </span>
        <h1 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(38px, 6vw, 62px); font-weight: 700; line-height: 1.15; margin-bottom: 20px; color: #FFFFFF; text-shadow: 0 4px 20px rgba(0,0,0,0.4);">
            {{ app()->getLocale() === 'vi' ? 'Tinh Hoa Cà Phê Việt Nam Thượng Hạng' : 'The Pinnacle of Vietnamese Artisan Coffee' }}
        </h1>
        <p style="font-size: clamp(15px, 2vw, 18px); line-height: 1.6; color: #E5DDD5; max-width: 720px; margin: 0 auto 36px; font-weight: 400;">
            {{ app()->getLocale() === 'vi' ? 'Khám phá hương vị Robusta đậm đà từ Đắk Lắk & Arabica thanh nhã Cầu Đất, được rang xay thủ công với độ chuẩn xác tuyệt đối.' : 'Discover rich Robusta from Dak Lak and elegant Arabica from Cau Dat, precision roasted for exquisite taste.' }}
        </p>
        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
            <a href="{{ route('client.catalog.index', ['locale' => app()->getLocale()]) }}" style="background-color: #D68E1D; color: #FFFFFF; padding: 14px 32px; border-radius: 4px; font-size: 13px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; text-decoration: none; transition: transform 0.2s, background 0.2s; box-shadow: 0 4px 16px rgba(214,142,29,0.35);">
                {{ app()->getLocale() === 'vi' ? 'Khám Phá Sản Phẩm' : 'Explore Products' }}
            </a>
            <a href="{{ route('client.pages.show', ['locale' => app()->getLocale(), 'slug' => 'our-story']) }}" style="background: transparent; color: #FAF6F1; border: 1.5px solid #FAF6F1; padding: 14px 32px; border-radius: 4px; font-size: 13px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; text-decoration: none; transition: all 0.2s;">
                {{ app()->getLocale() === 'vi' ? 'Câu Chuyện S54' : 'Our Heritage' }}
            </a>
        </div>
    </div>
</section>

{{-- Featured Collections Section --}}
<section class="c-featured-collections" style="background-color: #FAF8F5; padding: 70px 0 60px;">
    <div class="c-featured-collections__header" style="text-align: center; margin-bottom: 40px;">
        <h2 class="c-featured-collections__header-title" style="font-family: 'Cormorant Garamond', serif; font-size: 38px; font-weight: 700; color: #2F221A; margin-bottom: 24px;">
            {{ app()->getLocale() === 'vi' ? 'Sản Phẩm Bán Chạy Nhất' : 'Best Selling Coffee' }}
        </h2>
    </div>

    <div class="c-featured-collections__products-list is-active">
        @forelse($featuredProducts as $prod)
            <x-client.product-card :product="$prod" />
        @empty
            <div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: #8A7B70;">
                {{ app()->getLocale() === 'vi' ? 'Chưa có sản phẩm nào được hiển thị.' : 'No products available.' }}
            </div>
        @endforelse
    </div>

    <div style="text-align: center; margin-top: 48px;">
        <a href="{{ route('client.catalog.index', ['locale' => app()->getLocale()]) }}" style="display: inline-block; background-color: #2F221A; color: #FAF6F1; padding: 14px 36px; border-radius: 4px; font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; text-decoration: none; transition: background 0.2s;">
            {{ app()->getLocale() === 'vi' ? 'Xem Tất Cả Sản Phẩm' : 'View All Products' }} &rarr;
        </a>
    </div>
</section>

{{-- Philosophy Quote Section --}}
<section style="background-color: #241A14; color: #FAF6F1; padding: 80px 20px; text-align: center;">
    <div class="o-wrapper" style="max-width: 860px; margin: 0 auto;">
        <span style="color: #D68E1D; font-size: 42px; font-family: 'Cormorant Garamond', serif; display: block; line-height: 1;">“</span>
        <blockquote style="font-family: 'Cormorant Garamond', serif; font-size: clamp(22px, 3.5vw, 32px); font-style: italic; line-height: 1.4; color: #FAF6F1; margin: 0 0 20px 0;">
            {{ app()->getLocale() === 'vi' ? 'Thiết lập các giải pháp tốt trong việc cung cấp Cà phê Chất lượng với mức độ dịch vụ không ai sánh kịp.' : 'Establishing premier solutions in delivering Quality Coffee with unparalleled standards of service.' }}
        </blockquote>
        <cite style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #D68E1D; font-style: normal;">
            — {{ app()->getLocale() === 'vi' ? 'Triết lý Good Solutions & S54 Coffee' : 'Philosophy of Good Solutions & S54 Coffee' }}
        </cite>
    </div>
</section>
@endsection
