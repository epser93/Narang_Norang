import Vue from 'vue'
import Vuex from 'vuex'
import dummy from './dummy'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    dummy: dummy
  }
})