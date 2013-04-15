from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.title)


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)


admin.site.register(Post)
admin.site.register(Comment)