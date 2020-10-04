import Vue from 'vue'
import Vuex from 'vuex'
// import dummy from './dummy'
import helpdesk from './helpdesk'
import account from './account'
import fairytale from './fairytale'
import favorite from './favorite'
import voice from './voice'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    // dummy: dummy,
    help: helpdesk,
    user: account, 
    book: fairytale,
    favorite: favorite,
    voice: voice,
  }
})