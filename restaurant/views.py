from django.shortcuts import render
from .models import HomePage


# Create your views here.

def home(request):
    content_home = HomePage.objects.all()

    context = {'home': home,}

    return render(request, 'home/home.html', context)
