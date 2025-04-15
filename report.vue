<template>
  <div class="report-container">
    <h1>Report Missing Person</h1>
    <form @submit.prevent="submitReport" class="report-form">
      <div class="form-group">
        <label>Name</label>
        <input v-model="form.name" type="text" required />
      </div>

      <div class="form-group">
        <label>Age</label>
        <input v-model="form.age" type="number" required />
      </div>

      <!-- ✅ Gender field -->
      <div class="form-group">
        <label>Gender</label>
        <select v-model="form.gender" required>
          <option value="" disabled>Select Gender</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
        </select>
      </div>

      <div class="form-group">
        <label>Last Seen Location</label>
        <input v-model="form.lastSeen" type="text" required />
      </div>

      <div class="form-group">
        <label>Date & Time Last Seen</label>
        <input v-model="form.datetime" type="datetime-local" required />
      </div>

      <div class="form-group">
        <label>Dress Color</label>
        <input v-model="form.dressColor" type="text" />
      </div>

      <div class="form-group">
        <label>Hair Color</label>
        <input v-model="form.hairColor" type="text" />
      </div>

      <div class="form-group">
        <label>Height (in cm)</label>
        <input v-model="form.height" type="number" />
      </div>

      <div class="form-group">
        <label>Weight (in kg)</label>
        <input v-model="form.weight" type="number" />
      </div>

      <div class="form-group">
        <label>Face Color</label>
        <input v-model="form.faceColor" type="text" />
      </div>

      <div class="form-group">
        <label>Photo</label>
        <input type="file" @change="e => form.photo = e.target.files[0]" required />
      </div>

      <div class="form-group">
        <label>Additional Details</label>
        <textarea v-model="form.details"></textarea>
      </div>

      <button type="submit">Submit Report</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({
  name: '',
  age: '',
  gender: '',
  lastSeen: '',
  datetime: '',
  dressColor: '',
  hairColor: '',
  height: '',
  weight: '',
  faceColor: '',
  photo: null,
  details: '',
})

// ✅ Reset form fields after submission
const resetForm = () => {
  form.value = {
    name: '',
    age: '',
    gender: '',
    lastSeen: '',
    datetime: '',
    dressColor: '',
    hairColor: '',
    height: '',
    weight: '',
    faceColor: '',
    photo: null,
    details: '',
  }
}

// ✅ Submit report to FastAPI backend
const submitReport = async () => {
  try {
    const formData = new FormData()
    formData.append('name', form.value.name)
    formData.append('age', form.value.age)
    formData.append('gender', form.value.gender)
    formData.append('lastSeen', form.value.lastSeen)
    formData.append('datetime_str', form.value.datetime)
    formData.append('dressColor', form.value.dressColor || '')
    formData.append('hairColor', form.value.hairColor || '')
    formData.append('height', form.value.height || '')
    formData.append('weight', form.value.weight || '')
    formData.append('faceColor', form.value.faceColor || '')
    formData.append('details', form.value.details || '')
    formData.append('photo', form.value.photo)

    const response = await axios.post('http://localhost:8002/report', formData)

    alert('✅ Report submitted successfully!')
    console.log(response.data)

    resetForm() // Clear fields

  } catch (error) {
    console.error('Error submitting report:', error)
    alert('Failed to submit report.')
  }
}
</script>

<style scoped>
.report-page {
  font-family: 'Georgia', serif;
  background: #f5f5f5;
  color: #333;
  animation: fadeIn 1s ease-in-out;
}

.report-hero {
  background: url('C:\\Users\\jshre\\Downloads\\family-reunion-nuxt (1)\\assets\\images\\family-hugging.jpg') no-repeat center center/cover;
  height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay {
  background: rgba(0, 0, 0, 0.6);
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  color: #fff;
}

.title {
  font-size: 2.5rem;
}

.subtitle {
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.report-form-section {
  padding: 2rem;
  max-width: 700px;
  margin: auto;
}

.appearance-title {
  font-size: 1.3rem;
  margin: 1rem 0;
  font-weight: bold;
  color: #444;
}

.report-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input, textarea, select {
  padding: 0.8rem;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

button {
  padding: 1rem;
  font-size: 1.1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

