import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    quations: '',
  },

  mutations: {
    GET_QUATIONS(state, payload) {
      state.quations = payload
    },
  },

  actions: {
    getQuations({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.qna, rootGetters['user/config'])
        .then(({ data }) => {
          commit('GET_QUATIONS', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    postQuation({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.qna, rootGetters['user/config'])
        .then(({ data }) => {
          commit('GET_QUATIONS', data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },

}