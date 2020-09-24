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

//Kakao
window.Kakao.init(process.env.VUE_APP_KAKAO_KEY);

<<<<<<< HEAD
// Booklet
import 'vue-booklet/dist/lib/vue-booklet.min.css'

=======
>>>>>>> 7ca33f2390f35934b72122e10dcf27498deb7ef2
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
