<template>
  <div class="chat-container">
    <div class="message-block">
      <TextMessage></TextMessage>
      <TextMessage class="my"></TextMessage>
      <TextMessage class="my"></TextMessage>
      <TextMessage></TextMessage>
      <TextMessage class="my"></TextMessage>
      <TextMessage></TextMessage>
      <TextMessage></TextMessage>
      <TextMessage class="my"></TextMessage>
      <TextMessage class="my"></TextMessage>
      <TextMessage></TextMessage>
      <TextMessage class="my"></TextMessage>
      <TextMessage></TextMessage>
    </div>
    <div class="control-block">
      <Input :size="{width: '68%', height: '4vh'}" type="text"></Input>
      <Button text="Отправить"></Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import Input from '../atom/Input.vue';
import Button from '../atom/Button.vue';
import TextMessage from '../atom/TextMessage.vue';

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
