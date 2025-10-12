import { getCurrentUser } from "@/api/authApi";
import { defineStore } from "pinia";
import { ref, type Ref } from "vue";

export const useUserStore = defineStore("user_store", () => {
  const isAuth: Ref<boolean> = ref(false);
  const userId: Ref<number> = ref(Number.MIN_SAFE_INTEGER);


  const Initialize = async () => {
    const response = await getCurrentUser();
    isAuth.value = true;
    userId.value = response.data.content.id;
    localStorage.setItem('userId', String(response.data.content.id));
    localStorage.setItem("isAuth", "true");
  };
  const auth = async () => {
    isAuth.value = true;
    localStorage.setItem("isAuth", "true");
  };
  const logout = async () => {
    isAuth.value = false;
    localStorage.setItem("isAuth", "false");
  };

  return { isAuth, userId, Initialize, auth, logout };
});
