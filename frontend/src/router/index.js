import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/adopciones',
    name: 'adoptions',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Adoptions.vue')
  },
  {
    path: '/extravios',
    name: 'strayings',
    component: () => import('../views/Strayings.vue')
  },
  {
    path: '/hallazgos',
    name: 'findings',
    component: () => import('../views/Findings.vue')
  },
  {
    path: '/cruzas',
    name: 'crosses',
    component: () => import('../views/Crosses.vue')
  },
  {
    path: '/adiestradores',
    name: 'trainers',
    component: () => import('../views/Trainers.vue')
  },
  {
    path: '/anuncios',
    name: 'ads',
    component: () => import('../views/Ads.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
