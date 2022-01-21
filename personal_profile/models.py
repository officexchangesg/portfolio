from django.db import models
from django.db.models.fields import URLField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField( upload_to='personal_profile/images/')
    url = URLField(blank=True)
