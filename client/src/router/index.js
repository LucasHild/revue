import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import SignUp from '@/components/SignUp'
import Subvue from '@/components/Subvue'
import Post from '@/components/Post'
import User from '@/components/User'
import CreatePost from '@/components/CreatePost'
import CreateSubvue from '@/components/CreateSubvue'

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
      path: '/s/:name',
      name: 'Subvue',
      component: Subvue
    },
    {
      path: '/:subvuePermalink/:id',
      name: 'Post',
      component: Post
    },
    {
      path: '/u/:username',
      name: 'User',
      component: User
    },
    {
      path: '/create',
      name: 'CreatePost',
      component: CreatePost
    },
    {
      path: '/create/subvue',
      name: 'CreateSubvue',
      component: CreateSubvue
    }
  ]
})
