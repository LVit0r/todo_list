
from django.contrib import admin
from django.urls import path,include
from lista.views import home

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('cadastro/',include('lista.urls')),
    path('', home)
]
