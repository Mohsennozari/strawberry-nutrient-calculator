<template>
  <div class="bg-white rounded-b-xl shadow-lg p-6 font-vazir">

    <!-- ===== هدر ===== -->
    <div class="flex items-center gap-3 mb-6 border-b border-gray-200 pb-4">
      <div>
        <h2 class="text-2xl font-bold text-gray-800">درباره محاسبات</h2>
        <p class="text-sm text-gray-500 mt-0.5">
          درک کنید که سیستم چگونه نیاز غذایی توت‌فرنگی شما را محاسبه می‌کند
        </p>
      </div>
    </div>

    <!-- ===== مقدمه ===== -->
    <div class="mb-6 p-4 bg-green-50 rounded-xl border-2 border-green-200">
      <div class="flex items-start gap-3">
        <div>
          <h3 class="font-bold text-green-800">رسالت این سیستم</h3>
          <p class="text-sm text-gray-700 mt-1 leading-relaxed">
            این سیستم <span class="font-bold text-green-700">فقط و فقط یک ماشین‌حساب تغذیه</span> است که با توجه به وضعیت فعلی گیاه،
            میزان دقیق <span class="font-bold">ppm</span> از هر عنصر غذایی را محاسبه می‌کند.
          </p>
          <div class="mt-2 flex flex-wrap gap-2">
            <span class="px-3 py-1 bg-green-100 text-green-700 rounded-lg text-xs font-bold">مبتنی بر ۹ منبع علمی</span>
            <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-lg text-xs font-bold">۱۳ عنصر غذایی</span>
            <span class="px-3 py-1 bg-purple-100 text-purple-700 rounded-lg text-xs font-bold">۷ نسبت کلیدی</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ===== بخش ۱: فیلدهای ورودی ===== -->
    <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
      <span class="inline-block w-1.5 h-6 bg-blue-500 rounded-full"></span>
      فیلدهای ورودی (چطور اندازه‌گیری می‌کنیم؟)
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">

      <!-- قطر طوقه -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">قطر طوقه</span>
            <span class="text-xs text-gray-500 mr-2">(میلی‌متر)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              با کولیس دیجیتال دقیقاً بالای سطح بستر اندازه‌گیری کنید.
            </p>
            <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
              <span class="font-bold">محاسبه:</span> تشخیص مرحله رشد (رویشی/گلدهی/باردهی/رسیدگی) بر اساس قطر طوقه و سن بوته
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: Frontiers in Plant Science (2024) [5]
            </div>
          </div>
        </div>
      </div>

      <!-- ارتفاع بوته -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">ارتفاع بوته</span>
            <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              از سطح خاک تا بلندترین برگچه با خط‌کش اندازه‌گیری کنید.
            </p>
            <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
              <span class="font-bold">محاسبه:</span> شاخص رشد رویسی - در تشخیص مرحله رشد با قطر طوقه ترکیب می‌شود
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: UF/IFAS Extension (2024) [3]
            </div>
          </div>
        </div>
      </div>

      <!-- طول دمبرگ -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">طول دمبرگ</span>
            <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              از پایین‌ترین نقطه‌ی اتصال به ساقه تا قاعده‌ی برگچه را اندازه‌گیری کنید.
            </p>
            <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
              <span class="font-bold">محاسبه:</span> شاخص فعالیت متابولیک - در مدل SPT (Frontiers 2024) استفاده می‌شود
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: Frontiers in Plant Science (2024) [5]
            </div>
          </div>
        </div>
      </div>

      <!-- طول برگ + عرض برگ -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">طول و عرض برگ</span>
            <span class="text-xs text-gray-500 mr-2">(سانتی‌متر)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              بزرگترین برگچه را انتخاب کنید و طول و عرض آن را اندازه‌گیری کنید.
            </p>
            <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
              <span class="font-bold">محاسبه:</span>
              <span class="block mt-1">• سطح برگ = طول × عرض × ۰.۷۵</span>
              <span class="block">• اگر برگ کوچک باشد → کمبود نیتروژن → افزایش ۱۵٪ N</span>
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: Bottoms et al. (2013) DRIS California [2]
            </div>
          </div>
        </div>
      </div>

      <!-- اندازه میوه -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">اندازه میوه</span>
            <span class="text-xs text-gray-500 mr-2">(سانتی‌متر مربع)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              طول و عرض میوه را اندازه‌گیری کنید و طول × عرض را محاسبه کنید.
            </p>
            <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
              <span class="font-bold">محاسبه (مدل غیرخطی):</span>
              <span class="block mt-1">وزن = ۱.۲ × (اندازه ^ ۰.۸۵) + ۰.۸</span>
              <span class="block text-xs text-gray-500 mt-1">دقت: R² = 0.92 (Frontiers 2024)</span>
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: Frontiers in Plant Science (2024) - SPT Tool [5]
            </div>
          </div>
        </div>
      </div>

      <!-- سن بوته -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">سن بوته</span>
            <span class="text-xs text-gray-500 mr-2">(روز)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              تعداد روزهای گذشته از زمان نشاء را محاسبه کنید.
            </p>
            <div class="mt-2 bg-blue-50 p-2 rounded-lg text-xs text-blue-700 border border-blue-100">
              <span class="font-bold">محاسبه:</span>
              <span class="block mt-1">• ۰-۳۰ روز → رویشی</span>
              <span class="block">• ۳۰-۶۰ روز → گلدهی</span>
              <span class="block">• ۶۰-۱۲۰ روز → باردهی</span>
              <span class="block">• ۱۲۰+ روز → رسیدگی</span>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- ===== بخش ۲: اصلاحات محیطی ===== -->
    <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2 mt-8">
      <span class="inline-block w-1.5 h-6 bg-orange-500 rounded-full"></span>
      اصلاحات محیطی (چطور شرایط را در نظر می‌گیریم؟)
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">

      <!-- دما -->
      <div class="bg-orange-50 rounded-xl p-4 border border-orange-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">دمای روزانه</span>
            <span class="text-xs text-gray-500 mr-2">(درجه سانتی‌گراد)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              میانگین دمای ۲۴ ساعت گذشته را از دماسنج گلخانه ثبت کنید.
            </p>
            <div class="mt-2 bg-white p-2 rounded-lg text-xs border border-orange-100">
              <span class="font-bold text-orange-700">اصلاحات:</span>
              <span class="block mt-1">• دمای بالای ۲۸°C → Ca +۱۰%, K +۵%</span>
              <span class="block">• دمای پایین ۱۵°C → K +۱۰%</span>
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: UF/IFAS Extension (2024) [3]
            </div>
          </div>
        </div>
      </div>

      <!-- وضعیت هوا -->
      <div class="bg-orange-50 rounded-xl p-4 border border-orange-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">وضعیت هوا</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              وضعیت کلی آسمان را در طول روز انتخاب کنید.
            </p>
            <div class="mt-2 bg-white p-2 rounded-lg text-xs border border-orange-100">
              <span class="font-bold text-orange-700">اصلاحات:</span>
              <span class="block mt-1">• هوای ابری → N -۱۵% (فتوسنتز کاهش می‌یابد)</span>
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: Bottoms et al. (2013) DRIS California [2]
            </div>
          </div>
        </div>
      </div>

      <!-- EC -->
      <div class="bg-orange-50 rounded-xl p-4 border border-orange-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">EC</span>
            <span class="text-xs text-gray-500 mr-2">(dS/m)</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              با EC متر محلول خروجی را اندازه‌گیری کنید.
            </p>
            <div class="mt-2 bg-white p-2 rounded-lg text-xs border border-orange-100">
              <span class="font-bold text-orange-700">اصلاحات:</span>
              <span class="block mt-1">• EC > ۲.۵ → همه عناصر +۸% (تنش اسمزی)</span>
              <span class="block">• EC < ۱.۰ → همه عناصر -۸% (جذب بیش‌ازحد)</span>
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: Gil-Marín et al. (2025) [7]
            </div>
          </div>
        </div>
      </div>

      <!-- pH -->
      <div class="bg-orange-50 rounded-xl p-4 border border-orange-200 hover:shadow-md transition-shadow duration-200">
        <div class="flex items-start gap-3">
          <div>
            <span class="font-bold text-gray-800">pH</span>
            <p class="text-sm text-gray-600 mt-1 leading-relaxed">
              با pH متر محلول خروجی را اندازه‌گیری کنید.
            </p>
            <div class="mt-2 bg-white p-2 rounded-lg text-xs border border-orange-100">
              <span class="font-bold text-orange-700">اصلاحات:</span>
              <span class="block mt-1">• pH > ۶.۵ → Fe +۳۰%, Mn +۳۰% (رسوب آهن و منگنز)</span>
              <span class="block">• pH < ۵.۵ → Ca +۲۰%, Mg +۲۰% (اختلال جذب)</span>
            </div>
            <div class="mt-1.5 text-xs text-gray-500">
              منبع: UF/IFAS Extension (2024) [3]
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- ===== بخش ۳: خروجی‌ها ===== -->
    <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2 mt-8">
      <span class="inline-block w-1.5 h-6 bg-purple-500 rounded-full"></span>
      خروجی‌ها (چه چیزی دریافت می‌کنید؟)
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">

      <div class="bg-purple-50 rounded-xl p-4 border border-purple-200 text-center hover:shadow-md transition-shadow duration-200">
        <h4 class="font-bold text-gray-800 text-sm mt-2">۱۳ عنصر غذایی</h4>
        <p class="text-xs text-gray-600 mt-1 leading-relaxed">
          N, P, K, Ca, Mg, S, Fe, Zn, Mn, Cu, B, Mo, Cl
        </p>
        <div class="mt-2 bg-white p-2 rounded-lg text-xs">
          <span class="font-bold text-purple-700">محاسبه:</span>
          <span class="block mt-1">PPM نهایی = PPM پایه × اصلاحات</span>
        </div>
        <div class="mt-1 text-xs text-gray-500">
          ۹ منبع علمی معتبر
        </div>
      </div>

      <div class="bg-purple-50 rounded-xl p-4 border border-purple-200 text-center hover:shadow-md transition-shadow duration-200">
        <h4 class="font-bold text-gray-800 text-sm mt-2">۷ نسبت کلیدی</h4>
        <p class="text-xs text-gray-600 mt-1 leading-relaxed">
          K:Ca, K:Mg, Ca:Mg, N:K, K:S, Fe:Mn, B:Ca
        </p>
        <div class="mt-2 bg-white p-2 rounded-lg text-xs">
          <span class="font-bold text-purple-700">محاسبه:</span>
          <span class="block mt-1">نسبت = عنصر۱ ÷ عنصر۲</span>
        </div>
        <div class="mt-1 text-xs text-gray-500">
          Yousefi 2023 + UF/IFAS 2024
        </div>
      </div>

      <div class="bg-purple-50 rounded-xl p-4 border border-purple-200 text-center hover:shadow-md transition-shadow duration-200">
        <h4 class="font-bold text-gray-800 text-sm mt-2">هشدارها + توصیه‌ها</h4>
        <p class="text-xs text-gray-600 mt-1 leading-relaxed">
          بحرانی / هشدار / اطلاع‌رسانی
        </p>
        <div class="mt-2 bg-white p-2 rounded-lg text-xs">
          <span class="font-bold text-purple-700">محاسبه:</span>
          <span class="block mt-1">بر اساس خروجی از محدوده بهینه</span>
        </div>
        <div class="mt-1 text-xs text-gray-500">
          همراه با منبع علمی
        </div>
      </div>

    </div>

    <!-- ===== بخش ۴: منابع علمی ===== -->
    <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2 mt-8">
      <span class="inline-block w-1.5 h-6 bg-red-500 rounded-full"></span>
      منابع علمی (بر اساس چه تحقیقاتی؟)
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-6">
      <div v-for="ref in references" :key="ref.id"
           class="bg-gray-50 rounded-xl p-3 border border-gray-200 hover:shadow-md transition-shadow duration-200">
        <span class="font-bold text-gray-800 text-sm">{{ ref.id }}. {{ ref.title }}</span>
        <p class="text-xs text-gray-600 mt-1 leading-relaxed">{{ ref.description }}</p>
        <div class="mt-1.5 flex flex-wrap gap-1">
          <span v-for="tag in ref.tags" :key="tag"
                class="px-2 py-0.5 bg-green-100 text-green-700 rounded-full text-[10px]">
            {{ tag }}
          </span>
        </div>
      </div>
    </div>

    <!-- ===== بخش ۵: فرمول‌های کلیدی ===== -->
    <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2 mt-8">
      <span class="inline-block w-1.5 h-6 bg-yellow-500 rounded-full"></span>
      فرمول‌های کلیدی
    </h3>

    <div class="bg-gray-50 rounded-xl p-4 border border-gray-200">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <h5 class="font-bold text-sm text-gray-700">پیش‌بینی وزن میوه</h5>
          <code class="block bg-white p-2 rounded text-xs font-mono mt-1 border border-gray-200">
            وزن = ۱.۲ × (اندازه ^ ۰.۸۵) + ۰.۸
          </code>
          <span class="text-[10px] text-gray-500">R² = 0.92 (Frontiers 2024)</span>
        </div>
        <div>
          <h5 class="font-bold text-sm text-gray-700">سطح برگ</h5>
          <code class="block bg-white p-2 rounded text-xs font-mono mt-1 border border-gray-200">
            سطح = طول برگ × عرض برگ × ۰.۷۵
          </code>
          <span class="text-[10px] text-gray-500">مدل بیضوی</span>
        </div>
        <div>
          <h5 class="font-bold text-sm text-gray-700">اصلاح EC</h5>
          <code class="block bg-white p-2 rounded text-xs font-mono mt-1 border border-gray-200">
            اگر EC > ۲.۵ → ppm = ppm × ۱.۰۸
          </code>
          <span class="text-[10px] text-gray-500">Gil-Marín 2025</span>
        </div>
        <div>
          <h5 class="font-bold text-sm text-gray-700">اصلاح pH</h5>
          <code class="block bg-white p-2 rounded text-xs font-mono mt-1 border border-gray-200">
            اگر pH > ۶.۵ → Fe = Fe × ۱.۳
          </code>
          <span class="text-[10px] text-gray-500">UF/IFAS 2024</span>
        </div>
      </div>
    </div>

    <!-- ===== پایین صفحه ===== -->
    <div class="mt-6 p-4 bg-green-50 rounded-xl border-2 border-green-200 text-center">
      <p class="text-sm text-gray-700">
        <span class="font-bold text-green-700">همه محاسبات بر اساس منابع علمی معتبر است.</span>
      </p>
      <p class="text-xs text-gray-500 mt-1">
        برای مشاهده جزئیات کامل، به تب «منابع» مراجعه کنید.
      </p>
    </div>

  </div>
</template>

<script>
export default {
  name: 'AboutTab',
  data() {
    return {
      references: [
        {
          id: '[1]',
          title: 'Mashayekhi et al. (2013)',
          description: 'بررسی غلظت‌های N, P, K در هیدروپونیک - رقم Sweet Charlie',
          tags: ['هیدروپونیک', 'NPK', 'عملکرد']
        },
        {
          id: '[2]',
          title: 'Bottoms et al. (2013)',
          description: 'DRIS California - ۵۰ مزرعه رقم Albion - محدوده‌های اصلی عناصر',
          tags: ['DRIS', 'Albion', 'برگ']
        },
        {
          id: '[3]',
          title: 'UF/IFAS Extension (2024)',
          description: 'راهنمای آزمون شیره دمبرگ - مدیریت تغذیه توت‌فرنگی',
          tags: ['دمبرگ', 'نیترات', 'پتاسیم']
        },
        {
          id: '[4]',
          title: 'Yousefi et al. (2023)',
          description: 'بررسی نسبت‌های K/N در رقم Camarosa - هیدروپونیک',
          tags: ['K/N', 'Camarosa', 'نسبت']
        },
        {
          id: '[5]',
          title: 'Frontiers in Plant Science (2024)',
          description: 'ابزار فنوتایپ‌نگاری توت‌فرنگی (SPT) - مدل غیرخطی وزن میوه',
          tags: ['فنوتایپ', 'پیش‌بینی', 'وزن']
        },
        {
          id: '[6]',
          title: 'University of Delaware Extension',
          description: 'محدوده‌های کفایت عناصر برگ و دمبرگ',
          tags: ['کفایت', 'برگ', 'دمبرگ']
        },
        {
          id: '[7]',
          title: 'Gil-Marín et al. (2025)',
          description: 'بررسی سطوح EC در هیدروپونیک - رقم Albion',
          tags: ['EC', 'هیدروپونیک', 'عملکرد']
        },
        {
          id: '[8]',
          title: 'EFSA (2023)',
          description: 'بررسی آهن در توت‌فرنگی هیدروپونیک',
          tags: ['آهن', 'هیدروپونیک', 'عناصر ریز']
        },
        {
          id: '[9]',
          title: 'Ebrahimi & Abadía (2023)',
          description: 'جذب آهن در محصولات باغی - مکانیسم‌های جذب',
          tags: ['آهن', 'جذب', 'مکانیسم']
        }
      ]
    }
  }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

.font-vazir {
  font-family: 'Vazir', 'Tahoma', sans-serif;
}

code {
  direction: ltr;
  text-align: left;
}
</style>
