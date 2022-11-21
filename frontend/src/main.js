import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

// set base url
axios.defaults.baseURL = 'http://45.67.58.152:8000' //'http://127.0.0.1:8000'

// если ошибка авторизации кидает на регистарцию
// https://stackoverflow.com/questions/52096412/vue-js-and-axios-redirect-on-401
axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log(error.response.data)
  if (error.response.status === 401) {
    // store.dispatch('logout')
    router.push({ name: 'Login'})
  }
  return Promise.reject(error)
})

const app = createApp(App).use(store).use(router).mount('#app')

export default app
