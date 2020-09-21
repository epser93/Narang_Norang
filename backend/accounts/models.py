from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Fairytale
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    balance = models.IntegerField(default=0)
    favorite = models.ManyToManyField(Fairytale)


class Subscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
