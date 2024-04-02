from django.urls import path
from lista.views import todo_list


urlpatterns = [

path('cadastrotarefas/',todo_list, name="cadastrotarefas")

]