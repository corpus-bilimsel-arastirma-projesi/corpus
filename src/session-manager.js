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
    // if (!tokenExpiryDate) {
    //   console.log("No token expiry date. user probably never logged in");
    //   return Router.push("/sign-in");
    // }

    // let tenMinutesBeforeExpiry = subtractMinutes(tokenExpiryDate, 10);//If the token has expired or will expire in the next 30 minutes
    // const now = new Date();
    //
    // if (isAfter(now, tenMinutesBeforeExpiry)) { //If the token has expired or will expire in the next 10 minutes
    //   console.log("Token expired/will expire in the next 1 minutes");
    //   return Router.push("/sign-in");
    // }

    // console.log("Token Ok. Expiring at " + tokenExpiryDate);
    console.log('set timeout')
    setTimeout(refreshTokens, 5000) // differenceInMilliSeconds(tenMinutesBeforeExpiry, now)
  })
}

const refreshTokens = async () => {
  await store.dispatch("REFRESH_TOKEN")
  // const tokenExpiryDate = addSeconds(new Date(), store.getters.TOKENS_EXPIRY)
  // const tenMinutesBeforeExpiry = subtractMinutes(tokenExpiryDate, 10)
  // const now = new Date()
  console.log('new timeout')
  setTimeout(refreshTokens, 5000) // differenceInMilliSeconds(tenMinutesBeforeExpiry, now)
}
