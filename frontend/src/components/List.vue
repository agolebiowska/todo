<template>
  <v-container fluid>
    <v-row dense>
      <v-col
          v-for="list in lists"
          :key="list.id"
          cols="3"
          sm="4"
      >
        <v-card v-on:click="goToItem(list.id)"
            class="mx-auto"
            max-width="344"
            height="250"
        >
          <v-card-text>
            <p class="display-1 text--primary">
              {{ list.title }}
            </p>
            <p>{{ list.tasks.length }}</p>
            <div class="text--primary">
              {{ list.description }}
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import router from "@/router/router";

export default {
  name: "List",
  props: {
    lists: {
      type: Array,
      required: true,
    },
  },
  methods: {
    goToItem: function (id) {
      router.push({path: 'item/' + id, params: id})
    }
  }
}
</script>

<style scoped>

</style>