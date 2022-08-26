from django.db import models
from django.db.models import aggregates

class admin_limit(models.Model):
    entry_limit  = models.IntegerField()

class admin_date_block(models.Model):
    date_block  = models.CharField(max_length=100)