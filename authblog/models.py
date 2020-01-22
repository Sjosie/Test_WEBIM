from django.conf import settings
from django.db import models
import vk_api



class Greetings(models.Model):
    title = models.TextField()
    description = models.TextField()   


