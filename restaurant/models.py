from django.db import models


class HomePage(models.Model):
    """ 
    Model for the introduction section on landing page 
    """
    introduction = models.TextField()

    class Meta:
        verbose_name_plural = 'Home Page'

    def __str__(self):
        return "Content for Landing Page"


class Category(models.Model):
    """
    Model for menu items categories 
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    """
    Model for the menu items
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category,related_name='menu_items', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.name


class BeveragesCategory(models.Model):
    """
    Model for drink categories in menu
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Drink Categories'

    def __str__(self):
        return self.name


class BeveregeItems(models.Model):
    """
    Model for beverage items
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(DrinkCategoryCategory,related_name='beverege_items', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Beverage Items'

    def __str__(self):
        return self.name

