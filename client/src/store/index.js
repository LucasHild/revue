import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import UsersService from '@/services/UsersService'


Vue.use(Vuex)

export default new Vuex.Store({
    plugins: [createPersistedState()],

    state: {
        token: null,
        user: null,
        isUserLoggedIn: false,
        subscribedSubvues: []
    },

    mutations: {
        setToken(state, token) {
            state.token = token
            if (token) {
                state.isUserLoggedIn = true
            } else {
                state.isUserLoggedIn = false
            }
        },
        setUser(state, user) {
            state.user = user
        },
        setSubscribedSubvues(state, subvues) {
            state.subscribedSubvues = subvues
        }
    },

    actions: {
        setToken({ commit }, token) {
            commit('setToken', token)
        },
        setUser({ commit }, user) {
            commit('setUser', user)
        },
        updateSubscribedSubvues({ commit, state }, subscribedOptional) {
            if (state.isUserLoggedIn) {
                if (subscribedOptional) {
                    // If data was provided
                    commit('setSubscribedSubvues', subscribedOptional)
                } else {
                    UsersService.username(state.user.username)
                        .then(response => {
                            commit('setSubscribedSubvues', response.data.subscribed)
                        })
                        .catch(() => {
                            // console.error(e)
                        })
                }
            }
        }
    },

    modules: {
    }
})
