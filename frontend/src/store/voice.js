import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

export default {
	namespaced: true,

	state: {
		script: '',
		trains: '',
		train: '',
		voices: '',
	},
	mutations: {
		SET_SCRIPT(state, payload) {
			state.script = payload
		},
		SET_TRAINS(state, payload) {
			state.trains = payload
		},
		SET_TRAIN(state, payload) {
			state.train = payload
		},
		SET_VOICES(state, payload) {
			state.voices = payload
		},
	},
	actions: {
		getScript({ rootGetters , commit }) {
			axios.get(SERVER.URL + SERVER.ROUTER.script, rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_SCRIPT', data)
        })
        .catch((err) => {
          console.log(err)
        })
		},
		getTrains({ rootGetters , commit }) {
			axios.get(SERVER.URL + SERVER.ROUTER.train, rootGetters['user/config'])
        .then(({ data }) => {
          commit('SET_TRAINS', data)
        })
        .catch((err) => {
          console.log(err)
        })
		},
		postTrain({ rootGetters }, body) {
			axios.post(SERVER.URL + SERVER.ROUTER.train, body, rootGetters['user/config'])
        .then(({ data }) => {
          router.push({name:'REC', params:{vid: data.id}})
        })
        .catch((err) => {
          console.log(err)
        })
		},
		getTrain({ rootGetters , commit }, vid) {
			axios.get(SERVER.URL + SERVER.ROUTER.train + vid + '/', rootGetters['user/config'])
        .then(({ data }) => {
					commit('SET_TRAIN', data)
        })
        .catch((err) => {
          console.log(err)
        })
		},
		putTrain({ rootGetters, dispatch }, { index, body }) {
			axios.put(SERVER.URL + SERVER.ROUTER.train + index + '/', body, rootGetters['user/config'])
			.then(() => {
        dispatch('getTrains')
        alert('목소리 이름이 수정되었습니다.')
			})
			.catch((err) => {
				console.log(err)
			})
		},
		delTrain({ rootGetters, dispatch }, vid) {
			axios.delete(SERVER.URL + SERVER.ROUTER.train + vid + '/', rootGetters['user/config'])
        .then(() => {
          dispatch('getTrains')
          alert('목소리가 삭제되었습니다.')
        })
        .catch((err) => {
          console.log(err)
        })
		},
		startTrain({ rootGetters }, vid) {
			axios.post(SERVER.URL + SERVER.ROUTER.train + vid + '/', null, rootGetters['user/config'])
        .then(() => {
          router.push({name:'Voice'})
					alert('학습을 시작합니다.')
        })
        .catch((err) => {
          console.log(err)
        })
		},
		postCaption({ rootGetters }, { vid, cid, file }) {
			const formData = new FormData()
			formData.append('file', file, 'voice.wav')
			axios.post(SERVER.URL + SERVER.ROUTER.train + vid + '/' + cid + '/', formData, rootGetters['user/formconfig'])
        .then(() => {	
        })
        .catch((err) => {
          console.log(err)
        })
		},
		delCaption({ rootGetters }, { vid, cid }) {
			axios.delete(SERVER.URL + SERVER.ROUTER.train + vid + '/' + cid + '/', rootGetters['user/config'])
        .then(() => {
        })
        .catch((err) => {
          console.log(err)
        })
		},
		getVoices({ rootGetters , commit }) {
			axios.get(SERVER.URL + SERVER.ROUTER.voice, rootGetters['user/config'])
        .then(({ data }) => {
					commit('SET_VOICES', data)
        })
        .catch((err) => {
          console.log(err)
        })
		},
		putVoice({ rootGetters, dispatch }, { index, body }) {
			axios.put(SERVER.URL + SERVER.ROUTER.voice + 'voice/' + index + '/', body, rootGetters['user/config'])
			.then(() => {
        dispatch('getVoices')
        alert('목소리 이름이 수정되었습니다.')
			})
			.catch((err) => {
				console.log(err)
			})
		},
		delVoice({ rootGetters, dispatch }, vid) {
			axios.delete(SERVER.URL + SERVER.ROUTER.voice + 'voice/' + vid + '/', rootGetters['user/config'])
        .then(() => {
          dispatch('getVoices')
          alert('목소리가 삭제되었습니다.')
        })
        .catch((err) => {
          console.log(err)
        })
		},
		postVoice({ rootGetters, dispatch }, vid) {
			axios.post(SERVER.URL + SERVER.ROUTER.voice + 'voice/' + vid + '/', null, rootGetters['user/config'])
			.then(() => {
        dispatch('user/getUserInfo', null, { root: true })
        alert('현재 목소리가 변경되었습니다.')
			})
			.catch((err) => {
				console.log(err)
			})
		}
	}
}