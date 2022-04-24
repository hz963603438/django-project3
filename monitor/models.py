from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    emails = (
        (0, '123456@163.com'),
        (1, 'abcdef@qq.com'),
        (2, '1a2b3c@aa.com')
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=False, max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    d_time = models.CharField(max_length=128, default="aabb")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Node(models.Model):
    nodename = models.CharField(max_length=256)

    def __str__(self):
        return self.nodename

    class Meta:
        verbose_name = "node list"
        verbose_name_plural = "node"


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    #是否在当前发布的问卷
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

