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
              <v-btn
                  x-small
                  color="error"
                  v-on:click="isDelete=true;deleteList(list.id)">
                x
              </v-btn>
            </p>
            <p>{{ list.tasks.length }}</p>
            <div class="text--primary">
              {{ list.description }}
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-card v-on:click="isAdd=true"
              class="mx-auto"
              max-width="344"
              height="250"
      >
        <v-card-text>
          <div v-if="isAdd">
            <v-text-field
                label="Nazwa"
                v-model="newList.title"
                solo
                dense
            ></v-text-field>
            <v-text-field
                label="Opis"
                v-model="newList.description"
                solo
                dense
            ></v-text-field>
            <v-btn
                v-on:click="addList()">
              Zapisz
            </v-btn>
            <v-btn
                color="error"
                v-on:click="isAdd=false;">
              Anuluj
            </v-btn>
          </div>
          <v-btn v-else
              v-on:click="isAdd=true">
            Dodaj
          </v-btn>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import router from "@/router/router";
import axios from "axios";

export default {
  name: "List",
  props: {
    lists: {
      type: Array,
      required: true,
    },
  },
  data: function () {
    return {
      endpoint: process.env.VUE_APP_API_URL + 'lists/',
      isDelete: false,
      isAdd: false,
      newList: {
        title: '',
        description: ''
      }
    }
  },
  methods: {
    goToItem: function (id) {
      if (this.isDelete) return
      router.push({name: 'Item', params: {id: id}})
    },
    addList: function () {
      axios
          .post(this.endpoint, this.newList)
          .then((response) => {
            this.lists.push(response.data)
            this.isAdd = false
            console.log(response)
          })
          .catch(() => {
          })
    },
    deleteList: function (id) {
      axios
          .delete(`${this.endpoint + id}/`)
          .then((response) => {
            this.lists = this.lists.filter(x => { return x.id !== id })
            console.log(response)
          })
          .catch((error) => {
            console.log(error);
          })
          .finally(() => {
            this.newList = {
              title: '',
              description: ''
            }
            this.isDelete = false
          })
    }
  }
}
</script>

<style scoped>

</style>