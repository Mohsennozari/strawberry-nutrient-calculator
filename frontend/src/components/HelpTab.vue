<template>
  <div class="bg-white rounded-b-xl shadow-lg p-6 font-vazir">

    <!-- ===== هدر ===== -->
    <div class="flex items-center gap-3 mb-6 border-b border-gray-200 pb-4">
      <div>
        <h2 class="text-2xl font-bold text-gray-800">راهنمای کامل استفاده از سیستم</h2>
        <p class="text-sm text-gray-500 mt-0.5">این راهنما به شما کمک می‌کند تا از تمام امکانات سیستم به بهترین شکل استفاده کنید.</p>
      </div>
    </div>

    <!-- ============================================================ -->
    <!-- بخش ۱: فیلدهای ورودی -->
    <!-- ============================================================ -->
    <div class="mb-8">
      <h3 class="text-lg font-bold text-green-700 mb-4 flex items-center gap-2">
        <span class="inline-block w-1.5 h-6 bg-green-500 rounded-full"></span>
        فیلدهای ورودی (چگونه اندازه‌گیری کنیم؟)
      </h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- قطر طوقه -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">1</div>
            <div>
              <span class="font-bold text-gray-800">قطر طوقه</span>
              <span class="text-xs text-gray-500 mr-2">(میلی‌متر)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                با کولیس دیجیتال دقیقاً بالای سطح بستر اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۱۲ – ۱۷ میلی‌متر
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> قطر طوقه مهم‌ترین شاخص قدرت گیاه است. هرچه بزرگتر باشد، پتانسیل عملکرد بالاتر است.
              </div>
            </div>
          </div>
        </div>

        <!-- ارتفاع بوته -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">2</div>
            <div>
              <span class="font-bold text-gray-800">ارتفاع بوته</span>
              <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                از سطح خاک تا بلندترین برگچه با خط‌کش اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۲۰ – ۳۰ سانتی‌متر
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> ارتفاع بوته نشان‌دهنده‌ی رشد رویشی گیاه است.
              </div>
            </div>
          </div>
        </div>

        <!-- طول دمبرگ -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">3</div>
            <div>
              <span class="font-bold text-gray-800">طول دمبرگ</span>
              <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                از پایین‌ترین نقطه‌ی اتصال به ساقه تا قاعده‌ی برگچه را اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۱۰ – ۲۰ سانتی‌متر
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> طول دمبرگ نشان‌دهنده‌ی فعالیت متابولیک گیاه است.
              </div>
            </div>
          </div>
        </div>

        <!-- طول برگ -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">4</div>
            <div>
              <span class="font-bold text-gray-800">طول برگ</span>
              <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                بزرگترین برگچه را انتخاب کنید و طول آن را از قاعده تا نوک اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۶ – ۸ سانتی‌متر
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> طول برگ نشان‌دهنده‌ی وضعیت تغذیه‌ای نیتروژن است.
              </div>
            </div>
          </div>
        </div>

        <!-- عرض برگ -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">5</div>
            <div>
              <span class="font-bold text-gray-800">عرض برگ</span>
              <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                همان برگچه‌ای که طول آن را اندازه‌گرفتید، عریض‌ترین قسمت آن را اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۴.۵ – ۶.۵ سانتی‌متر
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> عرض برگ همراه با طول، شاخص سطح برگ (مساحت) را محاسبه می‌کند.
              </div>
            </div>
          </div>
        </div>

        <!-- اندازه میوه -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">6</div>
            <div>
              <span class="font-bold text-gray-800">اندازه میوه</span>
              <span class="text-xs text-gray-500 mr-2">(سانتی‌متر مربع)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                طول و عرض میوه را اندازه‌گیری کنید و طول × عرض را محاسبه کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۳ – ۱۰ سانتی‌متر مربع
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> از این عدد برای پیش‌بینی وزن نهایی میوه استفاده می‌شود.
              </div>
            </div>
          </div>
        </div>

        <!-- سن بوته -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">7</div>
            <div>
              <span class="font-bold text-gray-800">سن بوته</span>
              <span class="text-xs text-gray-500 mr-2">(روز)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                تعداد روزهای گذشته از زمان نشاء را محاسبه کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">چرخه رشد:</span> ۱-۲۸ روز (نشاء) • ۲۸-۵۶ روز (رویشی) • ۵۶-۱۱۲ روز (باردهی) • ۱۱۲+ روز (رسیدگی)
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> سن بوته برای تشخیص مرحله رشد و تنظیم نسبت عناصر استفاده می‌شود.
              </div>
            </div>
          </div>
        </div>

        <!-- تعداد میوه -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">8</div>
            <div>
              <span class="font-bold text-gray-800">تعداد میوه در هر بوته</span>
              <span class="text-xs text-gray-500 mr-2">(عدد)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                تمام میوه‌های در حال رشد روی بوته را بشمارید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده نرمال:</span> ۲ – ۱۰ عدد در بوته
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> هرچه تعداد میوه بیشتر باشد، نیاز به پتاسیم و کلسیم افزایش می‌یابد.
              </div>
            </div>
          </div>
        </div>

        <!-- دما -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">9</div>
            <div>
              <span class="font-bold text-gray-800">دمای روزانه</span>
              <span class="text-xs text-gray-500 mr-2">(درجه سانتی‌گراد)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                میانگین دمای ۲۴ ساعت گذشته را از دماسنج گلخانه ثبت کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده بهینه:</span> ۱۸ – ۲۸ درجه سانتی‌گراد
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> دمای بالای ۲۸ درجه باعث کاهش جذب کلسیم می‌شود.
              </div>
            </div>
          </div>
        </div>

        <!-- وضعیت هوا -->
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-sm font-bold flex-shrink-0">10</div>
            <div>
              <span class="font-bold text-gray-800">وضعیت هوا</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                وضعیت کلی آسمان را در طول روز انتخاب کنید.
              </p>
              <div class="mt-2 flex flex-wrap gap-2 text-sm">
                <span class="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-lg border border-yellow-200">آفتابی</span>
                <span class="px-3 py-1 bg-gray-200 text-gray-700 rounded-lg border border-gray-300">نیمه‌ابری</span>
                <span class="px-3 py-1 bg-gray-300 text-gray-600 rounded-lg border border-gray-400">ابری</span>
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> در هوای ابری، فتوسنتز کاهش می‌یابد و نیاز به نیتروژن کمتر می‌شود.
              </div>
            </div>
          </div>
        </div>

        <!-- EC (اختیاری) -->
        <div class="bg-gray-50 rounded-xl p-4 border-2 border-dashed border-gray-300 hover:border-blue-300 transition-colors duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-gray-200 rounded-lg flex items-center justify-center text-gray-600 text-sm font-bold flex-shrink-0">11</div>
            <div>
              <span class="font-bold text-gray-800">EC</span>
              <span class="text-xs text-gray-500 mr-2">(اختیاری - dS/m)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                با دستگاه EC متر محلول خروجی (Drain) را اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده بهینه:</span> ۱.۵ – ۲.۰ dS/m
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> EC بالا = تجمع نمک • EC پایین = جذب شدید عناصر
              </div>
            </div>
          </div>
        </div>

        <!-- pH (اختیاری) -->
        <div class="bg-gray-50 rounded-xl p-4 border-2 border-dashed border-gray-300 hover:border-blue-300 transition-colors duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-gray-200 rounded-lg flex items-center justify-center text-gray-600 text-sm font-bold flex-shrink-0">12</div>
            <div>
              <span class="font-bold text-gray-800">pH</span>
              <span class="text-xs text-gray-500 mr-2">(اختیاری)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                با دستگاه pH متر محلول خروجی (Drain) را اندازه‌گیری کنید.
              </p>
              <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
                <span class="font-bold">محدوده بهینه:</span> ۵.۸ – ۶.۲
              </div>
              <div class="mt-1.5 text-xs text-gray-500">
                <span class="text-yellow-600">نکته:</span> pH پایین = اختلال در جذب کلسیم و منیزیم • pH بالا = اختلال در جذب آهن و منگنز
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ============================================================ -->
    <!-- بخش ۲: نحوه استفاده از خروجی‌ها -->
    <!-- ============================================================ -->
    <div class="mb-8">
      <h3 class="text-lg font-bold text-green-700 mb-4 flex items-center gap-2">
        <span class="inline-block w-1.5 h-6 bg-blue-500 rounded-full"></span>
        نحوه استفاده از خروجی‌ها
      </h3>

      <div class="space-y-3">

        <!-- مرحله رشد -->
        <div class="bg-green-50 rounded-xl p-4 border border-green-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-green-200 rounded-lg flex items-center justify-center text-green-700 text-sm font-bold flex-shrink-0">1</div>
            <div>
              <span class="font-bold text-gray-800">مرحله رشد</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                سیستم بر اساس قطر طوقه و سن بوته، مرحله رشد را تشخیص می‌دهد:
              </p>
              <div class="flex flex-wrap gap-2 mt-2 text-sm">
                <span class="px-3 py-1 bg-green-100 text-green-700 rounded-lg border border-green-200">رویشی</span>
                <span class="px-3 py-1 bg-yellow-100 text-yellow-700 rounded-lg border border-yellow-200">گلدهی</span>
                <span class="px-3 py-1 bg-red-100 text-red-700 rounded-lg border border-red-200">باردهی</span>
                <span class="px-3 py-1 bg-gray-100 text-gray-600 rounded-lg border border-gray-200">رسیدگی</span>
              </div>
              <div class="mt-2 text-xs text-gray-600">
                <span class="text-blue-600 font-bold">کاربرد:</span> هر مرحله نیاز غذایی متفاوتی دارد. سیستم بر اساس این مرحله، PPM هدف را تنظیم می‌کند.
              </div>
            </div>
          </div>
        </div>

        <!-- عناصر غذایی -->
        <div class="bg-blue-50 rounded-xl p-4 border border-blue-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-blue-200 rounded-lg flex items-center justify-center text-blue-700 text-sm font-bold flex-shrink-0">2</div>
            <div>
              <span class="font-bold text-gray-800">عناصر غذایی (PPM هدف)</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                سیستم مقدار بهینه هر عنصر را نشان می‌دهد. هر عدد با کد رنگی مشخص شده است:
              </p>
              <div class="flex flex-wrap gap-2 mt-2 text-sm">
                <span class="px-3 py-1 bg-green-100 text-green-700 rounded-lg border border-green-200">سبز = بهینه</span>
                <span class="px-3 py-1 bg-red-100 text-red-700 rounded-lg border border-red-200">قرمز = کمبود</span>
                <span class="px-3 py-1 bg-orange-100 text-orange-700 rounded-lg border border-orange-200">نارنجی = بیش‌ازحد</span>
              </div>
              <div class="mt-2 text-xs text-gray-600">
                <span class="text-blue-600 font-bold">کاربرد:</span> اگر عنصری قرمز یا نارنجی است، باید کوددهی آن را تنظیم کنید.
              </div>
            </div>
          </div>
        </div>

        <!-- نسبت‌ها -->
        <div class="bg-purple-50 rounded-xl p-4 border border-purple-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-purple-200 rounded-lg flex items-center justify-center text-purple-700 text-sm font-bold flex-shrink-0">3</div>
            <div>
              <span class="font-bold text-gray-800">نسبت‌های کلیدی</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                نسبت بین عناصر از مقدار مطلق هر عنصر مهم‌تر است. مهم‌ترین نسبت‌ها:
              </p>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2">
                <div class="bg-white p-3 rounded-lg border border-gray-200">
                  <span class="font-bold text-gray-800">K:Ca</span>
                  <span class="text-xs text-gray-500 block">بهینه: ۱.۲-۱.۴</span>
                  <p class="text-xs text-gray-600 mt-0.5">اگر بالاتر باشد → خطر پوسیدگی نوک میوه</p>
                </div>
                <div class="bg-white p-3 rounded-lg border border-gray-200">
                  <span class="font-bold text-gray-800">K:Mg</span>
                  <span class="text-xs text-gray-500 block">بهینه: ۳-۴</span>
                  <p class="text-xs text-gray-600 mt-0.5">اگر بالاتر باشد → کمبود منیزیم</p>
                </div>
              </div>
              <div class="mt-2 text-xs text-gray-600">
                <span class="text-blue-600 font-bold">کاربرد:</span> اگر نسبتی خارج از محدوده بود، باید کوددهی را تنظیم کنید.
              </div>
            </div>
          </div>
        </div>

        <!-- EC و pH -->
        <div class="bg-teal-50 rounded-xl p-4 border border-teal-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-teal-200 rounded-lg flex items-center justify-center text-teal-700 text-sm font-bold flex-shrink-0">4</div>
            <div>
              <span class="font-bold text-gray-800">EC و pH</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                این دو پارامتر محیطی تأثیر مستقیم بر جذب عناصر دارند:
              </p>
              <div class="grid grid-cols-2 gap-3 mt-2">
                <div class="bg-white p-3 rounded-lg border border-gray-200 text-center">
                  <span class="font-bold text-gray-800">EC</span>
                  <span class="text-xs text-gray-500 block">بهینه: ۱.۵-۲.۰ dS/m</span>
                  <span class="text-xs text-gray-600">بالا = تجمع نمک</span>
                </div>
                <div class="bg-white p-3 rounded-lg border border-gray-200 text-center">
                  <span class="font-bold text-gray-800">pH</span>
                  <span class="text-xs text-gray-500 block">بهینه: ۵.۸-۶.۲</span>
                  <span class="text-xs text-gray-600">خارج = اختلال جذب</span>
                </div>
              </div>
              <div class="mt-2 text-xs text-gray-600">
                <span class="text-blue-600 font-bold">کاربرد:</span> اگر EC یا pH خارج از محدوده بود، قبل از کوددهی آن را اصلاح کنید.
              </div>
            </div>
          </div>
        </div>

        <!-- پیش‌بینی وزن میوه -->
        <div class="bg-pink-50 rounded-xl p-4 border border-pink-200 hover:shadow-md transition-shadow duration-200">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 bg-pink-200 rounded-lg flex items-center justify-center text-pink-700 text-sm font-bold flex-shrink-0">5</div>
            <div>
              <span class="font-bold text-gray-800">وزن میوه تخمینی</span>
              <p class="text-sm text-gray-600 mt-1 leading-relaxed">
                سیستم بر اساس اندازه میوه، وزن نهایی آن را تخمین می‌زند.
              </p>
              <div class="mt-2 flex flex-wrap gap-2 text-xs">
                <span class="px-3 py-1 bg-green-100 text-green-700 rounded-lg border border-green-200">دقت: R² = 0.92</span>
                <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-lg border border-blue-200">Frontiers 2024</span>
              </div>
              <div class="mt-1.5 text-xs text-gray-600">
                <span class="text-blue-600 font-bold">کاربرد:</span> برای برنامه‌ریزی برداشت و تخمین عملکرد کلی استفاده می‌شود.
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ============================================================ -->
    <!-- بخش ۳: هشدارها و توصیه‌ها -->
    <!-- ============================================================ -->
    <div class="mb-6">
      <h3 class="text-lg font-bold text-green-700 mb-4 flex items-center gap-2">
        <span class="inline-block w-1.5 h-6 bg-red-500 rounded-full"></span>
        هشدارها و توصیه‌ها
      </h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-red-50 rounded-xl p-4 border-2 border-red-200">
          <span class="font-bold text-red-700 flex items-center gap-2">
            <span class="w-4 h-4 bg-red-500 rounded-full inline-block"></span>
            هشدارهای قرمز (بحرانی)
          </span>
          <p class="text-sm text-gray-600 mt-1 leading-relaxed">
            این هشدارها نشان‌دهنده‌ی <span class="font-bold text-red-600">مشکل جدی</span> هستند که باید فوری به آن رسیدگی شود.
          </p>
          <ul class="text-xs text-gray-600 space-y-1 mt-2">
            <li class="flex items-start gap-2">- کمبود عنصر مهم (N, K, Ca)</li>
            <li class="flex items-start gap-2">- نسبت K:Ca بالاتر از ۱.۴</li>
            <li class="flex items-start gap-2">- دمای بالای ۳۰ درجه</li>
          </ul>
        </div>
        <div class="bg-yellow-50 rounded-xl p-4 border-2 border-yellow-200">
          <span class="font-bold text-yellow-700 flex items-center gap-2">
            <span class="w-4 h-4 bg-yellow-500 rounded-full inline-block"></span>
            هشدارهای زرد (هشدار)
          </span>
          <p class="text-sm text-gray-600 mt-1 leading-relaxed">
            این هشدارها نشان‌دهنده‌ی <span class="font-bold text-yellow-600">نیاز به توجه</span> هستند.
          </p>
          <ul class="text-xs text-gray-600 space-y-1 mt-2">
            <li class="flex items-start gap-2">- عنصر نزدیک به حد پایین</li>
            <li class="flex items-start gap-2">- نسبت K:Mg خارج از محدوده</li>
            <li class="flex items-start gap-2">- تعداد میوه زیاد</li>
          </ul>
        </div>
      </div>

      <div class="mt-4 p-4 bg-blue-50 rounded-xl border-2 border-blue-200">
        <span class="font-bold text-blue-700 flex items-center gap-2">
          <span class="w-4 h-4 bg-blue-500 rounded-full inline-block"></span>
          توصیه‌های عملی
        </span>
        <p class="text-sm text-gray-600 mt-1 leading-relaxed">
          سیستم به شما توصیه‌های عملی و دقیق می‌دهد، مانند:
        </p>
        <ul class="text-xs text-gray-600 space-y-1 mt-2">
          <li class="flex items-start gap-2">- میزان و نوع کودی که باید اضافه کنید</li>
          <li class="flex items-start gap-2">- تنظیم آبیاری بر اساس دما</li>
          <li class="flex items-start gap-2">- محلول‌پاشی عناصر در صورت نیاز</li>
        </ul>
        <p class="text-xs text-gray-500 mt-2">
          <span class="text-blue-500">نکته:</span> این توصیه‌ها بر اساس هشدارهای فعال تولید می‌شوند و به شما کمک می‌کنند تا سریعاً اقدام کنید.
        </p>
      </div>
    </div>

    <!-- ============================================================ -->
    <!-- بخش ۴: زمان‌بندی اندازه‌گیری -->
    <!-- ============================================================ -->
    <div class="mb-6">
      <h3 class="text-lg font-bold text-green-700 mb-4 flex items-center gap-2">
        <span class="inline-block w-1.5 h-6 bg-purple-500 rounded-full"></span>
        زمان‌بندی اندازه‌گیری (چقدر باید داده ثبت کرد؟)
      </h3>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-2xl block">روزانه</span>
          <ul class="text-xs text-gray-600 space-y-1 mt-2 text-right">
            <li>• دمای روزانه</li>
            <li>• وضعیت هوا</li>
          </ul>
          <div class="mt-2 inline-block px-3 py-1 bg-green-100 text-green-700 rounded-lg text-xs font-bold">زمان: ۲ دقیقه</div>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-2xl block">هفتگی</span>
          <ul class="text-xs text-gray-600 space-y-1 mt-2 text-right">
            <li>• ۶ صفت ریخت‌شناختی</li>
            <li>• تعداد میوه</li>
            <li>• سن بوته</li>
          </ul>
          <div class="mt-2 inline-block px-3 py-1 bg-yellow-100 text-yellow-700 rounded-lg text-xs font-bold">زمان: ۱۰ دقیقه</div>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-2xl block">ماهانه</span>
          <ul class="text-xs text-gray-600 space-y-1 mt-2 text-right">
            <li>• بررسی روند رشد</li>
            <li>• تعدیل ضرایب</li>
            <li>• بررسی عملکرد</li>
          </ul>
          <div class="mt-2 inline-block px-3 py-1 bg-red-100 text-red-700 rounded-lg text-xs font-bold">زمان: ۱۵ دقیقه</div>
        </div>
      </div>

      <div class="mt-4 p-4 bg-green-50 rounded-xl border-2 border-green-200 text-center">
        <p class="text-sm text-gray-700">
          <span class="font-bold">جمع زمان در هفته:</span>
          <span class="font-bold text-green-700 text-lg">۱۲ دقیقه</span>
        </p>
        <p class="text-xs text-gray-500 mt-1">با این زمان، شما می‌توانید تصمیمات کوددهی خود را بر اساس داده، نه حدس، بگیرید.</p>
      </div>
    </div>

    <!-- ============================================================ -->
    <!-- بخش ۵: ابزارهای مورد نیاز -->
    <!-- ============================================================ -->
    <div class="mb-6">
      <h3 class="text-lg font-bold text-green-700 mb-4 flex items-center gap-2">
        <span class="inline-block w-1.5 h-6 bg-orange-500 rounded-full"></span>
        ابزارهای مورد نیاز
      </h3>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-lg block">کولیس دیجیتال</span>
          <p class="text-xs text-gray-500">برای قطر طوقه</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-lg block">خط‌کش ۳۰ سانتی</span>
          <p class="text-xs text-gray-500">برای برگ و دمبرگ</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-lg block">دماسنج</span>
          <p class="text-xs text-gray-500">برای دمای گلخانه</p>
        </div>
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 text-center hover:shadow-md transition-shadow duration-200">
          <span class="text-lg block">گوشی هوشمند</span>
          <p class="text-xs text-gray-500">برای اجرای سیستم</p>
        </div>
      </div>
      <div class="mt-3 text-center text-xs text-gray-500">
        EC و pH متر (اختیاری، برای دقت بیشتر)
      </div>
    </div>

    <!-- ============================================================ -->
    <!-- بخش ۶: جمع‌بندی -->
    <!-- ============================================================ -->
    <div class="mt-6 p-5 bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl border-2 border-green-200">
      <h3 class="font-bold text-green-800 text-center text-lg">خلاصه: چگونه از سیستم استفاده کنیم؟</h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-3">
        <div class="bg-white p-3 rounded-xl text-center shadow-sm">
          <span class="text-lg block">۱</span>
          <span class="font-bold text-green-700 text-sm">اندازه‌گیری</span>
          <p class="text-xs text-gray-500">با کولیس و خط‌کش</p>
        </div>
        <div class="bg-white p-3 rounded-xl text-center shadow-sm">
          <span class="text-lg block">۲</span>
          <span class="font-bold text-green-700 text-sm">ورود</span>
          <p class="text-xs text-gray-500">در سیستم ثبت کنید</p>
        </div>
        <div class="bg-white p-3 rounded-xl text-center shadow-sm">
          <span class="text-lg block">۳</span>
          <span class="font-bold text-green-700 text-sm">دریافت</span>
          <p class="text-xs text-gray-500">PPM و هشدارها</p>
        </div>
        <div class="bg-white p-3 rounded-xl text-center shadow-sm">
          <span class="text-lg block">۴</span>
          <span class="font-bold text-green-700 text-sm">اقدام</span>
          <p class="text-xs text-gray-500">توصیه‌ها را اجرا کنید</p>
        </div>
      </div>
      <div class="text-center mt-4 pt-3 border-t border-green-200">
        <p class="text-sm text-gray-600">
          <span class="font-bold">زمان کل:</span> ۱۰-۱۲ دقیقه در هفته
          <span class="mx-2 text-gray-300">|</span>
          <span class="font-bold text-green-700">نتیجه:</span> افزایش ۱۵-۲۵٪ عملکرد
        </p>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'HelpTab'
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

.font-vazir {
  font-family: 'Vazir', 'Tahoma', sans-serif;
}
</style>
