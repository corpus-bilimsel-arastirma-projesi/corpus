const SET_STEP_NUMBER = (state, payload) => {
  state.STEP_NUMBER = parseInt(payload).toString()
}

const SET_JSON_FILE = (state, payload) => {
  state.JSON_FILE = payload
}

const SET_JSON_TABLE = (state, payload) => {
  state.JSON_TABLE = payload
}

const SET_WORD_CLOUD = (state, payload) => {
  state.WORD_CLOUD = payload
}

const POP_WORD_CLOUD = (state, payload) => {
  let removeIndex = state.WORD_CLOUD.map(item => item.text).indexOf(payload.text);
  state.WORD_CLOUD.splice(removeIndex, 1);
  state.JSON_FILE.splice(removeIndex, 1);
  state.JSON_TABLE.splice(removeIndex, 1);
}

const SET_READY = (state, payload) => {
  state.READY = payload
}

const SET_UUID = (state, payload) => {
  state.UUID = payload
}

const SET_BUTTON_NAME = (state, payload) => {
  state.BUTTON_NAME = payload
}

const SET_USER_FILES = (state, payload) => {
  state.USER_FILES = payload
}

const DEFAULT_STEP_STATES = (state) => {
  state.STEP_NUMBER = '1'
  state.JSON_FILE = ''
  state.JSON_TABLE = ''
  state.WORD_CLOUD = ''
  state.READY = false
  state.UUID = ''
  state.BUTTON_NAME = 'Cancel'
  state.USER_FILES = []
}

export default {
  SET_UUID,
  SET_READY,
  SET_JSON_FILE,
  SET_JSON_TABLE,
  SET_WORD_CLOUD,
  POP_WORD_CLOUD,
  SET_USER_FILES,
  SET_STEP_NUMBER,
  SET_BUTTON_NAME,
  DEFAULT_STEP_STATES
};
