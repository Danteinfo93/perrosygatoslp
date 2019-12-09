import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    adoptions: []
  },
  mutations: {
  },
  actions: {

    getAdoptions(){
      const path = 'localhost:80000/api/v1.0/adoptions' 
      Axios.get(path).then((response) => {
        this.adoptions = response.data
      })
      .catch((error) => {
        console.log(error)
      }) 
    }
  },
  modules: {
  }
})
