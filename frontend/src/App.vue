<template>
  <div dir="rtl" class="min-h-screen bg-gradient-to-br from-green-50 to-emerald-100 p-4 font-vazir flex items-center justify-center">
    <div class="max-w-6xl w-full mx-auto">

      <!-- کارت اصلی -->
      <div class="bg-white rounded-2xl shadow-2xl overflow-hidden border border-green-100">

        <!-- هدر داخل کارت با لوگو -->
        <div class="bg-gradient-to-r from-green-700 to-emerald-600 px-8 py-6 text-center">
          <div class="flex justify-center mb-3" v-html="IconLogo"></div>
          <h1 class="text-3xl font-bold text-white">سیستم تغذیه توت‌فرنگی</h1>
          <p class="text-green-100 mt-2 text-sm md:text-base">ماشین‌حساب تغذیه بر اساس فیزیولوژی برای توت‌فرنگی‌های هیدروپونیک</p>
        </div>

        <!-- نوار تب‌ها -->
        <div class="flex flex-wrap border-b border-gray-200 bg-gray-50">
          <button
            v-for="tab in tabs"
            :key="tab.key"
            @click="activeTab = tab.key"
            class="flex-1 py-3 px-4 text-center font-medium transition-all duration-200 min-w-[100px] flex items-center justify-center gap-2 text-sm md:text-base"
            :class="activeTab === tab.key ? 'bg-green-600 text-white shadow-md' : 'text-gray-700 hover:bg-gray-100'"
          >
            <span v-html="tab.icon"></span>
            {{ tab.label }}
          </button>
        </div>

        <!-- محتوای تب -->
        <div class="p-6 bg-white">
          <CalculatorTab
            v-if="activeTab === 'calculator'"
            @result-updated="handleResultUpdated"
          />
          <AlertsTab
            v-if="activeTab === 'alerts'"
            :result="sharedResult"
          />
          <HelpTab v-if="activeTab === 'help'" />
          <ReferencesTab v-if="activeTab === 'references'" />
        </div>

        <!-- فوتر کارت -->
        <div class="bg-gray-50 px-6 py-3 border-t border-gray-200 text-center text-xs text-gray-500">
          نسخه ۱.۰ | مبتنی بر فیزیولوژی گیاهی
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import CalculatorTab from './components/CalculatorTab.vue'
import AlertsTab from './components/AlertsTab.vue'
import HelpTab from './components/HelpTab.vue'
import ReferencesTab from './components/ReferencesTab.vue'

// ============================================================
// Import icons from centralized file
// ============================================================
import {
  IconLogo,
  IconCalculator,
  IconAlerts,
  IconHelp,
  IconReferences
} from './icons'

export default {
  name: 'App',
  components: {
    CalculatorTab,
    AlertsTab,
    HelpTab,
    ReferencesTab
  },
  data() {
    return {
      activeTab: 'calculator',
      sharedResult: null,
      tabs: [
        { key: 'calculator', label: 'ماشین‌حساب', icon: IconCalculator },
        { key: 'alerts', label: 'هشدارها', icon: IconAlerts },
        { key: 'help', label: 'راهنما', icon: IconHelp },
        { key: 'references', label: 'منابع', icon: IconReferences }
      ]
    }
  },
  methods: {
    handleResultUpdated(data) {
      this.sharedResult = data
      // ذخیره در localStorage برای ماندگاری
      localStorage.setItem('strawberry_result', JSON.stringify(data))
    }
  },
  mounted() {
    // بازیابی داده از localStorage در صورت موجود بودن
    const saved = localStorage.getItem('strawberry_result')
    if (saved) {
      try {
        this.sharedResult = JSON.parse(saved)
      } catch (e) {
        console.error('خطا در بازیابی داده:', e)
      }
    }
  }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

.font-vazir {
  font-family: 'Vazir', 'Tahoma', sans-serif;
}

button {
  position: relative;
  overflow: hidden;
}

button::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 3px;
  background: #16a34a;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

button:hover::after {
  width: 80%;
}

@media (max-width: 640px) {
  .p-6 {
    padding: 1rem;
  }
  .px-8 {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}
</style>
