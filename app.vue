<!-- Example HTML structure for Nuxt 3 with enhancements -->
<!-- Example HTML structure for Nuxt 3 with enhancements -->
<template>
  <div class="page-container">
    <header>
      <nav class="navbar">
        <NuxtLink to="/login" class="nav-link">Login</NuxtLink>
        <NuxtLink to="/" class="nav-link">Home</NuxtLink>
        
        <!--NuxtLink to="/about" class="nav-link">About</NuxtLink-->
        <NuxtLink to="/report" class="nav-link">Report</NuxtLink>
        <NuxtLink to="/search" class="nav-link">Search</NuxtLink>
        <!--NuxtLink to="/events" class="nav-link">Events</NuxtLink-->
        <NuxtLink to="/gallery" class="nav-link">Gallery</NuxtLink>
        <NuxtLink to="/contact" class="nav-link">Contact</NuxtLink>
        
        <NuxtLink to="/chatbot" class="nav-link">Chatbot</NuxtLink>

      </nav>
    </header>

    <main>
      <NuxtPage />
    </main>

    <footer class="footer">
      <p>© 2025 Family Reunion. All rights reserved.</p>
    </footer>
  </div>
</template>

<style scoped>
.page-container {
  background: url("/images/family-hugging.jpg") no-repeat center center/cover;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  animation: fadeIn 2s ease-in-out;
}

.navbar {
  display: flex;
  justify-content: center;
  gap: 2rem;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  animation: slideDown 1s ease-in-out;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-link {
  color: #fff;
  font-weight: bold;
  text-decoration: none;
  transition: color 0.3s ease, transform 0.3s ease;
}

.nav-link:hover {
  color: #ffc107;
  transform: scale(1.1);
}

.footer {
  text-align: center;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 1rem;
  font-size: 0.9rem;
  animation: fadeIn 1.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideDown {
  from { transform: translateY(-100%); }
  to { transform: translateY(0); }
}
</style>

<script setup>
// JavaScript enhancements (if needed)
</script>

<!-- Ensure image is placed at /public/images/family-hugging.jpg -->

