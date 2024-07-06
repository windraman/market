var app = new Vue({
    el: '#app',
    data: {
        password: '',
        email: '',
        user: sessionStorage.getItem("user"),
        slides: []
    },
    methods: {
        async signUp() {
            var bodyFormData = new FormData();
            bodyFormData.append('email', this.email);
            bodyFormData.append('password', this.password);
            axios({
                method: "post",
                url: "http://127.0.0.1:8000/login",
                data: bodyFormData,
                headers: { "Content-Type": "application/json" },
            })
                .then(function (response) {
                    //handle success
                    const data = response.data
                    // console.log(data)
                    if (data.id) {
                        sessionStorage.setItem('user', JSON.stringify(data))
                        // window.location.href = '/'
                    } else {
                        alert(response.detail);
                    }
                })
                .catch(function (response) {
                    //handle error
                    console.log(response);
                })
        },
        getProduk: async function () {
            axios({
                method: "get",
                url: 'http://127.0.0.1:8000/product/all',
            })
                .then(function (response) {
                    //handle success
                    const data = response.data
                    console.log(data)
                    if (data.length > 0) {
                        this.slides = data
                        const carousel = new bootstrap.Carousel('#myCarousel')
                    }
                })
                .catch(function (response) {
                    //handle error
                    console.log(response);
                })
        },
    },
    mounted: function () {
        if (sessionStorage.getItem('user')) {
            this.getProduk()
        }
    },
    created() {
        // sessionStorage.setItem('user', '')
    }
})