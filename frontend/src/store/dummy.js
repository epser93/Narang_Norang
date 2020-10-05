import axios from 'axios'
// import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    photos_1: [],
    page: 1,
  },

  mutations: {
    SET_POTHOS_1(state,payload){
      state.photos_1 = payload;
    },
  },

  actions: {
    getPhotos({ state, commit }) {
      const options = {
        params: {
          _page: state.page++,
          _limit: 3,
        }
      }
      axios.get('https://jsonplaceholder.typicode.com/photos', options)
          .then(res => {
            console.log(res.data)
            commit("SET_POTHOS_1", res.data)
          })
          .catch(err => console.error(err))
    }
  },

}