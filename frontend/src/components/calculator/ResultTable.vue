<template>
  <div v-if="result" class="bg-white rounded-xl shadow-lg p-6 overflow-x-auto">

    <!-- هدر -->
    <div class="flex items-center justify-between mb-4 flex-wrap gap-2">
      <div>
        <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
          <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
          </svg>
          نتیجه تحلیل تغذیه‌ای
        </h2>
        <div class="flex items-center gap-3 mt-1 text-sm text-gray-600">
          <span>🌱 مرحله: {{ translateStage(result.stage) }}</span>
          <span class="px-2 py-0.5 rounded-full text-xs font-bold" :class="statusClass">
            {{ translateHealth(result.health_status) }}
          </span>
        </div>
      </div>
      <div class="flex gap-2">
        <button @click="$emit('copy')" class="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 text-gray-700 text-sm rounded-lg transition-colors flex items-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
          کپی
        </button>
        <button @click="$emit('download')" class="px-3 py-1.5 bg-blue-100 hover:bg-blue-200 text-blue-700 text-sm rounded-lg transition-colors flex items-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          خروجی CSV
        </button>
      </div>
    </div>

    <!-- جدول -->
    <table class="w-full border-collapse text-sm" id="result-table">
      <thead>
        <tr class="bg-green-100">
          <th class="border border-gray-300 px-3 py-2 text-center">دسته</th>
          <th class="border border-gray-300 px-3 py-2 text-center">عنصر</th>
          <th class="border border-gray-300 px-3 py-2 text-center">مقدار (ppm)</th>
          <th class="border border-gray-300 px-3 py-2 text-center">وضعیت</th>
          <th class="border border-gray-300 px-3 py-2 text-center">محدوده بهینه (ppm)</th>
          <th class="border border-gray-300 px-3 py-2 text-center">نسبت</th>
          <th class="border border-gray-300 px-3 py-2 text-center">مقدار نسبت</th>
        </tr>
      </thead>
      <tbody>
        <!-- ماکروها -->
        <tr v-for="(item, index) in macroElements" :key="item.key" class="hover:bg-gray-50">
          <td class="border border-gray-300 px-3 py-2 text-center font-bold text-gray-600">{{ index === 0 ? 'ماکرو' : '' }}</td>
          <td class="border border-gray-300 px-3 py-2 font-bold text-center">{{ item.key }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-mono">{{ item.value }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center">
            <span class="px-2 py-0.5 rounded-full text-xs font-bold" :class="getStatusBadgeClass(item.status)">{{ item.status }}</span>
          </td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500">{{ item.range }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500">{{ item.ratioLabel || '-' }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-mono text-sm" :class="getRatioColorClass(item.ratioKey, item.ratioValue)">
            {{ item.ratioValue !== undefined ? item.ratioValue : '-' }}
          </td>
        </tr>

        <!-- میکروها -->
        <tr v-for="(item, index) in microElements" :key="item.key" class="hover:bg-gray-50">
          <td class="border border-gray-300 px-3 py-2 text-center font-bold text-gray-600">{{ index === 0 ? 'میکرو' : '' }}</td>
          <td class="border border-gray-300 px-3 py-2 font-bold text-center">{{ item.key }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-mono">{{ item.value }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center">
            <span class="px-2 py-0.5 rounded-full text-xs font-bold" :class="getStatusBadgeClass(item.status)">{{ item.status }}</span>
          </td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500">{{ item.range }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500">{{ item.ratioLabel || '-' }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-mono text-sm">{{ item.ratioValue !== undefined ? item.ratioValue : '-' }}</td>
        </tr>

        <!-- EC و pH -->
        <tr class="bg-blue-50">
          <td class="border border-gray-300 px-3 py-2 text-center font-bold text-gray-600">محیطی</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-bold">EC / pH</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-mono" colspan="2">EC: {{ result.ec_ph.EC.value }} dS/m | pH: {{ result.ec_ph.pH.value }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500">EC: {{ result.ec_ph.EC.optimal }}<br>pH: {{ result.ec_ph.pH.optimal }}</td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500" colspan="2">
            <span class="px-2 py-0.5 rounded-full text-xs font-bold" :class="getEcPhStatusClass(result.ec_ph.EC.status)">EC: {{ translateStatus(result.ec_ph.EC.status) }}</span>
            <span class="px-2 py-0.5 rounded-full text-xs font-bold" :class="getEcPhStatusClass(result.ec_ph.pH.status)">pH: {{ translateStatus(result.ec_ph.pH.status) }}</span>
          </td>
        </tr>

        <!-- وزن میوه -->
        <tr class="bg-gray-50">
          <td class="border border-gray-300 px-3 py-2 text-center font-bold text-gray-600">پیش‌بینی</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-bold">وزن میوه</td>
          <td class="border border-gray-300 px-3 py-2 text-center font-bold text-green-700" colspan="2">{{ result.fruit_weight_prediction }} گرم</td>
          <td class="border border-gray-300 px-3 py-2 text-center text-xs text-gray-500" colspan="3">R² = 0.92 (Frontiers 2024)</td>
        </tr>
      </tbody>
    </table>

    <div class="mt-4 p-3 bg-blue-50 rounded-lg border border-blue-200 text-center">
      <p class="text-sm text-blue-700">📊 برای مشاهده <span class="font-bold">جزئیات هشدارها و توصیه‌ها</span>، به تب <span class="font-bold">«هشدارها»</span> مراجعه کنید.</p>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ResultTable',
  props: { result: { type: Object, required: true } },
  computed: {
    statusClass() {
      const map = { 'Excellent': 'bg-green-100 text-green-700', 'Good': 'bg-blue-100 text-blue-700', 'Needs Attention': 'bg-yellow-100 text-yellow-700', 'Critical': 'bg-red-100 text-red-700' }
      return map[this.result.health_status] || 'bg-gray-100 text-gray-700'
    },
    macroElements() {
      const ppm = this.result.ppm, ratios = this.result.ratios || {}
      const macroKeys = ['N', 'P', 'K', 'Ca', 'Mg', 'S']
      const ranges = { 'N': {min: 156, max: 172}, 'P': {min: 54, max: 63}, 'K': {min: 400, max: 543}, 'Ca': {min: 244, max: 449}, 'Mg': {min: 40, max: 70}, 'S': {min: 30, max: 60} }
      const ratioMap = { 'K': {label: 'K:Ca', key: 'K_Ca'}, 'Ca': {label: 'K:Ca', key: 'K_Ca'}, 'Mg': {label: 'K:Mg', key: 'K_Mg'} }
      return macroKeys.map(key => {
        const value = ppm[key] || 0, range = ranges[key]
        let status = 'نامشخص'
        if (range) { if (value < range.min) status = 'کم'; else if (value > range.max) status = 'زیاد'; else status = 'بهینه' }
        const ratioInfo = ratioMap[key]
        let ratioValue, ratioLabel
        if (ratioInfo && ratios[ratioInfo.key] !== undefined) { ratioValue = ratios[ratioInfo.key]; ratioLabel = ratioInfo.label }
        return { key, value: value.toFixed(2), status, range: range ? `${range.min} - ${range.max}` : '-', ratioLabel, ratioKey: ratioInfo ? ratioInfo.key : null, ratioValue }
      })
    },
    microElements() {
      const ppm = this.result.ppm, ratios = this.result.ratios || {}
      const microKeys = ['Fe', 'Zn', 'Mn', 'Cu', 'B', 'Mo', 'Cl']
      const ranges = { 'Fe': {min: 1.5, max: 3.0}, 'Zn': {min: 0.3, max: 0.6}, 'Mn': {min: 0.5, max: 1.0}, 'Cu': {min: 0.1, max: 0.3}, 'B': {min: 0.2, max: 0.5}, 'Mo': {min: 0.01, max: 0.05}, 'Cl': {min: 0.5, max: 1.5} }
      const ratioMap = { 'Fe': {label: 'Fe:Mn', key: 'Fe_Mn'}, 'Mn': {label: 'Fe:Mn', key: 'Fe_Mn'}, 'B': {label: 'B:Ca', key: 'B_Ca'} }
      return microKeys.map(key => {
        const value = ppm[key] || 0, range = ranges[key]
        let status = 'نامشخص'
        if (range) { if (value < range.min) status = 'کم'; else if (value > range.max) status = 'زیاد'; else status = 'بهینه' }
        const ratioInfo = ratioMap[key]
        let ratioValue, ratioLabel
        if (ratioInfo && ratios[ratioInfo.key] !== undefined) { ratioValue = ratios[ratioInfo.key]; ratioLabel = ratioInfo.label }
        return { key, value: value.toFixed(2), status, range: range ? `${range.min} - ${range.max}` : '-', ratioLabel, ratioKey: ratioInfo ? ratioInfo.key : null, ratioValue }
      })
    }
  },
  methods: {
    translateStage(stage) { const map = { 'vegetative': 'رویشی', 'flowering': 'گلدهی', 'fruiting': 'باردهی', 'maturity': 'رسیدگی' }; return map[stage] || stage },
    translateHealth(status) { const map = { 'Excellent': 'عالی', 'Good': 'خوب', 'Needs Attention': 'نیاز به توجه', 'Critical': 'بحرانی' }; return map[status] || status },
    translateStatus(status) { const map = { 'optimal': 'بهینه', 'acceptable': 'قابل قبول', 'low': 'کم', 'high': 'زیاد' }; return map[status] || status },
    getStatusBadgeClass(status) { const map = { 'بهینه': 'bg-green-100 text-green-700', 'کم': 'bg-red-100 text-red-700', 'زیاد': 'bg-orange-100 text-orange-700', 'نامشخص': 'bg-gray-100 text-gray-500' }; return map[status] || 'bg-gray-100 text-gray-500' },
    getRatioColorClass(key, value) {
      if (!key || value === undefined) return 'text-gray-500'
      const ranges = { 'K_Ca': {min: 1.2, max: 1.4}, 'K_Mg': {min: 3.0, max: 4.0}, 'Ca_Mg': {min: 2.5, max: 3.5}, 'N_K': {min: 0.3, max: 0.4}, 'K_S': {min: 8.0, max: 10.0}, 'Fe_Mn': {min: 2.0, max: 3.0}, 'B_Ca': {min: 0.001, max: 0.002} }
      const range = ranges[key]
      if (!range) return 'text-gray-700'
      if (value < range.min) return 'text-red-600 font-bold'
      if (value > range.max) return 'text-orange-600 font-bold'
      return 'text-green-600 font-bold'
    },
    getEcPhStatusClass(status) { const map = { 'optimal': 'bg-green-100 text-green-700', 'acceptable': 'bg-blue-100 text-blue-700', 'low': 'bg-red-100 text-red-700', 'high': 'bg-orange-100 text-orange-700' }; return map[status] || 'bg-gray-100 text-gray-500' }
  }
}
</script>
