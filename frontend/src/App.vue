<template>
  <div id="app">
    <section v-if="errored">
      <p class="error">We're sorry, we're not able to retrieve this information at the moment,
        please try back later</p>
    </section>
    <section v-else>
      <div v-if="loading">
        <Spinner />
      </div>
      <div v-else class="container">
        <List v-bind:lists="lists"/>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import List from './components/List.vue'
import Spinner from './components/Spinner.vue'

export default {
  name: 'App',
  components: {
    List,
    Spinner
  },
  data() {
    return {
      lists: [],
      loading: true,
      errored: false,
    };
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/api/lists')
      .then((response) => {
        this.lists = response.data.results;
        console.log(this.lists);
      })
      .catch((error) => {
        this.errored = true;
        console.log(error);
      })
      .finally(() => {
        this.loading = false;
      });
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
