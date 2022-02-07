import { createWebHistory, createRouter } from "vue-router";
const routes =  [
  {
    path: "/",
    alias: "/user_list",
    name: "user_list",
    component: () => import("./components/UserList")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("./components/AddUser")
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
