import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// BootstrapVue
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Carousel3d
import Carousel3d from 'vue-carousel-3d'

Vue.use(Carousel3d);


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
