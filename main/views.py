from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item


# Create your views here.
def home(request, id):
    todo_list = TodoList.objects.get(id=id)
    item_list = todo_list.item_set.all()
    context = {
        'todo_list': todo_list,
        'item_list': item_list,
    }
    return render(request, 'main/home.html', context)


