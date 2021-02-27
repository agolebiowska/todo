<template>
  <v-app id="app">
    <h1 class="fs-h1 text-center">
      Todo
    </h1>

<!--    navigation-->
    <div class="nav text-center mt-3">
      <router-link class="rlink" to="/">Todos</router-link>
      <router-link class="rlink" to="/about">About</router-link>
    </div>

    <div class="main-content mt-5">
      <router-view />
    </div>
  </v-app>
</template>

<style scoped>
  .rlink {
    cursor: pointer;
    color: hotpink;
    text-decoration: none;
    padding: 14px 25px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
  }

  a.rlink:hover {
    color: #000000;
  }
</style>