<template lang="html">
  <div class="login">
    <form>
      <h1>Login</h1>
      <input type="text" placeholder="Username">
      <input type="password" placeholder="Password">
      <input class="button" type="submit" value="Login">
    </form>
  </div>
</template>

<script>
export default {
  name: 'login'
}
</script>

<style scoped lang="css">
.login {
  background: rgb(23, 92, 93);
  background-image: url(/static/newsletter-login.jpg);
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;

  width: 100%;
  height: calc(100vh - 49px);
  position: relative;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

form {
  background-color: white;
  max-width: 500px;
  width: 90%;
  margin-bottom: 49px;
  padding: 20px;
}

h1 {
  text-align: center;
}

input {
  display: block;
  width: 100%;
  margin: 0;
  border: none;
  background: rgb(223, 224, 221);
  padding: 15px;
  text-align: center;
  margin: 20px 0;

  -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
  -moz-box-sizing: border-box;    /* Firefox, other Gecko */
  box-sizing: border-box;         /* Opera/IE 8+ */
}
</style>
