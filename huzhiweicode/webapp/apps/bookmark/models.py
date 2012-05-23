from django.contrib.auth.models import User
from django.db import models

class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(blank=True, max_length=100, help_text='Limit of 100 characters')
    public = models.BooleanField(verbose_name='Public this bookmark', blank=True, default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.url