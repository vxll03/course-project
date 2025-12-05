<template>
  <div class="app-wrapper">
    <div class="content-wrapper">
        <RouterView />
    </div>
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
import { useUserStore } from './stores/userStore';
import 'vue3-toastify/dist/index.css';
import { onMounted } from "vue";

const userStore = useUserStore();
onMounted(() => {
  userStore.isAuth = localStorage.getItem('isAuth') == 'true'
  userStore.userId = Number(localStorage.getItem('userId'))
})
</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;
.app-wrapper {
  width: 100%;
  height: auto;
  min-height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: center;
}
.content-wrapper {
  width: 80%;
  height: auto;
  margin-top: 10px;
  border-radius: 20px;
}
</style>
