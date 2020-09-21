from django.db import models
from django.conf import settings


class FaQCategory(models.Model):
    name = models.CharField(max_length=40)


# Create your models here.
class FaQ(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    faq_category = models.ForeignKey(FaQCategory, on_delete=models.SET_NULL, related_name="faq", null=True)



class QnA(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    is_answer = models.BooleanField(default=False)


class QnaReply(models.Model):
    qna = models.ForeignKey(QnA, on_delete=models.CASCADE, related_name='qna_reply')
    content = models.TextField()
    date = models.DateField(auto_now=True)