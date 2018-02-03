<template lang="html">
  <div class="post-preview">
    <router-link :to="{name:'Post', params: {id: post.id}}" class="image-area">
      <div :style="'background-image: url(http://localhost:5000/api/file/' + post.image + ');'" class="image"></div>
    </router-link>
    <Vote :upvotes="post.upvotes" :downvotes="post.downvotes" :postId="post.id"></Vote>
    <router-link :to="{name:'Post', params: {id: post.id}}" class="body-area">
      <h3><slot></slot></h3>
      <p>{{ description }}</p>
    </router-link>
  </div>
</template>

<script>
import Vote from '@/components/Vote'

export default {
  name: 'post-preview',

  props: ['post'],

  components: { Vote },

  computed: {
    description() {
      return this.post.content.slice(0, 750) + '...'
    }
  }
}
</script>

<style scoped lang="css">
.post-preview {
  height: 150px;
  margin-bottom: 25px;
  display: block;
  color: black;
  display: grid;
  grid-template-columns: 3fr 1fr 15fr;
}

.image {
  width: 100%;
  height: 150px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.body-area {
  color: black;
}
</style>
