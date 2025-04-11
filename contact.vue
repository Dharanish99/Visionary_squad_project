<template>
  <div class="contact-page">
    <h1 class="title">Contact Us</h1>
    <p class="subtitle">We would love to hear from you!</p>
    <form class="contact-form" @submit.prevent="submitForm">
      <input v-model="form.name" type="text" placeholder="Your Name" required />
      <input v-model="form.email" type="email" placeholder="Your Email" required />
      <textarea v-model="form.message" rows="5" placeholder="Your Message" required></textarea>
      <button type="submit" class="submit-btn">Send Message</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  email: '',
  message: '',
})

const submitForm = () => {
  alert(`Thank you, ${form.value.name}! We'll get back to you soon.`)
  form.value = { name: '', email: '', message: '' }
}
</script>

<style scoped>
.contact-page {
  max-width: 600px;
  margin: auto;
  padding: 3rem 1rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(8px);
  border-radius: 1rem;
  animation: fadeInUp 1.5s ease-out;
  font-family: 'Georgia', serif;
  text-align: center;
  margin-top: 2rem;
}

.title {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 2rem;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1.2rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-family: 'Georgia', serif;
}

.submit-btn {
  background-color: #4a148c;
  color: #fff;
  border: none;
  padding: 0.75rem 2rem;
  font-size: 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.submit-btn:hover {
  background-color: #6a1b9a;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>

