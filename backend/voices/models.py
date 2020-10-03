from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

fs = OverwriteStorage()

class VoiceModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voice_model')
    name = models.CharField(max_length=40)
    model = models.FileField()

    def __str__(self):
        return self.name

    def update(self, data):
        self.name = data['name']
        self.save()


class Caption(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class VoiceCategory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return '{}_{}'.format(self.user,self.name)

    def create(self, data, user):
        self.name = data['name']
        self.user = user
        self.save()

    def update(self, data, user):
        self.user = user
        self.name = data['name']
        self.save()


class TrainVoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='train_voice')
    caption = models.ForeignKey(Caption, on_delete=models.SET_NULL, null=True)
    voice_category = models.ForeignKey(VoiceCategory, on_delete=models.SET_NULL, null=True)
    train_file = models.FileField()

    def __str__(self):
        return '{}_{}_{}'.format(self.user, self.voice_category, self.id)


    def create(self, filename, category, caption, user):
        self.user = user
        self.voice_category = category
        self.caption = caption
        self.train_file = filename
        self.save()

    def delete(self):
        # 파일삭제코드 추가
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.train_file.name))
        except :
            pass
        super().delete()


class VoiceRent(models.Model):
    voice_model = models.ForeignKey(VoiceModel, on_delete=models.PROTECT, related_name='voice_rent')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.voice_model


class VoicePurchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voice_purchase')
    voice_model = models.ForeignKey(VoiceModel, on_delete=models.PROTECT)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.voice_model