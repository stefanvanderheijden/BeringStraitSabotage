<template>
  <div class="container">
    <appHeader title="Bering Strait Sabotage" />
    <!-- <router-link to="/">Login</router-link>
    <router-link to="/game">Game</router-link> -->
    <router-view />
  </div>
</template>

<script>
import appHeader from "./components/appHeader.vue";
export default {
  name: "App",
  components: {
    appHeader,
  },
  data: function () {
    return {
      players: [
        {
          id: 1,
          name: "Player 1",
          emoticon: "😀",
        },
        {
          id: 2,
          name: "Player 2",
          emoticon: "😀",
        },
        {
          id: 3,
          name: "Player 3",
          emoticon: "😀",
        },
        {
          id: 4,
          name: "Player 4",
          emoticon: "😀",
        },
      ],
    };
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: "Poppins", sans-serif;
}
.container {
  max-width: 500px;
  height: 100vh;
  margin: 0px auto;
  overflow: auto;
  min-height: 300px;
  background-color: #d2dadf;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3);
  padding-bottom: 50px;
  background-image: url("./assets/iceCold.jpg");
  background-size: cover;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
