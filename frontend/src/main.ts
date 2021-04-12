import '@fontsource/inter/500.css'
import '@fontsource/inter/900.css'
import 'virtual:windi.css'
import 'virtual:windi-devtools'
import './styles/main.css'
import { ViteSSG } from 'vite-ssg'
import { appRoutes } from './routes'
import { store } from '~/modules/store'
import App from '~/App.vue'

store.commit('fromLocalStorage')

// https://github.com/antfu/vite-ssg
export const createApp = ViteSSG(
  App,
  {
    routes: appRoutes,
  },
  (ctx) => {
    // install all modules under `modules/`
    Object.values(import.meta.globEager('./modules/*.ts')).map(i =>
      i.install?.(ctx),
    )
  },
)
