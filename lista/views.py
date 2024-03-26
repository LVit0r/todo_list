from django.shortcuts import render

pessoas = []
def todo_list(request):
   
    if request.method == "POST":
        nome = request.POST.get('nome', None)
        pessoas.append(nome) 
        print(pessoas)
    return render(request, "lista/todo_list.html", {'pessoas': pessoas})


def home(request):
    return render(request, "lista/home.html")