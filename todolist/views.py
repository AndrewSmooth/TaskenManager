from django.shortcuts import render
from .models import Task


def index(request):
    tsks = Task.objects.filter(is_active=False)   
    context = {'tsks': tsks}
    return render(request, 'main/index.html', context)