const UPDATE_TOKEN = (state, newToken) => {
  localStorage.setItem('t', newToken)
  state.JWT = newToken
}

const REMOVE_TOKEN = (state) => {
  localStorage.removeItem('t')
  state.JWT = null
}

export default {
  UPDATE_TOKEN,
  REMOVE_TOKEN
}
