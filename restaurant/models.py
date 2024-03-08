from django.db import models

# Create your models here.

class HomePage(models.Model):
    introduction = models.TextField()

    class Meta:
        verbose_name_plural = 'Home Page'

    def __str__(self):
        return "Content for Landing Page"



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name