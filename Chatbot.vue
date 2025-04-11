<template>
    <div class="bg-white shadow-lg rounded p-4 w-full max-w-md mx-auto mt-6">
      <div class="h-64 overflow-y-auto mb-4">
        <div v-for="(msg, index) in messages" :key="index" class="mb-2">
          <p :class="msg.user ? 'text-right text-blue-600' : 'text-left text-gray-600'">{{ msg.text }}</p>
        </div>
      </div>
      <input
        v-model="input"
        @keyup.enter="sendMessage"
        class="border p-2 w-full rounded"
        placeholder="Ask something..."
      />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  const input = ref('')
  const messages = ref([{ text: 'Hello! How can I help you?', user: false }])
  
  function sendMessage() {
    if (!input.value) return
    messages.value.push({ text: input.value, user: true })
    setTimeout(() => {
      messages.value.push({ text: "I'm just a demo bot 🤖", user: false })
    }, 1000)
    input.value = ''
  }
  </script>
  