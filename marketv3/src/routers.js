import Home from './components/Home.vue';
import SignIn from './components/SignIn.vue';
import Splash from './components/Splash.vue'

import { createRouter, createWebHistory } from 'vue-router';


const routes = [
    {
        name: 'Splash',
        component: Splash,
        path: '/'
    },
    {
        name: 'Home',
        component: Home,
        path: '/home'
    },
    {
        name: 'SignIn',
        component: SignIn,
        path: '/sign-in'
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
})


export default router;
