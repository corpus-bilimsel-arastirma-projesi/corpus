import authenticationService from '@/services/authenticationService'

const SIGN_UP = (state, payload) => {
  return authenticationService.postSignup(payload).then(res => {
    let payload = [res.token.access, res.token.refresh]
    state.commit('UPDATE_TOKEN', payload)
    return res.success === true && 200
  }).catch(err => {
    console.log(err)
    return 404
  })
}

const OBTAIN_TOKEN = (state, payload) => {
  return authenticationService.postObtainToken(payload)
    .then(res => {
      console.log(`We will update token with using obtainJWT endpoint as ${res.access}`)
      let payload = [res.access, res.refresh]
      state.commit('UPDATE_TOKEN', payload)
      return 200
    })
    .catch(err => {
      console.log(err)
      return 404
    })
}

const REFRESH_TOKEN = (state) => {
  const payload = {
    refresh: state.getters.JWT_REFRESH
  }
  authenticationService.postRefreshToken(payload)
    .then(res => {
      console.log(`We will update token with using refreshJWT endpoint as ${res.access}`)
      let payload = [res.access, state.getters.JWT_REFRESH]
      state.commit('UPDATE_TOKEN', payload)
    })
    .catch(err => {
      console.log(err)
    })
}

const SET_EMAIL = (context, payload) => {
  context.commit("SET_EMAIL", payload);
}

export default {
  OBTAIN_TOKEN,
  REFRESH_TOKEN,
  SET_EMAIL,
  SIGN_UP
};
