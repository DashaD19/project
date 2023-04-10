<template>
  <div id="app" class="home-container " >
    <!-- Navigation -->
    <div class="navigation">
      <img src="public/logo.png" >
      <h1 color ="#5e5da9">Aliae</h1>
      <nav>
        <router-link to="/" :class="{ 'active': $route.path === '/' }"><h3 align="center">Home</h3></router-link>
        <router-link to="/data" :class="{ 'active': $route.path === '/data' }"><h3 align="center">Data</h3></router-link>
      </nav>
    </div>
    <div class="content">

    <!-- Router View -->
    <router-view></router-view>
  </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
nav {
  display: flex;
  flex-direction: column;
}

.home-container {
  display: flex;
}

.navigation {
  width: 20%;
  color: #5e5da9;
  text-align: center;
  position: fixed;
  direction: column;
}

.navigation h3 {
  margin: 1rem 0;
  cursor: pointer;
}

.navigation .active {
  color: white;
  font-weight: bold;
  background-color: #5e5da9;
  border-radius: 0px 10px 10px 0px;
}

.content {
  width: 80%;
  background-color: #f0f0f0;
  padding: 2rem;
  min-height: 100vh; /* Add this property to make content stretch to full height */
  margin-left: 20%; /* Account for the width of the navigation */
}
</style>