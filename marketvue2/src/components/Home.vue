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
    <carousel :perPage="4">
      <slide
        data-index="0"
        data-name="ProductSlide"
        v-for="(slide, index) in slides"
        :key="slide.id"
      >
        <div class="card" style="width: 18rem">
          <img class="card-img-top" :src="slide.picture" alt="Card image cap" />
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
                :show-rating="false"
              ></star-rating>
            </div>
            <br />
            <button
              type="button"
              class="btn btn-primary"
              @mouseover="selectedSlide = index"
              @click="addToSelected(`${slide.id}`)"
            >
              Rate This
            </button>
          </div>
        </div>
      </slide>
    </carousel>
    <Timbul name="example">This is an example</Timbul>
    <!-- <popup-rate></popup-rate> -->
    <Timbul name="popup" style="height: auto">
      <div class="card">
        <div class="card-header">Rating</div>
        <div class="card-body">
          <star-rating
            style="margin: auto"
            :increment="0.5"
            :star-size="40"
            :show-rating="true"
          ></star-rating>
        </div>
      </div>
    </Timbul>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import PopupRate from "./popups/PopupRate.vue";
import { Carousel, Slide } from "vue-carousel";

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
    Carousel,
    Slide,
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
    addToSelected(id) {
      sessionStorage.setItem("product_id", this.slides[this.selectedSlide].id);
      this.$modal.show("popup");
    },
    logout() {
      sessionStorage.setItem("product_id", 0);
      sessionStorage.setItem("user", "");
      window.location.href = "/";
    },
  },
  mounted: function () {
    this.getProduk();
    // this.$modal.show("example");
  },
};
</script>