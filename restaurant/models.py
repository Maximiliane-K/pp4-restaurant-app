from django.db import models

# Create your models here.

class HomePage(models.Model):
    introduction = models.TextField()

    class Meta:
        verbose_name_plural = 'Home Page'

    def __str__(self):
        return "Content for Landing Page"