<template>
  <div class="bg-white rounded-xl shadow-lg p-6 font-vazir">

    <!-- ===== هدر داشبورد ===== -->
    <div class="flex items-center justify-between mb-6 border-b border-gray-200 pb-4">
      <div>
        <h2 class="text-2xl font-bold text-gray-800">داشبورد کاربری</h2>
        <p class="text-sm text-gray-500 mt-0.5">
          خوش آمدید {{ user?.username || 'کاربر' }}! در این بخش می‌توانید وضعیت خود را مشاهده کنید.
        </p>
      </div>
      <div class="flex items-center gap-2">
        <span class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-bold">
          فعال
        </span>
        <button @click="refreshData" class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold hover:bg-blue-200 transition">
          🔄 بروزرسانی
        </button>
      </div>
    </div>

    <!-- ===== کارت‌های آماری (از API) ===== -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">

      <!-- کارت ۱: تعداد محاسبات -->
      <div class="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-4 border border-blue-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-blue-600 font-medium">تعداد محاسبات</p>
            <p class="text-2xl font-bold text-blue-800">{{ stats.total || 0 }}</p>
          </div>
          <div class="w-10 h-10 bg-blue-200 rounded-full flex items-center justify-center text-blue-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- کارت ۲: آخرین وضعیت سلامت -->
      <div class="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-4 border border-green-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-green-600 font-medium">وضعیت سلامت</p>
            <p class="text-2xl font-bold text-green-800">{{ lastHealthStatus || 'نامشخص' }}</p>
          </div>
          <div class="w-10 h-10 bg-green-200 rounded-full flex items-center justify-center text-green-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- کارت ۳: مرحله رشد فعلی -->
      <div class="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-4 border border-purple-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-purple-600 font-medium">مرحله رشد</p>
            <p class="text-2xl font-bold text-purple-800">{{ lastStage || 'نامشخص' }}</p>
          </div>
          <div class="w-10 h-10 bg-purple-200 rounded-full flex items-center justify-center text-purple-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.5A4.5 4.5 0 017.5 9H6.5a4.5 4.5 0 010-9h5A4.5 4.5 0 0116 4.5v5a4.5 4.5 0 01-4.5 4.5h-5a4.5 4.5 0 010-9h.5" />
            </svg>
          </div>
        </div>
      </div>

      <!-- کارت ۴: تاریخ عضویت -->
      <div class="bg-gradient-to-br from-orange-50 to-orange-100 rounded-xl p-4 border border-orange-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-orange-600 font-medium">تاریخ عضویت</p>
            <p class="text-sm font-bold text-orange-800">{{ user?.created_at || 'نامشخص' }}</p>
          </div>
          <div class="w-10 h-10 bg-orange-200 rounded-full flex items-center justify-center text-orange-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
      </div>

    </div>

    <!-- ===== اطلاعات کاربر ===== -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">

      <!-- اطلاعات شخصی -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-blue-500 rounded-full"></span>
          اطلاعات شخصی
        </h3>
        <div class="space-y-2 text-sm">
          <div class="flex justify-between py-1.5 border-b border-gray-100">
            <span class="text-gray-500">نام کاربری</span>
            <span class="font-medium text-gray-800">{{ user?.username || '-' }}</span>
          </div>
          <div class="flex justify-between py-1.5 border-b border-gray-100">
            <span class="text-gray-500">ایمیل</span>
            <span class="font-medium text-gray-800">{{ user?.email || '-' }}</span>
          </div>
          <div class="flex justify-between py-1.5">
            <span class="text-gray-500">تاریخ عضویت</span>
            <span class="font-medium text-gray-800">{{ user?.created_at || '-' }}</span>
          </div>
        </div>
      </div>

      <!-- فعالیت‌های اخیر -->
      <div class="bg-gray-50 rounded-xl p-4 border border-gray-200">
        <h3 class="font-bold text-gray-700 mb-3 flex items-center gap-2">
          <span class="inline-block w-1.5 h-5 bg-green-500 rounded-full"></span>
          آخرین محاسبات
        </h3>
        <div v-if="calculations.length > 0" class="space-y-2 max-h-60 overflow-y-auto">
          <div v-for="(calc, index) in calculations" :key="index"
               class="flex items-center justify-between py-2 px-3 bg-white rounded-lg border border-gray-100 hover:border-green-200 transition">
            <div>
              <span class="text-sm font-medium text-gray-800">{{ calc.stage || 'نامشخص' }}</span>
              <span class="text-xs text-gray-500 block">{{ calc.created_at }}</span>
            </div>
            <span class="px-2 py-1 rounded-full text-xs font-bold"
                  :class="getHealthClass(calc.health_status)">
              {{ calc.health_status || 'نامشخص' }}
            </span>
          </div>
        </div>
        <div v-else class="text-sm text-gray-500 text-center py-4">
          هیچ محاسبه‌ای ثبت نشده است.
          <br>
          <button @click="goToCalculator" class="text-green-600 hover:underline mt-1">
            اولین محاسبه را انجام دهید
          </button>
        </div>
      </div>

    </div>

    <!-- ===== اقدامات سریع ===== -->
    <div class="bg-blue-50 rounded-xl p-4 border border-blue-200">
      <h3 class="font-bold text-blue-800 mb-3">اقدامات سریع</h3>
      <div class="flex flex-wrap gap-3">
        <button @click="goToCalculator"
                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm transition">
          محاسبه جدید
        </button>
        <button @click="goToAlerts"
                class="px-4 py-2 bg-yellow-600 hover:bg-yellow-700 text-white rounded-lg text-sm transition">
          مشاهده هشدارها
        </button>
        <button @click="refreshData"
                class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg text-sm transition">
          بروزرسانی
        </button>
      </div>
    </div>

  </div>
</template>

<script>
import { getUser } from '../services/auth'
import { getCalculations, getCalculationStats } from '../services/api'

export default {
  name: 'DashboardTab',
  data() {
    return {
      user: null,
      stats: {
        total: 0,
        health_statuses: {},
        last_calculation: null
      },
      calculations: [],
      lastHealthStatus: null,
      lastStage: null,
      loading: false
    }
  },
  mounted() {
    this.loadUserData()
    this.loadData()
  },
  methods: {
    loadUserData() {
      this.user = getUser()
    },
    async loadData() {
      this.loading = true
      try {
        // دریافت آمار
        const statsData = await getCalculationStats()
        this.stats = statsData

        // دریافت تاریخچه محاسبات
        const calcData = await getCalculations(10)
        this.calculations = calcData.calculations || []

        // تنظیم آخرین وضعیت
        if (this.calculations.length > 0) {
          const last = this.calculations[0]
          this.lastHealthStatus = last.health_status
          this.lastStage = last.stage
        }
      } catch (error) {
        console.error('خطا در بارگذاری داده‌ها:', error)
      } finally {
        this.loading = false
      }
    },
    refreshData() {
      this.loadData()
    },
    getHealthClass(status) {
      const map = {
        'Excellent': 'bg-green-100 text-green-700',
        'Good': 'bg-blue-100 text-blue-700',
        'Needs Attention': 'bg-yellow-100 text-yellow-700',
        'Attention Required': 'bg-orange-100 text-orange-700',
        'Critical': 'bg-red-100 text-red-700'
      }
      return map[status] || 'bg-gray-100 text-gray-700'
    },
    goToCalculator() {
      this.$emit('navigate', 'calculator')
    },
    goToAlerts() {
      this.$emit('navigate', 'alerts')
    }
  }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

.font-vazir {
  font-family: 'Vazir', 'Tahoma', sans-serif;
}

.max-h-60 {
  max-height: 240px;
}

.max-h-60::-webkit-scrollbar {
  width: 4px;
}
.max-h-60::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 8px;
}
.max-h-60::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 8px;
}
.max-h-60::-webkit-scrollbar-thumb:hover {
  background: #9ca3af;
}
</style>
