<template>
<div class="container">
  <div class="books-block">
    <div class="book-container">
      <div class="book" v-for="book in newBooks">
        {{ book }}
      </div>
    </div>
    <div class="book-container">
      <div class="book" v-for="book in newBooks">
        {{ book }}
      </div>
    </div>
    <div class="author-container">
      <div class="book" v-for="book in newBooks">
        {{ book }}
      </div>
    </div>
  </div>
  <div class="chat-block">
    <h3>Общий чат</h3>
    <div class="chat">
      asd
    </div>
  </div>
</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const newBooks = ref({});
const bestBooks = ref({});
const bestAuthors = ref({});
</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;
.container {
  width: 100%;
  height: 92vh;
  margin-top: 1vh;

  display: flex;
  flex-direction: row;
  justify-content: space-between;

  border-radius: 20px;
}

.books-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;

  width: 65%;
  height: 100%;

  border-radius: inherit;

  background: $white;
}

.book-container,
.author-container {
  width: 96%;
  height: 29vh;
  background: #00000050;
  border-radius: 20px;
}

.chat-block {
  height: 100%;
  width: 34%;

  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: inherit;

  background: $white;
}

.chat {
  width: 93%;
  height: 90%;

  border-radius: 20px;
  padding: 10px;

  background: #00000050;
}
</style>
