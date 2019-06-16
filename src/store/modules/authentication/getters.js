const EMAIL = state => state.EMAIL
const JWT_ACCESS = state => state.JWT_ACCESS
const JWT_REFRESH = state => state.JWT_REFRESH
const ACCESS_EXPIRY = state => state.ACCESS_EXPIRY
const OBTAIN_JWT = state => state.ENDPOINTS.OBTAIN_JWT
const REFRESH_JWT = state => state.ENDPOINTS.REFRESH_JWT

export default {
  EMAIL,
  OBTAIN_JWT,
  JWT_ACCESS,
  JWT_REFRESH,
  REFRESH_JWT,
  ACCESS_EXPIRY
}
