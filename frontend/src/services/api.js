import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export const calculateNutrients = async (formData) => {
  try {
    const response = await axios.post(`${API_URL}/calculate`, formData)
    return response.data
  } catch (error) {
    console.error('خطا در محاسبه:', error)
    throw error
  }
}
