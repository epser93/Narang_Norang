from django.db import models
from django.conf import settings


class VoiceModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voice_model')
    name = models.CharField(max_length=40)
    model = models.FileField()

    def __str__(self):
        return self.name


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