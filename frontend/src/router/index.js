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
        component: Login,
        meta: {
            title: 'Регистрация',
            metaTags: [
                {
                    name: 'Регистрация',
                    content: 'The home page of our example app.'
                },
                {
                    property: 'og:description',
                    content: 'The home page of our example app.'
                }
            ]
        }
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

// https://www.digitalocean.com/community/tutorials/vuejs-vue-router-modify-head
router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  if(nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  } else if(previousNearestWithMeta) {
    document.title = previousNearestWithMeta.meta.title;
  }

  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  if(!nearestWithMeta) return next();

  nearestWithMeta.meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');
    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });
    tag.setAttribute('data-vue-router-controlled', '');
    return tag;
  }).forEach(tag => document.head.appendChild(tag));
  next();
});



export default router
