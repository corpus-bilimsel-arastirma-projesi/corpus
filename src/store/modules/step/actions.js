import axios from "axios";

const CLEAN_PARAMETERS = async (context, payload) => {
  await axios.post('https://localhost:8000/api/cleaning/', {
    uuid: payload[0],
    checkboxes: payload[1],
    mostCommon: payload[2],
  }).then((response) => {
    if (response.status === 200) {
      let payload = []
      let table = []
      let wordCloud = []
      let temp = 1
      response.data.forEach(x => {
        payload.push({key: x[0], value: parseInt(x[1])})
        table.push({number: temp, word: x[0], frequency: parseInt(x[1])})
        wordCloud.push({
          text: x[0],
          weight: parseInt(x[1]),
          rotation: 1,
          rotationUnit: 'turn',
          fontFamily: 'Anton',
          fontStyle: 'italic', // normal|italic|oblique|initial|inherit
          fontVariant: '', // normal|small-caps|initial|inherit
          fontWeight: '', // normal|bold|bolder|lighter|number|initial|inherit
          color: '#' + (Math.random().toString(16) + "000000").substring(2, 8)
        })
        temp = temp + 1
      })
      context.commit("SET_WORD_CLOUD", wordCloud)
      context.commit("SET_JSON_TABLE", table)
      context.commit("SET_JSON_FILE", payload)
      context.commit("SET_READY", true)
      return 200
    } else {
      return 404
    }
  })
};

const SET_HANDLE = (context, payload) => {
  context.commit("SET_HANDLE", payload);
}

const SET_EMPTY_STORE = (context, payload) => {
  context.commit("SET_EMPTY", payload);
}

const SET_STEP_NUMBER = (context, payload) => {
  context.commit("SET_STEP_NUMBER", payload)
}

const SET_DEFAULT_STATE = (context) => {
  context.commit("SET_DEFAULT_STATE")
}

const SET_JSON_FILE = async (context, payload) => {
  context.commit("SET_JSON_FILE", payload)
}

const SET_JSON_TABLE = async (context, payload) => {
  context.commit("SET_JSON_TABLE", payload)
}

const SET_WORD_CLOUD = async (context, payload) => {
  context.commit("SET_WORD_CLOUD", payload)
}

const SET_READY = async (context, payload) => {
  context.commit("SET_READY", payload)
}

export default {
  CLEAN_PARAMETERS,
  SET_HANDLE,
  SET_EMPTY_STORE,
  SET_STEP_NUMBER,
  SET_DEFAULT_STATE,
  SET_JSON_FILE,
  SET_JSON_TABLE,
  SET_WORD_CLOUD,
  SET_READY
};
