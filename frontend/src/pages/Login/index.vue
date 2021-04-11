<script setup lang="ts">
import Button from '~/components/Button.vue'
import { useStore } from '~/modules/store'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()

function login() {
  store.commit('login')
  router.push('/')
}
</script>

<template>
  <div class="absolute right-0"><DarkMode></DarkMode></div>
  <div class="flex flex-col flex-1 items-center justify-center h-full w-full">
    <h1 class="font-size text-7xl pb-10">Sign in.</h1>
    <Button text="Login with Google" @click="login"></Button>
  </div>
</template>
