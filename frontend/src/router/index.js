import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    redirect: '/main',
    children: [
      {
        path: 'main',
        name: 'Main',
        component: () => import('@/views/navigation/Main')
      },
      {
        path: 'mybook',
        name: 'MyBook',
        component: () => import('@/views/navigation/MyBookShelves')
      },
      {
        path: 'help',
        name: 'CS',
        component: () => import('@/views/navigation/CustomerService')
      },
      {
        path: 'userinfo',
        name: 'UserInfo',
        component: () => import('@/views/navigation/UserInfo.vue')
      },
    ]
  },
  {
    path: '/ebook',
    name: 'Ebook',
    component: () => import('@/views/Ebook.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue')
  },
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
