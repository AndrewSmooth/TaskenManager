from django.shortcuts import render
from .models import Task

from django.contrib.auth.decorators import login_required


def all_tasks(request):
    tsks = Task.objects.filter(is_active=False)   
    context = {'tsks': tsks}
    return render(request, 'todolist/index.html', context)



@login_required
def profile(request):
    return render(request, 'todolist/profile.html')



