<template lang="html">
  <div class="post">
    <div class="body container">
      <Vote :upvotes="upvotes" :downvotes="downvotes" :postId="id"></Vote>
      <div class="content">
        <svg id="delete-button" @click="deletePost" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
          <title>Delete Post</title>
          <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
          <path d="M0 0h24v24H0z" fill="none"/>
        </svg>
        <svg id="verify-delete-button" v-show="deleteVerify" @click="deleteVerify = false" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
          <title>Cancel</title>
          <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
          <path d="M0 0h24v24H0z" fill="none"/>
        </svg>

        <p class="error">{{ error }}</p>
        <h1>{{ title }}</h1>

        <h3>by
          <router-link :to="{ name: 'User', params: { 'username': user.username } }">
            {{ user.username }}
          </router-link>
           on {{ created }}
        </h3>

        <p v-html="content"></p>

        <i class="post-id">ID {{ id }}</i>
      </div>
    </div>

    <div class="container">
      <h2 v-show="comments == []" >Comments</h2>

      <form id="comment-form" @submit.prevent="createComment">
        <p class="error">{{ errorCreateComment }}</p>
        <textarea v-model="newCommentContent" name="name" placeholder="Content" rows="5" cols="80"></textarea>
        <input class="button" type="submit" value="Create comment">
      </form>

      <Comment v-for="comment in comments" :key="comment.id" :user="comment.user" :created="comment.created" :content="comment.content"></Comment>
    </div>
  </div>
</template>

<script>
import Comment from '@/components/Comment'
import Vote from '@/components/Vote'
import PostsService from '@/services/PostsService'

export default {
  name: 'post',

  components: { Comment, Vote },

  data() {
    return {
      error: null,
      id: this.$route.params.id,
      title: '',
      user: '',
      created: '',
      content: '',
      comments: [],
      upvotes: [],
      downvotes: [],
      deleteVerify: false,

      newCommentContent: '',
      errorCreateComment: null
    }
  },

  methods: {
    deletePost() {
      if (this.deleteVerify) {
        PostsService.delete(this.id)
          .then(response => {
            this.$router.push({ name: 'Home' })
          })
          .catch(e => {
            this.error = e.response.data.error
          })
      } else {
        this.deleteVerify = true
      }
    },

    createComment() {
      PostsService.addComment(this.id, this.newCommentContent)
        .then(response => {
          this.comments = response.data
          this.newCommentContent = ''
          this.errorCreateComment = null
        })
        .catch(e => {
          this.errorCreateComment = e.response.data.error
        })
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
        this.upvotes = response.data.upvotes
        this.downvotes = response.data.downvotes
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
    position: relative;
    display: grid;
    grid-template-columns: 1fr 20fr;
  }

  #delete-button {
    position: absolute;
    right: 15px;
    top: 15px;
    cursor: pointer;
  }

  #delete-button:hover {
    fill: rgb(163, 7, 7);
  }

  #verify-delete-button {
    position: absolute;
    right: 40px;
    top: 15px;
    cursor: pointer;
  }

  #verify-delete-button:hover {
    fill: rgb(7, 163, 70);
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

  #comment-form {
    max-width: 1500px;
    width: 100%;
    margin: 0 auto;
  }

  #comment-form textarea, #comment-form input {
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
