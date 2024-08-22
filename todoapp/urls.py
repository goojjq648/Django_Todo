from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo/', views.add_tododata, name='add'),
    path('change/<int:todo_id>', views.switchtodo_status, name='change'),
    path('delete/<int:todo_id>', views.delete_tododata, name='delete'),
]
