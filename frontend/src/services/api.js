import axios from 'axios'
import { getToken } from './auth'

const API_URL = 'http://127.0.0.1:5000'

const apiClient = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
})

// ✅ Interceptor برای اضافه کردن توکن
apiClient.interceptors.request.use(
    (config) => {
        const token = getToken()
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
            console.log('🔑 توکن به هدر اضافه شد')
        } else {
            console.warn('⚠️ توکن وجود ندارد!')
        }
        return config
    },
    (error) => {
        console.error('❌ خطا در interceptor:', error)
        return Promise.reject(error)
    }
)

// ✅ Interceptor برای مدیریت خطاها
apiClient.interceptors.response.use(
    (response) => {
        console.log('✅ پاسخ دریافت شد:', response.status)
        return response
    },
    (error) => {
        if (error.response?.status === 401) {
            console.error('❌ خطای 401: توکن نامعتبر یا منقضی')
            // پاک کردن توکن و هدایت به صفحه ورود
            localStorage.removeItem('auth_token')
            localStorage.removeItem('auth_user')
            window.location.reload()
        }
        return Promise.reject(error)
    }
)

// ============================================================
// API Functions
// ============================================================

export const register = async (data) => {
    const response = await apiClient.post('/auth/register', data)
    return response.data
}

export const login = async (data) => {
    const response = await apiClient.post('/auth/login', data)
    return response.data
}

export const getMe = async () => {
    const response = await apiClient.get('/auth/me')
    return response.data
}

export const calculateNutrients = async (formData) => {
    const response = await apiClient.post('/calculate', formData)
    return response.data
}

export const saveCalculation = async (result, inputData) => {
    const response = await apiClient.post('/calculations/save', {
        result: result,
        input_data: inputData
    })
    return response.data
}

export const getCalculations = async (limit = 10) => {
    const response = await apiClient.get(`/calculations?limit=${limit}`)
    return response.data
}

export const getCalculationStats = async () => {
    const response = await apiClient.get('/calculations/stats')
    return response.data
}

export const getCalculation = async (calcId) => {
    const response = await apiClient.get(`/calculations/${calcId}`)
    return response.data
}

export default apiClient
