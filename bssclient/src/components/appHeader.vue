<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
</template>

<script>
export default {
  name: "appHeader",
  props: {
    title: String,
  },
  components: {},
};
</script>

<style scoped>
@import url("https://fonts.cdnfonts.com/css/oleo-script");
header {
  padding: 10px;
  text-align: center;
  width: 100%;
  font-family: "Oleo Script", sans-serif;
  background-color: rgb(34, 56, 77);
}

h1 {
  font-size: 35px;
  color: rgb(210, 218, 223);
}
</style>
