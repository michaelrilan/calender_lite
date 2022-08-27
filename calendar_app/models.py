from django.db import models
from django.db.models import aggregates
# Create your models here.
class limit(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    date_saved = models.CharField(max_length=100)