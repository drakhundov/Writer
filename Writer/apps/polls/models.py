from django.db import models
from django.utils import timezone

import datetime

class Question(models.Model):
    title = models.CharField("Question", max_length = 200)
    pub_date = models.DateTimeField("date published", default = timezone.now())


    def __str__(self):
        return self.title

    def was_published_in_days(self, days):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=days)


    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    title = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Choise"
        verbose_name_plural = "Choices"