import { createApp } from 'vue'
import App from './App'
// import components from '@/components/UI';
import router from "@/router/router";
// import VIntersection from "@/directives/VIntersection";
// import directives from "@/directives";
import store from "@/store";
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from "axios"


axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)


app
    .use(router, axios)
    .use(store)
    .mount('#app');