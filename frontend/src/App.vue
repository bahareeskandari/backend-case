<script setup>
import { ref, onMounted } from "vue";

const API_URL = window.env?.VITE_API_URL || import.meta.env.VITE_API_URL;
console.log("Runtime API URL:", API_URL);
console.log("window.env", window.env);

// Start a CPU-intensive task
const startTask = async () => {
  console.log("API_URL", API_URL);
  try {
    const response = await fetch(`${API_URL}/start-task/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ n: 2000 }),
    });

    const data = await response.json();
    console.log("data", data);
    taskId.value = data.task_id;
    tasks.value.push({ id: data.task_id, status: "PENDING" });
  } catch (error) {
    console.error("Error starting task:", error);
  }
};

// Fetch task status every 3 seconds
const updateTaskStatuses = async () => {
  if (tasks.value.length === 0) return;

  const updatedTasks = await Promise.all(
    tasks.value.map(async (task) => {
      const response = await fetch(`${API_URL}/task-status/${task.id}`);
      const data = await response.json();
      console.log("update data", data);
      return { id: task.id, status: data.status };
    })
  );

  tasks.value = updatedTasks;
};

// Automatically poll for task updates
onMounted(() => {
  setInterval(updateTaskStatuses, 3000);
});
</script>

<template>
  <div style="padding: 20px; font-family: Arial">
    <h1>FastAPI & Celery Task Manager {{ API_URL }}</h1>
    <button @click="startTask" style="padding: 10px; font-size: 16px">Start Task</button>

    <h2>Task Status:</h2>
    <ul>
      <li v-for="task in tasks" :key="task.id">Task ID: {{ task.id }} - Status: {{ task.status }}</li>
    </ul>
  </div>
</template>
