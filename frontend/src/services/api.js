import axios from 'axios'
import { getToken, clearAuth } from './auth'

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

const api = axios.create({ baseURL: API_URL })

api.interceptors.request.use((config) => {
  const token = getToken()
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      clearAuth()
      window.dispatchEvent(new CustomEvent('auth:unauthorized'))
    }
    return Promise.reject(error)
  }
)

export const register = async (payload) => {
  const response = await api.post('/auth/register', payload)
  return response.data
}

export const login = async (payload) => {
  const response = await api.post('/auth/login', payload)
  return response.data
}

export const fetchMe = async () => {
  const response = await api.get('/auth/me')
  return response.data
}

export const calculateNutrients = async (formData) => {
  const response = await api.post('/calculate', formData)
  return response.data
}

export default api
