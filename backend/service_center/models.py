from django.db import models
from django.conf import settings


class FaQCategory(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

# Create your models here.
class FaQ(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    faq_category = models.ForeignKey(FaQCategory, on_delete=models.SET_NULL, related_name="faq", null=True)

    def __str__(self):
        return self.title


class QnA(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class QnaReply(models.Model):
    qna = models.ForeignKey(QnA, on_delete=models.CASCADE, related_name='qna_reply')
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)