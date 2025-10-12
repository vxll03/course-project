<template>
  <div class="header-container">
    <div class="logo">
      <img src="@/assets/img/logo.png" alt="Logo" @click="goToMain"/>
    </div>
    <div class="search">
      <Input type="text" img="search.svg" placeholder="Введите книгу" />
    </div>
    <div class="nav">
      <Button text="Каталог" />
      <Button text="Корзина" />
      <Button text="Закладки" />
      <Button v-if="!userStore.isAuth" text="Войти" :colorSet="greenColor" @click="goToAuth" />
      <Button v-if="userStore.isAuth" text="Выйти" :colorSet="greenColor" @click="exit" />
    </div>
  </div>
</template>

<script setup lang="ts">
import Button from "@/components/atom/Button.vue";
import { greenColor } from "@/services/ColorSet";
import Input from "../atom/Input.vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/userStore";
import { logout } from "@/api/authApi";

const router = useRouter()
const userStore = useUserStore();

const goToAuth = () => {
  router.push('/auth')
}
const goToMain = () => {
  router.push('/')
}
const exit = async () => {
  const response = await logout()
  if (response.status === 200) {
    userStore.logout();
  }
}
</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;
.header-container {
  width: 100%;
  height: 12vh;

  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;

  border-radius: 20px;
  background: $white;
}

.logo {
  img {
    height: 12vh;
  }
}

.search {
  width: 45%;
  height: 12vh;

  display: flex;
  align-items: center;

  input {
    width: 100%;
  }
}

.nav {
  width: 40%;

  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}
</style>
