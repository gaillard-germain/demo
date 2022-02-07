<template>
  <div class="row border">
    <div class="col-12 text-center py-2">
      Filter users by
    </div>
    <div class="form-group col-md-6">
      <input type="text" class="form-control" placeholder="hometown"
        v-model="hometown" @input="searchBy"/>
    </div>
    <div class="form-group col">
      <input type="number" class="form-control" placeholder="age mini"
        v-model="age_min" @input="searchBy"/>
    </div>
    <div class="form-group col">
      <input type="number" class="form-control" placeholder="age maxi"
        v-model="age_max" @input="searchBy"/>
    </div>
    <div class="form-row col-12 text-center py-2">
      <div class="form-check form-check-inline">
        <input type="radio" class="form-check-input" id="male" value="male"
          v-model="gender" @change="searchBy"/>
        <label for="male" class="form-check-label">Male</label>
      </div>
      <div class="form-check form-check-inline">
        <input type="radio" class="form-check-input" id="female" value="female"
          v-model="gender" @change="searchBy"/>
        <label for="female" class="form-check-label">Female</label>
      </div>
      <div class="form-check form-check-inline">
        <input type="radio" class="form-check-input" id="both" value=""
          v-model="gender" @change="searchBy"/>
        <label for="both" class="form-check-label">Both</label>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6 py-4 px-4">
      <h4>Users List</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(user, index) in users"
          :key="index"
          @click="setActiveUser(user, index)"
        >
          {{ user.user.username }}
        </li>
      </ul>
    </div>
    <div class="col-md-6 py-4 px-4">
      <div v-if="currentUser">
        <h4>{{ currentUser.user.username }}</h4>
        <div>
          <label>Hometown:</label> {{ currentUser.hometown }}
        </div>
        <div>
          <label>age:</label> {{ currentUser.age }}
        </div>
        <div>
          <label>gender:</label> {{ currentUser.gender }}
        </div>
      </div>
      <div v-else>
        <p>Please click on a user to display details...</p>
      </div>
    </div>
  </div>
</template>
<script>
import DemoDataService from "../services/DemoDataService";
export default {
  name: "user-list",
  data() {
    return {
      users: [],
      currentUser: null,
      currentIndex: -1,
      hometown: "",
      age_min: "",
      age_max: "",
      gender: ""
    };
  },
  methods: {
    retrieveUsers() {
      DemoDataService.getAll()
        .then(response => {
          this.users = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveUsers();
      this.currentUser = null;
      this.currentIndex = -1;
    },
    setActiveUser(user, index) {
      this.currentUser = user;
      this.currentIndex = user ? index : -1;
    },

    searchBy() {
      DemoDataService.findByFilter(
        this.hometown,
        this.age_min,
        this.age_max,
        this.gender
      )
        .then(response => {
          this.users = response.data;
          this.setActiveUser(null);
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveUsers();
  }
};
</script>
