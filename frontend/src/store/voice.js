import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

export default {
	namespaced: true,

	state: {
		script: '',
		trains: '',
		train: '',
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
					console.log(data)
          commit('SET_TRAIN', data)
        })
        .catch((err) => {
          console.log(err)
        })
		},
	}
}