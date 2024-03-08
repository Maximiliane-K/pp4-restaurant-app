from django.shortcuts import render
from .models import HomePage, Category, MenuItems


# Create your views here.

def home(request):
    content_home = HomePage.objects.last()

    context = {'content_home': content_home}

    return render(request, 'index.html', context)


def foodmenu(request):
    categories = Category.objects.all()
    menu_items = MenuItems.objects.all()
    context = {'categories': categories, 'menu_items': menu_items}
    return render(request, 'menu.html', context)


