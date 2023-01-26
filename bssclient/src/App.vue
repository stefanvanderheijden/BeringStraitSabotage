<template>
  <div class="container">
    <appHeader title="Bering Strait Sabotage" subtitle="By Umit and Stefan" />
    <windowMain title="Construction Plan" author="SVDH" scale="1:1000" rev="3B">
      <cardLane
        titleTop="Bridge Sections"
        :cardLane="$store.state.democratic_lane"
        primaryColor="#6DD544"
        secondaryColor="#B6DA93"
        titleBottom=""
      />
      <cardLane
        titleTop=""
        :cardLane="$store.state.fascist_lane"
        primaryColor="#8D5723"
        secondaryColor="#C2946F"
        titleBottom="Construction Errors"
      />
      <infoBox />
    </windowMain>
  </div>
</template>

<script>
import cardLane from "./components/cardLane.vue";
import infoBox from "./components/infoBox.vue";
import "./assets/style.css";
import appHeader from "./components/appHeader.vue";
import windowMain from "./components/window/windowMain.vue";
export default {
  name: "App",
  components: {
    appHeader,
    windowMain,
    cardLane,
    infoBox,
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
.container {
  max-width: 500px;
  margin: 0px auto;
  overflow: auto;
}
</style>
