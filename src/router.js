import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/operations',
      name: 'operations',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Operations.vue')
    },
    {
      path: '/sign-up',
      name: 'sign-up',
      component: () => import('./views/SignUp')
    },
    {
      path: '/sign-in',
      name: 'sign-in',
      component: () => import('./views/SignIn')
    }
  ]
})
