<script lang="ts" setup>
import Button from '~/components/Button.vue'
import DarkMode from '~/components/DarkMode.vue'
import { useStore } from '~/modules/store'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()

function logout() {
  store.commit('logout')
  router.push('/login')
}
</script>

<template>
  <div class="absolute right-0"><DarkMode></DarkMode></div>
  <div class="flex flex-1 flex-col justify-center items-center h-full w-full">
    <h1 class="font-size text-7xl pb-10">signed in :)</h1>
    <Button text="Sign out" @click="logout"></Button>
  </div>
</template>