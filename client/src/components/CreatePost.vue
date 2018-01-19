<template lang="html">
  <div class="create-post container">
    <h1>Create Post</h1>
    <form @submit.prevent="create">
      <p class="error">{{ error }}</p>
      <input v-model="title" type="text" placeholder="Title">
      <textarea v-model="content" name="name" placeholder="Content" rows="25" cols="80"></textarea>
      <input class="button" type="submit" value="Create post">
    </form>
  </div>
</template>

<script>
import PostsService from '@/services/PostsService'

export default {
  name: 'create-post',

  data() {
    return {
      title: '',
      content: '',
      error: null
    }
  },

  methods: {
    create() {
      PostsService.create({
        title: this.title,
        content: this.content
      })
        .then(response => {
          this.$router.push({
            name: 'Post',
            params: { id: response.data.id }
          })
        })
        .catch(e => {
          this.error = e.response.data.error
        })
    }
  }
}
</script>

<style scoped lang="css">
form {
  max-width: 1500px;
  width: 100%;
  margin: 0 auto;
}

input, textarea {
  display: block;
  width: 100%;
  margin: 0;
  border: none;
  background: rgb(223, 224, 221);
  padding: 15px;
  margin: 20px 0;

  -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
  -moz-box-sizing: border-box;    /* Firefox, other Gecko */
  box-sizing: border-box;         /* Opera/IE 8+ */
}
</style>
