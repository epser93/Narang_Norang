from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Subscribe
# admin 페이지에 보여질 내용 추가하기

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'balance','is_superuser', 'is_staff', 'current_voice']
    fields = ['username', 'is_staff', 'current_voice']


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'start_date', 'end_date', 'tid', 'is_return']
    fields = ['user', 'end_date', 'tid', 'is_return']

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Subscribe, SubscribeAdmin)