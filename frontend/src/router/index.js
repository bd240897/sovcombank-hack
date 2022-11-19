import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
// import TestView from "../views/TestView";
import ProfileView from "@/views/ProfileView";
// import ChatView from "@/views/ChatView";
// import ListExpertsView from "@/views/ListExpertsView";

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  //     {
  //   path: '/experts',
  //   name: 'ListExpertsView',
  //   component: ListExpertsView
  // },
  // {
  //   path: '/chat',
  //   name: 'ChatView',
  //   component: ChatView
  // },
  // {
  // path: '/test/:id',
  // name: 'TestView',
  // component: TestView
  // },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
