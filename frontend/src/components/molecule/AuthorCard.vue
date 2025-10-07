<template>
  <div class="card">
    <img :src="imgPath" alt="картинка">
    <div class="content">
      <h5>{{ name }}</h5>
      <p>{{ text }}</p>
      <div class="bottom-block">
        <span>{{ bookCount }} Книг</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  name: string;
  text: string;
  img?: string;
  bookCount: number;
}
const props = withDefaults(defineProps<Props>(), {
  img: "placeholder.png"
});
const imgPath = `src/assets/img/${props.img}`;

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
}
</style>
