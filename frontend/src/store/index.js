import { createStore } from "vuex"
import axios from "axios";

export default createStore ({
    state: {
        token: '',
        isAuthenticated: false,
        userName: '',
        isSuperUser: false,
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                axios.defaults.headers.common['Authorization'] = "Token " + state.token
                state.isAuthenticated = true
                this.dispatch('fetchUser')
            } else {
                state.token = ''
                axios.defaults.headers.common['Authorization'] = ''
                state.isAuthenticated = false
                state.userName = ''
            }
        },
        setToken(state, token) {
            state.token = token
            localStorage.setItem("token", token)
            axios.defaults.headers.common['Authorization'] = "Token " + token
            state.isAuthenticated = true
            this.dispatch('fetchUser')
        },
        removeToken(state) {
            state.token = ''
            axios.defaults.headers.common['Authorization'] = ''
            state.isAuthenticated = false
            state.userName = ''
            state.isSuperUser = false
            localStorage.clear()
        },
        setUserName(state, userName) {
            state.userName = userName
        },
        setIsSuperUser(state, isSuperUser) {
            state.isSuperUser = isSuperUser
        }
    },
    actions: {
        async fetchUser ({ state, commit }) {
            if (state.token) {
                try {
                    const response  = await axios.get('/api/auth/users/me/');
                    commit('setUserName', response.data.username)
                    commit('setIsSuperUser', response.data.is_superuser)
                } catch(e) {
                    console.log(e)
                }
            }
        }
    },
    getters: {
        userName(state) {
            return state.userName
        },
        isSuperUser(state) {
            return state.isSuperUser
        }
    },
    modules: {

    },
})