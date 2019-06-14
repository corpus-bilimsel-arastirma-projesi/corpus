import store from "./store/index";
import Router from "./router";
import isAfter from "date-fns/is_after";
import subtractMinutes from "date-fns/sub_minutes";
import addSeconds from "date-fns/add_seconds";
import differenceInMilliSeconds from "date-fns/difference_in_milliseconds";

export {initSession}

const initSession = () => {
  return new Promise((resolve) => {
    let tokenExpiryDate = store.getters.TOKENS_EXPIRY
    if (!tokenExpiryDate) {
      console.log("No token expiry date. user probably never logged in");
      return Router.push("/sign-in");
    }

    let oneMinuteBeforeExpiry = subtractMinutes(tokenExpiryDate, 1)
    const now = new Date();

    if (isAfter(now, oneMinuteBeforeExpiry)) {
      console.log('set timeout')
      refreshTokens() // differenceInMilliSeconds(tenMinutesBeforeExpiry, now)
    }

  })
}

const refreshTokens = () => {
  store.dispatch("REFRESH_TOKEN")
  setTimeout(refreshTokens, 4.5 * 1000 * 60) // differenceInMilliSeconds(tenMinutesBeforeExpiry, now)
}

