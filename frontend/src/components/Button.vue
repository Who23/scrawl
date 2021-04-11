<script lang="ts" setup="props">
import { defineProps } from 'vue'

defineProps({
  text: String,
})
</script>

<template>
  <button
    class="dark:bg-black dark:text-white bg-white text-black dark:hover:bg-white dark:hover:text-black border dark:hover:border-white hover:bg-black hover:text-white hover:border-black dark:border-true-gray-400 border-true-gray-500 border rounded p-1.5 px-5 inline-block duration-150"
  >
    {{ text }}
  </button>
</template>
