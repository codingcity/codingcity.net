from django.db import models
from django.contrib.auth.models import User

class Question2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question2')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question2')  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer2')
    question = models.ForeignKey(Question2, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer2')


class Comment2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question2, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer2, null=True, blank=True, on_delete=models.CASCADE)

