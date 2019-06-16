const UPDATE_TOKEN = (state, payload) => {
  // access token
  localStorage.setItem('accessToken', payload[0])
  state.JWT_ACCESS = payload[0]

  // refresh token
  localStorage.setItem('refreshToken', payload[1])
  state.JWT_REFRESH = payload[1]

  // expires time
  let jwt = JSON.parse(atob(payload[0].split('.')[1]))
  let date = new Date(0)
  let exp = date.setUTCSeconds(parseInt(jwt.exp))
  localStorage.setItem('accessExpiry', exp.toString())
  state.ACCESS_EXPIRY = jwt.exp
}

const REMOVE_TOKEN = (state) => {
  localStorage.removeItem('accessToken')
  localStorage.removeItem('refreshToken')
  localStorage.removeItem('accessExpiry')
  state.JWT_ACCESS = null
  state.JWT_REFRESH = null
  state.ACCESS_EXPIRY = null
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
