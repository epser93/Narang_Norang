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
    getQuestion({ rootGetters, commit }, index) {
      commit('SET_QUESTION', '')
      axios.get(SERVER.URL + SERVER.ROUTER.qna + index + '/', rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_QUESTION', data)
        })
        .catch((err) => {
          console.log(err)
        })   
    },
    putQuestion({ rootGetters }, { index, body }) {
      axios.put(SERVER.URL + SERVER.ROUTER.qna + index + '/', body, rootGetters['user/config'])
        .then(({ data }) => {
          router.push({name:'QAdetail', params:{qid: data.id}})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    delQuestion({ rootGetters }, index) {
      axios.delete(SERVER.URL + SERVER.ROUTER.qna + index + '/', rootGetters['user/config'])
        .then(() => {
          router.push({name:'QA'})
          alert("삭제가 완료되었습니다.")
        })
        .catch((err) => {
          console.log(err)
        })   
    },
    postReply({ rootGetters }, { index, body }) {
      axios.post(SERVER.URL + SERVER.ROUTER.qna + index + '/reply/', body, rootGetters['user/config'])
        .then(() => {
          router.push({name:'QA'})
          alert("답변이 완료되었습니다.")
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },

}