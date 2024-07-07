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
    <carousel :items-to-show="3">
      <slide v-for="(slide, index) in slides" :key="slide.id">
        <div class="card" style="width: 18rem">
          <img
            class="card-img-top"
            v-bind:src="slide.picture"
            alt="Card image cap"
          />
          <div class="card-body">
            <h5 class="card-title">{{ slide.name }}</h5>
            <h3>Rp. {{ slide.price }}</h3>
            <small class="card-text">{{ slide.description }}</small>
            <div class="card-text">
              <label for="rating">Rating:</label>
              <vue3-star-ratings
                style="margin: auto"
                v-model="slide.rating"
                v-bind:id="slide.id"
                :disableClick="true"
                :starSize="20"
              />
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
      </slide>
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
    <popup-rate></popup-rate>
  </div>
</template>

<script>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";
import PopupRate from "../components/popups/PopupRate.vue";
import axios from "axios";

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
  created() {
    this.useritem = JSON.parse(sessionStorage.getItem("user"));
    this.username = this.useritem.name;
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
    PopupRate,
  },
  methods: {
    getProduk: async function () {
      const response = await axios.get("http://127.0.0.1:8000/product/all");

      const data = response.data;
      console.log(data);
      this.slides = data;
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