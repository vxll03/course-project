import { createApp } from 'vue'
import App from './App.vue'
import './assets/style/_base.scss'
import router from './services/VueRouter'

createApp(App).use(router).mount('#app')
