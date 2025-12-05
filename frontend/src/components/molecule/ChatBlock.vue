<template>
  <div class="chat-container">
    <div class="message-block">
      <TextMessage
        v-for="message in messages"
        :key="message.id"
        :author="message.author"
        :date="message.timestamp"
        :text="message.text"
        :class="message.author == userStore.userId ? 'my' : 'other'"
      >
      </TextMessage>
    </div>
    <div class="control-block" v-if="ws">
      <Input
        :size="{ width: '68%', height: '4vh' }"
        type="text"
        v-model="currentMessage"
      ></Input>
      <Button text="Отправить" @click="sendMessage"></Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import Input from "../atom/Input.vue";
import Button from "../atom/Button.vue";
import TextMessage from "../atom/TextMessage.vue";
import { getChatHistory } from "@/api/chatApi";
import { onBeforeUnmount, ref, watch, type Ref } from "vue";
import type { Message } from "@/services/ApiInterfaces";
import { useUserStore } from "@/stores/userStore";

interface Props {
  chatName: string;
}
const props = defineProps<Props>();
const chatId = ref();
const ws = ref();
const userStore = useUserStore();

const messages: Ref<Message[]> = ref([]);
const currentMessage = ref("");

const collectChatHistory = async () => {
  const response = await getChatHistory(props.chatName);
  chatId.value = response.data.content.id;
  messages.value = response.data.content.messages as Message[];
};

const sendMessage = async () => {
  if (ws.value && ws.value.readyState === WebSocket.OPEN) {
    if (currentMessage.value.length >= 5) ws.value.send(currentMessage.value);
    currentMessage.value = "";
  }
};

watch(
  () => props.chatName,
  async () => {
    await collectChatHistory();
    if (userStore.userId) {
      ws.value = new WebSocket(
        `ws://localhost:8001/chat/connect/${chatId.value}/?user_id=${userStore.userId}`
      );
    } else {
      ws.value = new WebSocket(
        `ws://localhost:8001/chat/connect/${chatId.value}/?user_id=${userStore.userId}`
      );
    }

    ws.value.onopen = () => console.log("WebSocket connected");

    ws.value.onmessage = (event: any) => {
      console.log(event);
      messages.value.push(JSON.parse(event.data));
    };
  },
  { immediate: true }
);

onBeforeUnmount(async () => {
  ws.value.close();
});
</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;
.chat-container {
  width: 95%;
  height: 90%;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.message-block {
  width: 100%;
  height: 94%;
  gap: 10px;

  display: flex;
  flex-direction: column;

  overflow-y: auto;
  scrollbar-width: none;
}

.my {
  margin-left: 1vw;
}

.control-block {
  width: 100%;
  height: 5%;

  display: flex;
  flex-direction: row;
  justify-content: space-between;

  background: $white;
}
</style>