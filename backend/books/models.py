from django.db import models
from django.conf import settings

from voices.models import VoiceModel

import os


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Writer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Fairytale(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = models.ImageField()
    date = models.DateField()
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, related_name='fairytales', null=True)
    Genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, related_name='fairytales', null=True)

    def __str__(self):
        return self.title


    # 이미지 삭제 함수
    def image_delete(self):
        if self.exists(self.image.name):
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))

    # 해당 데이터가 삭제된다면 이미지 삭제함수 호출
    def delete(self):
        self.image_delete()
        super().delete()


class BookMark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='book_marks')
    fairytale = models.ForeignKey(Fairytale, on_delete=models.CASCADE)
    page = models.IntegerField()
    last_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.fairytale.title

    def create(self, data, user, fairytale):
        self.user = user
        self.page = data['id']
        self.fairytale = fairytale
        self.save()
    
    def update(self, data, user, fairytale):
        self.page = data['id']
        self.save()


class Scenario(models.Model):
    fairytale = models.ForeignKey(Fairytale, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class VoiceStorage(models.Model):
    fairytale = models.ForeignKey(Fairytale, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    voice_model = models.ForeignKey(VoiceModel, on_delete=models.CASCADE, null=True)
    voice_file = models.FileField()