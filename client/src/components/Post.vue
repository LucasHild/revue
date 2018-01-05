<template lang="html">
  <div class="post container">
    <h1>Post ({{ id }})</h1>
  </div>
</template>

<script>
export default {
  name: 'post',
  data() {
    return {
      id: this.$route.params.id
    }
  }
}
</script>

<style lang="css">
</style>
