<template>
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
			<b-tab title-link-class="text-dark" title="1 : 1 문의" @click="onRoute('QA')">
				<router-view/>
			</b-tab>
		</b-tabs>
	</b-card>
</template>

<script>
export default {
	name:"CustomerService",
	data() {
		return {
			// FAQ
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
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    }
  }
}
</script>

<style>

</style>