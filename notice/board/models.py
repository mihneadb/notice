from django.db import models
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.title)


admin.site.register(Post)

