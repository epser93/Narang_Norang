import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// BootstrapVue
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

// Carousel3d
import Carousel3d from 'vue-carousel-3d'
Vue.use(Carousel3d);

// Kakao
window.Kakao.init(process.env.VUE_APP_KAKAO_KEY);

// Booklet
import 'vue-booklet/dist/lib/vue-booklet.min.css'

// VueCookies
import VueCookies  from 'vue-cookies'
Vue.use(VueCookies)

// vue-record
import VueRecord from '@codekraft-studio/vue-record'
Vue.use(VueRecord)

// vue-text-highlight

import TextHighlight from 'vue-text-highlight';
Vue.component('text-highlight', TextHighlight)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')