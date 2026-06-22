<template>
  <div v-if="result" class="mt-6">

    <!-- ===== کارت دوره اعتبار ===== -->
    <div v-if="result.validity" class="mb-6 p-4 bg-yellow-50 border-2 border-yellow-200 rounded-xl">
      <div class="flex items-start gap-3">
        <span class="text-2xl flex-shrink-0">⏰</span>
        <div class="w-full">
          <h4 class="font-bold text-yellow-800">دوره اعتبار خروجی</h4>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mt-2">
            <div class="bg-white rounded-lg p-2 text-center border border-yellow-100">
              <span class="text-xs text-gray-500">تاریخ محاسبه</span>
              <p class="text-sm font-bold text-gray-700">{{ result.validity.valid_from }}</p>
            </div>
            <div class="bg-white rounded-lg p-2 text-center border border-yellow-100">
              <span class="text-xs text-gray-500">معتبر تا</span>
              <p class="text-sm font-bold text-green-700">{{ result.validity.valid_until }}</p>
            </div>
            <div class="bg-white rounded-lg p-2 text-center border border-yellow-100">
              <span class="text-xs text-gray-500">دوره اعتبار</span>
              <p class="text-sm font-bold text-blue-700">{{ result.validity.valid_days }} روز</p>
            </div>
          </div>
          <p class="text-sm text-gray-600 mt-2">
            💡 {{ result.validity.recommendation }}
          </p>
          <p class="text-xs text-gray-500 mt-1">
            📌 {{ result.validity.note }}
          </p>
          <div class="mt-2 flex flex-wrap gap-2">
            <span class="px-2 py-1 bg-green-100 text-green-700 rounded-full text-xs">✅ معتبر</span>
            <span class="px-2 py-1 bg-yellow-100 text-yellow-700 rounded-full text-xs">⏳ تا {{ result.validity.valid_until }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ===== جدول نتایج ===== -->
    <div class="bg-white rounded-xl shadow-lg overflow-hidden border border-gray-200">
      <table id="result-table" class="w-full text-sm border-collapse">
        <thead>
          <tr class="bg-green-50">
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">عنصر</th>
            <th class="border border-gray-200 px-4 py-2.5 text-center font-bold text-gray-700">مقدار (ppm)</th>
            <th class="border border-gray-200 px-4 py-2.5 text-center font-bold text-gray-700">وضعیت</th>
            <th class="border border-gray-200 px-4 py-2.5 text-center font-bold text-gray-700">محدوده بهینه</th>
            <th class="border border-gray-200 px-4 py-2.5 text-right font-bold text-gray-700">منبع</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key) in result.ppm" :key="key" class="hover:bg-gray-50 transition-colors duration-150">
            <td class="border border-gray-200 px-4 py-2.5 font-bold text-gray-800">{{ key }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-center font-mono font-medium text-gray-700">{{ value }}</td>
            <td class="border border-gray-200 px-4 py-2.5 text-center">
              <span :class="getStatusClass(key, value)" class="px-3 py-1 rounded-full text-xs font-bold">
                {{ getStatusText(key, value) }}
              </span>
            </td>
            <td class="border border-gray-200 px-4 py-2.5 text-center text-xs text-gray-600">
              {{ getRange(key) }}
            </td>
            <td class="border border-gray-200 px-4 py-2.5 text-xs text-gray-500">
              {{ getSource(key) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ===== دکمه‌های عملیات ===== -->
    <div class="flex flex-wrap gap-3 mt-4">
      <button @click="$emit('copy')" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors duration-200 flex items-center gap-2 text-sm">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
        </svg>
        کپی جدول
      </button>
      <button @click="$emit('download')" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors duration-200 flex items-center gap-2 text-sm">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
        </svg>
        دانلود CSV
      </button>

      <!-- دکمه ذخیره -->
      <button @click="saveCalculation"
              :disabled="saving"
              class="px-4 py-2 bg-purple-600 hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg transition-colors duration-200 flex items-center gap-2 text-sm">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
        </svg>
        {{ saving ? 'در حال ذخیره...' : 'ذخیره در حساب کاربری' }}
      </button>

      <!-- پیام ذخیره‌سازی -->
      <span v-if="saveMessage" class="flex items-center text-sm" :class="saveMessageType === 'success' ? 'text-green-600' : 'text-red-600'">
        {{ saveMessage }}
      </span>
    </div>

  </div>
</template>

<script>
import { saveCalculation as saveCalculationApi } from '../../services/api'
import { getToken } from '../../services/auth'

export default {
  name: 'ResultTable',
  props: {
    result: {
      type: Object,
      required: true
    },
    inputData: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      saving: false,
      saveMessage: '',
      saveMessageType: 'success'
    }
  },
  computed: {
    isTokenValid() {
      return !!getToken()
    }
  },
  methods: {
    getStatusClass(key, value) {
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
      if (!ranges[key]) return 'bg-gray-100 text-gray-600'
      const r = ranges[key]
      if (value < r.min) return 'bg-red-100 text-red-700'
      if (value > r.max) return 'bg-orange-100 text-orange-700'
      return 'bg-green-100 text-green-700'
    },
    getStatusText(key, value) {
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
    getRange(key) {
      const ranges = {
        'N': '۱۵۶ - ۱۷۲',
        'P': '۵۴ - ۶۳',
        'K': '۴۰۰ - ۵۴۳',
        'Ca': '۲۴۴ - ۴۴۹',
        'Mg': '۴۰ - ۷۰',
        'S': '۳۰ - ۶۰',
        'Fe': '۱.۵ - ۳.۰',
        'Zn': '۰.۳ - ۰.۶',
        'Mn': '۰.۵ - ۱.۰',
        'Cu': '۰.۱ - ۰.۳',
        'B': '۰.۲ - ۰.۵',
        'Mo': '۰.۰۱ - ۰.۰۵',
        'Cl': '۰.۵ - ۱.۵'
      }
      return ranges[key] || 'نامشخص'
    },
    getSource(key) {
      if (!this.result.nutrient_sources || !this.result.nutrient_sources[key]) {
        return 'نامشخص'
      }
      return this.result.nutrient_sources[key].source
    },

    // ===== ذخیره محاسبه =====
    async saveCalculation() {
      if (this.saving) return

      if (!this.isTokenValid) {
        this.saveMessage = '❌ لطفاً ابتدا وارد حساب کاربری خود شوید.'
        this.saveMessageType = 'error'
        setTimeout(() => { this.saveMessage = '' }, 5000)
        return
      }

      this.saving = true
      this.saveMessage = ''

      try {
        const inputData = this.inputData || {}

        if (!this.result || !this.result.stage) {
          throw new Error('داده‌های محاسبه کامل نیستند.')
        }

        await saveCalculationApi(this.result, inputData)

        this.saveMessage = '✅ محاسبه با موفقیت ذخیره شد!'
        this.saveMessageType = 'success'

        setTimeout(() => {
          this.saveMessage = ''
        }, 5000)

      } catch (error) {
        console.error('❌ خطا در ذخیره:', error)

        let errorMessage = 'خطا در ذخیره محاسبه. '
        if (error.response?.status === 401) {
          errorMessage += 'توکن منقضی شده است. لطفاً دوباره وارد شوید.'
        } else if (error.response?.data?.error) {
          errorMessage += error.response.data.error
        } else if (error.message) {
          errorMessage += error.message
        } else {
          errorMessage += 'دوباره تلاش کنید.'
        }

        this.saveMessage = `❌ ${errorMessage}`
        this.saveMessageType = 'error'

        setTimeout(() => {
          this.saveMessage = ''
        }, 8000)
      } finally {
        this.saving = false
      }
    }
  }
}
</script>
