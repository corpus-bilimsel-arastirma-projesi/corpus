import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import store from './store/index'

Vue.use(Router)

const router = new Router({
  mode: 'history',
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
      component: () => import(/* webpackChunkName: "about" */ './views/Operations'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/plotly',
      name: 'plotly',
      component: () => import(/* webpackChunkName: "about" */ './views/Plot'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/preparation',
      name: 'preparation',
      component: () => import(/* webpackChunkName: "about" */ './views/Preparation'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/preparation2',
      name: 'preparation2',
      component: () => import(/* webpackChunkName: "about" */ './views/Preparation2'),
      meta: {
        requiresAuth: true
      }
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
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('./views/Profile'),
      meta: {
        requiresAuth: true
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.JWT_ACCESS !== null) {
      next()
      return
    }
    next('/sign-in')
  } else {
    next()
  }
})

export default router