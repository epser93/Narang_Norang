<template>
  <div>
    <GoogleLogin
      class="GoogleLogin"
      :params="params"
      :onSuccess="onSuccess"
      :onFailure="onFailure">
      Sign in with Google
    </GoogleLogin>
  </div>
</template>

<script>
import GoogleLogin from 'vue-google-login';

export default {
  name: 'Login',
  components: {
    GoogleLogin
  },
  data() {
      return {
          // client_id is the only required property but you can add several more params, full list down bellow on the Auth api section
          params: {
              client_id: "xxxxxx"
          },
          // only needed if you want to render the button with the google ui
          renderParams: {
              width: 250,
              height: 50,
              longtitle: true
          }
      }
  },
  methods: {
      onSuccess(googleUser) {
          console.log(googleUser);

          // This only gets the user information: id, name, imageUrl and email
          console.log(googleUser.getBasicProfile());
      }
  },
}
</script>

<style>
.GoogleLogin {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  box-shadow: 0 3px 0 #0f69ff;
}
</style>