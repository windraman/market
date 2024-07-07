<template>
  <div>
    <div>
      <h1>Home</h1>
      <p>Welcome {{ username }}</p>
      <button type="button" class="btn btn-danger" @click="logout()">
        <i class="fa fa-lock"></i>
        Logout
      </button>
    </div>
    <br />
    <div class="row">
      <div class="col-sm" v-for="(slide, index) in slides" :key="slide.id">
        <div class="card" style="width: 18rem">
          <img
            class="card-img-top"
            v-bind:src="`.${slide.picture}`"
            alt="Card image cap"
          />
          <div class="card-body">
            <h5 class="card-title">{{ slide.name }}</h5>
            <h3>Rp. {{ slide.price }}</h3>
            <small class="card-text">{{ slide.description }}</small>
            <div class="card-text">
              <label for="rating">Rating:</label>
              <star-rating
                style="margin: auto"
                :increment="0.5"
                :star-size="20"
                v-model="slide.rating"
                v-bind:id="slide.id"
                :disableClick="true"
              ></star-rating>
            </div>
            <br />
            <button
              type="button"
              class="btn btn-primary"
              data-bs-toggle="modal"
              data-bs-target="#modal"
              @mouseover="selectedSlide = index"
              @click="addToSelected()"
            >
              Rate This
            </button>
          </div>
        </div>
      </div>
    </div>

    <popup-rate></popup-rate>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import PopupRate from "./popups/PopupRate.vue";

export default {
  name: "Home",
  username: "",
  useritem: {},
  data() {
    return {
      slides: [],
      showModal: false,
      selectedSlide: 0,
    };
  },
  components: {
    StarRating,
    PopupRate,
  },
  created() {
    this.useritem = JSON.parse(sessionStorage.getItem("user"));
    this.username = this.useritem.name;
  },
  methods: {
    getProduk: async function () {
      const response = await fetch("http://127.0.0.1:8000/product/all")
        .then((response) => response.json())
        .then((data) => {
          this.slides = data;
        })
        .catch(function (response) {
          //handle error
          console.log(response);
        });
    },
    addToSelected() {
      sessionStorage.setItem("product_id", this.slides[this.selectedSlide].id);
    },
    logout() {
      sessionStorage.setItem("product_id", 0);
      sessionStorage.setItem("user", "");
      window.location.href = "/";
    },
  },
  mounted: function () {
    this.getProduk();
  },
};
</script>