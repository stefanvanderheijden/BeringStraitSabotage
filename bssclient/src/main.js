import { createApp } from "vue";
import App from "./App.vue";
import LoginPlayer from "./views/Login.vue";
import GamePage from "./views/Game.vue";
import { store } from "./store/store.js";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "game",
    component: GamePage,
  },
  {
    path: "/login",
    name: "login",
    component: LoginPlayer,
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
createApp(App).use(store).use(router).mount("#app");
