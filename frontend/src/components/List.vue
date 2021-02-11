<template>
  <v-container fluid>
    <v-row dense>
      <v-col
          v-for="list in lists"
          :key="list.id"
      >
        <v-card>
          <ListItem v-bind:list="list"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ListItem from "@/components/ListItem";

export default {
  name: "List",
  components: {ListItem},
  props: {
    lists: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped>

</style>