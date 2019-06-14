const UPDATE_TOKEN = (state, payload) => {
  localStorage.setItem('a', payload[0])
  localStorage.setItem('r', payload[1])
  state.JWT_ACCESS = payload[0]
  state.JWT_REFRESH = payload[1]
}

const REMOVE_TOKEN = (state) => {
  localStorage.removeItem('a')
  localStorage.removeItem('r')
  state.JWT_ACCESS = null
  state.JWT_REFRESH = null
}

const SET_EMAIL = (state, payload) => {
  state.EMAIL = payload
}

export default {
  UPDATE_TOKEN,
  REMOVE_TOKEN,
  SET_EMAIL
}
