<template lang="html">
  <div class="create-post container">
    <h1>Create Post</h1>
    <form @submit.prevent="create" enctype="multipart/form-data">
      <p class="error">{{ error }}</p>
      <input v-model="title" type="text" placeholder="Title" ref="title">
      <div v-if="imagePreview" id="image-preview" :style="'background-image: url(' + imagePreview + ')'"></div>
      <div id="image-upload">
        <p>
          <span v-if="!image">Drag your image here to begin<br> or click to browse</span>
          <span v-else="">
            {{ image.name }}
          </span>
        </p>
        <input type="file" @change="fileChanged" accept="image/*">
      </div>
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
      error: null,
      image: null,
      imagePreview: null,
    }
  },

  methods: {
    create() {
      var formData = new FormData();
      formData.append('title', this.title)
      formData.append('content', this.content)

      // If photo has been set
      if (this.image) {
        formData.append('image', this.image, this.image.name)
      }

      PostsService.create(formData)
        .then(response => {
          this.$router.push({
            name: 'Post',
            params: { id: response.data.id }
          })
        })
        .catch(e => {
          this.error = e.response.data.error
        })
    },

    fileChanged(e) {
      this.image = e.target.files[0]

      // Show image preview
      var reader = new FileReader();
      reader.onload = (e) => {
        this.imagePreview = e.target.result;
      };
      reader.readAsDataURL(this.image);
    }
  },

  mounted() {
    // Focus title
    this.$refs.title.focus();
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

#image-upload {
  outline: 2px dashed grey;
  outline-offset: -10px;
  background: rgb(223, 224, 221);
  color: dimgray;
  cursor: pointer;
  position: relative;
  height: 100px;
}

#image-upload:hover {
  background: rgb(191, 191, 191);
}

#image-upload input {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 100%;
  cursor: pointer;
}

#image-upload p {
  text-align: center;
  position: absolute;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 50%;
  height: 30%;
  margin: auto;
  width: 100%;
}

#image-preview {
  margin: 0 auto;
  max-width: 250px;
  width: 100%;
  height: 150px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
</style>
