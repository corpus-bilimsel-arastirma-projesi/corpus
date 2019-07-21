import preparationService from '@/services/preparationService'

const DELETE_END = async (context, payload) => {
  return await preparationService.postDeleteEnd(payload)
}

const DELETE_WORD = async (context, payload) => {
  return await preparationService.postDeleteWord(payload)
}

const REPLACE_WORDS = async (context, payload) => {
  return await preparationService.postReplaceWords(payload)
}

const DELETE_BETWEEN = async (context, payload) => {
  return await preparationService.postDeleteBetween(payload)
}

const DELETE_CONTAIN = async (context, payload) => {
  return await preparationService.postDeleteContain(payload)
}

const ADD_DATE_COLUMN = async (context, payload) => {
  return await preparationService.postAddDateColumn(payload)
}

const DELETE_BEGINNING = async (context, payload) => {
  return await preparationService.postDeleteBeginning(payload)
}

export default {
  DELETE_END,
  DELETE_WORD,
  REPLACE_WORDS,
  DELETE_BETWEEN,
  DELETE_CONTAIN,
  ADD_DATE_COLUMN,
  DELETE_BEGINNING
}
