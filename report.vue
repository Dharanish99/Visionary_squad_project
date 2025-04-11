<template>
  <div class="report-page">
    <section class="report-hero">
      <div class="overlay">
        <h1 class="title">Report a Missing Person</h1>
        <p class="subtitle">Help bring someone home by providing detailed information.</p>
      </div>
    </section>

    <section class="report-form-section">
      <form @submit.prevent="submitReport" class="report-form">
        <div class="form-group">
          <label>Full Name</label>
          <input type="text" v-model="form.name" required />
        </div>

        <div class="form-group">
          <label>Age</label>
          <input type="number" v-model="form.age" required />
        </div>

        <div class="form-group">
          <label>Last Seen Location</label>
          <input type="text" v-model="form.lastSeen" required />
        </div>

        <div class="form-group">
          <label>Date & Time Last Seen</label>
          <input type="datetime-local" v-model="form.datetime" required />
        </div>

        <div class="appearance-title">Appearance Details</div>

        <div class="form-group">
          <label>Dress Color</label>
          <input type="text" v-model="form.dressColor" />
        </div>

        <div class="form-group">
          <label>Hair Color</label>
          <input type="text" v-model="form.hairColor" />
        </div>

        <div class="form-group">
          <label>Height (cm)</label>
          <input type="number" v-model="form.height" />
        </div>

        <div class="form-group">
          <label>Weight (kg)</label>
          <input type="number" v-model="form.weight" />
        </div>

        <div class="form-group">
          <label>Face Color</label>
          <input type="text" v-model="form.faceColor" />
        </div>

        <div class="form-group">
          <label>Upload Recent Photo</label>
          <input type="file" accept="image/*" @change="handlePhoto" />
        </div>

        <div class="form-group">
          <label>Additional Details</label>
          <textarea v-model="form.details" rows="4"></textarea>
        </div>

        <div class="form-group">
          <button type="submit">Submit Report</button>
        </div>
      </form>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  age: '',
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

const handlePhoto = (e) => {
  form.value.photo = e.target.files[0]
}

const submitReport = () => {
  console.log('Form submitted:', form.value)
  alert('Thank you. The report has been submitted!')
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
  background: url('C:\Users\jshre\Downloads\family-reunion-nuxt (1)\assets\images\family-hugging.jpg') no-repeat center center/cover;
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

input, textarea {
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
