import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

export default {
  namespaced: true,

  state: {
    questions: '',
    question: '',
  },

  mutations: {
    SET_QUESTIONS(state, payload) {
      state.questions = payload
    },
    SET_QUESTION(state, payload) {
      state.question = payload
    }
  },

  actions: {
    getQuestions({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.qna, rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_QUESTIONS', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    postQuestion({ rootGetters }, body) {
      axios.post(SERVER.URL + SERVER.ROUTER.qna, body, rootGetters['user/config'])
        .then(({ data }) => {
          router.push({name:'QAdetail', params:{qid: data.id}})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getQuestion({ rootGetters , commit }, index) {
      axios.get(SERVER.URL + SERVER.ROUTER.qna + index + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_QUESTION', data)
        })
        .catch((err) => {
          console.log(err)
        })   
    }
  },

}