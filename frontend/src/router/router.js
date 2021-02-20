import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import About from '../views/About'
import Item from '../views/Item'

Vue.use(VueRouter)

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
    base: 'localhost:8080',
    routes
})

export default router