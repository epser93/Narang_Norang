<template>
<<<<<<< HEAD
	<b-card no-body style="min-height: 500px;" >
=======
	<b-card v-if="faq" no-body style="min-height: 500px;">
>>>>>>> 7bdb492d1d514b761f42bea27a8ef9b26c432708
		<b-tabs card>
			<b-tab title-link-class="text-dark" title="자주 묻는 질문">

				<div class="accordion" role="tablist" v-for="question in faq" :key="question.id">
					<b-card no-body class="mb-1">
						<b-card-header header-tag="header" class="p-1" role="tab">
							<b-button block v-b-toggle="`accordion-${question.id}`">{{ question.title }}</b-button>
						</b-card-header>
						<b-collapse :id="`accordion-${question.id}`" accordion="my-accordion" role="tabpanel">
							<b-card-body>
								<b-card-text>{{ question.content }}</b-card-text>
							</b-card-body>
							<div v-if="(userInfo.is_staff)">
								<hr>
								<b-button v-b-modal="'new-question'" @click="onUpdate(question)" variant="outline-info" class="mb-3 mr-2">
									<b-icon icon="pencil-square" class="pt-1" aria-hidden="true"></b-icon> 수정
								</b-button>
								<b-button @click="onDelete(question.id)" variant="outline-danger" class="mb-3 mr-2">
									<b-icon icon="x-square" class="pt-1" aria-hidden="true"></b-icon> 삭제
								</b-button>
							</div>
						</b-collapse>
					</b-card>
				</div>

				<b-card v-if="(userInfo.is_staff)" no-body class="mb-1">
					<b-card-header header-tag="header" class="p-1" role="tab">
						<b-button block v-b-modal="'new-question'">FAQ 추가</b-button>
					</b-card-header>
				</b-card>

				<b-modal :id="'new-question'" :title="form_type ? 'FAQ 추가' : 'FAQ 수정'" no-close-on-backdrop>

					<b-container style="min-height: 400px;">
						<b-row class="mt-2">
							<b-col cols="12">
								<b-form-input v-model="form.title" id="input-lg" size="lg" placeholder="제목을 적어주세요."></b-form-input>
							</b-col>
						</b-row>
						<b-row class="mt-2">
							<b-col cols="12">
								<b-form-textarea
									id="textarea-large"
									size="lg"
									placeholder="내용을 적어주세요."
									rows="10"
									v-model="form.content"
								></b-form-textarea>
							</b-col>
						</b-row>
					</b-container>

					<template v-slot:modal-footer="{ cancel }">
						<b-button v-if="form_type" @click="onCreate(); cancel();" variant="outline-secondary" class="mb-3 mr-2">
							<b-icon icon="pencil-square" class="pt-1" aria-hidden="true"></b-icon> 추가
						</b-button>
						<b-button v-else @click="onUpdate(); cancel();" variant="outline-info" class="mb-3 mr-2">
							<b-icon icon="pencil-square" class="pt-1" aria-hidden="true"></b-icon> 수정
						</b-button>
						<b-button @click="onCancel(); cancel();" variant="outline-secondary" class="mb-3 mr-2">
							<b-icon icon="x-square" class="pt-1" aria-hidden="true"></b-icon> 닫기
						</b-button>
					</template>

				</b-modal>

			</b-tab>
			<b-tab title-link-class="text-dark" title="1 : 1 문의" @click="onRoute('QA')">
				<router-view/>
			</b-tab>
		</b-tabs>
	</b-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
	name:"CustomerService",
	computed: {
		...mapState('help', ['faq']),
		...mapState('user', ['userInfo'])
	},
	data() {
		return {
			form_type: true,
			index: '',
			form: {
				title: "",
				content: "",
				faq_category: 1
			}
		}
	},
	methods: {
		...mapActions('help', ['getFAQ', 'postFAQ', 'putFAQ', 'delFAQ']),
    onRoute(name) {
      this.$router.push({name: name}, () => {})
		},
		onCreate() {
			this.postFAQ(this.form)
		},
		onUpdate(question) {
			if (this.index) {
				this.putFAQ({ index: this.index, body: this.form })
			} else {
				this.index = question.id
				this.form.title = question.title
				this.form.content = question.content
				this.form_type = false
			}
		},
		onDelete(qid) {
			if (confirm("정말 삭제하시겠습니까??") == true) { 
        this.delFAQ(qid)
      }
		},
		onCancel() {
			this.index = ''
			this.form.title = ''
			this.form.content = ''
			this.form_type = true
		}
	},
	created() {
		this.getFAQ()
	}
}
</script>

<style>

</style>