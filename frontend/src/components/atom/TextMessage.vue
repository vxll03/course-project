<template>
<div class="message-container">
  <div class="message-head">
    <h5>Чел ваще йоу да</h5>
    <p>5.10.2025</p>
  </div>
  <div class="message-text">
    <p>
      тут текст и увеличиваться должно все
    </p>
  </div>
</div>  
</template>

<script setup lang="ts">

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
  h5, p{
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