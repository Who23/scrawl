<script setup lang="ts">
import { useHead } from '@vueuse/head'
import { useRouter } from 'vue-router'
import { useStore } from '~/modules/store'

const router = useRouter()
const store = useStore()

// https://github.com/vueuse/head
// you can use this to manipulate the document head in any components,
// they will be rendered correctly in the html results with vite-ssg
useHead({
  title: 'Vitesse',
  meta: [{ name: 'description', content: 'Opinionated Vite Starter Template' }],
})

// if we get logged in or logged out,
// go back to index route and vue-router will
// take care of it
store.subscribe((mutation, state) => {
  router.push('/')
})

</script>

<template>
  <router-view />
</template>
