const SET_UUID = (state, payload) => {
  state.UUID = payload
}

const SET_USER_FILES = (state, payload) => {
  state.USER_FILES = payload
}

const DEFAULT_STEP_STATES = (state) => {
  state.UUID = ''
  state.USER_FILES = []
}

export default {
  SET_UUID,
  SET_USER_FILES,
  DEFAULT_STEP_STATES
};
