import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import SignUp from '@/components/SignUp'
import Post from '@/components/Post'
import User from '@/components/User'
import CreatePost from '@/components/CreatePost'

Vue.use(Router)

require('@/assets/css/style.css')

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/post/:id',
      name: 'Post',
      component: Post
    },
    {
      path: '/user/:username',
      name: 'User',
      component: User
    },
    {
      path: '/create',
      name: 'CreatePost',
      component: CreatePost
    }
  ]
})
