<template>
    <h1>Home</h1>
    <div class="cards">
      <div v-for="task in tasks" :key="task.id" class="card">
        <h2>{{ task.title }}</h2>
        <img src="https://i.pinimg.com/564x/bb/87/b7/bb87b743b9ed1dc1516a08955fe51842.jpg">
        <p>{{ task.description }}</p>
        <div class="status-purple">
          <p  class="status-text">{{ task.status }}</p>
        </div>
      </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  name: 'Home',
  data() {
    return {
    }
  },
  computed: {
    // Map tasks from the store state to a computed property
    ...mapState(['tasks']),
  },
  created() {
    this.fetchTasks();
  },
  methods: {
    // Map fetchTasks and addTask actions from the store to methods
    ...mapActions(['fetchTasks', 'addTask']),
  },
}
</script>

<style scoped>

h1{
  color: #5e5da9;
  text-align: center;
}

.status-purple {
  padding: 0.5rem;
  height: 25px;
  background-color: #5e5da9;
  border-radius: 5px;
  display: flex;
  align-items: flex-end ; /* Align vertically */
  justify-content: center; /* Align horizontally */
}

.status-text {
  color: white;
}

.cards {
  padding: 10% 0% 0% 0%;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  Justify-content: center;
}

.card {
  width:200px;
  padding: 1rem;
  color: #5e5da9;
  border-radius: 5px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column; /* To stack elements vertically */
  justify-content: space-between; /* To push status to the bottom */
  }

.card h2 {
  margin-bottom: 0.5rem;
}
.card p {
  margin-bottom: 0.5rem;
}

.card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 5px;
}
</style>