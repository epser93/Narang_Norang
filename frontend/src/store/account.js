// import axios from 'axios'
import cookies from 'vue-cookies'

export default {
  namespaced: true,

  state: {
    authToken: cookies.get('auth-token'),
  },

  getters: {
    config(state) {
      return {
        headers: {
          'Authorization': `JWT ${state.authToken}`
        }
      }
    },

  },

  mutations: {

  },

  actions: {

  },

}