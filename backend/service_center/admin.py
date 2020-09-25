from django.contrib import admin
from .models import FaQCategory, FaQ, QnA, QnaReply
# Register your models here.

class FaQCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']


class FaQAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'faq_category']
    fields = ['title', 'content', 'faq_category']


class QnAAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'create_date', 'is_answer']
    fields = ['user', 'title', 'content', 'is_answer']


class QnAReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'qna', 'content', 'create_date']
    fields = ['qna', 'content',]


admin.site.register(FaQCategory, FaQCategoryAdmin)
admin.site.register(FaQ, FaQAdmin)
admin.site.register(QnA, QnAAdmin)
admin.site.register(QnaReply, QnAReplyAdmin)