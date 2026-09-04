<?php

namespace Database\Seeders;

use App\Models\Brand;
use App\Models\Category;
use App\Models\Language;
use App\Models\Post;
use App\Models\PostCategory;
use App\Models\Product;
use App\Models\ProductImage;
use App\Models\ProductVariant;
use App\Models\ProjectSetting;
use Illuminate\Database\Seeder;

class S54StorefrontSeeder extends Seeder
{
    public function run(): void
    {
        // 1. Languages
        Language::firstOrCreate(['code' => 'vi'], ['name' => 'Tiếng Việt', 'is_default' => true, 'is_active' => true]);
        Language::firstOrCreate(['code' => 'en'], ['name' => 'English', 'is_default' => false, 'is_active' => true]);

        // 2. Brand
        $brand = Brand::firstOrCreate(
            ['slug' => 's54-coffee'],
            ['name' => 'S54 COFFEE', 'is_active' => true]
        );

        // 3. Categories with Translatable Names
        $catBeans = Category::firstOrCreate(
            ['slug' => 'ca-phe-hat'],
            [
                'name' => ['vi' => 'Cà Phê Hạt Rang Mộc', 'en' => 'Roasted Coffee Beans'],
                'description' => ['vi' => 'Cà phê hạt rang mộc công nghệ Hot-Air Đức', 'en' => 'Hot-Air roasted artisan coffee beans'],
                'is_active' => true,
                'is_draft' => false,
            ]
        );

        $catSpecialty = Category::firstOrCreate(
            ['slug' => 'specialty-coffee'],
            [
                'name' => ['vi' => 'Specialty Tuyển Chọn', 'en' => 'Specialty Coffee Range'],
                'description' => ['vi' => 'Dòng Specialty giới hạn từ các nông trại riêng', 'en' => 'Micro-lot specialty single origin coffee'],
                'is_active' => true,
                'is_draft' => false,
            ]
        );

        $catInstant = Category::firstOrCreate(
            ['slug' => 'ca-phe-hoa-tan'],
            [
                'name' => ['vi' => 'Cà Phê Hòa Tan 3in1', 'en' => 'Instant 3-in-1 Coffee'],
                'description' => ['vi' => 'Hòa tan & sấy lạnh cao cấp giữ trọn hương vị', 'en' => 'Premium instant and freeze-dried coffee'],
                'is_active' => true,
                'is_draft' => false,
            ]
        );

        // 4. Products with Translatable Names, Descriptions, and Image Assets
        $productsData = [
            [
                'name' => [
                    'vi' => 'S54 Robusta Rang Mộc Nguyên Chất',
                    'en' => 'S54 Pure Roasted Robusta Beans',
                ],
                'slug' => 's54-robusta-rang-moc-nguyen-chat',
                'sku' => 'S54-ROB-01',
                'price' => 145000,
                'short_description' => [
                    'vi' => 'Dòng blend phục vụ khách sạn & nhà hàng được ưa chuộng nhất.',
                    'en' => 'Our premiere blend, served in leading restaurants and hotels.',
                ],
                'description' => [
                    'vi' => 'Cà phê Robusta Đắk Lắk tuyển chọn, rang mộc bằng công nghệ Hot-Air của Đức. Vị đậm đà truyền thống, hậu vị ngọt kéo dài.',
                    'en' => 'Premium Dak Lak Robusta precision roasted with German Hot-Air technology. Bold, rich and deeply satisfying.',
                ],
                'image_url' => 'client-assets/images/s54/robusta_1.jpg',
                'category_id' => $catBeans->id,
            ],
            [
                'name' => [
                    'vi' => 'Cinque Stelle® S54 Arabica Cầu Đất Thượng Hạng',
                    'en' => 'Cinque Stelle® S54 Cau Dat Arabica',
                ],
                'slug' => 'cinque-stelle-s54-arabica-cau-dat',
                'sku' => 'S54-ARA-01',
                'price' => 150000,
                'short_description' => [
                    'vi' => 'Dòng cà phê thượng hạng phục vụ tại các nhà hàng & quán cafe cao cấp.',
                    'en' => 'Artisan Arabica blend for premium cafes and fine dining.',
                ],
                'description' => [
                    'vi' => '100% Arabica Cầu Đất ở độ cao 1.600m. Hương thơm hoa quả thanh khiết, chua thanh tao nhã và ngọt hậu mật ong.',
                    'en' => '100% Cau Dat Arabica grown at 1600m elevation. Floral aroma, bright acidity and lingering honey finish.',
                ],
                'image_url' => 'client-assets/images/s54/instant_3in1_1.jpg',
                'category_id' => $catBeans->id,
            ],
            [
                'name' => [
                    'vi' => 'Lab Release - Blend No. 58 Specialty Coffee',
                    'en' => 'Lab Release - Blend No. 58 Specialty',
                ],
                'slug' => 'lab-release-blend-no-58-specialty',
                'sku' => 'S54-LAB-58',
                'price' => 185000,
                'short_description' => [
                    'vi' => 'Dòng Specialty Tuyển Chọn từ các mẻ hạt giới hạn.',
                    'en' => 'Exclusive Specialty micro-lot selection.',
                ],
                'description' => [
                    'vi' => 'Phiên bản giới hạn phối trộn giữa Arabica Cầu Đất và Fine Robusta Gia Lai lên men tự nhiên. Tầng hương phức hợp caramel và quả mọng.',
                    'en' => 'Limited edition blend of Cau Dat Arabica and naturally fermented Fine Robusta. Complex notes of berry and caramel.',
                ],
                'image_url' => 'client-assets/images/s54/arabica_beans.jpg',
                'category_id' => $catSpecialty->id,
            ],
            [
                'name' => [
                    'vi' => 'S54 Espresso Rang Mộc Đậm Đà',
                    'en' => 'S54 Espresso Dark Roast Beans',
                ],
                'slug' => 's54-espresso-rang-moc-dam-da',
                'sku' => 'S54-ESP-01',
                'price' => 165000,
                'short_description' => [
                    'vi' => 'Độ rang đậm đà, mang lại hương vị espresso nồng nàn và mạnh mẽ.',
                    'en' => 'Dark roast profile delivering bold crema and intense espresso.',
                ],
                'description' => [
                    'vi' => 'Chuyên dụng cho máy pha espresso. Cho lớp crema dày vàng óng, vị đắng socola đậm đà, cực kỳ phù hợp cho latte và cappuccino.',
                    'en' => 'Crafted for commercial espresso machines. Produces thick golden crema, dark chocolate richness, perfect for milk blends.',
                ],
                'image_url' => 'client-assets/images/s54/instant_3in1_2.jpg',
                'category_id' => $catBeans->id,
            ],
            [
                'name' => [
                    'vi' => 'S54 Cà Phê Hòa Tan 3in1 Tinh Hoa Việt',
                    'en' => 'S54 Instant 3-in-1 Vietnamese Coffee',
                ],
                'slug' => 's54-ca-phe-hoa-tan-3in1',
                'sku' => 'S54-INS-3IN1',
                'price' => 65000,
                'short_description' => [
                    'vi' => 'Hương vị đậm đà, béo ngậy tiện lợi cho cuộc sống hiện đại.',
                    'en' => 'Rich and creamy instant coffee for modern lifestyle.',
                ],
                'description' => [
                    'vi' => 'Được chiết xuất từ cốt cà phê nguyên chất, giữ trọn hương vị cà phê sữa đá truyền thống Việt Nam chỉ trong 1 phút pha chế.',
                    'en' => 'Extracted from pure coffee brew, recreating the authentic Vietnamese iced milk coffee experience in 1 minute.',
                ],
                'image_url' => 'client-assets/images/s54/instant_3in1_1.jpg',
                'category_id' => $catInstant->id,
            ],
            [
                'name' => [
                    'vi' => 'S54 Freeze-Dried Sấy Lạnh Cao Cấp',
                    'en' => 'S54 Freeze-Dried Premium Instant',
                ],
                'slug' => 's54-freeze-dried-say-lanh',
                'sku' => 'S54-INS-FD',
                'price' => 120000,
                'short_description' => [
                    'vi' => 'Công nghệ sấy lạnh giữ trọn 99% hương thơm cà phê nguyên bản.',
                    'en' => 'Freeze-dried technology preserving 99% of original aroma.',
                ],
                'description' => [
                    'vi' => 'Sử dụng công nghệ thăng hoa lạnh ở nhiệt độ -40 độ C, bảo toàn nguyên vẹn các hợp chất hương thơm tự nhiên của hạt cà phê Arabica.',
                    'en' => 'Sublimation freeze-drying at -40°C preserves all delicate aromatic compounds of premium Arabica beans.',
                ],
                'image_url' => 'client-assets/images/s54/instant_3in1_2.jpg',
                'category_id' => $catInstant->id,
            ],
        ];

        foreach ($productsData as $pData) {
            $product = Product::firstOrCreate(
                ['slug' => $pData['slug']],
                [
                    'brand_id' => $brand->id,
                    'category_id' => $pData['category_id'],
                    'name' => $pData['name'],
                    'sku' => $pData['sku'],
                    'price' => $pData['price'],
                    'short_description' => $pData['short_description'],
                    'description' => $pData['description'],
                    'image_url' => $pData['image_url'],
                    'is_active' => true,
                    'is_featured' => true,
                    'manage_stock' => false,
                    'stock_quantity' => 500,
                ]
            );

            // Add Product Image Gallery
            ProductImage::firstOrCreate(
                ['product_id' => $product->id, 'image_url' => $pData['image_url']],
                ['sort_order' => 1]
            );

            // Add Variants
            ProductVariant::firstOrCreate(
                ['product_id' => $product->id, 'sku' => $product->sku . '-1KG'],
                [
                    'name' => ['vi' => '1kg', 'en' => '1kg'],
                    'price' => $product->price,
                    'is_active' => true,
                    'is_default' => true,
                    'stock_quantity' => 200,
                ]
            );
            ProductVariant::firstOrCreate(
                ['product_id' => $product->id, 'sku' => $product->sku . '-500G'],
                [
                    'name' => ['vi' => '500g', 'en' => '500g'],
                    'price' => round($product->price * 0.55),
                    'is_active' => true,
                    'is_default' => false,
                    'stock_quantity' => 200,
                ]
            );
        }

        // 5. Blog Category & Posts
        $postCat = PostCategory::firstOrCreate(
            ['slug' => 'cam-nang-ca-phe'],
            [
                'name' => ['vi' => 'Cẩm Nang Cà Phê', 'en' => 'Coffee Journal'],
                'is_active' => true,
            ]
        );

        Post::firstOrCreate(
            ['slug' => 'bi-quyet-pha-phin-truyen-thong-dam-da'],
            [
                'category_id' => $postCat->id,
                'title' => [
                    'vi' => 'Bí Quyết Pha Cà Phê Phin Truyền Thống Đậm Đà Đúng Chuẩn Barista',
                    'en' => 'The Art of Traditional Vietnamese Phin Brewing',
                ],
                'summary' => [
                    'vi' => 'Cách kiểm soát nhiệt độ nước và thời gian ủ để có ly cà phê phin sánh mịn, béo ngậy.',
                    'en' => 'How to control water temperature and blooming time for the perfect rich phin coffee.',
                ],
                'content' => [
                    'vi' => '<p>Cà phê phin là nét văn hóa thưởng thức đặc trưng của người Việt Nam. Để có được ly cà phê hoàn hảo, nhiệt độ nước lý tưởng nên ở mức 92-96 độ C...</p>',
                    'en' => '<p>Traditional Phin filter is the heart of Vietnamese coffee culture. Ideal brewing temperature is between 92-96 degrees Celsius...</p>',
                ],
                'image_url' => 'client-assets/images/s54/story_cupping_barista.jpg',
                'is_active' => true,
                'published_at' => now(),
            ]
        );

        Post::firstOrCreate(
            ['slug' => 'cong-nghe-rang-hot-air-la-gi'],
            [
                'category_id' => $postCat->id,
                'title' => [
                    'vi' => 'Công Nghệ Rang Hot-Air: Bước Đột Phá Giữ Trọn Tinh Túy Hạt Cà Phê',
                    'en' => 'German Hot-Air Roasting Technology Explained',
                ],
                'summary' => [
                    'vi' => 'Khám phá sự khác biệt giữa rang truyền thống và công nghệ Hot-Air kiểm soát luồng khí nóng hồi nhiệt.',
                    'en' => 'Discover how convective hot air roasting unlocks pure, uncharred bean flavours.',
                ],
                'content' => [
                    'vi' => '<p>Rang Hot-Air sử dụng luồng khí nóng đối lưu tuần hoàn giúp hạt cà phê chín đều từ trong lõi mà không làm cháy lớp vỏ ngoài...</p>',
                    'en' => '<p>Hot-Air convective roasting ensures uniform heat transfer throughout the bean core without scorching the surface...</p>',
                ],
                'image_url' => 'client-assets/images/s54/story_roasting_master.jpg',
                'is_active' => true,
                'published_at' => now(),
            ]
        );

        // 6. Project Settings
        ProjectSetting::updateOrCreate(['setting_key' => 'site_name'], ['setting_value' => 'S54 COFFEE', 'updated_at' => now()]);
        ProjectSetting::updateOrCreate(['setting_key' => 'hotline'], ['setting_value' => '0383.707.578', 'updated_at' => now()]);
        ProjectSetting::updateOrCreate(['setting_key' => 'address'], ['setting_value' => 'Số 35, Đường T8, Manhattan, Vinhomes Grand Park, TP. Thủ Đức, TP.HCM', 'updated_at' => now()]);
        ProjectSetting::updateOrCreate(['setting_key' => 'company_name'], ['setting_value' => 'CÔNG TY TNHH GIẢI PHÁP TỐT (Good Solutions Co., Ltd)', 'updated_at' => now()]);
    }
}
