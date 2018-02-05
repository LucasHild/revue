<template lang="html">
  <div class="create-post container">
    <h1>Create Subvue</h1>
    <form @submit.prevent="create" enctype="multipart/form-data">
      <p class="error">{{ error }}</p>
      <input v-model="name" type="text" placeholder="Name" ref="name">
      <p class="permalink">{{ permalink }}</p>
      <textarea v-model="description" name="description" placeholder="Description" rows="25" cols="80"></textarea>
      <input v-model="moderators" type="text" placeholder="Moderators">
      <input class="button" type="submit" value="Create Subvue">
    </form>
  </div>
</template>

<script>
import SubvuesService from '@/services/SubvuesService'

export default {
  name: 'create-post',

  data() {
    return {
      name: '',
      description: '',
      moderators: '',
      error: null
    }
  },

  computed: {
    permalink() {
      if (this.name) {
        return 'https://#/s/' + this.name.toLowerCase()
          .replace(new RegExp(' ', 'g'), '-')
          .replace(new RegExp('\\.', 'g'), '')
          .replace(new RegExp(',', 'g'), '')
          .replace(new RegExp('!', 'g'), '')
          .replace(new RegExp('\\?', 'g'), '')
      } else {
        return null
      }
    }
  },

  methods: {
    create() {
      SubvuesService.create({
        name: this.name,
        description: this.description,
        moderators: this.moderators
      })
        .then(response => {

        })
        .catch(e => {
          this.error= e.response.data.error
        })
    }
  },

  mounted() {
    // Focus name
    this.$refs.name.focus();
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

.permalink {
  color: gray;
  text-align: right;
}
</style>
