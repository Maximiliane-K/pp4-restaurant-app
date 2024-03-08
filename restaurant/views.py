from django.shortcuts import render
from .models import HomePage


# Create your views here.

def home(request):
    content_home = HomePage.objects.last()

    context = {'content_home': content_home}

    return render(request, 'index.html', context)
