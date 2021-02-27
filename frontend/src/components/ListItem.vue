<template>
  <v-container style="max-width: 900px">
<!--    if in edit state show input fields else show title and description-->
    <v-text-field
        v-if="isEdit"
        :label="list.title"
        v-model="editedList.title"
        :rules="['Required']"
        solo
        dense
    ></v-text-field>
    <div v-else>
      <label> {{ list.title }} </label>
      <v-btn
          v-on:click="isEdit = true;">
        Edytuj
      </v-btn>
    </div>

    <div v-if="isEdit">
      <v-text-field
          :label="list.description"
          v-model="editedList.description"
          solo
          dense
      ></v-text-field>
      <v-btn
          v-on:click="editList()">
        Zapisz
      </v-btn>
    </div>
    <div v-else>
      <label> {{ list.description }} </label>
    </div>

    <div
        style="margin-top: 20px"
        v-for="task in list.tasks"
        :key="task.id"
    >
      <v-row no-gutters>
        <v-col
            cols="2"
            sm="6"
        >
          <v-checkbox
              v-on:click="updateTask(task, !task.is_done)"
              :label="task.description"
              :input-value="task.is_done"
              color="success"
          ></v-checkbox>
        </v-col>

        <v-col
            cols="2"
            sm="6"
        >
          <v-btn
              v-on:click="deleteTask(task.id)"
              style="margin-top: 16px"
              small depressed color="error">
            Usuń
          </v-btn>
        </v-col>
      </v-row>
    </div>

    <v-row style="margin-top: 10px">
      <v-col
          cols="2"
          sm="6"
      >
        <v-text-field
            label="Nowe zadanie"
            :rules="['Required']"
            v-model="newTask"
            solo
            dense
        ></v-text-field>
      </v-col>

      <v-col
          cols="2"
          sm="6"
      >
        <v-btn
            v-on:click="addTask(newTask)">
          Dodaj
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "ListItem",
  props: {
    list: {
      type: Object,
      required: true,
    }
  },
  data: function() {
    return {
      endpoint: process.env.VUE_APP_API_URL + 'lists/',
      newTask: '',
      isEdit: false,
      editedList: {
        title: this.list.title,
        description: this.list.description
      }
    }
  },
  methods: {
    deleteTask: function (id) {
      axios
          .delete(`${this.endpoint + this.list.id}/tasks/${id}`)
          .then(() => {
            // remove deleted task from local data
            this.list.tasks = this.list.tasks.filter(x => { return x.id !== id })
          })
          .catch(() => {
          })
    },
    addTask: function (desc) {
      const task = {
        description: desc,
        task_list: this.list.id
      }
      axios
          .post(`${this.endpoint + this.list.id}/tasks/`, task)
          .then((response) => {
            // update tasks list
            this.list.tasks.push(response.data)
            // set form field back to empty
            this.newTask = ''
          })
          .catch(() => {
          })
    },
    updateTask: function (task, done) {
      task.is_done = done
      axios
          .put(`${this.endpoint + this.list.id}/tasks/${task.id}/`, task)
          .catch(() => {
          })
    },
    editList: function () {
      this.isEdit = false
      axios
          .put(`${this.endpoint + this.list.id}/`, this.editedList)
          .then(() => {
            // Update local fields with new values
            this.list.title = this.editedList.title
            this.list.description = this.editedList.description
          })
          .catch(() => {
          })
    }
  }
}
</script>

<style scoped>
</style>