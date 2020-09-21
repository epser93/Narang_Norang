import axios from 'axios'

export default {
  namespaced: true,

  state: {
    photos_1: [],
    photos_2: [],
    photos_3: [],
    page: 1,
  },

  mutations: {
    SET_POTHOS_1(state,payload){
      state.photos_1 = payload;
    },
    SET_POTHOS_2(state,payload){
      state.photos_2 = payload;
    },
    SET_POTHOS_3(state,payload){
      state.photos_3 = payload;
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

      axios.get('https://jsonplaceholder.typicode.com/photos', options)
          .then(res => {
            console.log(res.data)
            commit("SET_POTHOS_2", res.data)
          })
          .catch(err => console.error(err))

      axios.get('https://jsonplaceholder.typicode.com/photos', options)
          .then(res => {
            console.log(res.data)
            commit("SET_POTHOS_3", res.data)
          })
          .catch(err => console.error(err))
    },
  },

}