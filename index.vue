<template>
  <div class="home-wrapper">
    <!-- Hero section with intro text -->
    <section class="hero">
      <div class="hero-overlay">
        <h1 class="title">Reuniting Families</h1>
        <p class="subtitle">Find your loved ones with our missing person tracker</p>
      </div>
    </section>

    <!-- Animated procedure section -->
    <section class="procedure">
      <h2 class="section-title">How It Works</h2>
      <div class="steps">
        <div class="step" v-for="(step, i) in steps" :key="i" :style="{ animationDelay: `${i * 0.4}s` }">
          <h3>{{ step.title }}</h3>
          <p>{{ step.desc }}</p>
        </div>
      </div>
    </section>

    <!-- Animated bottom navigation -->
    <section class="bottom-nav">
      <NuxtLink to="/search" class="nav-box search">🔍 Search Person</NuxtLink>
      <NuxtLink to="/report" class="nav-box report">📢 Report Missing</NuxtLink>
    </section>
  </div>
</template>

<script setup>
const steps = [
  { title: "1. Report", desc: "Submit missing person details including name, photo, and last seen location." },
  { title: "2. Search", desc: "Browse or search through reported persons and found individuals." },
  { title: "3. Connect", desc: "Contact authorities or listed family once someone is identified." },
  { title: "4. Reunite", desc: "Bring families back together and update the case status." }
]
</script>

<style scoped>
.home-wrapper {
  font-family: 'Georgia', serif;
  color: #333;
  padding: 2rem;
}

.hero {
  background: linear-gradient(to right,  #444,  #444);
  padding: 4rem 2rem;
  text-align: center;
  animation: fadeIn 4s ease-in;
  border-radius: 1rem;
  margin-bottom: 3rem;
}

.hero-overlay .title {
  font-size: 3rem;
  color: white;
  margin-bottom: 1rem;
  animation: slideInDown 4s ease;
}

.hero-overlay .subtitle {
  font-size: 1.2rem;
  color: #fff;
  animation: slideInUp 1.2s ease;
}

.procedure {
  text-align: center;
  margin: 4rem 0;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 2rem;
  animation: fadeIn 2s ease;
}

.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
}

.step {
  background: #fefefe;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  transition: transform 2s ease;
  animation: bounceInUp 1.5s ease forwards;
  opacity: 0;
}
.step:hover {
  transform: translateY(-10px);
}

.bottom-nav {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 3rem;
  animation: fadeInUp 4s ease;
}

.nav-box {
  padding: 1.5rem 2.5rem;
  background:  #444;
  color: white;
  border-radius: 1rem;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  box-shadow: 0 8px 20px rgba(0,0,0,0.2);
  transition: transform 0.3s ease, background 0.3s ease;
}
.nav-box:hover {
  transform: scale(1.05);
  background:  #444;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInDown {
  from { opacity: 0; transform: translateY(-30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes bounceInUp {
  0% { opacity: 0; transform: translateY(100px); }
  60% { opacity: 1; transform: translateY(-20px); }
  80% { transform: translateY(10px); }
  100% { transform: translateY(0); }
}
</style>




