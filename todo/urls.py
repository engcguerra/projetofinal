from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
     path('', views.home, name='home'),
     path('del/<int:id>', views.delete_task, name='delete_task'),
]