<template>
  <div class="data-container">
    <h1>Data</h1>
    <form @submit.prevent="addTask(newTask); clearInputs()">
      <div class="form-container">
        <input v-model="newTask.title" type="text" id="title"  placeholder="title" class="input-field" required>
        <input v-model="newTask.description" type="text" placeholder="description" id="description" class="input-field"  required>
        <select v-model="newTask.status" id="status" class="input-field" required>
          <option selected>nouveau</option>
          <option>non lu</option>
          <option>lu</option>
        </select>
        <button type="submit"  class="add-button">Ajouter</button>
     </div>
   </form>
 

    <table class="data-table">
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Status</th>
      </tr>
      <tr v-for="task in tasks" :key="task.id" >
        <td>{{ task.title }}</td>
        <td>{{ task.description }}</td>
        <td>{{ task.status }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Data',
  data() {
    return {
      newTask: { title: '', description: '', status: '' } // New task to be added
    }
  },
  computed: {
    // Map tasks from the store state to a computed property
    ...mapState(['tasks']),
  },
  methods: {
    // Map fetchTasks and addTask actions from the store to methods
    ...mapActions(['fetchTasks', 'addTask']),
    clearInputs(){
      this.newTask = { title: '', description: '', status: '' };
    }
  }
}
</script>


<style scoped>

h1 {
  color: #5e5da9;
  text-align: center
}

.form-container {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  padding: 0% 20% 10% 20%;
}

.input-field {
  padding: 0.5rem;
  border-radius: 30px;
  border: 2px solid #5e5da9;
}

.add-button {
  background-color: #5e5da9;
  color: white;
  border-radius: 30px;
  padding: 0.5rem;
  cursor: pointer;
  width: 120px; /* Update width to make button bigger */
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th,
.data-table td {
  border-bottom: 1px solid #5e5da9;
  padding: 0.5rem;
  text-align: center;
  color: #5e5da9;
}

</style>