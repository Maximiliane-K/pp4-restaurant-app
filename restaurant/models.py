from django.db import models

# Create your models here.

class HomePage(models.Model):
    introduction = models.TextField()

    def __str__(self):
        return "Context for Landing Page"