from django.db import models


    


class TodoList(models.Model):
    tarefa = models.CharField(max_length = 100, null = False, blank = False)
    descricao = models.TextField(max_length = 1000, null = True, blank = True)

