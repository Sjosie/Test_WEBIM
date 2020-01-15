from django.conf import settings
from django.db import models
from django.utils import timezone

class Greetings(models.Model):
    title = models.TextField()
    description = models.TextField()