<script lang="ts" setup="props">
import { defineProps } from 'vue'

defineProps({
  text: String,
})
</script>

<template>
  <button
    class="bg-black hover:bg-white hover:text-black text-white border-true-gray-400 hover:border-white border rounded p-1.5 px-5 inline-block duration-150"
  >
    {{ text }}
  </button>
</template>
