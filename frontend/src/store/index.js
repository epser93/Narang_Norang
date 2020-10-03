import Vue from 'vue'
import Vuex from 'vuex'
// import dummy from './dummy'
import helpdesk from './helpdesk'
import account from './account'
import fairytale from './fairytale'
<<<<<<< frontend/src/store/index.js
import favorite from './favorite'
=======
import voice from './voice'
>>>>>>> frontend/src/store/index.js

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    // dummy: dummy,
    help: helpdesk,
    user: account, 
    book: fairytale,
<<<<<<< frontend/src/store/index.js
    favorite: favorite,
=======
    voice: voice,
>>>>>>> frontend/src/store/index.js
  }
})