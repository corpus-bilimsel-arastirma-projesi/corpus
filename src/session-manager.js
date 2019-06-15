import store from "./store/index";
import Router from "./router";
import isAfter from "date-fns/is_after";
import subtractMinutes from "date-fns/sub_minutes";

export {initSession}

const initSession = () => {
  const time = new Date()
  let tokenExpiryDate = store.getters.TOKENS_EXPIRY
  let date = new Date(0)
  let tokensExpiry = date.setUTCSeconds(parseInt(tokenExpiryDate))
  if (tokenExpiryDate === null) {
    console.log("No token expiry date. user probably never logged in")
    return
  } else if (isAfter(time, tokensExpiry)) { // TODO: Check Refresh Token EXP Time
    // return Router.push("/sign-in")
  }

  let oneMinuteBeforeExpiry = subtractMinutes(tokensExpiry, 1)
  const now = new Date();

  if (isAfter(now, oneMinuteBeforeExpiry)) {
    refreshTokens()
  }
}

const refreshTokens = () => {
  store.dispatch("REFRESH_TOKEN")
  setTimeout(refreshTokens, 4.5 * 1000 * 60)
}

