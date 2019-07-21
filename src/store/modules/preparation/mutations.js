const DEFAULT_PREPARATION_STATES = (state) => {
  state.FILE_ID = null
  state.COLUMNS = []
}

const SET_FILE_ID = (state, payload) => {
  state.FILE_ID = payload
}

const SET_COLUMNS = (state, payload) => {
  state.COLUMNS = payload
}

export default {
  SET_FILE_ID,
  SET_COLUMNS,
  DEFAULT_PREPARATION_STATES
}
