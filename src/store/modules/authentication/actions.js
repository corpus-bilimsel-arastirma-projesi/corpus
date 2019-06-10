import axios from "axios";
import authenticationService from '@/services/authenticationService' // TODO: Will be used, when it is completed
import jwt_decode from 'jwt-decode'

const obtainToken = (username, password) => {
  const payload = {
    username: username,
    password: password
  }
  axios.post(this.state.endpoints.obtainJWT, payload)
    .then((response) => {
      console.log(`We will update token with using obtainJWT endpoint as ${response.data.token}`)
      this.commit('updateToken', response.data.token);
    })
    .catch((error) => {
      console.log(error);
    })
}

const refreshToken = () => {
  const payload = {
    token: this.state.jwt
  }
  axios.post(this.state.endpoints.refreshJWT, payload)
    .then((response) => {
      console.log(`We will update token with using refreshJWT endpoint as ${response.data.token}`)
      this.commit('updateToken', response.data.token)
    })
    .catch((error) => {
      console.log(error)
    })
}

const inspectToken = () => { // TODO: This method will be used to check token is expired
  const token = this.state.jwt;
  if (token) {
    const decoded = jwt_decode(token);
    const exp = decoded.exp
    const orig_iat = decode.orig_iat
    if (exp - (Date.now() / 1000) < 1800 && (Date.now() / 1000) - orig_iat < 628200) {
      this.dispatch('refreshToken')
    } else if (exp - (Date.now() / 1000) < 1800) {
      // DO NOTHING, DO NOT REFRESH
    } else {
      // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
    }
  }
}

export default {
  obtainToken,
  refreshToken,
  inspectToken
};
