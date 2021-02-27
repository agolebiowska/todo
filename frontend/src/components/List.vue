<template>
  <v-container fluid>
    <v-row dense>
<!--      Loop through lists and display cards-->
      <v-col
          v-for="list in lists"
          :key="list.id"
          cols="3"
          sm="4"
      >
        <v-card v-on:click="goToItem(list.id)"
              style="width: 250px;height: 250px"
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
<!--            Display number of finished tasks-->
            <p>{{ getDoneTasksNumber(list.tasks) }}/{{ list.tasks.length }}</p>
            <div class="text--primary">
              {{ list.description }}
            </div>
          </v-card-text>
        </v-card>
      </v-col>
<!--      Add list form-->
      <v-card v-on:click="isAdd=true"
              style="width: 250px;height: 250px"
      >
        <v-card-text>
          <div v-if="isAdd">
            <v-text-field
                :rules="['Required']"
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
      // when we click on delete button we don't want to go to item page
      if (this.isDelete) return

      router.push({name: 'Item', params: {id: id}})
    },
    addList: function () {
      axios
          .post(this.endpoint, this.newList)
          .then((response) => {
            this.lists.push(response.data)
            this.isAdd = false
          })
          .catch(() => {
          })
          .finally(() => {
            this.newList = {
              title: '',
              description: ''
            }
          })
    },
    deleteList: function (id) {
      axios
          .delete(`${this.endpoint + id}/`)
          .then(() => {
            // after deleting a list in api also remove from it local data
            this.lists = this.lists.filter(x => { return x.id !== id })
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
    },
    // Get number of done tasks for a list
    getDoneTasksNumber(tasks) {
      return tasks.filter(task => { return task.is_done }).length
    }
  }
}
</script>

<style scoped>
</style>