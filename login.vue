<template>
  <div class="login-page">
    <div class="login-box">
      <h1>Login</h1>
      <input type="email" v-model="email" placeholder="Email" />
      <input type="password" v-model="password" placeholder="Password" />
      <button @click="login">Login</button>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = () => {
  if (email.value === 'user@example.com' && password.value === '123456') {
    localStorage.setItem('loggedIn', 'true')
    router.push('/')
  } else {
    error.value = 'Invalid credentials. Try again.'
  }
  const loggedIn = useCookie('loggedIn')
loggedIn.value = true  // This marks the user as authenticated

}
</script>

<style scoped>
.login-page {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
  font-family: 'Georgia', serif;
  animation: fadeIn 2s ease;
}

.login-box {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  width: 300px;
  text-align: center;
  animation: bounceIn 1s;
}

input {
  width: 100%;
  padding: 0.8rem;
  margin: 1rem 0;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
  transition: 0.3s;
}

input:focus {
  border-color: #fda085;
  outline: none;
}

button {
  background: #fda085;
  border: none;
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}

button:hover {
  background: #f6a265;
}

.error {
  color: red;
  margin-top: 1rem;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes bounceIn {
  0% { transform: scale(0.5); opacity: 0; }
  60% { transform: scale(1.1); opacity: 1; }
  80% { transform: scale(0.9); }
  100% { transform: scale(1); }
}
</style>


  