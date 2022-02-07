import http from "../http-common";
class DemoDataService {
  getAll() {
    return http.get("/user_list");
  }
  findByFilter(hometown, age_min, age_max, gender) {
    return http.get(`/user_list?hometown=${hometown}&age_min=${age_min}&age_max=${age_max}&gender=${gender}`);
  }
  addUser(data) {
    return http.post("/user_list", data);
  }
}
export default new DemoDataService();
