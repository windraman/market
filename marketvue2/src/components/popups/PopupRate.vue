<template>
  <div
    class="modal fade"
    id="modal"
    tabindex="-1"
    aria-labelledby="modalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="modalLabel">RATING</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <star-rating style="margin: auto" :starSize="40" v-model="rating" />
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            @click="this.rating = 0"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary" @click="saveRating()">
            Save changes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      rating: 0,
      useritem: {},
      username: "",
      userid: 0,
      product_id: 0,
    };
  },
  props: {
    title: String,
  },
  methods: {
    async saveRating() {
      this.useritem = JSON.parse(sessionStorage.getItem("user"));
      this.username = this.useritem.name;
      this.userid = this.useritem.id;
      this.product_id = sessionStorage.getItem("product_id");
      //   console.log(this.product_id, this.userid, this.rating);
      var bodyFormData = new FormData();

      bodyFormData.append("product_id", parseInt(this.product_id));
      bodyFormData.append("user_id", this.userid);
      bodyFormData.append("rate", this.rating);

      await fetch({
        method: "post",
        url: "http://127.0.0.1:8000/rating",
        body: bodyFormData,
        headers: { "Content-Type": "application/json" },
      })
        .then(function (response) {
          //handle response
          console.log(response);
          window.location.href = "/home";
        })
        .catch(function (response) {
          //handle error
          console.log(response);
        });
      this.rating = 0;
    },
  },
};
</script>