import { createApp } from "vue";
import App from "./App.vue";
import LoginPlayer from "./views/Login.vue";
import GamePage from "./views/Game.vue";

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
createApp(App).use(router).mount("#app");
