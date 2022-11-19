import {createRouter, createWebHistory} from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
// import TestView from "../views/TestView";
import ProfileView from "@/views/ProfileView";
import Transfer from "@/views/Transfer";
// import ChatView from "@/views/ChatView";
// import ListExpertsView from "@/views/ListExpertsView";

const routes = [
    {
        path: '/',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/profile',
        name: 'ProfileView',
        component: ProfileView
    },
    {
        path: '/transfer/:id',
        name: 'Transfer',
        component: Transfer
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
