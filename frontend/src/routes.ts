import { RouteRecordRaw } from 'vue-router'
import Home from '~/pages/index.vue'
import Login from '~/pages/Login/index.vue'
import { store } from '~/modules/store'

const isNotLoggedIn = (to, from, next) => {
  if (!store.getters.isLoggedIn) {
    next()
    return
  }
  next('/')
}

const isLoggedIn = (to, from, next) => {
  if (store.getters.isLoggedIn) {
    next()
    return
  }
  next('/login')
}

export const appRoutes: RouteRecordRaw[] = [
  {
    path: '/',
    component: Home,
    beforeEnter: isLoggedIn,
  },
  {
    path: '/login',
    component: Login,
    beforeEnter: isNotLoggedIn,
  },
]
