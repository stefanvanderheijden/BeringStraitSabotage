// Vue component for the info box

<template>
  <div class="infoBox">{{ $store.state.infoBox.message }}</div>
</template>

<script>
export default {
  name: "infoBox",
  components: {},
  computed: {},
};
</script>

<style scoped>
.infoBox {
  white-space: pre-wrap;
  border: 2px solid white;

  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
  background-color: rgb(34, 56, 77);
  color: rgb(210, 218, 223);
  /* background-image: radial-gradient(rgba(0, 150, 0, 0.75), black 120%); */
  width: 70%;
  height: 60px;
  overflow: hidden;
  padding: 0.5rem;
  text-align: left;
  font: 0.7rem Inconsolata, monospace;
  text-shadow: 0 0 5px #ffffff;
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.4);
}

::selection {
  background: #0080ff;
  text-shadow: none;
}
pre {
  margin: 0;
}
</style>
