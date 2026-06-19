<template>
  <div class="bg-white rounded-b-xl shadow-lg p-6 font-vazir">

    <!-- هدر -->
    <div class="flex items-center gap-3 mb-6 border-b border-gray-200 pb-4">
      <svg class="w-8 h-8 text-green-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
      </svg>
      <div>
        <h2 class="text-2xl font-bold text-gray-800">منابع و مراجع علمی</h2>
        <p class="text-sm text-gray-500 mt-0.5">
          تمام اعداد، هشدارها و فرمول‌های این سیستم بر اساس پژوهش‌های معتبر زیر است.
          برای مشاهده جزئیات، روی لینک هر منبع کلیک کنید.
        </p>
      </div>
    </div>

    <!-- ====== جدول ۱: منابع اصلی ====== -->
    <h3 class="text-lg font-bold text-green-700 mb-3 flex items-center gap-2">
      <span class="inline-block w-1.5 h-5 bg-green-500 rounded-full"></span>
      منابع اصلی
    </h3>
    <div class="overflow-x-auto mb-6 rounded-xl border border-gray-200">
      <table class="w-full text-sm border-collapse">
        <thead>
          <tr class="bg-green-50">
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">منبع</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">شرح</th>
            <th class="border border-gray-200 px-4 py-2.5 text-center font-bold text-gray-700">لینک</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="source in mainSources" :key="source.id" class="hover:bg-gray-50 transition-colors duration-150">
            <td class="border border-gray-200 px-4 py-2.5 font-bold text-gray-800">{{ source.title }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-gray-600 text-sm leading-relaxed">{{ source.description }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-center">
              <a :href="source.url" target="_blank" rel="noopener noreferrer"
                 class="inline-flex items-center gap-1 text-blue-600 hover:text-blue-800 hover:underline font-medium text-sm transition-colors duration-150">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                مشاهده
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ====== جدول ۲: محدوده‌های بهینه عناصر ====== -->
    <h3 class="text-lg font-bold text-green-700 mb-3 flex items-center gap-2">
      <span class="inline-block w-1.5 h-5 bg-blue-500 rounded-full"></span>
      محدوده‌های بهینه عناصر
    </h3>
    <div class="overflow-x-auto mb-6 rounded-xl border border-gray-200">
      <table class="w-full text-sm border-collapse">
        <thead>
          <tr class="bg-blue-50">
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">عنصر</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">محدوده بهینه (ppm)</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">مرجع</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in nutrientRanges" :key="item.element" class="hover:bg-gray-50 transition-colors duration-150">
            <td class="border border-gray-200 px-4 py-2.5 font-bold text-gray-800">{{ item.element }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-center font-mono font-medium text-gray-700">{{ item.range }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-gray-600 text-sm">
              <span class="inline-flex items-center gap-1">
                <span class="text-gray-400">[{{ item.refId }}]</span>
                {{ item.refName }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ====== جدول ۳: نسبت‌های کلیدی ====== -->
    <h3 class="text-lg font-bold text-green-700 mb-3 flex items-center gap-2">
      <span class="inline-block w-1.5 h-5 bg-purple-500 rounded-full"></span>
      نسبت‌های کلیدی
    </h3>
    <div class="overflow-x-auto mb-6 rounded-xl border border-gray-200">
      <table class="w-full text-sm border-collapse">
        <thead>
          <tr class="bg-purple-50">
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">نسبت</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">محدوده بهینه</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">خطر خارج از محدوده</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">مرجع</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in ratioRanges" :key="item.ratio" class="hover:bg-gray-50 transition-colors duration-150">
            <td class="border border-gray-200 px-4 py-2.5 font-bold text-gray-800">{{ item.ratio }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-center font-mono font-medium text-gray-700">{{ item.range }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-sm">
              <span class="px-2 py-0.5 rounded-full text-xs font-bold"
                :class="item.dangerLevel === 'high' ? 'bg-red-100 text-red-700' : 'bg-yellow-100 text-yellow-700'">
                {{ item.danger }}
              </span>
            </td>
            <td class="border border-gray-200 px-4 py-2.5 text-gray-600 text-sm">
              <span class="inline-flex items-center gap-1">
                <span class="text-gray-400">[{{ item.refId }}]</span>
                {{ item.refName }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ====== جدول ۴: تشخیص مرحله رشد ====== -->
    <h3 class="text-lg font-bold text-green-700 mb-3 flex items-center gap-2">
      <span class="inline-block w-1.5 h-5 bg-yellow-500 rounded-full"></span>
      تشخیص مرحله رشد
    </h3>
    <div class="overflow-x-auto mb-6 rounded-xl border border-gray-200">
      <table class="w-full text-sm border-collapse">
        <thead>
          <tr class="bg-yellow-50">
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">مرحله رشد</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">قطر طوقه (میلی‌متر)</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">سن (روز)</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">مرجع</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in growthStages" :key="item.stage" class="hover:bg-gray-50 transition-colors duration-150">
            <td class="border border-gray-200 px-4 py-2.5 font-bold text-gray-800">
              <span class="inline-flex items-center gap-1">
                <span>{{ item.icon }}</span>
                {{ item.stage }}
              </span>
            </td>
            <td class="border border-gray-200 px-4 py-2.5 text-center font-mono text-gray-700">{{ item.crown }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-center font-mono text-gray-700">{{ item.age }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-gray-600 text-sm">
              <span class="inline-flex items-center gap-1">
                <span class="text-gray-400">[{{ item.refId }}]</span>
                {{ item.refName }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ====== ارجاعات کامل ====== -->
    <h3 class="text-lg font-bold text-green-700 mb-3 flex items-center gap-2">
      <span class="inline-block w-1.5 h-5 bg-gray-600 rounded-full"></span>
      ارجاعات کامل با لینک
    </h3>
    <div class="bg-gray-50 rounded-xl p-4 text-sm text-gray-700 space-y-3 border border-gray-200">
      <div v-for="ref in references" :key="ref.id"
        class="border-b border-gray-200 pb-3 last:border-b-0 last:pb-0">
        <p class="leading-relaxed">
          <span class="font-bold text-gray-800">[{{ ref.id }}]</span>
          <span v-html="ref.text"></span>
        </p>
        <div class="flex flex-wrap gap-2 mt-1.5">
          <a v-for="link in ref.links" :key="link.url"
             :href="link.url" target="_blank" rel="noopener noreferrer"
             class="inline-flex items-center gap-1 text-blue-600 hover:text-blue-800 hover:underline text-xs transition-colors duration-150">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
            </svg>
            {{ link.label }}
          </a>
        </div>
      </div>
    </div>

    <!-- ====== هشدار مهم ====== -->
    <div class="mt-6 p-4 bg-yellow-50 rounded-xl border-2 border-yellow-200 flex items-start gap-3">
      <span class="text-2xl flex-shrink-0">⚠️</span>
      <div>
        <span class="font-bold text-yellow-800">توجه:</span>
        <p class="text-sm text-yellow-700 mt-0.5 leading-relaxed">
          داده‌های DRIS برای رقم <span class="font-bold">Albion</span> در خاک‌های ساحلی کالیفرنیا (Bottoms et al., 2013)
          <span class="text-gray-500">[۱]</span>.
          پژوهش Yousefi et al. (2023) برای رقم <span class="font-bold">Camarosa</span> در کشت هیدروپونیک انجام شده است
          <span class="text-gray-500">[۳]</span>.
          سیستم شما این داده‌ها را به‌عنوان «خط پایه» در نظر می‌گیرد و بر اساس ورودی‌های واقعی، اصلاحات لازم را اعمال می‌کند.
        </p>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ReferencesTab',
  data() {
    return {
      mainSources: [
        {
          id: 1,
          title: 'Bottoms et al. (2013) — DRIS California',
          description: 'نمونه‌برداری از ۵۳ مزرعه تجاری رقم Albion در دره‌های ساحلی کالیفرنیا — تعیین محدوده‌های بهینه DRIS برای عناصر برگ. منتشرشده در HortTechnology جلد ۲۳.',
          url: 'https://ouci.dntb.gov.ua/en/works/7p8Bxbk7/'
        },
        {
          id: 2,
          title: 'UF/IFAS Extension (2024)',
          description: 'راهنمای آزمون شیره دمبرگ به‌عنوان روش مدیریت بهینه تغذیه در دره سووانی — دانشگاه فلوریدا',
          url: 'https://blogs.ifas.ufl.edu/nmp/2024/04/08/petiole-sap-testing-as-a-best-management-practice-in-the-suwannee-valley/'
        },
        {
          id: 3,
          title: 'Yousefi et al. (2023)',
          description: 'بررسی نسبت‌های K/N در محلول غذایی روی رقم Camarosa — Journal of Berry Research، جلد ۱۳، شماره ۲',
          url: 'https://ouci.dntb.gov.ua/en/works/4rNXMdE4/'
        },
        {
          id: 4,
          title: 'Ndikumana et al. (2024) — Frontiers in Plant Science',
          description: 'توسعه ابزار فنوتایپ‌نگاری توت‌فرنگی (SPT) با یادگیری عمیق — اندازه‌گیری صفات ریخت‌شناختی از جمله قطر طوقه',
          url: 'https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1418383/full'
        },
        {
          id: 5,
          title: 'OMAFRA — Strawberry Nutrient Sufficiency Ranges',
          description: 'محدوده‌های کفایت عناصر برگ و دمبرگ توت‌فرنگی — سازمان کشاورزی و غذای انتاریو / دانشگاه دلاور',
          url: 'https://cropipm.omafra.gov.on.ca/en-ca/soil-diagnostics/plant-tissue-analysis/strawberry-nutrient-sufficiency-ranges'
        },
        {
          id: 6,
          title: 'Gil-Marín et al. (2025) — Agrociencia',
          description: 'بررسی تأثیر مصرف آب بستر و سطوح مختلف EC محلول Steiner روی عملکرد رقم Albion — Agrociencia جلد ۵۹',
          url: 'https://agrociencia-colpos.org/index.php/agrociencia/article/view/3035'
        },
        {
          id: 7,
          title: 'UF/IFAS — ویدیوهای آموزشی آزمون دمبرگ',
          description: 'ویدیوهای دوزبانه آموزش آزمون نیترات و پتاسیم شیره دمبرگ — دانشگاه فلوریدا IFAS Extension',
          url: 'https://urbanagnews.com/blog/news/new-english-spanish-videos-on-petiole-sap-nutrient-testing-from-university-of-florida-ifas-extension/'
        }
      ],

      nutrientRanges: [
        { element: 'نیتروژن (N) — مرحله پیش‌برداشت', range: '۳.۱ – ۳.۸ %', refId: '۱', refName: 'Bottoms et al. 2013 (DRIS)' },
        { element: 'نیتروژن (N) — مرحله برداشت', range: '۲.۴ – ۳.۰ %', refId: '۱', refName: 'Bottoms et al. 2013 (DRIS)' },
        { element: 'پتاسیم (K) — مرحله پیش‌برداشت', range: '۱.۸ – ۲.۲ %', refId: '۱', refName: 'Bottoms et al. 2013 (DRIS)' },
        { element: 'پتاسیم (K) — مرحله برداشت', range: '۱.۳ – ۱.۸ %', refId: '۱', refName: 'Bottoms et al. 2013 (DRIS)' },
        { element: 'کلسیم (Ca) — مرحله برداشت', range: '۱.۰ – ۲.۲ %', refId: '۱', refName: 'Bottoms et al. 2013 (DRIS)' },
        { element: 'منیزیم (Mg) — مرحله برداشت', range: '۰.۲۸ – ۰.۴۲ %', refId: '۱', refName: 'Bottoms et al. 2013 (DRIS)' },
        { element: 'پتاسیم محلول (K هیدروپونیک)', range: '۲۰۰ – ۳۰۰ mg/L', refId: '۳', refName: 'Yousefi et al. 2023' }
      ],

      ratioRanges: [
        {
          ratio: 'K/N — مرحله رویشی (هیدروپونیک)',
          range: '~۱.۱۱',
          danger: 'کاهش رشد رویشی',
          dangerLevel: 'medium',
          refId: '۳',
          refName: 'Yousefi et al. 2023'
        },
        {
          ratio: 'K/N — مرحله میوه‌دهی (هیدروپونیک)',
          range: '~۲.۵۰',
          danger: 'کاهش عملکرد',
          dangerLevel: 'high',
          refId: '۳',
          refName: 'Yousefi et al. 2023'
        },
        {
          ratio: 'نیترات دمبرگ — پیش‌برداشت',
          range: '> ۱۰۰۰ ppm',
          danger: 'کمبود نیتروژن',
          dangerLevel: 'high',
          refId: '۱',
          refName: 'Bottoms et al. 2013'
        },
        {
          ratio: 'نیترات دمبرگ — برداشت',
          range: '> ۴۰۰ ppm',
          danger: 'کمبود نیتروژن',
          dangerLevel: 'high',
          refId: '۱',
          refName: 'Bottoms et al. 2013'
        }
      ],

      growthStages: [
        { stage: 'رویشی', icon: '🌿', crown: '< ۱۲', age: '< ۳۰', refId: '۴', refName: 'Ndikumana et al. 2024' },
        { stage: 'گلدهی', icon: '🌸', crown: '۱۲ – ۱۴', age: '۳۰ – ۶۰', refId: '۴', refName: 'Ndikumana et al. 2024' },
        { stage: 'باردهی', icon: '🍓', crown: '۱۴ – ۱۷', age: '۶۰ – ۱۲۰', refId: '۴', refName: 'Ndikumana et al. 2024' },
        { stage: 'رسیدگی', icon: '🌾', crown: '> ۱۷', age: '> ۱۲۰', refId: '۴', refName: 'Ndikumana et al. 2024' }
      ],

      references: [
        {
          id: 1,
          text: ' Bottoms, T.G., Bolda, M.P., Gaskell, M.L., & Hartz, T.K. (2013). <span class="italic">Determination of Strawberry Nutrient Optimum Ranges through Diagnosis and Recommendation Integrated System Analysis</span>. HortTechnology, 23(3), 312–318. DOI: 10.21273/HORTTECH.23.3.312',
          links: [
            { label: 'مشاهده چکیده (OUCI)', url: 'https://ouci.dntb.gov.ua/en/works/7p8Bxbk7/' },
            { label: 'ResearchGate', url: 'https://www.researchgate.net/publication/286005019_Determination_of_Strawberry_Nutrient_Optimum_Ranges_through_Diagnosis_and_Recommendation_Integrated_System_Analysis' },
            { label: 'راهنمای UC Davis', url: 'http://geisseler.ucdavis.edu/Guidelines/Strawberry.html' }
          ]
        },
        {
          id: 2,
          text: ' Williams, S. & Hochmuth, B. (2024). <span class="italic">Petiole Sap Testing as a Best Management Practice in the Suwannee Valley</span>. UF/IFAS Nutrient Management Program Blog.',
          links: [
            { label: 'مشاهده متن کامل', url: 'https://blogs.ifas.ufl.edu/nmp/2024/04/08/petiole-sap-testing-as-a-best-management-practice-in-the-suwannee-valley/' }
          ]
        },
        {
          id: 3,
          text: ' Yousefi, S., Eshghi, S., & Jamali, B. (2023). <span class="italic">Evaluation of yield, biochemical characteristics and nutrient composition of \'Camarosa\' strawberry in response to different K/N ratios</span>. Journal of Berry Research, 13(2), 95–106.',
          links: [
            { label: 'مشاهده چکیده (OUCI)', url: 'https://ouci.dntb.gov.ua/en/works/4rNXMdE4/' },
            { label: 'Semantic Scholar', url: 'https://www.semanticscholar.org/paper/Evaluation-of-yield%2C-biochemical-characteristics-of-Yousefi-Eshghi/df6fdaad884a6aa499fe6432604ed83cdaa26380' }
          ]
        },
        {
          id: 4,
          text: ' Ndikumana, J.N., Lee, U., Yoo, J.H., et al. (2024). <span class="italic">Development of a deep-learning phenotyping tool for analyzing image-based strawberry phenotypes</span>. Frontiers in Plant Science, 15, 1418383. DOI: 10.3389/fpls.2024.1418383',
          links: [
            { label: 'مشاهده متن کامل', url: 'https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1418383/full' }
          ]
        },
        {
          id: 5,
          text: ' OMAFRA / Ontario Crop IPM. <span class="italic">Strawberry Nutrient Sufficiency Ranges</span>. Ontario Ministry of Agriculture, Food and Rural Affairs.',
          links: [
            { label: 'مشاهده راهنما', url: 'https://cropipm.omafra.gov.on.ca/en-ca/soil-diagnostics/plant-tissue-analysis/strawberry-nutrient-sufficiency-ranges' }
          ]
        },
        {
          id: 6,
          text: ' Gil-Marín, J.A., Zermeño-González, A., Moreno-Ibarra, L.A., Hernández-Pérez, A., Ramírez-Rodríguez, H., & Gaspar-Ramírez, O. (2025). <span class="italic">Effect of substrate water consumption and fertilization levels in the yield of strawberry (Fragaria × ananassa Duch.)</span>. Agrociencia, 59(2), 246–261. DOI: 10.47163/agrociencia.v59i2.3035',
          links: [
            { label: 'دانلود PDF (Agrociencia)', url: 'https://agrociencia-colpos.org/index.php/agrociencia/article/download/3035/2377/12111' },
            { label: 'ResearchGate', url: 'https://www.researchgate.net/publication/389712848_EFFECT_OF_SUBSTRATE_WATER_CONSUMPTION_AND_FERTILIZATION_LEVELS_IN_THE_YIELD_OF_STRAWBERRY_Fragaria_x_ananassa_Duch' }
          ]
        },
        {
          id: 7,
          text: ' UF/IFAS Extension. <span class="italic">Petiole Sap Nutrient Testing — English/Spanish Educational Videos</span>. University of Florida IFAS Extension.',
          links: [
            { label: 'مشاهده منابع آموزشی', url: 'https://urbanagnews.com/blog/news/new-english-spanish-videos-on-petiole-sap-nutrient-testing-from-university-of-florida-ifas-extension/' }
          ]
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

.italic {
  font-style: italic;
}

tbody tr:hover {
  background-color: #f9fafb;
}

a {
  transition: color 0.15s ease;
}
</style>
