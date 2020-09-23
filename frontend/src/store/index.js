import Vue from 'vue'
import Vuex from 'vuex'
// import dummy from './dummy'
import helpdesk from './helpdesk'
import account from './account'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    // dummy: dummy,
    help: helpdesk,
    user: account, 
  }
})