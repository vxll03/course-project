<template>
  <div class="page-container">
    <Header></Header>
    <div class="book-container">
      <div class="top">
        <h1>НАЗВАНИЕ КНИГИ | АВТОР АВТОРОВ АВТОРОВИЧ</h1>
      </div>
      <div class="bot">
        <div class="left-block">
          <div class="left">
            <img src="@/assets/img/placeholder.png" alt="ОБЛОЖКА КНИГИ" />
            <p>Здесь какая-то инфа по обложке мб</p>
            <Button text="Купить" :colorSet="greenColor" />
          </div>
          <div class="center">
            <h3>Описание</h3>
            <p>
              тут текста многотут текста многотут текста многотут текста многотут
              текста многотут текста много тут текста многотут текста многотут
              текста многотут текста многотут текста многотут текста много тут
              текста многотут текста многотут текста многотут текста многотут
              текста многотут текста много тут текста многотут текста многотут
              текста многотут текста многотут текста многотут текста много
            </p>
            <h3>Похожие товары</h3>
            <div class="suggest-books">
              <BookCard
                v-for="book in suggest"
                :title="book.title"
                :text="book.text"
                :price="book.price"
              />
            </div>
          </div>  
        </div>
        <div class="right-block">
          <ChatBlock></ChatBlock>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/molecule/Header.vue";
import BookCard from "@/components/molecule/BookCard.vue";
import type { Ref } from "vue";
import { ref } from "vue";
import type { IBook } from "@/services/ApiInterfaces";
import Button from "@/components/atom/Button.vue";
import { greenColor } from "@/services/ColorSet";
import ChatBlock from '@/components/molecule/ChatBlock.vue';

const suggest: Ref<IBook[]> = ref([
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
  {
    title: "Название книги",
    text: "Краткое описание в 100 символов обрезаное но тут очень много текста прям слишком",
    price: 1520.2,
    img: null,
  },
]);
</script>

<style lang="scss" scoped>
@use "@/assets/style/variables" as *;
.book-container {
  width: 100%;
  height: 80vh;

  margin-top: 2vh;

  border-radius: 20px;
  background: $white;
}

.top {
  width: 97%;
  height: 8%;
  display: flex;
  align-items: center;
  padding: 1% 0 0 3%;
}

.bot {
  width: 100%;
  height: 90%;
  margin-top: 1%;

  display: flex;
  flex-direction: row;
}

.left {
  width: 35%;
  height: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  img {
    width: 80%;
    height: 50vh;
    border-radius: 10px;
    border: 4px solid $gray;
  }
}

.center {
  width: 63%;
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: start;

  h3 {
    margin: 0;
    padding: 0;
  }
}

.suggest-books {
  height: 60%;
  margin-top: 2%;

  display: flex;
  flex-direction: row;
  gap: 10px;

  overflow-x: auto;
}

.left-block {
  width: 67%;
  height: 100%;

  display: flex;
  flex-direction: row;
}

.right-block {
  position: relative;
  width: 32%;
  height: 100%;
  margin-left: 10px;
}
.right-block::before {
  content: '';
  position: absolute;
  left: -1vw;
  width: 2px;
  height: 85%;
  background: #00000050;
  border-radius: 5px;
}
</style>
