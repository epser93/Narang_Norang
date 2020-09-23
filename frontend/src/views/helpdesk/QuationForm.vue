<template>
  <div>
    <h2 class="mt-2 mb-4">문의하기</h2>
    <b-container style="min-height: 400px;">
      <b-row class="mt-2">
        <b-col sm="2">
          <label for="textarea-large">제목:</label>
        </b-col>
        <b-col sm="10">
          <b-form-input id="input-lg" size="lg" placeholder="제목"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="mt-2">
        <b-col sm="2">
          <label for="textarea-large">문의사항:</label>
        </b-col>
        <b-col sm="10">
          <b-form-textarea
            id="textarea-large"
            size="lg"
            placeholder="문의사항"
            rows="10"
          ></b-form-textarea>
        </b-col>
      </b-row>
    </b-container>

    <b-button variant="outline-secondary" class="my-2">
      <b-icon icon="pencil-square" aria-hidden="true"></b-icon> 작성하기
    </b-button>
  </div>
</template>

<script>
export default {
  name:"QuationForm",
  methods: {

  }
}
</script>

<style>

</style>