import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    fairytales: '',
    fairytale: '',
    ebook: '',
  },

  mutations: {
    SET_FAIRYTALES(state, payload){
      state.fairytales = payload
    },
    SET_FAIRYTALE(state, payload){
      state.fairytale = payload
    },
    SET_EBOOK(state, payload){
      state.ebook = payload
    },
  },

  actions: {
    getFairytales({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.book, rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_FAIRYTALES', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getFairytale({ rootGetters , commit }, bid) {
      axios.get(SERVER.URL + SERVER.ROUTER.book + bid + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_FAIRYTALE', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getEbook({ rootGetters , commit }, { bid, vid }) {
      axios.get(SERVER.URL + SERVER.ROUTER.book + bid + '/voice/' + vid + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_EBOOK', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getSearch({ rootGetters , commit }, search) {
      axios.get(SERVER.URL + SERVER.ROUTER.search + search + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_FAIRYTALES', data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },

}