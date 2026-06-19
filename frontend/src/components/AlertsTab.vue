<template>
  <div class="bg-white rounded-b-xl shadow-lg p-6 font-vazir">

    <!-- هدر -->
    <div class="flex items-center justify-between mb-6 border-b border-gray-200 pb-4">
      <div>
        <h2 class="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <svg class="w-7 h-7 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
          هشدارها و وضعیت‌ها
        </h2>
        <p class="text-sm text-gray-500 mt-1">خلاصه‌ای از وضعیت عناصر، نسبت‌ها و پارامترهای محیطی</p>
      </div>
      <!-- شمارنده وضعیت -->
      <div v-if="result" class="flex items-center gap-2">
        <span class="px-3 py-1 rounded-full text-xs font-bold bg-green-100 text-green-700">
          ✅ {{ getHealthyCount }} سالم
        </span>
        <span v-if="result.alerts && result.alerts.length > 0" class="px-3 py-1 rounded-full text-xs font-bold bg-red-100 text-red-700">
          ⚠️ {{ result.alerts.length }} هشدار
        </span>
      </div>
    </div>

    <!-- ====== حالت خالی ====== -->
    <div v-if="!result" class="text-center py-16">
      <svg class="w-20 h-20 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <p class="text-gray-400 text-lg">هنوز محاسبه‌ای انجام نشده است</p>
      <p class="text-sm text-gray-400 mt-1">لطفاً ابتدا در تب «محاسبه‌گر» اطلاعات را وارد کنید.</p>
    </div>

    <!-- ====== نتیجه موجود ====== -->
    <div v-else>

      <!-- ====== وضعیت کلی (کارت بزرگ) ====== -->
      <div class="mb-6 p-5 rounded-xl border-2 transition-all duration-300"
        :class="getOverallClass(result.health_status)">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center gap-3">
            <span class="text-3xl">{{ getOverallIcon(result.health_status) }}</span>
            <div>
              <span class="font-bold text-lg block">{{ translateHealth(result.health_status) }}</span>
              <span class="text-sm text-gray-600">{{ getOverallDescription(result.health_status) }}</span>
            </div>
          </div>
          <span class="px-4 py-2 rounded-full text-sm font-bold"
            :class="getHealthBadgeClass(result.health_status)">
            {{ translateHealth(result.health_status) }}
          </span>
        </div>
        <!-- نوار پیشرفت وضعیت -->
        <div class="mt-3 h-1.5 w-full bg-gray-200 rounded-full overflow-hidden">
          <div class="h-full rounded-full transition-all duration-500"
            :class="getProgressClass(result.health_status)"
            :style="{ width: getHealthProgress(result.health_status) + '%' }">
          </div>
        </div>
      </div>

      <!-- ====== هشدارهای فعال ====== -->
      <div v-if="result.alerts && result.alerts.length > 0" class="mb-6">
        <h3 class="font-bold text-red-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-red-500 rounded-full"></span>
          هشدارهای فعال ({{ result.alerts.length }})
        </h3>
        <div class="space-y-2 max-h-60 overflow-y-auto pr-1">
          <div v-for="(alert, index) in result.alerts" :key="index"
            class="p-3 bg-red-50 border border-red-200 rounded-lg flex items-start gap-3 hover:bg-red-100 transition-colors duration-150">
            <span class="text-red-500 text-xl flex-shrink-0">⚠️</span>
            <span class="text-sm text-red-700 leading-relaxed">{{ alert }}</span>
          </div>
        </div>
      </div>
      <div v-else class="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl text-center">
        <span class="text-green-700 flex items-center justify-center gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          هیچ هشدار فعالی وجود ندارد. همه چیز در وضعیت مطلوب است.
        </span>
      </div>

      <!-- ====== وضعیت عناصر ====== -->
      <div v-if="result.ppm" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-blue-500 rounded-full"></span>
          وضعیت عناصر غذایی
        </h3>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
          <div v-for="(value, key) in result.ppm" :key="key"
            class="p-3 rounded-xl border-2 text-center transition-all duration-200 hover:shadow-md"
            :class="getElementStatusClass(key, value)">
            <span class="font-bold text-sm block text-gray-700">{{ key }}</span>
            <span class="text-xl font-bold block">{{ value }}</span>
            <span class="text-xs font-medium block mt-1">{{ getElementStatus(key, value) }}</span>
          </div>
        </div>
      </div>

      <!-- ====== وضعیت نسبت‌ها ====== -->
      <div v-if="result.ratios" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-purple-500 rounded-full"></span>
          وضعیت نسبت‌های کلیدی
        </h3>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
          <div v-for="(value, key) in result.ratios" :key="key"
            class="p-3 rounded-xl border-2 text-center transition-all duration-200 hover:shadow-md"
            :class="getRatioStatusClass(key, value)">
            <span class="font-bold text-sm block text-gray-700">{{ key.replace('_', ':') }}</span>
            <span class="text-xl font-bold block">{{ value }}</span>
            <span class="text-xs font-medium block mt-1">{{ getRatioStatus(key, value) }}</span>
          </div>
        </div>
      </div>

      <!-- ====== وضعیت EC و pH ====== -->
      <div v-if="result.ec_ph" class="mb-6">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-yellow-500 rounded-full"></span>
          وضعیت EC و pH
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div v-for="(item, key) in result.ec_ph" :key="key"
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

      <!-- ====== توصیه‌ها ====== -->
      <div v-if="result.recommendations && result.recommendations.length > 0"
        class="mt-4 p-4 bg-blue-50 border-2 border-blue-200 rounded-xl">
        <h3 class="font-bold text-blue-800 mb-2 flex items-center gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
          </svg>
          توصیه‌ها
        </h3>
        <ul class="space-y-1.5">
          <li v-for="rec in result.recommendations" :key="rec"
            class="text-sm text-blue-700 flex items-start gap-2">
            <span class="text-blue-400">▸</span>
            {{ rec }}
          </li>
        </ul>
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
  computed: {
    getHealthyCount() {
      if (!this.result || !this.result.ppm) return 0
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
      for (const [key, value] of Object.entries(this.result.ppm)) {
        const r = ranges[key]
        if (r && value >= r.min && value <= r.max) healthy++
      }
      return healthy
    }
  },
  methods: {
    // ========== ترجمه‌ها ==========
    translateHealth(status) {
      const map = { 'Excellent': 'عالی', 'Good': 'خوب', 'Needs Attention': 'نیاز به توجه', 'Critical': 'بحرانی' }
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
        'Critical': 'border-red-300 bg-red-50/70'
      }
      return map[status] || 'border-gray-300 bg-gray-50/70'
    },
    getOverallIcon(status) {
      const map = { 'Excellent': '✅', 'Good': '👍', 'Needs Attention': '⚠️', 'Critical': '🚨' }
      return map[status] || '📊'
    },
    getHealthBadgeClass(status) {
      const map = {
        'Excellent': 'bg-green-100 text-green-700',
        'Good': 'bg-blue-100 text-blue-700',
        'Needs Attention': 'bg-yellow-100 text-yellow-700',
        'Critical': 'bg-red-100 text-red-700'
      }
      return map[status] || 'bg-gray-100 text-gray-700'
    },
    getOverallDescription(status) {
      const map = {
        'Excellent': 'همه چیز در وضعیت مطلوب است. ادامه دهید.',
        'Good': 'وضعیت خوب است. چند مورد نیاز به پایش دارد.',
        'Needs Attention': 'چندین مورد نیاز به توجه و اقدام اصلاحی دارند.',
        'Critical': 'وضعیت بحرانی! اقدام فوری لازم است.'
      }
      return map[status] || 'وضعیت نامشخص'
    },
    getProgressClass(status) {
      const map = {
        'Excellent': 'bg-green-500',
        'Good': 'bg-blue-500',
        'Needs Attention': 'bg-yellow-500',
        'Critical': 'bg-red-500'
      }
      return map[status] || 'bg-gray-500'
    },
    getHealthProgress(status) {
      const map = { 'Excellent': 100, 'Good': 75, 'Needs Attention': 45, 'Critical': 20 }
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
      if (value < r.min) return '🔴 کم'
      if (value > r.max) return '🟠 زیاد'
      return '🟢 بهینه'
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
      if (value < r.min) return '🔴 کم'
      if (value > r.max) return '🟠 زیاد'
      return '🟢 بهینه'
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

/* اسکرول‌بار سفارشی برای بخش هشدارها */
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
