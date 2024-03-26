
from django.contrib import admin
from django.urls import path
from lista.views import todo_list

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('cadastro/',todo_list )
]
