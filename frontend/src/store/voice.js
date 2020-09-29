import axios from 'axios'
import SERVER from '@/api/drf'
// import router from '@/router'

export default {
	namespaced: true,

	state: {
		script: '',
	},
	mutations: {
		SET_SCRIPT(state, payload) {
			state.script = payload
		}
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
	}
}