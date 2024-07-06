import { createApp, onMounted } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.css'
import router from './routers'
import vue3StarRatings from "vue3-star-ratings";

const app = createApp(App)

app.component("vue3-star-ratings", vue3StarRatings)
app.use(router)
app.mount('#app')

