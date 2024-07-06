

<template>
  <section class="vh-100" style="background-color: #eee">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">
                    Sign in
                  </p>

                  <form class="mx-1 mx-md-4">
                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div
                        data-mdb-input-init
                        class="form-outline flex-fill mb-0"
                      >
                        <label class="form-label" for="form3Example1c"
                          >Your Email</label
                        >
                        <input
                          type="text"
                          id="form3Example1c"
                          class="form-control"
                          v-model="email"
                        />
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div
                        data-mdb-input-init
                        class="form-outline flex-fill mb-0"
                      >
                        <label class="form-label" for="form3Example4c"
                          >Password</label
                        >
                        <input
                          type="password"
                          id="form3Example4c"
                          class="form-control"
                          v-model="password"
                        />
                      </div>
                    </div>

                    <div
                      class="d-flex justify-content-center mx-4 mb-3 mb-lg-4"
                    >
                      <button
                        type="button"
                        data-mdb-button-init
                        data-mdb-ripple-init
                        class="btn btn-primary btn-lg"
                        v-on:click="signUp"
                      >
                        LOGIN
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import md5 from "md5";
import axios from "axios";

export default {
  name: "SignIn",
  data() {
    return {
      nik: "",
      password: "",
      email: "",
    };
  },
  methods: {
    async signUp() {
      var bodyFormData = new FormData();
      bodyFormData.append("email", this.email);
      bodyFormData.append("password", this.password);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/login",
        data: bodyFormData,
        headers: { "Content-Type": "application/json" },
      })
        .then(function (response) {
          //handle success
          const data = response.data;
          console.log(data);
          if (data.id) {
            sessionStorage.setItem("user", JSON.stringify(data));
            window.location.href = "/home";
          } else {
            alert(response.detail);
          }
        })
        .catch(function (response) {
          //handle error
          console.log(response);
        });
    },
  },
};
</script>