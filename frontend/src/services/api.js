import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

export const calculateNutrients = async (formData) => {
  const response = await axios.post(`${API_URL}/calculate`, formData)
  return response.data
}
