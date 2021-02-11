<template>
  <v-card>
    <v-card-text>
      <v-card-title class="white--text mt-8">
        <p class="ml-3">
          {{ list.title }}
        </p>
      </v-card-title>

      <div class="font-weight-bold ml-8 mb-2">
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