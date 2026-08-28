@extends('client.layouts.app')

@section('title', 'B2B & Đại Lý S54 Coffee — Giải Pháp Cà Phê Doanh Nghiệp')

@section('content')
<section class="s54-page-hero s54-page-hero--wholesale" style="background: radial-gradient(circle at center, rgba(62,42,30,0.85) 0%, rgba(36,26,20,0.96) 100%), url('{{ asset('client-assets/images/s54/wholesale_hero_b2b.jpg') }}') center/cover no-repeat; padding: 100px 20px 80px; text-align: center; color: #FFFFFF;">
    <div class="o-wrapper" style="max-width: 900px; margin: 0 auto;">
        <span style="display: inline-block; background: rgba(214,142,29,0.25); border: 1px solid #D68E1D; color: #F7D08A; padding: 6px 18px; border-radius: 20px; font-size: 11.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 20px;">
            {{ app()->getLocale() === 'vi' ? 'GIẢI PHÁP B2B & NHÀ HÀNG KHÁCH SẠN' : 'B2B & HOSPITALITY SOLUTIONS' }}
        </span>
        <h1 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(38px, 6vw, 56px); font-weight: 700; line-height: 1.2; margin-bottom: 20px; color: #FFFFFF;">
            {{ app()->getLocale() === 'vi' ? 'Giải Pháp Cung Ứng Cà Phê Toàn Diện Cho Doanh Nghiệp' : 'Comprehensive Coffee Solutions for Enterprise & HoReCa' }}
        </h1>
        <p style="font-size: 16px; line-height: 1.6; color: #E5DDD5; max-width: 700px; margin: 0 auto;">
            {{ app()->getLocale() === 'vi' ? 'Cung cấp cà phê hạt rang mộc theo yêu cầu, máy pha cà phê chuyên nghiệp và đào tạo barista chuẩn quốc tế.' : 'Custom profile roasting, commercial espresso equipment and barista training.' }}
        </p>
    </div>
</section>

<section style="background-color: #FAF8F5; padding: 70px 20px;">
    <div class="o-wrapper" style="max-width: 1100px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-bottom: 60px;">
            <div style="background: #FFFFFF; border-radius: 8px; padding: 32px 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); text-align: center;">
                <div style="font-size: 36px; margin-bottom: 16px;">☕</div>
                <h3 style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 700; color: #2F221A; margin-bottom: 12px;">Rang Xay Theo Yêu Cầu (OEM)</h3>
                <p style="color: #5C4A3E; font-size: 14px; line-height: 1.6;">Tùy chỉnh tỷ lệ Arabica/Robusta và profile rang riêng biệt cho chuỗi cafe, nhà hàng và khách sạn 5 sao.</p>
            </div>
            <div style="background: #FFFFFF; border-radius: 8px; padding: 32px 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); text-align: center;">
                <div style="font-size: 36px; margin-bottom: 16px;">🚚</div>
                <h3 style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 700; color: #2F221A; margin-bottom: 12px;">Chính Sách Chiết Khấu Cao</h3>
                <p style="color: #5C4A3E; font-size: 14px; line-height: 1.6;">Chiết khấu hấp dẫn cho nhà phân phối và đại lý với nguồn hàng ổn định quanh năm từ các nông trại riêng.</p>
            </div>
            <div style="background: #FFFFFF; border-radius: 8px; padding: 32px 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); text-align: center;">
                <div style="font-size: 36px; margin-bottom: 16px;">🎓</div>
                <h3 style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 700; color: #2F221A; margin-bottom: 12px;">Đào Tạo & Setup Quán</h3>
                <p style="color: #5C4A3E; font-size: 14px; line-height: 1.6;">Tư vấn setup quầy bar, bảo dưỡng máy pha định kỳ và đào tạo kỹ năng pha chế cho đội ngũ nhân viên.</p>
            </div>
        </div>

        {{-- B2B Contact Form --}}
        <div style="background: #241A14; color: #FAF6F1; border-radius: 12px; padding: 48px clamp(20px, 4vw, 48px); max-width: 760px; margin: 0 auto;">
            <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 700; text-align: center; margin-bottom: 12px; color: #FAF6F1;">Đăng Ký Tư Vấn B2B</h2>
            <p style="text-align: center; color: #BAADA1; font-size: 14px; margin-bottom: 32px;">Để lại thông tin để nhận bảng giá sỉ & mẫu thử cà phê miễn phí từ chuyên gia S54.</p>
            
            <form action="#" method="POST" style="display: grid; gap: 18px;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <input type="text" placeholder="Họ và tên *" required style="padding: 12px 16px; border: 1px solid #4A3A2F; background: #2F221A; color: #FAF6F1; border-radius: 4px;">
                    <input type="tel" placeholder="Số điện thoại *" required style="padding: 12px 16px; border: 1px solid #4A3A2F; background: #2F221A; color: #FAF6F1; border-radius: 4px;">
                </div>
                <input type="text" placeholder="Tên doanh nghiệp / Quán cafe" style="padding: 12px 16px; border: 1px solid #4A3A2F; background: #2F221A; color: #FAF6F1; border-radius: 4px;">
                <textarea rows="4" placeholder="Nhu cầu cụ thể (Sản lượng ước tính / Dòng cà phê quan tâm)..." style="padding: 12px 16px; border: 1px solid #4A3A2F; background: #2F221A; color: #FAF6F1; border-radius: 4px;"></textarea>
                <button type="submit" style="background-color: #D68E1D; color: #FFFFFF; border: none; padding: 14px; border-radius: 4px; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; cursor: pointer; transition: background 0.2s;">Gửi Yêu Cầu Tư Vấn & Nhận Mẫu Thử</button>
            </form>
        </div>
    </div>
</section>
@endsection
