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
          :bookId="book.id"
        />
      </div>
      <div class="book-container">
        <BookCard
          v-for="book in bestBooks"
          :title="book.title"
          :text="book.text"
          :price="book.price"
          :bookId="book.id"
        />
      </div>
      <div class="author-container">
        <AuthorCard
          v-for="author in bestAuthors"
          :name="author.name"
          text="Здесь пока пусто"
          :bookCount="author.bookCount"
        />
      </div>
    </div>
    <div class="chat-block">
      <h3>Общий чат</h3>
      <ChatBlock> </ChatBlock>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, type Ref } from "vue";
import BookCard from "@/components/molecule/BookCard.vue";
import AuthorCard from "@/components/molecule/AuthorCard.vue";
import ChatBlock from "@/components/molecule/ChatBlock.vue";
import Header from "@/components/molecule/Header.vue";
import { getBooks } from "@/api/booksApi";
import { getAuthors } from "@/api/authorsApi";
import type { IAuthor, IBook } from "@/services/ApiInterfaces";

const newBooks: Ref<IBook[]> = ref([]);
const bestBooks: Ref<IBook[]> = ref([]);
const bestAuthors: Ref<IAuthor[]> = ref([]);

const collectBooks = async () => {
  const books = await getBooks();
  let randNum = 0;
  for (let i = 0; i < 10; i++) {
    randNum = Math.floor(Math.random() * (books.data.content.length - 0 + 1));
    newBooks.value.push({
      id: books.data.content[randNum].id,
      title: books.data.content[randNum].title,
      text: books.data.content[randNum].description,
      price: Math.floor(Math.random() * (5000 - 1000 + 1) + 1000),
    });
    randNum = Math.floor(Math.random() * (books.data.content.length - 0 + 1));
    bestBooks.value.push({
      id: books.data.content[randNum].id,
      title: books.data.content[randNum].title,
      text: books.data.content[randNum].description,
      price: Math.floor(Math.random() * (5000 - 1000 + 1) + 1000),
    });
  }
  console.log(books);
};
const collectAuthors = async () => {
  const authors = await getAuthors();
  let randNum = 0;
  let curAuthor;
  for (let i = 0; i < 4; i++) {
    randNum = Math.floor(Math.random() * (authors.data.content.length - 0 + 1));
    curAuthor = authors.data.content[randNum];
    bestAuthors.value.push({
      name: `${curAuthor.last_name} ${curAuthor.first_name}`,
      bookCount: Math.floor(Math.random() * (100 - 1 + 1) + 1),
    });
  }
};
const collectChatHistory = async () => {
  
}

onMounted(async () => {
  await collectBooks();
  await collectAuthors();
});
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
