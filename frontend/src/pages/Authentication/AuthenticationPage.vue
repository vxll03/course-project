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
          @input="(event: { target: { value: string; }; }) => authData.login = event.target.value"
        ></Input>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Пароль"
          type="password"
          @input="(event: { target: { value: string; }; }) => authData.password = event.target.value"
        ></Input>
        <Button text="Войти" @click="Authenticate"></Button>
      </div>
      <div class="block registration">
        <h3>Регистрация</h3>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Логин"
          type="text"
          @input="(event: { target: { value: string; }; }) => registerData.login = event.target.value"
        ></Input>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Пароль"
          type="password"
          @input="(event: { target: { value: string; }; }) => registerData.password1 = event.target.value"
        ></Input>
        <Input
          :size="{ width: '70%', height: '4vh' }"
          placeholder="Повтор пароля"
          type="password"
          @input="(event: { target: { value: string; }; }) => registerData.password2 = event.target.value"
        ></Input>
        <Button text="Зарегистрироваться" @click="Register"></Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { login, register } from "@/api/authApi";
import Button from "@/components/atom/Button.vue";
import Input from "@/components/atom/Input.vue";
import { useUserStore } from "@/stores/userStore";
import type { AxiosResponse } from "axios";
import { ref, type Ref } from "vue";
import { useRouter } from "vue-router";
import { toast } from "vue3-toastify";

const router = useRouter();
const currentRoute = router.currentRoute.value;
const neededRoute: string | undefined = currentRoute.fullPath.split("auth")[0];
const authData = ref({
  login: "",
  password: "",
});
const registerData: Ref<Record<string, string>> = ref({
  login: "",
  password1: "",
  password2: "",
});
const userStore = useUserStore();

const goBack = () => router.push(neededRoute ?? "/");

const Authenticate = async () => {
  try {
    const response: AxiosResponse = await login(
      authData.value.login ?? "",
      authData.value.password ?? ""
    );
    if (response.status === 200 || response.status === 201) {
      userStore.isAuth = true;
      localStorage.setItem("isAuth", "true");
      router.push(neededRoute ?? "/");
    }
  } catch (error: any) {
    toast.error(`Ошибка авторизации`);
  }
};

const Register = async () => {
  try {
    const response = await register(
      registerData.value.login ?? "",
      registerData.value.password1 ?? "",
      registerData.value.password2 ?? ""
    );
    if (response.status === 201) {
      userStore.isAuth = true;
      localStorage.setItem("isAuth", "true");
      router.push(neededRoute ?? "");
    }
  } catch (error: any) {
    toast.error("Ошибка регистрации");
  }
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
