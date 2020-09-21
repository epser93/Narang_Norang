import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/',
    name: 'Login',
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   const publicPages = ['Login', 'SignUp']  // Login 안해도 됨
//   const authPages = ['Login', 'Signup']  // Login 되어있으면 안됨

//   const authRequired = !publicPages.includes(to.name)  // 로그인 해야 함.
//   const unauthRequired = authPages.includes(to.name)  // 로그인 해서는 안됨
//   const isLoggedIn = !!cookies.get('auth-token')

//   if (unauthRequired && isLoggedIn) {
//     next('/')
//   }

//   authRequired && !isLoggedIn ? next({ name: 'Login' }) : next()
// })

export default router
