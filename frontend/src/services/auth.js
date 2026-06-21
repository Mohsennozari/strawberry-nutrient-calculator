// مدیریت احراز هویت

const TOKEN_KEY = 'auth_token'
const USER_KEY = 'auth_user'

export function getToken() {
    return localStorage.getItem(TOKEN_KEY)
}

export function setAuth(token, user) {
    localStorage.setItem(TOKEN_KEY, token)
    localStorage.setItem(USER_KEY, JSON.stringify(user))
}

export function clearAuth() {
    localStorage.removeItem(TOKEN_KEY)
    localStorage.removeItem(USER_KEY)
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

export function getAuthHeader() {
    const token = getToken()
    if (!token) return {}
    return { Authorization: `Bearer ${token}` }
}
