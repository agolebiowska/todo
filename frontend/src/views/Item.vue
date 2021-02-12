<template>
  <section v-if="errored">
    <p>We're sorry, we're not able to retrieve this information at the moment,
      please try back later</p>
  </section>
  <section v-else>
    <div v-if="loading">
      <Spinner />
    </div>
    <ListItem :list="list"/>
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
      list: null,
      loading: true,
      errored: false,
    };
  },
  mounted() {
    axios
        .get('http://127.0.0.1:8000/api/lists/' + 1)
        .then((response) => {
          this.list = response.data;
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

<style scoped>

</style>