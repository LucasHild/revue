<template lang="html">
  <div class="user container">
    <h1>{{ username }}</h1>
    <div class="len-posts button">{{ posts.length }} Posts</div>
    <div class="stars button">{{ stars }} Stars</div>

    <div class="post-list">
      <PostPreview v-for="post in posts" :key="post.id" :post="post">
        {{ post.title }}
      </PostPreview>
    </div>

    <CreateButton></CreateButton>
  </div>
</template>

<script>
import PostPreview from '@/components/PostPreview'
import CreateButton from '@/components/CreateButton'
import PostsService from '@/services/PostsService'

export default {
  name: 'user',

  components: { CreateButton, PostPreview },

  data() {
    return {
      username: this.$route.params.username,
      posts: [],
      stars: 16
    }
  },

  mounted() {
    PostsService.user(this.username)
      .then(response => {
        this.posts = response.data
      })
      .catch(e => {
        this.error = e.response.data.error
      })
  }
}
</script>

<style lang="css">
.button {
  background: blue;
  display: inline;
  padding: 10px 20px;
}

.stars {
  background-color: rgb(194, 194, 36) !important;
}

.post-preview:first-of-type {
  margin-top: 25px;
}
</style>
