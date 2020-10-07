from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Fairytale
from django.conf import settings
from voices.models import VoiceModel
import datetime
# Create your models here.

class User(AbstractUser):
    balance = models.IntegerField(default=0)
    favorite = models.ManyToManyField(Fairytale, related_name='like_user')
    current_voice = models.IntegerField(default=1)

    def __str__(self):
        return self.username

    def update(self, data):
        self.first_name = data['nick_name']
        self.save()

    def set_voice(self, voice):
        if voice.id == 1 or voice.user == self:
            self.current_voice = voice.id
            self.save()
            return True
        return False


class Subscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    tid = models.CharField(max_length=20, default=None, null=True)
    is_return = models.BooleanField(default=False)

    def create(self, user, tid):
        self.user = user
        self.end_date = datetime.datetime.today() + datetime.timedelta(days=30)
        self.tid = tid
        self.save()

    def refund(self):
        self.is_return = True
        self.end_date = datetime.datetime.today() - datetime.timedelta(days=1)
        self.save()
        
    