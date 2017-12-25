from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    upl_text=models.TextField(blank=True, null=True)
    def __unicode__(self):
        return '%s'%self.id