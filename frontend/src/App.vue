<template>
  <div class="app-wrapper">
    <div class="content-wrapper">
      <Header />
      <MainPage></MainPage>
    </div>
  </div>
</template>

<script setup lang="ts">
import Header from "./components/compose/Header.vue";
import MainPage from "@/pages/MainPage/MainPage.vue";
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
  margin-top: 3vh;
  border-radius: 20px;
}
</style>
