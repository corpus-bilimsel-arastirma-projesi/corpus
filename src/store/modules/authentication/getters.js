const JWT_ACCESS = state => state.JWT_ACCESS
const JWT_REFRESH = state => state.JWT_REFRESH
const OBTAIN_JWT = state => state.ENDPOINTS.OBTAIN_JWT
const REFRESH_JWT = state => state.ENDPOINTS.REFRESH_JWT
const EMAIL = state => state.EMAIL

export default {
  JWT_ACCESS,
  JWT_REFRESH,
  OBTAIN_JWT,
  REFRESH_JWT,
  EMAIL
}
