import authenticationService from '@/services/authenticationService'
import jwt_decode from 'jwt-decode'

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
    token: state.getters.JWT_REFRESH
  }
  authenticationService.postRefreshToken(payload)
    .then(res => {
      console.log(`We will update token with using refreshJWT endpoint as ${res.refresh}`) // TODO: Decide which one is it access or refresh?
      let payload = [res.access, state.getters.JWT_REFRESH]
      state.commit('UPDATE_TOKEN', payload)
    })
    .catch(err => {
      console.log(err)
    })
}

const INSPECT_TOKEN = (state) => { // TODO: This method will be used to check token is expired
  const token = state.getters.JWT_ACCESS;
  if (token) {
    const decoded = jwt_decode(token)
    const exp = decoded.exp
    const orig_iat = decode.orig_iat // TODO: decode.orig_iat ? What is that?
    if (exp - (Date.now() / 1000) < 1800 && (Date.now() / 1000) - orig_iat < 628200) {
      state.dispatch('REFRESH_TOKEN')
    } else if (exp - (Date.now() / 1000) < 1800) {
      // DO NOTHING, DO NOT REFRESH
    } else {
      // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
      state.commit('REMOVE_TOKEN')
      this.$router.replace({path: '/sign-in'})
    }
  }
}

const SET_EMAIL = (context, payload) => {
  context.commit("SET_EMAIL", payload);
}

export default {
  OBTAIN_TOKEN,
  REFRESH_TOKEN,
  INSPECT_TOKEN,
  SET_EMAIL,
  SIGN_UP
};
