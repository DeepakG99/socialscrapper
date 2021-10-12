from django.db import models

# Create your models here.


class twitter(models.Model):
    status_num = models.IntegerField(null=True, blank=True)
    status_text = models.TextField(null=True, blank=True)
    status_name = models.TextField(null=True, blank=True)
    status_created_at = models.TextField(null=True, blank=True)
    status_favourate_Count = models.TextField(null=True, blank=True)
    status_lang = models.TextField(null=True, blank=True)


class trumbler(models.Model):
    status_num = models.IntegerField(null=True, blank=True)
    status_text = models.TextField(null=True, blank=True)
    status_name = models.TextField(null=True, blank=True)
    status_created_at = models.TextField(null=True, blank=True)
    status_favourate_Count = models.TextField(null=True, blank=True)
    status_lang = models.TextField(null=True, blank=True)