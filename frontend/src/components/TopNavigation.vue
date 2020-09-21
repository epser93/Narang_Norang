<template>
  <div>
    <b-navbar type="dark" variant="secondary">
      <b-navbar-brand href="#">나랑노랑</b-navbar-brand>

      <b-navbar-nav class="ml-auto">

				<b-button v-b-toggle.sidebar-right class="my-2 my-sm-0"><b-icon icon="list"></b-icon></b-button>
        
      </b-navbar-nav>
    </b-navbar>

    <b-sidebar id="sidebar-right" right shadow backdrop-variant="dark" backdrop> 

      <b-card no-body style="min-height: 100%;">
        <b-card-text class="mt-4">
          <b-avatar class="mr-3"></b-avatar>
          <span class="mr-auto"> ~ 님 환영합니다</span>
        </b-card-text>

        <b-card-body>
          <b-container>
            <strong>현재 목소리 - 엄마</strong>
            <b-row>
              <b-col cols="6" class="py-3">
                <b-card bg-variant="info">
                  <b-avatar size="lg" rounded="lg" text="엄마" variant="info"></b-avatar>
                </b-card>
              </b-col>
              <b-col cols="6" class="py-3">
                <b-card>
                  <b-avatar size="lg" rounded="lg" src="https://placekitten.com/300/300"></b-avatar>
                </b-card>
              </b-col>
              <b-col cols="6" class="py-3">
                <b-card>
                  <b-avatar size="lg" rounded="lg" icon="plus"></b-avatar>
                </b-card>
              </b-col>
            </b-row>
          </b-container>
        </b-card-body>

        <b-list-group>
          <b-list-group-item v-b-modal.bookshelves>내 서재</b-list-group-item>
          <b-list-group-item href="#">Not yet...</b-list-group-item>
          <b-list-group-item href="#">Not yet...</b-list-group-item>
        </b-list-group>
      </b-card>

      <template v-slot:footer="{}">
       <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
        <strong class="mr-auto">나랑노랑</strong>
        <b-button v-b-modal.cs-center>
          <b-icon icon="headset" aria-hidden="true"></b-icon> 고객센터
        </b-button>
       </div>
      </template>

    </b-sidebar>

    <!-- 내 서재 -->
    <b-modal id="bookshelves" size="lg" scrollable title="우리아이 책장" no-close-on-backdrop>
      <b-card no-body style="min-height: 500px;">
        
      </b-card>

      <template v-slot:modal-footer="{ cancel }">
        <b-button @click="cancel()">
          닫기
        </b-button>
      </template>
    </b-modal>

    <!-- 고객샌터 -->
    <b-modal id="cs-center" size="lg" scrollable title="고객센터 / 도움말" no-close-on-backdrop>
      <b-card no-body style="min-height: 500px;">
        <b-tabs card>
          <b-tab title-link-class="text-dark" title="자주 묻는 질문">

            <div class="accordion" role="tablist" v-for="(accordion, i) in accordions" :key="i">
              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" class="p-1" role="tab">
                  <b-button block v-b-toggle="`accordion-${i}`">Accordion {{i}}</b-button>
                </b-card-header>
                <b-collapse :id="`accordion-${i}`" accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>{{i}} {{ text }}</b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>
            </div>

          </b-tab>
          <b-tab title-link-class="text-dark" title="1 : 1 문의">
            <b-card-text>Not yet</b-card-text>
          </b-tab>
        </b-tabs>
      </b-card>

      <template v-slot:modal-footer="{ cancel }">
        <b-button @click="cancel()">
          닫기
        </b-button>
      </template>
    </b-modal>

  </div>
</template>

<script>
export default {
  name: "TopNavigation",
  data() {
    return {   
      accordions: 5,
      text: `
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
        richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor
        brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon
        tempor, sunt aliqua put a bird on it squid single-origin coffee nulla
        assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore
        wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher
        vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic
        synth nesciunt you probably haven't heard of them accusamus labore VHS.
      `,
        
    }
  },
  methods: {

  }
}
</script>

<style>
</style>