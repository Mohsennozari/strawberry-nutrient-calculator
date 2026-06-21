import axios from 'axios'
import { getToken } from './auth'

const API_URL = 'http://127.0.0.1:5000'

// ============================================================
// API Client با احراز هویت خودکار
// ============================================================
const apiClient = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
})

// اضافه کردن توکن به همه درخواست‌ها
apiClient.interceptors.request.use(
    (config) => {
        const token = getToken()
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
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
    try {
        const response = await apiClient.post('/calculate', formData)
        return response.data
    } catch (error) {
        console.error('خطا در محاسبه:', error)
        throw error
    }
}

export default apiClient
