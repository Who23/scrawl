<script lang="ts" setup="props">
import { isDark, toggleDark } from '~/logic/dark'
</script>

<template>
  <button @click="toggleDark">
    <clarity-moon-solid v-if="!isDark" />
    <eva-sun-fill v-else />
  </button>
</template>
