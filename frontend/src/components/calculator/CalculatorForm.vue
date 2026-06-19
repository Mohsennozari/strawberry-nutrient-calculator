<template>
  <div class="bg-white rounded-xl shadow-lg p-6 mb-6">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

      <!-- قطر طوقه -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>
            </svg>
            قطر طوقه (میلی‌متر)
          </span>
        </label>
        <input v-model="localForm.crown_diameter" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- ارتفاع بوته -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
            </svg>
            ارتفاع بوته (سانتی‌متر)
          </span>
        </label>
        <input v-model="localForm.plant_height" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- طول دمبرگ -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 4h14M5 4v16M5 4h4m10 0v16m-4 0H7M9 8h6M9 12h6M9 16h6"></path>
            </svg>
            طول دمبرگ (سانتی‌متر)
          </span>
        </label>
        <input v-model="localForm.petiole_length" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- طول برگ -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.5A4.5 4.5 0 017.5 9H6.5a4.5 4.5 0 010-9h5A4.5 4.5 0 0116 4.5v5a4.5 4.5 0 01-4.5 4.5h-5a4.5 4.5 0 010-9h.5"></path>
            </svg>
            طول برگ (سانتی‌متر)
          </span>
        </label>
        <input v-model="localForm.leaf_length" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- عرض برگ -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5v-4m0 4h-4m4 0l-5-5"></path>
            </svg>
            عرض برگ (سانتی‌متر)
          </span>
        </label>
        <input v-model="localForm.leaf_width" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- اندازه میوه -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 7v6l3 3" />
            </svg>
            اندازه میوه (سانتی‌متر مربع)
          </span>
        </label>
        <input v-model="localForm.fruit_size" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- سن بوته -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
            </svg>
            سن بوته (روز)
          </span>
        </label>
        <input v-model="localForm.age_days" type="number"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- تعداد میوه -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
            </svg>
            تعداد میوه در هر بوته
          </span>
        </label>
        <input v-model="localForm.fruits_per_plant" type="number"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- دما -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
            </svg>
            دمای روزانه (°C)
          </span>
        </label>
        <input v-model="localForm.temp_c" type="number" step="0.1"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- وضعیت هوا -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"></path>
            </svg>
            وضعیت هوا
          </span>
        </label>
        <select v-model="localForm.weather"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500">
          <option value="sunny">☀️ آفتابی</option>
          <option value="cloudy">☁️ ابری</option>
        </select>
      </div>

      <!-- EC -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
            </svg>
            EC (dS/m) - اختیاری
          </span>
        </label>
        <input v-model="localForm.ec" type="number" step="0.1" placeholder="مثلاً 1.8"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

      <!-- pH -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          <span class="inline-flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
            </svg>
            pH - اختیاری
          </span>
        </label>
        <input v-model="localForm.ph" type="number" step="0.1" placeholder="مثلاً 6.0"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500" />
      </div>

    </div>

    <button @click="$emit('calculate', localForm)"
      :disabled="loading"
      class="mt-6 w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-4 rounded-lg transition-all duration-200 transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path>
      </svg>
      {{ loading ? '⏳ در حال محاسبه...' : 'محاسبه نیاز غذایی' }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'CalculatorForm',
  props: {
    form: { type: Object, required: true },
    loading: { type: Boolean, default: false }
  },
  data() {
    return {
      localForm: { ...this.form }
    }
  },
  watch: {
    form: {
      deep: true,
      handler(newVal) {
        this.localForm = { ...newVal }
      }
    }
  }
}
</script>
