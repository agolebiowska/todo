<template>
  <v-card
      class="mx-auto"
      max-width="344"
      height="250"
  >
    <v-card-text>
      <p class="display-1 text--primary">
        {{ list.title }}
      </p>
      <p>3/10</p>
      <div class="text--primary">
        {{ list.description }}
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "ListItem",
  props: {
    list: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>

</style>