<template lang="html">
  <router-link :to="{name:'Post', params: {id: id}}" class="post-preview">
    <div class="image-area">
      <div :style="'background-image: url(' + img + ');'" class="image"></div>
    </div>
    <div class="body-area">
      <h3><slot></slot></h3>
      <p>{{ description }}</p>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'post-preview',

  props: [
    'content',
    'link',
    'img',
    'id'
  ],

  computed: {
    description() {
      return this.content.slice(0, 750) + '...'
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
}

.image-area {
  width: 15%;
  float: left;
}

.image {
  width: 100%;
  height: 150px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;

}

.body-area {
  width: 85%;
  float: right;
  padding-left: 20px;
}
</style>
