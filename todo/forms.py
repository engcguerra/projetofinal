from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = "__all__"
        
        widgets = {}
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'tarefa...'}),
        }
    
    