<template>
  <section v-if="errored">
    <p>We're sorry, we're not able to retrieve this information at the moment,
      please try back later</p>
  </section>
  <section v-else>
    <div v-if="loading">
      <Spinner />
    </div>
    <div v-else>
      <ListItem v-bind:list="list"/>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import ListItem from "@/components/ListItem"
import Spinner from '../components/Spinner.vue'

export default {
  name: "Item",
  components: {
    ListItem,
    Spinner
  },
  data() {
    return {
      endpoint: process.env.VUE_APP_API_URL + 'lists/',
      list: null,
      loading: true,
      errored: false,
    };
  },
  mounted() {
    // Get list by id after component gets mounted
    const id = this.$route.params.id
    axios
        .get(this.endpoint + id)
        .then((response) => {
          this.list = response.data;
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