import { createRouter, createWebHistory } from 'vue-router'
import Main from "@/pages/Main.vue";
import SignUp from "@/pages/SignUp.vue";
import LogIn from "@/pages/LogIn.vue";
import PostPage from "@/pages/PostPage.vue";

const routes = [
    {
        path: '/',
        name: 'main',
        component: Main,
      },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp,
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LogIn,
    },
    {
        path: '/posts/:id',
        component: PostPage,
        name: 'PostPage'
    },
]

const router = createRouter({
  routes: routes,
  history: createWebHistory()
})
export default router
