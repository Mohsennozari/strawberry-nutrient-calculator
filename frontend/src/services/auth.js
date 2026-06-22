const TOKEN_KEY = 'auth_token'
const USER_KEY = 'auth_user'

export function getToken() {
    const token = localStorage.getItem(TOKEN_KEY)
    console.log('📤 دریافت توکن:', token ? 'توکن موجود است' : 'توکن وجود ندارد')
    return token
}

export function setAuth(token, user) {
    localStorage.setItem(TOKEN_KEY, token)
    localStorage.setItem(USER_KEY, JSON.stringify(user))
    console.log('✅ توکن و کاربر ذخیره شد')
}

export function clearAuth() {
    localStorage.removeItem(TOKEN_KEY)
    localStorage.removeItem(USER_KEY)
    console.log('🗑️ توکن و کاربر پاک شد')
}

export function getUser() {
    const user = localStorage.getItem(USER_KEY)
    if (!user) return null
    try {
        return JSON.parse(user)
    } catch {
        return null
    }
}

export function isAuthenticated() {
    return !!getToken()
}
