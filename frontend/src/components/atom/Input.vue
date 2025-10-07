<template>
  <div
    class="input-container"
    :style="customStyle"
  >
    <input :type="props.type" :placeholder="props.placeholder" />
    <img v-if="props.img" :src="imgPath" alt="img" />
  </div>
</template>

<script setup lang="ts">
import { grayColor, type ColorSet } from "@/services/ColorSet";
import type { Size } from "@/services/BasicInterfaces";
import { ref } from "vue";

interface Props {
  placeholder?: string;
  img?: string;
  type: string;
  colorSet?: ColorSet;
  size?: Size | null;
}
const props = withDefaults(defineProps<Props>(), {
  placeholder: "Введите текст",
  colorSet: () => grayColor,
});

const imgPath = `src/assets/img/${props.img}`;
const customStyle = ref({});
customStyle.value = Object.assign({}, props.colorSet?.unpack(), {
  '--width': props.size?.width,
  '--height': props.size?.height
});

</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;
.input-container {
  --width: 50vw;
  --height: 4vh;

  width: var(--width);
  height: var(--height);

  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;

  background: var(--back);
  border-radius: 10px;
  color: $black;
  border: 2px solid var(--border);

  transition: 0.5s all;

  &:focus-within {
    border: 2px solid $accent;
  }

  &:focus-within img {
    opacity: 1;
  }

  input {
    height: 100%;
    width: 100%;
    border: none;
    background: #00000000;
    border-radius: inherit;
    padding-left: 8px;
    &:focus {
      outline: none;
    }
    &:focus .input-container {
      border: 20px solid black;
    }
  }

  img {
    height: 90%;
    cursor: pointer;
    color: var(--fore);
    margin-right: 4px;
    border-radius: inherit;
    opacity: 0.5;
    transition: 0.5s all;
  }
}
</style>
