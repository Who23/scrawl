/* eslint-disable import/no-duplicates */
import { ComponentCustomProperties } from 'vue'
import { Store } from 'vuex'

declare interface Window {
  // extend the window
}

// declare vue files as components
declare module '*.vue' {
  import { ComponentOptions } from 'vue'
  const component: ComponentOptions
  export default component
}

declare module '@vue/runtime-core' {
  // declare your own store states
  interface State {
    token: String
  }

  // provide typings for `this.$store`
  interface ComponentCustomProperties {
    $store: Store<State>
  }
}
