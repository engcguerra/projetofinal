from django.shortcuts import render,redirect
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.
def home(request):
    if request.method=="GET":
        tarefas = Tarefa.objects.all()
        formulario = TarefaForm()
    elif request.method=="POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("todo:home")
    return render(request, 'todo/home.html',{'tarefas':tarefas,"formulario":formulario})

def delete_task(request, id):
    tarefa = Tarefa.objects.filter(pk=id)
    tarefa.delete()    
    return redirect("todo:home")