const DEFAULT_PLOTLY_STATES = (state) => {
  state.PREVIEW_SOURCES = null
  state.SET_MULTIPLE_LINES = null
  state.STACKED = null
}

const SET_PREVIEW_SOURCES = (state, payload) => {
  state.PREVIEW_SOURCES = payload
}

const SET_MULTIPLE_LINES = (state, payload) => {
  state.MULTIPLE_LINES = payload
}

const SET_STACKED = (state, payload) => {
  state.STACKED = payload
}

export default {
  SET_PREVIEW_SOURCES,
  DEFAULT_PLOTLY_STATES,
  SET_MULTIPLE_LINES,
  SET_STACKED
}
