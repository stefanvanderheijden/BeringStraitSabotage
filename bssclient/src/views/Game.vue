<template>
  <div>Hello from the game page</div>
  <playerField> </playerField>
</template>

<script>
import playerField from "../components/playerField.vue";
export default {
  name: "GamePage",
  components: {
    playerField,
  },
};
</script>
