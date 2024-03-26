from django.shortcuts import render


def todo_list(request):
    pessoas = []
    if request.method == "POST":
        nome = request.POST.get('nome', None)
        pessoas.append(nome) 
    return render(request, "lista/todo_list.html", {'pessoas': pessoas})