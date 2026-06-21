<template>
  <div dir="rtl" class="min-h-screen">

    <!-- ============================================================ -->
    <!-- صفحه احراز هویت (اگر لاگین نکرده باشد) -->
    <!-- ============================================================ -->
    <AuthView v-if="!isAuthenticated" @authenticated="onAuthenticated" />

    <!-- ============================================================ -->
    <!-- صفحه اصلی (اگر لاگین کرده باشد) -->
    <!-- ============================================================ -->
    <div v-else class="min-h-screen bg-gradient-to-br from-green-50 via-emerald-50 to-teal-50 p-4 font-vazir flex items-center justify-center">
      <div class="max-w-6xl w-full mx-auto">

        <!-- کارت اصلی با سایه و حاشیه زیبا -->
        <div class="bg-white/95 backdrop-blur-sm rounded-3xl shadow-2xl overflow-hidden border border-green-100/50">

          <!-- هدر با طراحی مدرن -->
          <div class="relative bg-gradient-to-r from-green-800 via-green-700 to-emerald-600 px-8 py-8 text-center overflow-hidden">
            <!-- افکت پس‌زمینه -->
            <div class="absolute inset-0 opacity-10">
              <svg class="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
                <path d="M0,0 Q25,50 50,20 T100,40 L100,100 L0,100 Z" fill="white"/>
                <path d="M0,40 Q30,80 60,30 T100,70 L100,100 L0,100 Z" fill="white" opacity="0.5"/>
              </svg>
            </div>

            <div class="relative z-10">
              <div class="flex justify-center mb-4" v-html="IconLogo"></div>
              <h1 class="text-3xl md:text-4xl font-bold text-white tracking-wide">
                سیستم تغذیه توت‌فرنگی
              </h1>
              <p class="text-green-100/90 mt-2 text-sm md:text-base font-light">
                ماشین‌حساب تغذیه بر اساس فیزیولوژی برای کشت هیدروپونیک
              </p>

              <!-- نوار کاربر -->
              <div class="mt-4 flex items-center justify-center gap-4 bg-white/10 backdrop-blur-sm rounded-full px-6 py-2 inline-flex mx-auto">
                <span class="text-green-100 text-sm flex items-center gap-2">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                  </svg>
                  {{ user?.username || 'کاربر' }}
                </span>
                <span class="w-px h-6 bg-green-400/30"></span>
                <button
                  @click="logout"
                  class="text-green-100 hover:text-white text-sm transition hover:scale-105 flex items-center gap-1"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
                  </svg>
                  خروج
                </button>
              </div>
            </div>
          </div>

          <!-- ===== نوار تب‌ها با طراحی مدرن ===== -->
          <div class="flex flex-wrap border-b border-gray-200/80 bg-gray-50/80 backdrop-blur-sm">
            <button
              v-for="tab in tabs"
              :key="tab.key"
              @click="activeTab = tab.key"
              class="flex-1 py-3.5 px-4 text-center font-medium transition-all duration-300 min-w-[80px] flex items-center justify-center gap-2.5 text-sm md:text-base relative group"
              :class="activeTab === tab.key ? 'text-green-700' : 'text-gray-600 hover:text-green-600'"
            >
              <span class="transition-transform duration-300 group-hover:scale-110" :class="activeTab === tab.key ? 'text-green-600' : 'text-gray-400'">
                <span v-html="tab.icon"></span>
              </span>
              {{ tab.label }}
              <!-- خط زیر تب فعال -->
              <span class="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-green-500 to-emerald-500 transition-all duration-300"
                :class="activeTab === tab.key ? 'opacity-100 scale-x-100' : 'opacity-0 scale-x-0'">
              </span>
              <!-- افکت hover -->
              <span class="absolute inset-0 bg-green-500/5 transition-opacity duration-300 rounded-t-lg"
                :class="activeTab === tab.key ? 'opacity-100' : 'opacity-0 group-hover:opacity-100'">
              </span>
            </button>
          </div>

          <!-- ===== محتوای تب‌ها ===== -->
          <div class="p-6 md:p-8 bg-white/50">
            <!-- انیمیشن ورود ملایم -->
            <div class="transition-all duration-300 ease-in-out">
              <!-- تب ۱: محاسبه‌گر -->
              <CalculatorTab
                v-if="activeTab === 'calculator'"
                @result-updated="handleResultUpdated"
              />

              <!-- تب ۲: هشدارها -->
              <AlertsTab
                v-if="activeTab === 'alerts'"
                :result="sharedResult"
              />

              <!-- تب ۳: درباره محاسبات -->
              <AboutTab v-if="activeTab === 'about'" />

              <!-- تب ۴: راهنما -->
              <HelpTab v-if="activeTab === 'help'" />

              <!-- تب ۵: منابع -->
              <ReferencesTab v-if="activeTab === 'references'" />
            </div>
          </div>

          <!-- فوتر با طراحی مینیمال -->
          <div class="bg-gray-50/80 px-6 py-4 border-t border-gray-200/50 text-center">
            <div class="flex flex-wrap items-center justify-center gap-4 text-xs text-gray-500">
              <span class="flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 bg-green-500 rounded-full inline-block"></span>
                نسخه ۱.۰
              </span>
              <span class="text-gray-300">|</span>
              <span class="flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 bg-blue-500 rounded-full inline-block"></span>
                مبتنی بر فیزیولوژی گیاهی
              </span>
              <span class="text-gray-300">|</span>
              <span class="flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 bg-emerald-500 rounded-full inline-block"></span>
                احراز هویت فعال
              </span>
            </div>
          </div>
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
import AuthView from './views/AuthView.vue'

// ============================================================
// آیکون‌ها (طراحی مدرن و مینیمال)
// ============================================================
const IconLogo = `
<svg class="w-20 h-20 text-white/90 drop-shadow-lg" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
    ReferencesTab,
    AuthView
  },
  data() {
    return {
      activeTab: 'calculator',
      sharedResult: null,
      isAuthenticated: false,
      user: null,
      tabs: [
        { key: 'calculator', label: 'محاسبه‌گر', icon: IconCalculator },
        { key: 'alerts', label: 'هشدارها', icon: IconAlerts },
        { key: 'about', label: 'درباره محاسبات', icon: IconAbout },
        { key: 'help', label: 'راهنما', icon: IconHelp },
        { key: 'references', label: 'منابع', icon: IconReferences }
      ]
    }
  },
  mounted() {
    // بررسی وضعیت احراز هویت در localStorage
    const token = localStorage.getItem('auth_token')
    const user = localStorage.getItem('auth_user')
    if (token && user) {
      this.isAuthenticated = true
      this.user = JSON.parse(user)
    }

    // بازیابی نتیجه محاسبه
    const saved = localStorage.getItem('strawberry_result')
    if (saved) {
      try {
        this.sharedResult = JSON.parse(saved)
      } catch (e) {
        console.error('خطا در بازیابی داده:', e)
      }
    }
  },
  methods: {
    onAuthenticated(user) {
      this.isAuthenticated = true
      this.user = user
      localStorage.setItem('auth_user', JSON.stringify(user))
    },
    logout() {
      localStorage.removeItem('auth_token')
      localStorage.removeItem('auth_user')
      this.isAuthenticated = false
      this.user = null
    },
    handleResultUpdated(data) {
      this.sharedResult = data
      localStorage.setItem('strawberry_result', JSON.stringify(data))
    }
  }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

.font-vazir {
  font-family: 'Vazir', 'Tahoma', sans-serif;
}

/* انیمیشن نرم برای تب‌ها */
button {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* اسکرول‌بار سفارشی برای کل صفحه */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #86efac;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #22c55e;
}

/* ریسپانسیو برای موبایل */
@media (max-width: 640px) {
  .p-6 {
    padding: 0.75rem;
  }
  .p-8 {
    padding: 1rem;
  }
  .px-8 {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  .py-8 {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
  }
  .text-3xl {
    font-size: 1.5rem;
  }
  .text-4xl {
    font-size: 2rem;
  }
}

/* افکت شیشه‌ای (Glassmorphism) برای کارت */
.bg-white\/95 {
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

/* انیمیشن ورود ملایم برای محتوا */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}

/* هدر گرادیانت با افکت حرکت */
.bg-gradient-to-r {
  background-size: 200% 200%;
  animation: gradientMove 8s ease-in-out infinite;
}

@keyframes gradientMove {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* حلقه برای کاربر */
.rounded-full {
  border-radius: 9999px;
}

/* خط زیر تب‌ها */
.scale-x-0 {
  transform: scaleX(0);
}
.scale-x-100 {
  transform: scaleX(1);
}
</style>
