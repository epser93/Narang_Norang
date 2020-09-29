<template>
<div>
  <!-- 읽고 있어요 -->
  <div class="mt-4">
    <h2 class="mb-4">읽고 있어요 <b-icon icon="book"></b-icon></h2>
    <b-container fluid class="p-2">
      <b-row>
        <b-col>
          <b-img thumbnail class="thumbnail" fluid src="https://picsum.photos/250/250/?image=54" alt="Image 1"></b-img>
        </b-col>
        <b-col>
          <b-img thumbnail class="thumbnail" fluid src="https://picsum.photos/250/250/?image=58" alt="Image 2"></b-img>
        </b-col>
        <b-col>
          <b-img thumbnail class="thumbnail" fluid src="https://picsum.photos/250/250/?image=59" alt="Image 3"></b-img>
        </b-col>
      </b-row>
    </b-container>
    <hr>
  </div>

<!-- 보고 싶어요 -->
  <div style="margin-top: 6vmin;">
    <h2 class="mb-4">보고 싶어요 <b-icon icon="bookmark-heart"></b-icon></h2>
    <b-container fluid class="p-2">
      <b-row>
        <b-col>
          <b-img thumbnail class="thumbnail" fluid src="https://picsum.photos/250/250/?image=54" alt="Image 1"></b-img>
        </b-col>
        <b-col>
          <b-img thumbnail class="thumbnail" fluid src="https://picsum.photos/250/250/?image=58" alt="Image 2"></b-img>
        </b-col>
        <b-col>
          <b-img thumbnail class="thumbnail" fluid src="https://picsum.photos/250/250/?image=59" alt="Image 3"></b-img>
        </b-col>
      </b-row>
    </b-container>
    <hr>
  </div>

</div>
</template>

<script>
// import BookShelves from "@/components/BookShelves.vue"

export default {
  name:"MyBookShelves",

}
</script>

<style scoped>
.thumbnail {
  box-shadow: 4px 10px 5px #00000063;
}

hr {
  margin-top: -2rem;
  margin-bottom: 1rem;
  border-top: 8vmin solid #b07112b0;
  width: 170vmin;
}
</style>