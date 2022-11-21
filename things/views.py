from django.shortcuts import render
from .forms import ThingForum


def home(request):
    form = ThingForum
    return render(request, 'home.html', {'form': form})
