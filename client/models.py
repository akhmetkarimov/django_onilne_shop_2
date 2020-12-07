from django.db import models
from django.contrib.auth.models import AbstractUser
    
class BaseUser(AbstractUser):
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    img_source = models.FileField(upload_to=None, max_length = 100, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)