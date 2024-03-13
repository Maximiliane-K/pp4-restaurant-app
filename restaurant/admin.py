from django.contrib import admin
from .models import HomePage, Category, MenuItems, BeverageCategory, BeverageItems


admin.site.register(HomePage)
admin.site.register(Category)
admin.site.register(MenuItems)
admin.site.register(BeverageCategory)
admin.site.register(BeverageItems)
