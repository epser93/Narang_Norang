import Vue from 'vue'
import VueRouter from 'vue-router'
import cookies from 'vue-cookies'

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
        path: '/books',
        name: 'Books',
        component: () => import('@/views/Books.vue')
      },
      {
        path: 'mybook',
        name: 'MyBook',
        component: () => import('@/views/navigation/MyBookShelves')
      },
      {
        path: 'help',
        name: 'CS',
        component: () => import('@/views/navigation/CustomerService'),
        redirect: 'help',
        children: [
          {
            path: '/',
            name: 'QA',
            component: () => import('@/views/helpdesk/MyQuestions')
          },
          {
            path: 'QA/:qid/',
            name: 'QAdetail',
            component: () => import('@/views/helpdesk/QuestionDetail')
          },
          {
            path: 'QA/',
            name: 'Question',
            component: () => import('@/views/helpdesk/QuestionForm')
          },
          {
            path: 'QA/:qid/:update',
            name: 'QAupdate',
            component: () => import('@/views/helpdesk/QuestionForm')
          },
        ]
      },
      {
        path: 'voice',
        name: 'Voice',
        component: () => import('@/views/navigation/VoiceCloud')
      },
      {
        path: 'userinfo',
        name: 'UserInfo',
        component: () => import('@/views/navigation/UserInfo')
      },
    ]
  },
  {
    path: '/onAir/:vid',
    name: 'REC',
    component: () => import('@/views/VoiceRecord')
  },
  {
    path: '/ebook/:bid/:bname/:vid',
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
  {
    path: '/payment',
    name: 'Payment',
    component: () => import('@/views/KakaoPay.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Login']  // Login 안해도 됨
  const authPages = ['Login']  // Login 되어있으면 안됨
  const KakaoPayPage = ['Payment']

  const authRequired = !publicPages.includes(to.name)  // 로그인 해야 함.
  const unauthRequired = authPages.includes(to.name)  // 로그인 해서는 안됨
  const TidRequired = KakaoPayPage.includes(to.name) 
  const isLoggedIn = !!cookies.get('auth-token')
  const isPaiedIn = !!cookies.get('tid')

  if (unauthRequired && isLoggedIn) {
    next('/')
  }

  authRequired && !isLoggedIn ? next({ name: 'Login' }) : next()

  TidRequired && !isPaiedIn ? next('/') : next()
})

export default router