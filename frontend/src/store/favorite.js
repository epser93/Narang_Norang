import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    favorites: ''
  },

  mutations: {
    SET_FAVORITES(state, payload){
      state.favorites = payload
    },
  },

  actions: {
    getFavorites({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.favorite, rootGetters['user/config'])
      .then(({ data }) => {
        commit('SET_FAVORITES', data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    postFavorites({ rootGetters }, bid) {
      axios.post(SERVER.URL + SERVER.ROUTER.favorite + bid + '/', {  }, rootGetters['user/config'])
      .then(() => {
        alert('추가되었습니다.')
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}