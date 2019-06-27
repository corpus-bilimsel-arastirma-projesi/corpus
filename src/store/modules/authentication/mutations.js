const UPDATE_TOKEN = (state, payload) => {
  // access token
  localStorage.setItem('accessToken', payload[0])
  state.JWT_ACCESS = payload[0]

  // expires time for Access
  let accessJWT = JSON.parse(atob(payload[0].split('.')[1]))
  let accessDate = new Date(0)
  let accessExp = accessDate.setUTCSeconds(parseInt(accessJWT.exp))
  localStorage.setItem('accessExpiry', accessExp.toString())
  state.ACCESS_EXPIRY = accessJWT.exp

   // refresh token
  localStorage.setItem('refreshToken', payload[1])
  state.JWT_REFRESH = payload[1]

  // expires time for refresh
  let refreshJwt = JSON.parse(atob(payload[1].split('.')[1]))
  let refreshDate = new Date(0)
  let refreshExp = refreshDate.setUTCSeconds(parseInt(refreshJwt.exp))
  localStorage.setItem('refreshExpiry', refreshExp.toString())
  state.REFRESH_EXPIRY = refreshJwt.exp
}

const REMOVE_TOKEN = (state) => {
  localStorage.removeItem('accessToken')
  localStorage.removeItem('refreshToken')
  localStorage.removeItem('accessExpiry')
  localStorage.removeItem('refreshExpiry')
  state.JWT_ACCESS = null
  state.JWT_REFRESH = null
  state.ACCESS_EXPIRY = null
  state.REFRESH_EXPIRY = null
  state.EMAIL = ''
}

const SET_EMAIL = (state, payload) => {
  state.EMAIL = payload
}

export default {
  UPDATE_TOKEN,
  REMOVE_TOKEN,
  SET_EMAIL
}
