<template>
  <v-container fluid>
    <section v-if="errored">
      <p>We're sorry, we're not able to retrieve this information at the moment,
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
  </v-container>
</template>

<script>
import axios from 'axios'
import List from '../components/List.vue'
import Spinner from '../components/Spinner.vue'

export default {
  name: 'Home',
  components: {
    List,
    Spinner
  },
  data() {
    return {
      endpoint: process.env.VUE_APP_API_URL + 'lists',
      lists: [],
      loading: true,
      errored: false,
    };
  },
  mounted() {
    axios
        .get(this.endpoint)
        .then((response) => {
          this.lists = response.data.results;
        })
        .catch(() => {
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });
  },
}
</script>

<style scoped>
</style>