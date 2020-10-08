import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'
import swal from 'sweetalert'

export default {
  namespaced: true,

  state: {
    questions: '',
    question: '',
    faq: '',
  },

  mutations: {
    SET_QUESTIONS(state, payload) {
      state.questions = payload
    },
    SET_QUESTION(state, payload) {
      state.question = payload
    },
    SET_FAQ(state, payload) {
      state.faq = payload
    },
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
          swal("삭제가 완료되었습니다.", { buttons: '확인' })
        })
        .catch((err) => {
          console.log(err)
        })   
    },
    postReply({ rootGetters }, { index, body }) {
      axios.post(SERVER.URL + SERVER.ROUTER.qna + index + '/reply/', body, rootGetters['user/config'])
        .then(() => {
          router.push({name:'QA'})
          swal("답변이 완료되었습니다.", { buttons: '확인' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getFAQ({ rootGetters , commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.faq, rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_FAQ', data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    postFAQ({ rootGetters }, body) {
      axios.post(SERVER.URL + SERVER.ROUTER.faq, body, rootGetters['user/config'])
        .then(() => {
          window.location.reload(true)
          swal("추가가 완료되었습니다.", { buttons: '확인' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    putFAQ({ rootGetters }, { index, body }) {
      axios.put(SERVER.URL + SERVER.ROUTER.faq + index + '/', body, rootGetters['user/config'])
        .then(() => {
          window.location.reload(true)
          swal("수정이 완료되었습니다.", { buttons: '확인' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    delFAQ({ rootGetters }, index) {
      axios.delete(SERVER.URL + SERVER.ROUTER.faq + index + '/', rootGetters['user/config'])
        .then(() => {
          window.location.reload(true)
          swal("삭제가 완료되었습니다.", { buttons: '확인' })
        })
        .catch((err) => {
          console.log(err)
        })   
    },
  },

}