import { createStore } from 'vuex'
import login from "./modules/login/";
import profile from "./modules/profile/";
import transfer from "./modules/transfer/";
import history from "./modules/history/";

export default createStore({
  state() {
    return {
      // TODO
      BASE_URL: 'http://45.67.58.152:8000', // 'http://127.0.0.1:8000',
      LOGIN_URL: "/auth/token/login",
      USER_INFO_URL: "/api/v1/auth/users/me/",
      PROFILE_URL: "/api/v1/profile/",
      WALLETS_LIST_URL: "/api/v1/wallet/list/",
      WallET_URL: "api/v1/wallet/",
      MAKE_TRANSFER_URL: "api/v1/transfer/",
      HISTORY_URL: "api/v1/transfer/history/",
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
    profile,
    transfer,
    history
  }
})
