import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import About from '../views/About'
import Item from '../views/Item'

Vue.use(VueRouter)

// define routes in our application
const routes = [
    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'Item',
        path: '/item/:id',
        component: Item,
        params: {id: null}
    },
    {
        name: 'About',
        path: '/about',
        component: About
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.VUE_APP_HOST+process.env.VUE_APP_PORT,
    routes
})

export default router