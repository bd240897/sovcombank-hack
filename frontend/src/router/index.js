import {createRouter, createWebHistory} from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import ProfileView from "@/views/ProfileView";
import Transfer from "@/views/Transfer";
import History from "@/views/History";

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
        {
        path: '/history',
        name: 'History',
        component: History
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
