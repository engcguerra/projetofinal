from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField('nova tarefa',max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nome