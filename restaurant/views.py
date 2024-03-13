from django.shortcuts import render
from .models import HomePage, Category, MenuItems, BeverageCategory, BeverageItems


def home(request):
    """
    View to display introduction text on landing page
    """
    content_home = HomePage.objects.last()

    context = {'content_home': content_home}

    return render(request, 'index.html', context)


def foodmenu(request):
    """
    View to show all food menu items 
    """
    categories = Category.objects.all()
    menu_items = MenuItems.objects.all()
    
    context = {'categories': categories, 'menu_items': menu_items}

    return render(request, 'food.html', context)


def beveragemenu(request):
    """
    View to show all beverages available 
    """
    beverage_categories = BeverageCategory.objects.all()
    beverage_items = BeverageItems.objects.all()
    
    context = {'beverage_categories': beverage_categories, 'beverage_items': beverage_items}

    return render(request, 'drinks.html', context)


