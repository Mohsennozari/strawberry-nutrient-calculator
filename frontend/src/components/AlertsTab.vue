<template>
  <div class="bg-white rounded-b-xl shadow-lg p-6 font-vazir">

    <!-- ===== هدر ===== -->
    <div class="flex items-center justify-between mb-6 border-b border-gray-200 pb-4">
      <div>
        <h2 class="text-2xl font-bold text-gray-800">
          هشدارها و وضعیت‌ها
        </h2>
        <p class="text-sm text-gray-500 mt-1">خلاصه‌ای از وضعیت عناصر، نسبت‌ها و پارامترهای محیطی</p>
      </div>
      <!-- شمارنده وضعیت -->
      <div v-if="effectiveResult" class="flex items-center gap-2">
        <span class="px-3 py-1 rounded-full text-xs font-bold bg-green-100 text-green-700">
          {{ getHealthyCount }} سالم
        </span>
        <span v-if="getTotalAlerts > 0" class="px-3 py-1 rounded-full text-xs font-bold bg-red-100 text-red-700">
          {{ getTotalAlerts }} هشدار
        </span>
      </div>
    </div>

    <!-- ====== حالت خالی ====== -->
    <div v-if="!effectiveResult" class="text-center py-16">
      <p class="text-gray-400 text-lg">هنوز محاسبه‌ای انجام نشده است</p>
      <p class="text-sm text-gray-400 mt-1">لطفاً ابتدا در تب «محاسبه‌گر» اطلاعات را وارد کنید.</p>
    </div>

    <!-- ====== نتیجه موجود ====== -->
    <div v-else>

      <!-- ====== وضعیت کلی (کارت بزرگ) ====== -->
      <div class="mb-6 p-5 rounded-xl border-2 transition-all duration-300"
        :class="getOverallClass(effectiveResult.health_status)">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center gap-3">
            <div>
              <span class="font-bold text-lg block">{{ translateHealth(effectiveResult.health_status) }}</span>
              <span class="text-sm text-gray-600">{{ getOverallDescription(effectiveResult.health_status) }}</span>
            </div>
          </div>
          <span class="px-4 py-2 rounded-full text-sm font-bold"
            :class="getHealthBadgeClass(effectiveResult.health_status)">
            {{ translateHealth(effectiveResult.health_status) }}
          </span>
        </div>
        <!-- نوار پیشرفت وضعیت -->
        <div class="mt-3 h-1.5 w-full bg-gray-200 rounded-full overflow-hidden">
          <div class="h-full rounded-full transition-all duration-500"
            :class="getProgressClass(effectiveResult.health_status)"
            :style="{ width: getHealthProgress(effectiveResult.health_status) + '%' }">
          </div>
        </div>
      </div>

      <!-- ====== هشدارهای فعال (دسته‌بندی‌شده) ====== -->
      <div v-if="getTotalAlerts > 0" class="mb-6">
        <h3 class="font-bold text-red-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-red-500 rounded-full"></span>
          هشدارهای فعال ({{ getTotalAlerts }})
        </h3>

        <!-- هشدارهای بحرانی -->
        <div v-if="effectiveResult.alerts.critical && effectiveResult.alerts.critical.length > 0" class="mb-3">
          <h4 class="text-sm font-bold text-red-600 mb-2">بحرانی ({{ effectiveResult.alerts.critical.length }})</h4>
          <div class="space-y-2 max-h-60 overflow-y-auto pr-1">
            <div v-for="(alert, index) in effectiveResult.alerts.critical" :key="'critical-' + index"
              class="p-3 bg-red-50 border border-red-200 rounded-lg flex items-start gap-3 hover:bg-red-100 transition-colors duration-150">
              <span class="text-red-500 text-xl flex-shrink-0">!</span>
              <span class="text-sm text-red-700 leading-relaxed">{{ alert.message }}</span>
            </div>
          </div>
        </div>

        <!-- هشدارهای ملایم -->
        <div v-if="effectiveResult.alerts.warning && effectiveResult.alerts.warning.length > 0" class="mb-3">
          <h4 class="text-sm font-bold text-yellow-600 mb-2">هشدار ({{ effectiveResult.alerts.warning.length }})</h4>
          <div class="space-y-2 max-h-60 overflow-y-auto pr-1">
            <div v-for="(alert, index) in effectiveResult.alerts.warning" :key="'warning-' + index"
              class="p-3 bg-yellow-50 border border-yellow-200 rounded-lg flex items-start gap-3 hover:bg-yellow-100 transition-colors duration-150">
              <span class="text-yellow-500 text-xl flex-shrink-0">?</span>
              <span class="text-sm text-yellow-700 leading-relaxed">{{ alert.message }}</span>
            </div>
          </div>
        </div>

        <!-- اطلاع‌رسانی‌ها -->
        <div v-if="effectiveResult.alerts.info && effectiveResult.alerts.info.length > 0">
          <h4 class="text-sm font-bold text-blue-600 mb-2">اطلاع‌رسانی ({{ effectiveResult.alerts.info.length }})</h4>
          <div class="space-y-2 max-h-60 overflow-y-auto pr-1">
            <div v-for="(alert, index) in effectiveResult.alerts.info" :key="'info-' + index"
              class="p-3 bg-blue-50 border border-blue-200 rounded-lg flex items-start gap-3 hover:bg-blue-100 transition-colors duration-150">
              <span class="text-blue-500 text-xl flex-shrink-0">i</span>
              <span class="text-sm text-blue-700 leading-relaxed">{{ alert.message }}</span>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl text-center">
        <span class="text-green-700">
          هیچ هشدار فعالی وجود ندارد. همه چیز در وضعیت مطلوب است.
        </span>
      </div>

      <!-- ====== وضعیت عناصر ====== -->
      <div v-if="effectiveResult.ppm" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-blue-500 rounded-full"></span>
          وضعیت عناصر غذایی
        </h3>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
          <div v-for="(value, key) in effectiveResult.ppm" :key="key"
            class="p-3 rounded-xl border-2 text-center transition-all duration-200 hover:shadow-md"
            :class="getElementStatusClass(key, value)">
            <span class="font-bold text-sm block text-gray-700">{{ key }}</span>
            <span class="text-xl font-bold block">{{ value }}</span>
            <span class="text-xs font-medium block mt-1">{{ getElementStatus(key, value) }}</span>
          </div>
        </div>
      </div>

      <!-- ====== وضعیت نسبت‌ها ====== -->
      <div v-if="effectiveResult.ratios" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-purple-500 rounded-full"></span>
          وضعیت نسبت‌های کلیدی
        </h3>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
          <div v-for="(value, key) in effectiveResult.ratios" :key="key"
            class="p-3 rounded-xl border-2 text-center transition-all duration-200 hover:shadow-md"
            :class="getRatioStatusClass(key, value)">
            <span class="font-bold text-sm block text-gray-700">{{ key.replace('_', ':') }}</span>
            <span class="text-xl font-bold block">{{ value }}</span>
            <span class="text-xs font-medium block mt-1">{{ getRatioStatus(key, value) }}</span>
          </div>
        </div>
      </div>

      <!-- ====== وضعیت EC و pH ====== -->
      <div v-if="effectiveResult.ec_ph" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-yellow-500 rounded-full"></span>
          وضعیت EC و pH
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div v-for="(item, key) in effectiveResult.ec_ph" :key="key"
            class="p-4 rounded-xl border-2 text-center transition-all duration-200 hover:shadow-md"
            :class="getEcPhStatusClass(item.status)">
            <span class="font-bold text-sm block text-gray-700">{{ key }}</span>
            <span class="text-2xl font-bold block">{{ item.value }}</span>
            <div class="flex flex-wrap justify-center gap-2 mt-1">
              <span class="text-xs px-2 py-0.5 bg-gray-100 rounded text-gray-500">محدوده: {{ item.range }}</span>
              <span class="text-xs px-2 py-0.5 bg-green-100 rounded text-green-600">بهینه: {{ item.optimal }}</span>
            </div>
            <span class="text-xs font-bold block mt-2">{{ translateStatus(item.status) }}</span>
          </div>
        </div>
      </div>

      <!-- ====== پیش‌بینی وزن میوه ====== -->
      <div v-if="effectiveResult.fruit_weight_prediction" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-pink-500 rounded-full"></span>
          پیش‌بینی وزن میوه
        </h3>
        <div class="p-4 bg-pink-50 rounded-xl border-2 border-pink-200 text-center">
          <span class="text-3xl font-bold text-pink-700">{{ effectiveResult.fruit_weight_prediction }} گرم</span>
          <p class="text-xs text-gray-500 mt-1">بر اساس مدل غیرخطی Frontiers 2024</p>
        </div>
      </div>

      <!-- ====== دوره اعتبار ====== -->
      <div v-if="effectiveResult.validity" class="mb-6 p-4 bg-yellow-50 border-2 border-yellow-200 rounded-xl">
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h4 class="font-bold text-yellow-800">دوره اعتبار خروجی</h4>
            <p class="text-sm text-gray-700 mt-1">
              این محاسبات برای <span class="font-bold">{{ effectiveResult.validity.valid_days }} روز</span> معتبر است.
            </p>
            <p class="text-sm text-gray-600">
              تا تاریخ <span class="font-bold">{{ effectiveResult.validity.valid_until }}</span>
            </p>
            <p class="text-xs text-gray-500 mt-1">
              {{ effectiveResult.validity.recommendation }}
            </p>
          </div>
          <div class="flex flex-wrap gap-2">
            <span class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-bold">معتبر</span>
            <span class="px-3 py-1 bg-yellow-100 text-yellow-700 rounded-full text-xs font-bold">تا {{ effectiveResult.validity.valid_until }}</span>
          </div>
        </div>
      </div>

      <!-- ====== توصیه‌ها ====== -->
      <div v-if="effectiveResult.recommendations && effectiveResult.recommendations.length > 0"
        class="mt-4 p-4 bg-blue-50 border-2 border-blue-200 rounded-xl">
        <h3 class="font-bold text-blue-800 mb-2">
          توصیه‌ها
        </h3>
        <div class="space-y-2">
          <div v-for="(rec, index) in effectiveResult.recommendations" :key="index"
            class="p-3 bg-white rounded-lg border border-blue-100">
            <div class="flex items-start gap-3">
              <span class="text-blue-500 text-lg">&#9654;</span>
              <div>
                <p class="text-sm font-bold text-blue-800">{{ rec.action }}</p>
                <p class="text-sm text-blue-700">{{ rec.detail }}</p>
                <p class="text-xs text-gray-500 mt-1">روش: {{ rec.method }}</p>
                <span class="text-xs px-2 py-0.5 rounded-full mt-1 inline-block"
                  :class="rec.priority === 'high' ? 'bg-red-100 text-red-700' : rec.priority === 'medium' ? 'bg-yellow-100 text-yellow-700' : 'bg-green-100 text-green-700'">
                  {{ rec.priority === 'high' ? 'اولویت بالا' : rec.priority === 'medium' ? 'اولویت متوسط' : 'اطلاع‌رسانی' }}
                </span>
                <span v-if="rec.reference" class="text-xs text-gray-400 block mt-1">
                  منبع: {{ rec.reference }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ====== منابع علمی ====== -->
      <div v-if="effectiveResult.nutrient_sources" class="mt-6 pt-4 border-t border-gray-200">
        <h3 class="font-bold text-gray-700 mb-2">
          منابع علمی
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
          <div v-for="(source, element) in effectiveResult.nutrient_sources" :key="element"
            class="text-xs text-gray-600 p-2 bg-gray-50 rounded-lg">
            <span class="font-bold">{{ element }}</span>: {{ source.value }} ppm
            <span class="text-gray-400">({{ source.range[0] }} - {{ source.range[1] }})</span>
            <br>
            <span class="text-gray-400">{{ source.source }}</span>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: 'AlertsTab',
  props: {
    result: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      localResult: null
    }
  },
  watch: {
    result: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          console.log('AlertsTab دریافت داده:', newVal)
        }
      }
    }
  },
  mounted() {
    if (!this.result) {
      const saved = localStorage.getItem('strawberry_result')
      if (saved) {
        try {
          this.localResult = JSON.parse(saved)
          console.log('AlertsTab بازیابی از localStorage:', this.localResult)
        } catch (e) {
          console.error('خطا در بازیابی:', e)
        }
      }
    }
  },
  computed: {
    effectiveResult() {
      return this.result || this.localResult
    },
    getHealthyCount() {
      const res = this.effectiveResult
      if (!res || !res.ppm) return 0
      const ranges = {
        'N': {min: 156, max: 172},
        'P': {min: 54, max: 63},
        'K': {min: 400, max: 543},
        'Ca': {min: 244, max: 449},
        'Mg': {min: 40, max: 70},
        'S': {min: 30, max: 60},
        'Fe': {min: 1.5, max: 3.0},
        'Zn': {min: 0.3, max: 0.6},
        'Mn': {min: 0.5, max: 1.0},
        'Cu': {min: 0.1, max: 0.3},
        'B': {min: 0.2, max: 0.5},
        'Mo': {min: 0.01, max: 0.05},
        'Cl': {min: 0.5, max: 1.5}
      }
      let healthy = 0
      for (const [key, value] of Object.entries(res.ppm)) {
        const r = ranges[key]
        if (r && value >= r.min && value <= r.max) healthy++
      }
      return healthy
    },
    getTotalAlerts() {
      const res = this.effectiveResult
      if (!res || !res.alerts) return 0
      return (res.alerts.critical?.length || 0) +
             (res.alerts.warning?.length || 0) +
             (res.alerts.info?.length || 0)
    }
  },
  methods: {
    // ========== ترجمه‌ها ==========
    translateHealth(status) {
      const map = {
        'Excellent': 'عالی',
        'Good': 'خوب',
        'Needs Attention': 'نیاز به توجه',
        'Attention Required': 'نیاز به اقدام',
        'Critical': 'بحرانی'
      }
      return map[status] || status
    },
    translateStatus(status) {
      const map = { 'optimal': 'بهینه', 'acceptable': 'قابل قبول', 'low': 'کم', 'high': 'زیاد' }
      return map[status] || status
    },

    // ========== وضعیت کلی ==========
    getOverallClass(status) {
      const map = {
        'Excellent': 'border-green-300 bg-green-50/70',
        'Good': 'border-blue-300 bg-blue-50/70',
        'Needs Attention': 'border-yellow-300 bg-yellow-50/70',
        'Attention Required': 'border-orange-300 bg-orange-50/70',
        'Critical': 'border-red-300 bg-red-50/70'
      }
      return map[status] || 'border-gray-300 bg-gray-50/70'
    },
    getHealthBadgeClass(status) {
      const map = {
        'Excellent': 'bg-green-100 text-green-700',
        'Good': 'bg-blue-100 text-blue-700',
        'Needs Attention': 'bg-yellow-100 text-yellow-700',
        'Attention Required': 'bg-orange-100 text-orange-700',
        'Critical': 'bg-red-100 text-red-700'
      }
      return map[status] || 'bg-gray-100 text-gray-700'
    },
    getOverallDescription(status) {
      const map = {
        'Excellent': 'همه چیز در وضعیت مطلوب است. ادامه دهید.',
        'Good': 'وضعیت خوب است. چند مورد نیاز به پایش دارد.',
        'Needs Attention': 'چندین مورد نیاز به توجه و اقدام اصلاحی دارند.',
        'Attention Required': 'وضعیت نیاز به اقدام فوری دارد.',
        'Critical': 'وضعیت بحرانی! اقدام فوری لازم است.'
      }
      return map[status] || 'وضعیت نامشخص'
    },
    getProgressClass(status) {
      const map = {
        'Excellent': 'bg-green-500',
        'Good': 'bg-blue-500',
        'Needs Attention': 'bg-yellow-500',
        'Attention Required': 'bg-orange-500',
        'Critical': 'bg-red-500'
      }
      return map[status] || 'bg-gray-500'
    },
    getHealthProgress(status) {
      const map = {
        'Excellent': 100,
        'Good': 75,
        'Needs Attention': 45,
        'Attention Required': 30,
        'Critical': 15
      }
      return map[status] || 50
    },

    // ========== عناصر ==========
    getElementStatusClass(key, value) {
      const ranges = {
        'N': {min: 156, max: 172},
        'P': {min: 54, max: 63},
        'K': {min: 400, max: 543},
        'Ca': {min: 244, max: 449},
        'Mg': {min: 40, max: 70},
        'S': {min: 30, max: 60},
        'Fe': {min: 1.5, max: 3.0},
        'Zn': {min: 0.3, max: 0.6},
        'Mn': {min: 0.5, max: 1.0},
        'Cu': {min: 0.1, max: 0.3},
        'B': {min: 0.2, max: 0.5},
        'Mo': {min: 0.01, max: 0.05},
        'Cl': {min: 0.5, max: 1.5}
      }
      if (!ranges[key]) return 'border-gray-200 bg-gray-50'
      const r = ranges[key]
      if (value < r.min) return 'border-red-300 bg-red-50'
      if (value > r.max) return 'border-orange-300 bg-orange-50'
      return 'border-green-300 bg-green-50'
    },
    getElementStatus(key, value) {
      const ranges = {
        'N': {min: 156, max: 172},
        'P': {min: 54, max: 63},
        'K': {min: 400, max: 543},
        'Ca': {min: 244, max: 449},
        'Mg': {min: 40, max: 70},
        'S': {min: 30, max: 60},
        'Fe': {min: 1.5, max: 3.0},
        'Zn': {min: 0.3, max: 0.6},
        'Mn': {min: 0.5, max: 1.0},
        'Cu': {min: 0.1, max: 0.3},
        'B': {min: 0.2, max: 0.5},
        'Mo': {min: 0.01, max: 0.05},
        'Cl': {min: 0.5, max: 1.5}
      }
      if (!ranges[key]) return 'نامشخص'
      const r = ranges[key]
      if (value < r.min) return 'کم'
      if (value > r.max) return 'زیاد'
      return 'بهینه'
    },

    // ========== نسبت‌ها ==========
    getRatioStatusClass(key, value) {
      const ranges = {
        'K_Ca': {min: 1.2, max: 1.4},
        'K_Mg': {min: 3.0, max: 4.0},
        'Ca_Mg': {min: 2.5, max: 3.5},
        'N_K': {min: 0.3, max: 0.4},
        'K_S': {min: 8.0, max: 10.0},
        'Fe_Mn': {min: 2.0, max: 3.0},
        'B_Ca': {min: 0.001, max: 0.002}
      }
      if (!ranges[key]) return 'border-gray-200 bg-gray-50'
      const r = ranges[key]
      if (value < r.min) return 'border-red-300 bg-red-50'
      if (value > r.max) return 'border-orange-300 bg-orange-50'
      return 'border-green-300 bg-green-50'
    },
    getRatioStatus(key, value) {
      const ranges = {
        'K_Ca': {min: 1.2, max: 1.4},
        'K_Mg': {min: 3.0, max: 4.0},
        'Ca_Mg': {min: 2.5, max: 3.5},
        'N_K': {min: 0.3, max: 0.4},
        'K_S': {min: 8.0, max: 10.0},
        'Fe_Mn': {min: 2.0, max: 3.0},
        'B_Ca': {min: 0.001, max: 0.002}
      }
      if (!ranges[key]) return 'نامشخص'
      const r = ranges[key]
      if (value < r.min) return 'کم'
      if (value > r.max) return 'زیاد'
      return 'بهینه'
    },

    // ========== EC و pH ==========
    getEcPhStatusClass(status) {
      const map = {
        'optimal': 'border-green-300 bg-green-50',
        'acceptable': 'border-blue-300 bg-blue-50',
        'low': 'border-red-300 bg-red-50',
        'high': 'border-orange-300 bg-orange-50'
      }
      return map[status] || 'border-gray-300 bg-gray-50'
    }
  }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

.font-vazir {
  font-family: 'Vazir', 'Tahoma', sans-serif;
}

.max-h-60::-webkit-scrollbar {
  width: 4px;
}
.max-h-60::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 8px;
}
.max-h-60::-webkit-scrollbar-thumb {
  background: #e5e7eb;
  border-radius: 8px;
}
.max-h-60::-webkit-scrollbar-thumb:hover {
  background: #d1d5db;
}
</style>
