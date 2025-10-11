import { defineStore } from "pinia";

export const useUserStore = defineStore('user_store', () => {
  const isAuth = false;

  return { isAuth }
})