from django.shortcuts import render
from .models import HomePage, Category, MenuItems


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

    return render(request, 'menu.html', context)


