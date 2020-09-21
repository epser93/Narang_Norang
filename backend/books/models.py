from django.db import models
from django.conf import settings

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
    content = models.TextField()
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
        return self.fairytale
