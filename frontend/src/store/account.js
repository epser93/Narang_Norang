import axios from 'axios'
import cookies from 'vue-cookies'
import SERVER from '@/api/drf'
import router from '@/router'
import swal from 'sweetalert'

export default {
  namespaced: true,

  state: {
    authToken: cookies.get('auth-token'),
    // 1. 받아올 거 선언
    userInfo: '',
    subscribes: ''
  },

  getters: {
    isLoggedIn(state) {
      return !!state.authToken
    },

    config(state) {
      return {
        headers: {
          'Authorization': `JWT ${state.authToken}`
        }
      }
    },

    formconfig(state) {
      return {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `JWT ${state.authToken}`
        }
      }
    },
  },
  // 2. 받아올 정보를 저장할 mutations 설정
  // state 받아올 거니까 써주기
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_USERINFO(state, payload) {
      state.userInfo = payload
    },
    SET_SUBSCRIBES(state, payload) {
      state.subscribes = payload
    },
  },

  actions: {
    // 3. 받아올 함수 저장
    // get은 뒤에 오는 변수 없음
    // mutations 쓸 때는 commit 사용
    getUserInfo({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.user, getters.config)
      .then(({ data }) => {
        commit('SET_USERINFO', data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    putUserInfo({ getters, commit }, nick_name) {
      const bodydata = {
        "nick_name": nick_name
      }
      axios.put(SERVER.URL + SERVER.ROUTER.user, bodydata, getters.config)
      .then(({ data }) => {
        commit('SET_USERINFO', data)
        swal('개인정보가 수정되었습니다.', { buttons: '확인' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    startKakaoPay({ getters }) {
      axios.post(SERVER.URL + SERVER.ROUTER.kakaopay, null, getters.config)
      .then(({ data }) => {
        cookies.set('tid', data.tid)
        location.href = data.next_redirect_pc_url
      })
      .catch((err) => {
        console.log(err)
      })
    },
    progressKakaoPay({ getters }, body) {
      axios.post(SERVER.URL + SERVER.ROUTER.kakaopay + 'approval/', body, getters.config)
      .then(() => {
        cookies.remove('tid')
        router.push({name:'Main'})
        swal('결제가 완료 되었습니다.', { buttons: '확인' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getsubscribes({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.subscribe, getters.config)
      .then(({ data }) => {
        commit('SET_SUBSCRIBES', data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    delsubscribe({ getters, dispatch }, tid) {
      axios.post(SERVER.URL + SERVER.ROUTER.kakaopay + 'refund/', tid, getters.config)
      .then(() => {
        dispatch('getUserInfo')
        dispatch('getsubscribes')
        swal('결제가 취소 되었습니다.', { buttons: '확인' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    
  },
}