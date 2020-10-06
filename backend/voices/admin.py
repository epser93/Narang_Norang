from django.contrib import admin
from .models import (
    VoiceCategory, VoiceModel, VoicePurchase, VoiceRent,
    Caption, TrainVoice)


class VoiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'is_train']
    fields = ['user', 'name', 'is_train']


class VoiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']
    fields = ['user', 'name', 'model']


class VoicePurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'voice_model', 'start_date', 'end_date']
    fields = ['user', 'voice_model', 'end_date']


class VoiceRentAdmin(admin.ModelAdmin):
    list_display = ['id', 'voice_model', 'price']
    fields = ['voice_model', 'price']


class CaptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    fields = ['content']


class TrainVoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'caption', 'voice_category']
    fields = ['user', 'caption', 'voice_category', 'train_file']


admin.site.register(VoiceCategory, VoiceCategoryAdmin)
admin.site.register(VoiceModel, VoiceModelAdmin)
admin.site.register(VoicePurchase, VoicePurchaseAdmin)
admin.site.register(VoiceRent, VoiceRentAdmin)
admin.site.register(Caption, CaptionAdmin)
admin.site.register(TrainVoice, TrainVoiceAdmin)