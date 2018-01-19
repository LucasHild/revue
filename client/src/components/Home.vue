<template lang="html">
  <div class="home container">
    <h1>Recenst Posts</h1>
    <PostPreview
      v-for="post in posts"
      img="http://fillmurray.com/225/150"
      :content="post.content"
      :id="post.id"
      :key="post.id"
      :comments="post.comments"
      >
      {{ post.title }}
    </PostPreview>

    <CreateButton></CreateButton>
  </div>
</template>

<script>
import PostPreview from '@/components/PostPreview'
import PostsService from '@/services/PostsService'
import CreateButton from '@/components/CreateButton'

export default {
  name: 'home',

  components: { PostPreview, CreateButton },

  data() {
    return {
      posts: null
    }
  },

  mounted() {
    PostsService.index()
      .then(response => {
        this.posts = response.data
      })
  }
}
</script>

<style lang="css">
</style>
