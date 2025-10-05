<template>
  <div class="btn-container" :style="customStyle">
    <img src="" alt="" />
    {{ props.text }}
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { mainColor, type ColorSet } from "@/services/ColorSet";

// Props
interface Props {
  text: string;
  img?: string;
  colorSet?: ColorSet;
}
const props = withDefaults(defineProps<Props>(), {
  isBorder: false,
  colorSet: () => mainColor,
});

// Refs
const customStyle = ref({});
customStyle.value = {
  "--back": props.colorSet.background,
  "--fore": props.colorSet.border,
  "--border": props.colorSet.border,
};
</script>

<style scoped lang="scss">
@use "@/assets/style/variables" as *;

.btn-container {
  width: 7vw;
  height: 4vh;

  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;

  background: var(--back);
  color: var(--fore);
  border: 3px solid var(--border);
  border-radius: 12px;

  cursor: pointer;

  transition: 0.4s all;
  &:hover {
    background: var(--border);
    color: var(--back);
  }
}
</style>
