import stepService from '@/services/stepService'

const GET_FILE_NAMES_GIVEN_USER = async (context, payload) => {
  let res = await stepService.postFileNamesGivenUser({
    user: payload
  })

  if (JSON.parse(res).data) {
    let USER_FILES = []

    JSON.parse(res).data.forEach(x => USER_FILES.push({
      id: x.id,
      uuid: x.uuid,
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

const DELETE_FILE_GIVEN_USER = (context, payload) => {
  return stepService.deleteGivenFileName({
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
  GET_FILE_NAMES_GIVEN_USER,
  SET_USER_FILES,
  DELETE_FILE_GIVEN_USER
}
