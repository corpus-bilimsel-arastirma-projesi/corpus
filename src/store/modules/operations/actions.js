import operationService from '@/services/operationService'

const GET_FILE_NAMES_GIVEN_USER = async (context, payload) => {
  let res = await operationService.postFileNamesGivenUser({
    user: payload
  })

  if (JSON.parse(res).data) {
    let USER_FILES = []

    JSON.parse(res).data.forEach(x => USER_FILES.push({
      id: x.id,
      checkbox: false,
      title: x.filename,
      icon: 'assignment',
      iconClass: 'blue white--text',
      subtitle: Date.now() // TODO: Get from DB
    }))

    context.commit("SET_USER_FILES", USER_FILES)

    return 200
  } else {
    return 404
  }
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
  GET_FILE_NAMES_GIVEN_USER,
  DELETE_FILE_GIVEN_USER
}
