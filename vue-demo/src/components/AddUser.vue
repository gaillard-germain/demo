<template>

  <div class="submit-form">
    <h3>Create New user</h3>
    <div v-if="!submitted">
      <div class="form-group">
        <label for="username">Username</label>
        <input
          type="text"
          class="form-control"
          id="username"
          required
          v-model="user.username"
          name="username"
        />
      </div>

      <div class="form-group">
        <label for="hometown">Hometown</label>
        <input
          type="text"
          class="form-control"
          id="hometown"
          required
          v-model="user.hometown"
          name="hometown"
        />
      </div>

      <div class="form-group">
        <label for="age">Age</label>
        <input
          type="number"
          class="form-control"
          id="age"
          required
          v-model="user.age"
          name="age"
        />
      </div>
      <p class="mb-0">Gender</p>
      <div class="border rounded py-2">
        <div class="form-check form-check-inline">
          <input type="radio" class="form-check-input" id="male" value="male"
            v-model="user.gender" @change="searchBy"/>
          <label for="male" class="form-check-label">Male</label>
        </div>
        <div class="form-check form-check-inline">
          <input type="radio" class="form-check-input" id="female" value="female"
            v-model="user.gender" @change="searchBy"/>
          <label for="female" class="form-check-label">Female</label>
        </div>
      </div>
      <div class="text-center">
        <button @click="saveUser" class="btn btn-success mt-4">Submit</button>
      </div>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newUser">Add another user</button>
      <router-link to="/" class="nav-link">Back to list</router-link>
    </div>
  </div>
</template>
<script>
import DemoDataService from "../services/DemoDataService";
export default {
  name: "add-user",
  data() {
    return {
      user: {
        id: null,
        username: "",
        hometown: "",
        age: "",
        gender: ""
      },
      submitted: false
    };
  },
  methods: {
    saveUser() {
      var data = {
        user: {username: this.user.username},
        hometown: this.user.hometown,
        age: this.user.age,
        gender: this.user.gender
      };
      console.log(data)

      DemoDataService.addUser(data)
        .then(response => {
          this.user.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },

    newUser() {
      this.submitted = false;
      this.user = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
  text-align: center;
}
</style>
