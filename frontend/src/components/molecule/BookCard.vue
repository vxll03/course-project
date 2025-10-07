<template>
  <div class="card">
    <img :src="imgPath" alt="картинка">
    <div class="content">
      <h5>{{ title }}</h5>
      <p>{{ text }}</p>
      <div class="bottom-block">
        <span>{{ price }} Руб.</span>
        <a @click="goToBook">Перейти</a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

interface Props {
  title: string;
  text: string;
  img?: string;
  price: number;
  book_id: string;
}
const props = withDefaults(defineProps<Props>(), {
  img: "placeholder.png"
});
const imgPath = `src/assets/img/${props.img}`;

const router = useRouter();
const goToBook = () => {
  router.push(`/book/${props.book_id}`)
}

</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;

.card {
  width: 20%;
  height: 95%;
  
  min-width: 180px;  
  
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  border-radius: 10px;
  border: 4px solid $gray;
  
  img {
    height: 40%;
  }
}

.content {
  width: 100%;
  height: 60%;

  display: flex;
  flex-direction: column;
  align-items: center;  
  justify-content: space-around;

  h5, p {
    margin: 0;
  }

  p {
    font-size: 12px;
    padding: 10px;
    text-overflow: ellipsis;
  }
}

.bottom-block {
  width: 100%;

  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;

  span {
    color: $accent;
    font-size: 12px;
    cursor: pointer;
  }
  a {
    color: $black;
    text-decoration: none;
    font-size: 14px;
    cursor: pointer;
    
    transition: .4s all;
    &:hover {
      color: $accent;
    }
  }
}
</style>
