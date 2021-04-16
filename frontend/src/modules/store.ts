import { createStore, Store, useStore as useVuexStore } from 'vuex'
import { InjectionKey } from 'vue'
import { UserModule } from '~/types'

// define your typings for the store state
export interface State {
  loggedIn: boolean
}

// define injection key
export const key: InjectionKey<Store<State>> = Symbol('vuex injection key for ts')

export const store = createStore<State>({
  state() {
    return {
      loggedIn: false,
    }
  },
  getters: {
    isLoggedIn: state => state.loggedIn,
  },
  mutations: {
    rawUpdateSessionState(state, newLoggedIn) {
      state.loggedIn = newLoggedIn
    },
  },
})

export const install: UserModule = ({ app, router, isClient }) => {
  fetch('/api/logged_in')
    .then(rawResponse => rawResponse.json())
    .then((data) => {
      store.commit('rawUpdateSessionState', data.response)
    })

  app.use(store, key)
}

export function useStore() {
  return useVuexStore(key)
}
