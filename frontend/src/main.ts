import { ViteSSG } from 'vite-ssg'
import App from './App.vue'
import 'virtual:windi.css'
import 'virtual:windi-devtools'
import './styles/main.css'
import { appRoutes } from './routes'

// https://github.com/antfu/vite-ssg
export const createApp = ViteSSG(
  App,
  {
    routes: appRoutes,
  },
  (ctx) => {
    // install all modules under `modules/`
    Object.values(import.meta.globEager('./modules/*.ts')).map((i) =>
      i.install?.(ctx),
    )
  },
)
