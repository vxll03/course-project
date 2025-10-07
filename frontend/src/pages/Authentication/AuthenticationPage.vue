<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="back" @click="goBack">
        <img src="@/assets/img/back.svg" alt="Назад" />
      </div>

      <div class="block authentication">
        <h3>Авторизация</h3>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Логин"
          type="text"
        ></Input>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Пароль"
          type="password"
        ></Input>
        <Button text="Войти"></Button>
      </div>
      <div class="block registration">
        <h3>Регистрация</h3>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Логин"
          type="text"
        ></Input>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Пароль"
          type="password"
        ></Input>
        <Button text="Зарегистрироваться"></Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Button from "@/components/atom/Button.vue";
import Input from "@/components/atom/Input.vue";
import { useRouter } from "vue-router";

const router = useRouter();

const goBack = () => {
  const currentRoute = router.currentRoute.value;
  const neededRoute: string | undefined =
    currentRoute.fullPath.split("auth")[0];
  router.push(neededRoute ?? "/");
};
</script>

<style lang="scss" scoped>
@use "@/assets/style/variables" as *;
.auth-page {
  width: 100%;
  height: 90vh;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.auth-container {
  position: relative;
  width: 60%;
  height: 40%;

  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;

  border-radius: 20px;
  border: 2px solid $accent;
  background: $white;
}
.back {
  position: absolute;
  top: 6px;
  right: 10px;
  width: 32px;
  height: 32px;

  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;
  z-index: 1;
  img {
    height: 32px;
  }
}

.block {
  position: relative;
  width: 50%;
  height: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
}
.authentication::after {
  content: "";
  position: absolute;
  top: 20%;
  right: 0;

  width: 2px;
  height: 60%;
  background: #00000050;
  border-radius: 5px;
}
</style>
