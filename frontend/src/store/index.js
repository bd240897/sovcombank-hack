import { createStore } from 'vuex'
import login from "./modules/login/";
import chat from "./modules/chat/";
import profile from "./modules/profile/";
import transfer from "./modules/transfer/";
import history from "./modules/history/";

export default createStore({
  state() {
    return {
      // TODO
      BASE_URL: 'http://127.0.0.1:8000',
      LOGIN_URL: "/auth/token/login",
      USER_INFO_URL: "/api/v1/auth/users/me/",
      PROFILE_URL: "/api/v1/profile/",
      WALLETS_LIST_URL: "/api/v1/wallet/list/",
      WallET_URL: "api/v1/wallet/",
      MAKE_TRANSFER_URL: "api/v1/transfer/",
      HISTORY_URL: "api/v1/transfer/history/",

      CHAT_HISTORY_URL: "/chat/history",
      CHAT_SEND_URL: "/message/send",
      CHAT_ID_DIALOG_URL: '/chat/dialog',
      IS_TOKEN_VALID_URL: "/jwt/verify",
      SEND_MSG_URL: "/message/send"
      // IS_TOKEN_VALID_URL_full: "https://hack.invest-open.ru/jwt/verify"
    }
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    login,
    chat,
    profile,
    transfer,
    history
  }
})
