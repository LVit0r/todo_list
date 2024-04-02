from django.shortcuts import render
from lista.models import TodoList

pessoas = []
def todo_list(request):
   
    todos = TodoList.objects.all()
    return render(request, "lista/todo_list.html", {'todos': todos})


def home(request):
    return render(request, "lista/home.html")