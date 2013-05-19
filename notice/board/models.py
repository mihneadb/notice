from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from datetime import datetime


class Category(models.Model):
    class Meta:
        permissions = (
                ('rights', "Can edit categories"),
        )
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('Category', null=True, blank=True, default=None)

    def __unicode__(self):
        return unicode(self.name)

class Post(models.Model):
    class Meta:
        permissions = (
                ('rights', "Can edit posts"),
        )
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return unicode(self.title)


class Comment(models.Model):
    class Meta:
        permissions = (
                ('important', "Replies are important"),
        )
    text = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

