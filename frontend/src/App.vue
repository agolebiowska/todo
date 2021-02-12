<template>
  <v-app id="app">
    <h1 class="fs-h1 text-center">
      Todo
    </h1>

    <div class="nav text-center mt-3">
      <router-link to="/">Todos</router-link>
      <router-link to="/about">About</router-link>
    </div>

    <div class="main-content mt-5">
      <router-view />
    </div>
  </v-app>
</template>
