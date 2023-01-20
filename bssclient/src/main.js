import { createApp } from "vue";
import App from "./App.vue";
import LoginPlayer from "./views/Login.vue";
import GamePage from "./views/Game.vue";
import { createStore } from "./store/index.js";
// Create a new store instance or import from module.
const store = createStore;

import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "login",
    component: LoginPlayer,
  },
  {
    path: "/game",
    name: "game",
    component: GamePage,
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
createApp(App).use(store).use(router).mount("#app");
