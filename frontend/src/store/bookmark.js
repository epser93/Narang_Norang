import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    bookmarks: '',
    bookmark: '',
  },

  mutations: {
    SET_BOOKMARKS(state, payload){
      state.bookmarks = payload
    },
    SET_BOOKMARK(state, payload){
      state.bookmark = payload
    },
  },

  actions: {
    getBookmarks({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.mark, rootGetters['user/config'])
      .then(({ data }) => {
          commit('SET_BOOKMARKS', data)
      })
      .catch((err) => {
          console.log(err)
      })
    },
    getBookmark({ rootGetters , commit }, bid) {
      axios.get(SERVER.URL + SERVER.ROUTER.mark + bid + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_BOOKMARK', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    postBookmark({ rootGetters }, { bid, body }) {
      axios.post(SERVER.URL + SERVER.ROUTER.mark + bid + '/', body, rootGetters['user/config'])
        .then(() => {
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}