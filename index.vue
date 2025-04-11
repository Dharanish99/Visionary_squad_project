<template>
  <div class="events-page">
    <section class="hero">
      <div class="overlay">
        <h1 class="hero-title">Our Journey of Reunions</h1>
        <p class="hero-subtitle">A glimpse into the events that brought hearts back together.</p>
      </div>
    </section>

    <section class="event-grid">
      <div
        v-for="(event, index) in events"
        :key="index"
        class="event-card"
        :style="`animation-delay: ${index * 0.3}s`"
      >
        <img :src="event.image" alt="event photo" class="event-img" />
        <h3>{{ event.title }}</h3>
        <p>{{ event.description }}</p>
      </div>
    </section>
  </div>
</template>

<script setup>
const events = [
  {
    title: 'Family Found Fair',
    description: 'A heartwarming fair where multiple families were reunited after years.',
    image: 'C:\Users\jshre\Downloads\family-reunion-nuxt (1)\assets\images\ChatGPT Image Apr 10, 2025, 12_15_07 PM.png',
  },
  {
    title: 'Missing to Meeting',
    description: 'An emotional event that connected lost individuals with their loved ones.',
    image: 'C:\Users\jshre\Downloads\family-reunion-nuxt (1)\assets\images\ChatGPT Image Apr 10, 2025, 12_15_07 PM.png',
  },
  {
    title: 'Hope Reunited',
    description: 'A reunion program backed by community volunteers and technology.',
    image: '/images/event3.jpg',
  },
]
</script>

<style scoped>
.events-page {
  font-family: 'Georgia', serif;   
  color: #333;
}

.hero {
  background: url('C:\Users\jshre\Downloads\family-reunion-nuxt (1)\assets\images\family-hugging.jpg') no-repeat center center/cover;
  height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  animation: fadeIn 2s ease-in-out;
}

.overlay {
  background: rgba(0, 0, 0, 0.5);
  padding: 2rem;
  text-align: center;
  color: white;
  border-radius: 1rem;
  animation: slideUp 1.5s ease-in-out;
}

.hero-title {
  font-size: 3rem;
  margin-bottom: 1rem;
  animation: fadeInDown 2s;
}

.hero-subtitle {
  font-size: 1.2rem;
  animation: fadeInUp 2s;
}

.event-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  padding: 3rem;
  animation: fadeIn 2s ease-in-out;
}

.event-card {
  background: #fff;
  border-radius: 1rem;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  padding: 1rem;
  text-align: center;
  transform: translateY(30px);
  animation: bounceInUp 1s forwards;
}

.event-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { transform: translateY(100px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-50px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(50px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes bounceInUp {
  0% {
    opacity: 0;
    transform: translateY(200px);
  }
  60% {
    opacity: 1;
    transform: translateY(-20px);
  }
  80% {
    transform: translateY(10px);
  }
  100% {
    transform: translateY(0);
  }
}
</style>




