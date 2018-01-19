<template lang="html">
  <div class="post">
    <div class="body container">
      <p class="error">{{ error }}</p>
      <h1>{{ title }}</h1>

      <h3>by
        <router-link :to="{ name: 'User', params: { 'username': user.username } }">
          {{ user.username }}
        </router-link>
         {{ created.date }}
      </h3>

      <p v-html="content"></p>

      <i class="post-id">ID {{ id }}</i>
    </div>

    <div class="container">
      <h2 v-show="comments == []" >Comments</h2>
      <Comment v-for="comment in comments" :key="comment.id" :user="comment.user" :created="comment.created" :content="comment.content"></Comment>
    </div>
  </div>
</template>

<script>
import Comment from '@/components/Comment'
import PostsService from '@/services/PostsService'

export default {
  name: 'post',
  components: { Comment },
  data() {
    return {
      error: null,
      id: this.$route.params.id,
      title: '',
      user: '',
      created: '',
      content: '',
      comments: []
    }
  },

  mounted() {
    PostsService.item(this.id)
      .then(response => {
        this.title = response.data.title
        this.user = response.data.user
        this.created = response.data.created
        this.content = response.data.content
        this.comments = response.data.comments
      })
      .catch(e => {
        this.error = e.response.data.error
      })
  }
}
</script>

<style scoped lang="css">
  .body {
    background: #eeeeee;
  }

  h1 {
    margin: 0;
  }

  h3 {
    margin: 0;
    font-weight: 400;
  }

  .post-id {
    text-align: right;
    display: block;
  }
</style>
