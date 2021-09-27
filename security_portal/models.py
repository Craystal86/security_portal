from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/no_img.jpg')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="security_portal")
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # modify_date = models.DateTimeField(null=True, blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()