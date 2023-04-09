import { createRouter, createWebHistory } from 'vue-router'; // Import the createRouter and createWebHistory functions
import {createApp} from 'vue';
import App from './App.vue';
import Home from './components/Home.vue';
import Data from './components/Data.vue';
import Vuex from 'vuex';

// Define routes
const routes = [
  { path: '/', component: Home },
  { path: '/data', component: Data }
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes
});

const store = new Vuex.Store({
  state: {
    tasks: [], // The list of tasks
  },
  mutations: {
    setTasks(state, tasks) {
      state.tasks = tasks;
    },
    addTask(state, task) {
      state.tasks.push(task);
    },
  },
  actions: {
    fetchTasks(context) {
      // Make API call to fetch tasks
      // Update the state using the setTasks mutation
      fetch('http://localhost:8000/tasks')
        .then(response => response.json())
        .then(tasks => {
          context.commit('setTasks', tasks);
        })
        .catch(error => console.error('Error fetching tasks:', error));
    },
    addTask(context, task) {
    	console.log(task);
      // Make API call to add task
      // Update the state using the addTask mutation
      fetch('http://localhost:8000/tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(task),
      })
        .then(response => response.json())
        .then(newTask => {
          context.commit('addTask', newTask);
        })
        .catch(error => console.error('Error adding task:', error));
    },
  },
});


createApp(App) // Use createApp to create the Vue app instance
  .use(router) // Use the VueRouter plugin
  .use(store)
  .mount('#app'); // Mount the app to the DOM