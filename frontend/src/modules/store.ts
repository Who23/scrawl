import { createStore, Store, useStore as useVuexStore } from 'vuex'
import { InjectionKey } from 'vue'
import { UserModule } from '~/types'

// define your typings for the store state
export interface State {
  token: string
}

// define injection key
export const key: InjectionKey<Store<State>> = Symbol('vuex injection key for ts')

export const store = createStore<State>({
  state() {
    return {
      token: '',
    }
  },
  getters: {
    isLoggedIn: state => state.token !== '',
  },
  mutations: {
    fromLocalStorage(state) {
      state.token = localStorage.getItem('token') || ''
    },
    login(state) {
      state.token = 'hello'
      localStorage.setItem('token', state.token)
    },
    logout(state) {
      state.token = ''
      localStorage.setItem('token', state.token)
    },
  },
})

export const install: UserModule = ({ app, router, isClient }) => {
  app.use(store, key)
}

export function useStore() {
  return useVuexStore(key)
}
