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
    postFavorites({ rootGetters, dispatch }, bid) {
      axios.post(SERVER.URL + SERVER.ROUTER.favorite + bid + '/', null, rootGetters['user/config'])
      .then(() => {
        dispatch('getFavorites')
        alert('추가되었습니다.')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteFavorites({ rootGetters, dispatch }, bid) {
      axios.delete(SERVER.URL + SERVER.ROUTER.favorite + bid + '/', rootGetters['user/config'])
      .then(() => {
        dispatch('getFavorites')
        alert('삭제되었습니다.')
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}