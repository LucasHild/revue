<template lang="html">
  <div class="user">

    <div class="container">
      <div class="post-list">
        <PostPreview hideUser="true" v-for="post in posts" :key="post.id" :post="post">
          {{ post.title }}
        </PostPreview>
      </div>
    </div>

    <div class="info">
      <img :src="'https://www.gravatar.com/avatar/' + this.hashedEmail + '?s=200'" />
      <h1>{{ username }}</h1>
      <div class="len-posts button">{{ posts.length }} Posts</div>
    </div>

    <CreateButton></CreateButton>
  </div>
</template>

<script>
import PostPreview from '@/components/PostPreview'
import CreateButton from '@/components/CreateButton'
import PostsService from '@/services/PostsService'
import UsersService from '@/services/UsersService'

export default {
  name: 'user',

  components: { CreateButton, PostPreview },

  data() {
    return {
      username: this.$route.params.username,
      posts: [],
      hashedEmail: ''
    }
  },

  mounted() {
    this.fetchData()
  },

  watch: {
    $route() {
      this.username = this.$route.params.username
      this.fetchData()
    }
  },

  methods: {
    fetchData() {
      UsersService.username(this.username)
        .then(response => {
          this.hashedEmail = response.data.hashedEmail
        })

      PostsService.user(this.username)
        .then(response => {
          this.posts = response.data
        })
        .catch(e => {
          this.error = e.response.data.error
        })
    }
  }
}
</script>

<style lang="css">
.container {
  width: 80%;
  float: left;
}

.info {
  width: 20%;
  float: right;
  padding-top: 20px;
}

.info img {
  display: block;
  margin: 0 auto;
}

.button {
  background: blue;
  display: inline;
  padding: 10px 20px;
}

.post-preview:first-of-type {
  margin-top: 25px;
}
</style>
