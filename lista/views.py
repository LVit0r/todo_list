from django.shortcuts import render


def todo_list(request):
    nome = 'Luiz'
    pessoas = ['Luiz', 'Fernanda', 'Ariadne']
    return render(request, "lista/todo_list.html", {"nome": nome, 'pessoas': pessoas})