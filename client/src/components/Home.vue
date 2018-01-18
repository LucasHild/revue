<template lang="html">
  <div class="home container">
    <h1>Recenst Posts</h1>
    <PostPreview
      v-for="post in posts"
      img="http://fillmurray.com/225/150"
      :description="post.content | description"
      :id="post._id"
      :key="post._id.$oid"
      >
      {{ post.title }}
    </PostPreview>
  </div>
</template>

<script>
import PostPreview from '@/components/PostPreview'
import PostsService from '@/services/PostsService'

export default {
  name: 'home',

  components: { PostPreview },

  data() {
    return {
      posts: null
    }
  },

  filters: {
    description(value) {
      return value.slice(0, 750) + '...'
    }
  },

  mounted() {
    PostsService.index()
      .then(response => {
        this.posts = response.data.posts
      })
  }
}
</script>

<style lang="css">
</style>
