import operationService from '@/services/operationService'

const GET_FILE_NAMES_GIVEN_USER = async (context, payload) => {
  let res = await operationService.postFileNamesGivenUser({
    user: payload
  })

  if (JSON.parse(res).data) {
    let USER_FILES = []

    JSON.parse(res).data.forEach(file => USER_FILES.push({
      id: file.id,
      date: file.date,
      checkbox: false,
      title: file.filename,
      icon: 'assignment',
      isReady: file['is_ready'],
      iconClass: 'blue white--text'
    }))

    context.commit("SET_USER_FILES", USER_FILES)

    return 200
  } else {
    return 404
  }
}

const GET_COLUMN_NAMES = async (context, payload) => {
  return await operationService.getColumnNames(payload)
}

const POST_COLUMN_MAPPING = async (context, payload) => {
  return await operationService.postColumnMapping(payload)
}

const CONCAT_FILES = async (context, payload) => {
  return await operationService.postConcatFiles({
    files: payload[0],
    file_name: `MERGED ${payload[1].toString()}`
  })
}

const DELETE_FILE_GIVEN_USER = (context, payload) => {
  return operationService.deleteGivenFileName({
    data: {
      id: payload
    }
  })
}

const SET_USER_FILES = (context, payload) => {
  context.commit("SET_USER_FILES", payload)
}

const SET_HANDLE = (context, payload) => {
  context.commit("SET_HANDLE", payload);
}

export default {
  SET_HANDLE,
  CONCAT_FILES,
  SET_USER_FILES,
  GET_COLUMN_NAMES,
  POST_COLUMN_MAPPING,
  GET_FILE_NAMES_GIVEN_USER,
  DELETE_FILE_GIVEN_USER
}
