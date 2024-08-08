from django.db import models

from django.utils import timezone
import datetime


class Article(models.Model):
    title = models.CharField("Article Title", max_length=50)
    text = models.TextField("Article Text")
    pub_date = models.DateTimeField("date published", default=timezone.now())

    def __str__(self):
        return self.title

    def was_published_in_days(self, days=3):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=days))

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    author = models.CharField("Comment Author", max_length=15)
    text = models.CharField("Comment Text", max_length=250)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
