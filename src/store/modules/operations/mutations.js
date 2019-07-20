const SET_USER_FILES = (state, payload) => {
  state.USER_FILES = payload
}

const SET_IS_READY = (state, payload) => {
  state.IS_READY = payload
}

const DEFAULT_STEP_STATES = (state) => {
  state.USER_FILES = []
}

export default {
  SET_IS_READY,
  SET_USER_FILES,
  DEFAULT_STEP_STATES
}
