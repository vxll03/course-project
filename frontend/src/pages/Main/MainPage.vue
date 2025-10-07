<template>
  <Header></Header>
  <div class="container">
    <div class="books-block">
      <div class="book-container">
        <BookCard
          v-for="book in newBooks"
          :title="book.title"
          :text="book.text"
          :price="book.price"
          book_id="1"
        />
      </div>
      <div class="book-container">
        <BookCard
          v-for="book in newBooks"
          :title="book.title"
          :text="book.text"
          :price="book.price"
        />
      </div>
      <div class="author-container">
        <AuthorCard
          v-for="author in bestAuthors"
          :name="author.name"
          :text="author.text"
          :bookCount="author.bookCount"
        />
      </div>
    </div>
    <div class="chat-block">
      <h3>Общий чат</h3>
      <ChatBlock>
        
      </ChatBlock>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, type Ref } from "vue";
import type { IBook, IAuthor } from "@/services/ApiInterfaces";
import BookCard from "@/components/molecule/BookCard.vue";
import AuthorCard from "@/components/molecule/AuthorCard.vue";
import ChatBlock from "@/components/molecule/ChatBlock.vue";
import Header from "@/components/molecule/Header.vue";

const newBooks: Ref<IBook[]> = ref([
  {
    title: "Название книги",
    text: "Краткое описание в 100 символов обрезаное но тут очень много текста прям слишком",
    price: 1520.2,
    img: null,
  },
  {
    title: "Название книги",
    text: "Краткое описание в 100 символов обрезаное но тут очень много текста прям слишком",
    price: 1520.2,
    img: null,
  },
  {
    title: "Название книги",
    text: "Краткое описание в 100 символов обрезаное но тут очень много текста прям слишком",
    price: 1520.2,
    img: null,
  },
]);
const bestBooks: Ref<IBook[]> = ref([]);
const bestAuthors: Ref<IAuthor[]> = ref([
  {
    name: "Автор Авторович",
    text: "Родился там в годах былых и очень крутой",
    bookCount: 150,
  },
  {
    name: "Автор Авторович",
    text: "Родился там в годах былых и очень крутой",
    bookCount: 150,
  },
  {
    name: "Автор Авторович",
    text: "Родился там в годах былых и очень крутой",
    bookCount: 150,
  },
  {
    name: "Автор Авторович",
    text: "Родился там в годах былых и очень крутой",
    bookCount: 150,
  },
]);
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
  padding: 0 10px 5px;

  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  overflow-x: auto;
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
