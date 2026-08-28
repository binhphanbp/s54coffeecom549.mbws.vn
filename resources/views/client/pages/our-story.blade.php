@extends('client.layouts.app')

@section('title', 'Câu Chuyện S54 Coffee — Hành Trình Tinh Hoa Cà Phê Việt')

@section('content')
<section class="s54-page-hero" style="background: radial-gradient(circle at center, rgba(62,42,30,0.85) 0%, rgba(36,26,20,0.96) 100%), url('{{ asset('client-assets/images/s54/story_hero_heritage.jpg') }}') center/cover no-repeat; padding: 100px 20px 80px; text-align: center; color: #FFFFFF;">
    <div class="o-wrapper" style="max-width: 900px; margin: 0 auto;">
        <span style="display: inline-block; background: rgba(214,142,29,0.25); border: 1px solid #D68E1D; color: #F7D08A; padding: 6px 18px; border-radius: 20px; font-size: 11.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 20px;">
            {{ app()->getLocale() === 'vi' ? 'HÀNH TRÌNH TỪ NĂM 2012' : 'ESTABLISHED 2012' }}
        </span>
        <h1 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(38px, 6vw, 56px); font-weight: 700; line-height: 1.2; margin-bottom: 20px; color: #FFFFFF;">
            {{ app()->getLocale() === 'vi' ? 'Hành Trình Tinh Hoa Cà Phê Việt & Khát Vọng Good Solutions' : 'The Vietnamese Coffee Heritage & Good Solutions Vision' }}
        </h1>
        <p style="font-size: 16px; line-height: 1.6; color: #E5DDD5; max-width: 700px; margin: 0 auto;">
            {{ app()->getLocale() === 'vi' ? 'Khởi nguồn từ niềm đam mê hạt cà phê Việt Nam và triết lý kinh doanh bền vững.' : 'Born from deep passion for Vietnamese coffee beans and sustainable business philosophy.' }}
        </p>
    </div>
</section>

<section class="c-stories" style="background-color: #FAF8F5; padding: 80px 20px;">
    <div class="o-wrapper" style="max-width: 1100px; margin: 0 auto;">
        <div class="c-stories__stories" style="position: relative;">
            
            {{-- Story 1 --}}
            <article class="c-stories__story" style="display: flex; gap: 40px; align-items: center; margin-bottom: 70px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="{{ asset('client-assets/images/s54/story_farm_origin.jpg') }}" alt="Origin" style="width: 100%; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.1);">
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <span style="font-size: 12px; font-weight: 700; color: #D68E1D; text-transform: uppercase; letter-spacing: 1px;">2012 • Khởi Nguồn</span>
                    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 700; color: #2F221A; margin: 10px 0 16px;">Vùng Đất Di Sản Cà Phê Tây Nguyên</h3>
                    <p style="color: #5C4A3E; line-height: 1.7;">Được thành lập từ năm 2012 bởi Công Ty TNHH Giải Pháp Tốt (Good Solutions), S54 Coffee đặt nền móng tại những vùng nguyên liệu trứ danh Đắk Lắk và Cầu Đất (Lâm Đồng), đồng hành cùng nông dân canh tác hữu cơ bền vững.</p>
                </div>
            </article>

            {{-- Story 2 --}}
            <article class="c-stories__story is-reversed" style="display: flex; gap: 40px; align-items: center; margin-bottom: 70px; flex-wrap: wrap-reverse;">
                <div style="flex: 1; min-width: 300px;">
                    <span style="font-size: 12px; font-weight: 700; color: #D68E1D; text-transform: uppercase; letter-spacing: 1px;">2016 • Đột Phá Công Nghệ</span>
                    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 700; color: #2F221A; margin: 10px 0 16px;">Công Nghệ Rang Hot-Air Đức Tối Tân</h3>
                    <p style="color: #5C4A3E; line-height: 1.7;">S54 đầu tư hệ thống máy rang Hot-Air hồi khí tiên tiến, kiểm soát chính xác từng giây trong profile rang, giúp hạt bung đều, giải phóng trọn vẹn tầng hương hoa quả và chocolate mà không bị cháy cạnh.</p>
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <img src="{{ asset('client-assets/images/s54/story_roasting_master.jpg') }}" alt="Roasting" style="width: 100%; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.1);">
                </div>
            </article>

            {{-- Story 3 --}}
            <article class="c-stories__story" style="display: flex; gap: 40px; align-items: center; margin-bottom: 70px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="{{ asset('client-assets/images/s54/story_cupping_barista.jpg') }}" alt="Cupping Lab" style="width: 100%; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.1);">
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <span style="font-size: 12px; font-weight: 700; color: #D68E1D; text-transform: uppercase; letter-spacing: 1px;">2020 • Cupping Lab & Q-Grader</span>
                    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 700; color: #2F221A; margin: 10px 0 16px;">Tiêu Chuẩn Đánh Giá SCA Quốc Tế</h3>
                    <p style="color: #5C4A3E; line-height: 1.7;">Mọi mẻ rang tại S54 đều trải qua quy trình Cupping nghiêm ngặt theo thang điểm SCA. Chúng tôi cam kết mỗi tách cà phê trao đến tay khách hàng đều giữ trọn độ tươi mới và tinh túy hương vị.</p>
                </div>
            </article>

        </div>
    </div>
</section>
@endsection
