const DEFAULT_PREVIEW_STATES = (state) => {
  state.PREVIEW_VERTICAL_BAR = null
  state.PREVIEW_WORD_CLOUD = null
}

const SET_PREVIEW_WORD_CLOUD = (state, payload) => {
  state.PREVIEW_WORD_CLOUD = payload
}

const SET_PREVIEW_VERTICAL_BAR = (state, payload) => {
  state.PREVIEW_VERTICAL_BAR = payload
}

const SET_PREVIEW_VERTICAL_BAR_CATEGORIES = (state, payload) => {
  state.PREVIEW_VERTICAL_BAR_CATEGORIES = payload
}

export default {
  DEFAULT_PREVIEW_STATES,
  SET_PREVIEW_WORD_CLOUD,
  SET_PREVIEW_VERTICAL_BAR,
  SET_PREVIEW_VERTICAL_BAR_CATEGORIES
}
