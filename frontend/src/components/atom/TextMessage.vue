<template>
  <div class="message-container">
    <div class="message-head">
      <h5>{{ messageAuthor }}</h5>
      <p>{{ date }}</p>
    </div>
    <div class="message-text">
      <p>{{ text }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { getUserById } from "@/api/authApi";
import { onMounted, ref, type Ref } from "vue";

interface Props {
  author: number | string;
  text: string;
  date: string;
}
const props = defineProps<Props>();
const messageAuthor: Ref<string> = ref("Неизвестный пользователь");

onMounted(async () => {
  if (typeof props.author === "number")
    messageAuthor.value =
      (await getUserById(props.author)).data.content.username ??
      "Неизвестный пользователь";
});
</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;
.message-container {
  width: 90%;
  height: auto;
  padding: 10px;

  border-radius: 10px;
  border: 3px solid $accent;
}

.message-head {
  width: 100%;
  height: auto;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  h5,
  p {
    margin: 0;
  }
  p {
    font-size: 14px;
  }
}

.message-text {
  font-size: 14px;
  p {
    margin: 10px 0 0 0;
  }
}
</style>
