import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    bookmarks: ''
  },

  mutations: {
    SET_BOOKMARKS(state, payload){
      state.bookmarks = payload
    },
  },

  actions: {
    getBookmarks({ rootGetters , commit }, bid) {
    axios.get(SERVER.URL + SERVER.ROUTER.book + bid + '/', rootGetters['user/config'])
    .then(({ data }) => {
        commit('SET_BOOKMARKS', data)
    })
    .catch((err) => {
        console.log(err)
    })
    },
  },
}