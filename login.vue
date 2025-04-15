<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('user@example.com')
const password = ref('123456')
const error = ref('')
const router = useRouter()

const login = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: email.value,
        password: password.value
      })
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.detail || 'Login failed')
    }

    const data = await response.json()
    
    localStorage.setItem('auth_token', data.access_token)
    localStorage.setItem('user_email', email.value)
    
    router.push('/')
  } catch (err) {
    error.value = err.message
    console.error('Login error:', err)
  }
}
</script>

<template>
  <!-- Keep your existing template exactly as is -->
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

<style scoped>
/* Keep all your existing styles exactly as is */
.login-page {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
  font-family: 'Georgia', serif;
  animation: fadeIn 0.6s ease-out;
}

.login-box {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  width: 300px;
  text-align: center;
  animation: smoothAppear 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  opacity: 0;
}

input {
  width: 100%;
  padding: 12px 15px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 25px;
  font-size: 14px;
  transition: all 0.3s;
  box-sizing: border-box;
}

input:focus {
  outline: none;
  border-color: #fda085;
  box-shadow: 0 0 0 2px rgba(253, 160, 133, 0.2);
}

button {
  background: #fda085;
  border: none;
  color: white;
  padding: 12px 20px;
  border-radius: 25px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
  width: 100%;
  margin-top: 10px;
}

button:hover {
  background: #f6a265;
}

.error {
  color: red;
  margin-top: 1rem;
}

@keyframes fadeIn {
  from { 
    opacity: 0;
    transform: translateY(20px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes smoothAppear {
  0% {
    opacity: 0;
    transform: scale(0.98);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
</style>


  
