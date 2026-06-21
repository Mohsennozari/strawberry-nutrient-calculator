<template>
  <div dir="rtl" class="min-h-screen bg-gradient-to-br from-green-50 to-emerald-100 p-4 font-vazir flex items-center justify-center">
    <div class="max-w-md w-full mx-auto">
      <div class="bg-white rounded-2xl shadow-2xl overflow-hidden border border-green-100">

        <!-- هدر -->
        <div class="bg-gradient-to-r from-green-700 to-emerald-600 px-8 py-6 text-center">
          <div class="flex justify-center mb-3" v-html="IconLogo"></div>
          <h1 class="text-2xl font-bold text-white">سیستم تغذیه توت‌فرنگی</h1>
          <p class="text-green-100 mt-2 text-sm">
            {{ mode === 'login' ? 'برای ادامه وارد حساب کاربری خود شوید' : 'برای شروع یک حساب کاربری بسازید' }}
          </p>
        </div>

        <!-- فرم -->
        <div class="p-6 sm:p-8">
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">نام کاربری</label>
              <input
                v-model.trim="formData.username"
                type="text"
                autocomplete="username"
                placeholder="مثال: mohsen"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 outline-none transition"
              />
            </div>

            <div v-if="mode === 'register'">
              <label class="block text-sm font-medium text-gray-700 mb-1">ایمیل</label>
              <input
                v-model.trim="formData.email"
                type="email"
                dir="ltr"
                autocomplete="email"
                placeholder="you@example.com"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 outline-none transition text-right"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">رمز عبور</label>
              <input
                v-model="formData.password"
                type="password"
                :autocomplete="mode === 'login' ? 'current-password' : 'new-password'"
                placeholder="••••••••"
                class="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 outline-none transition"
              />
            </div>

            <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 text-sm rounded-lg px-4 py-2.5">
              {{ error }}
            </div>

            <button
              type="submit"
              :disabled="loading"
              class="w-full bg-green-600 hover:bg-green-700 disabled:opacity-60 disabled:cursor-not-allowed text-white font-medium py-2.5 rounded-lg transition shadow-md"
            >
              {{ loading ? 'لطفاً صبر کنید...' : (mode === 'login' ? 'ورود' : 'ثبت‌نام') }}
            </button>
          </form>

          <div class="text-center mt-5 text-sm text-gray-600">
            <template v-if="mode === 'login'">
              حساب کاربری ندارید؟
              <button @click="switchMode('register')" class="text-green-700 font-medium hover:underline mr-1">ثبت‌نام کنید</button>
            </template>
            <template v-else>
              قبلاً ثبت‌نام کرده‌اید؟
              <button @click="switchMode('login')" class="text-green-700 font-medium hover:underline mr-1">وارد شوید</button>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { login as loginApi, register as registerApi } from '../../services/api'
import { setAuth } from '../../services/auth'
import { IconLogo } from '../../icons'

export default {
  name: 'AuthView',
  emits: ['authenticated'],
  data() {
    return {
      mode: 'login',
      loading: false,
      error: '',
      IconLogo,
      formData: {
        username: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    switchMode(mode) {
      this.mode = mode
      this.error = ''
    },
    async handleSubmit() {
      this.error = ''

      if (!this.formData.username || !this.formData.password) {
        this.error = 'نام کاربری و رمز عبور الزامی است'
        return
      }
      if (this.mode === 'register' && !this.formData.email) {
        this.error = 'ایمیل الزامی است'
        return
      }

      this.loading = true
      try {
        const payload = this.mode === 'login'
          ? { username: this.formData.username, password: this.formData.password }
          : { username: this.formData.username, email: this.formData.email, password: this.formData.password }

        const data = this.mode === 'login'
          ? await loginApi(payload)
          : await registerApi(payload)

        setAuth(data.token, data.user)
        this.$emit('authenticated', data.user)
      } catch (err) {
        if (err.response && err.response.data && err.response.data.error) {
          this.error = err.response.data.error
        } else {
          this.error = 'خطا در ارتباط با سرور. مطمئن شوید سرور Flask روشن است.'
        }
      } finally {
        this.loading = false
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
</style>
