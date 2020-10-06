<template>
	<div>
    <b-card no-body style="min-height: 600px;">
      <b-tabs pills card vertical nav-wrapper-class="w-25" style="min-height: 600px;">
        
        <b-tab title-link-class="text-dark">
          <template v-slot:title>
            <h3 class="my-3"><strong>내 목소리</strong></h3>
          </template>
          <my-voice />
        </b-tab>
        
        <!-- <b-tab title-link-class="text-dark">
          <template v-slot:title>
            <h3 class="my-3"><strong>목소리 찾기</strong></h3>
          </template>
          <all-voice />
        </b-tab> -->
        
        <b-tab title-link-class="text-dark">
          <template v-slot:title>
            <h3 class="my-3"><strong>목소리 만들기</strong></h3>
          </template>
          <new-voice />
        </b-tab>
      
      </b-tabs>
    </b-card>
	</div>
</template>

<script>
import MyVoice from '@/views/voicecloud/MyVoice'
// import AllVoice from '@/views/voicecloud/AllVoice'
import NewVoice from '@/views/voicecloud/NewVoice'

export default {
  name:"VoiceCloud",
  components: {
    MyVoice,
    // AllVoice,
    NewVoice,
  }
}
</script>

<style>
.nav-pills .nav-link.active {
  background-color: #89aef3;
}
</style>