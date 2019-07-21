const DEFAULT_PREPARATION_STATES = (state) => {
  state.FILE_ID = null
}

const SET_FILE_ID = (state, payload) => {
  state.FILE_ID = payload
}

export default {
  SET_FILE_ID,
  DEFAULT_PREPARATION_STATES
}
