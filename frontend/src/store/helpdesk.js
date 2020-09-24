import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    questions: '',
    question: '',
  },

  mutations: {
    GET_QUESTIONS(state, payload) {
      state.questions = payload
    },
    GET_QUESTION(state, payload) {
      state.question = payload
    }
  },

  actions: {
    getQuestions({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.qna, rootGetters['user/config'])
        .then(({ data }) => {
          commit('GET_QUESTIONS', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    postQuestion({ rootGetters , commit }, body) {
      axios.post(SERVER.URL + SERVER.ROUTER.qna, body, rootGetters['user/config'])
        .then(({ data }) => {
          commit('GET_QUESTIONS', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getQuestion({ rootGetters , commit }, index) {
      axios.get(SERVER.URL + SERVER.ROUTER.qna + index + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('GET_QUESTION', data)
        })
        .catch((err) => {
          console.log(err)
        })   
    }
  },

}