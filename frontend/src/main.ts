import { createApp } from 'vue'
import App from './App.vue'
import './assets/style/_base.scss'
import router from './services/VueRouter'
import Vue3Toastify, { type ToastContainerOptions } from 'vue3-toastify';
import { createPinia } from 'pinia';

createApp(App).use(router).use(Vue3Toastify, {
  autoClose: 3000,
} as ToastContainerOptions).use(createPinia()).mount('#app')
