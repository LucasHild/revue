<template lang="html">
  <div @click="$router.push({name: 'CreatePost'})" class="create-button">
      <svg fill="#FFFFFF" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
        <path d="M0 0h24v24H0z" fill="none"/>
      </svg>
  </div>
</template>

<script>
export default {
  name: 'create-button'
}
</script>

<style scoped lang="css">
.create-button {
  position: fixed;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  bottom: 3%;
  right: 1%;
  background-color: rgb(23, 92, 93);
  width: 56px;
  height: 56px;
  border-radius: 50%;
  cursor: pointer;
  -webkit-box-shadow: 2px 2px 10px rgba(10, 10, 10, 0.3);
  box-shadow: 2px 2px 10px rgba(10, 10, 10, 0.3);
  -webkit-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
</style>
