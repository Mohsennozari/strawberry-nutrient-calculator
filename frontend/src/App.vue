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
            class="flex-1 py-3 px-4 text-center font-medium transition-all duration-200 min-w-[80px] flex items-center justify-center gap-2 text-sm md:text-base"
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
          <AboutTab v-if="activeTab === 'about'" />
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
import AboutTab from './components/AboutTab.vue'
import HelpTab from './components/HelpTab.vue'
import ReferencesTab from './components/ReferencesTab.vue'

// ============================================================
// آیکون‌ها (همه در یک جا)
// ============================================================

const IconLogo = `
<svg class="w-16 h-16 text-green-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 7v6l3 3" />
</svg>`

const IconCalculator = `
<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
</svg>`

const IconAlerts = `
<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
</svg>`

// ✅ NEW: آیکون About
const IconAbout = `
<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
</svg>`

const IconHelp = `
<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>`

const IconReferences = `
<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
</svg>`

export default {
  name: 'App',
  components: {
    CalculatorTab,
    AlertsTab,
    AboutTab,
    HelpTab,
    ReferencesTab
  },
  data() {
    return {
      activeTab: 'calculator',
      sharedResult: null,
      tabs: [
        { key: 'calculator', label: 'محاسبه‌گر', icon: IconCalculator },
        { key: 'alerts', label: 'هشدارها', icon: IconAlerts },
        { key: 'about', label: 'درباره محاسبات', icon: IconAbout },
        { key: 'help', label: 'راهنما', icon: IconHelp },
        { key: 'references', label: 'منابع', icon: IconReferences }
      ]
    }
  },
  methods: {
    handleResultUpdated(data) {
      this.sharedResult = data
      localStorage.setItem('strawberry_result', JSON.stringify(data))
    }
  },
  mounted() {
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
