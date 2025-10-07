import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/pages/Main/MainPage.vue"),
  },
  {
    path: "/auth",
    name: "Authentication",
    component: () => import ("@/pages/Authentication/AuthenticationPage.vue")
  },
  {
    path: "/book/:id",
    name: "BookInfo",
    component: () => import ("@/pages/Book/BookPage.vue")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
