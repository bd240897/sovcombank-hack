import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            TOKEN: "",
            userInfo: {},
        }
    },
    getters: {},
    mutations: {
        SET_TOKEN(state, TOKEN) {
            state.TOKEN = TOKEN
            axios.defaults.headers.common['Authorization'] = 'Token ' + TOKEN;
        },
        SET_USER_INFO(state, userInfo) {
            state.userInfo = userInfo
        },
    },
    actions: {

        isTokenValid({commit, rootState}, {
            url = this.state.IS_TOKEN_VALID_URL,
            data = {"jwt": this.state.login.TOKEN}
        }) {
            axios.post(url, data, {
                headers: {
                    Authorization: '',
                }
            })
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },

        login({commit, rootState, dispatch}, {url = this.state.LOGIN_URL, data = {"login": '', "password": ''}}) {
            axios.post(url, data)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');

                    commit('SET_TOKEN', x.data.auth_token)
                    dispatch("getUserInfo", {})
                    router.push({ name: 'ProfileView'})

                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },

        getUserInfo({commit, rootState}, {url = this.state.USER_INFO_URL}) {
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_USER_INFO', x.data)
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },
    },


})

