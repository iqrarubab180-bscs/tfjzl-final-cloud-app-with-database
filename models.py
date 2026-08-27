from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    submission_content = models.FileField(upload_to='submission_files/')
    submission_date = models.DateField()
