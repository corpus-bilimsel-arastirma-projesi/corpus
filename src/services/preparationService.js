import api from '@/services/api'

export default {
  postAddDateColumn(payload) {
    return api.post(`file/add-date-column/`, payload)
      .then(response => response.data)
  },
  postDeleteBetween(payload) {
    return api.post(`file/delete-between/`, payload)
      .then(response => response.data)
  },
  postDeleteWord(payload) {
    return api.post(`file/delete-word/`, payload)
      .then(response => response.data)
  },
  postDeleteContain(payload) {
    return api.post(`file/delete-contain/`, payload)
      .then(response => response.data)
  },
  postDeleteBeginning(payload) {
    return api.post(`file/delete-beginning/`, payload)
      .then(response => response.data)
  },
  postDeleteEnd(payload) {
    return api.post(`file/delete-end/`, payload)
      .then(response => response.data)
  },
  postReplaceWords(payload) {
    return api.post(`file/replace-words/`, payload)
      .then(response => response.data)
  }
}