import store from "./store/index"
import router from "./router"
import isAfter from "date-fns/is_after"
import subtractMinutes from "date-fns/sub_minutes"

export {initSession}

const initSession = () => {
  const time = new Date()

  let refreshDate = new Date(0)
  let accessDate = new Date(0)

  let refreshTokenExpiryDate = store.getters.REFRESH_EXPIRY
  let refreshTokenExpiry = refreshDate.setUTCSeconds(parseInt(refreshTokenExpiryDate))

  let accessTokenExpiryDate = store.getters.ACCESS_EXPIRY
  let accessTokenExpiry = accessDate.setUTCSeconds(parseInt(accessTokenExpiryDate))

  if (accessTokenExpiry === null) {
    console.log("No token expiry date. user probably never logged in")
    return
  } else if (isAfter(time, refreshTokenExpiry)) {
    store.commit("DEFAULT_STEP_STATES")
    store.commit("DEFAULT_PLOTLY_STATES")
    store.commit("DEFAULT_PREVIEW_STATES")
    store.commit("REMOVE_TOKEN")
    return router.push("/sign-in")
  }

  let oneMinuteBeforeExpiry = subtractMinutes(accessTokenExpiry, 1)
  const now = new Date();

  if (isAfter(now, oneMinuteBeforeExpiry)) {
    refreshTokens()
  }
}

const refreshTokens = () => {
  store.dispatch("REFRESH_TOKEN")
  setTimeout(refreshTokens, 4.5 * 1000 * 60)
}

