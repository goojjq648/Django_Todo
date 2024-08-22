from django.shortcuts import render, redirect
from todoapp.models import Todolist
from todoapp.models import TodoStatus
from django.contrib import messages

# Create your views here.


def index(request):
    allTodoData = Todolist.objects.all()
    return render(request, 'todoapp/todo.html', locals())


def switchtodo_status(request, todo_id):
    try:
        todoData = Todolist.objects.get(todo_id=todo_id)
        todoData.completed = not todoData.completed
        todoData.save()
    except Todolist.DoesNotExist:
        messages.error(request, '待辦事項不存在。')
        print('doesNotExist')
    except Todolist.MultipleObjectsReturned:
        messages.error(request, '待辦事項有異常重覆。')
        print('multipleObjectsReturned')

    return redirect('todo:index')


def add_tododata(request):
    if not request.method == 'POST':
        return redirect('todo:index')

    todo = Todolist()
    todo.completed = TodoStatus.UNFINISHED.value
    todo.todo = request.POST.get('todo_content')

    todo.save()
    return redirect('todo:index')


def delete_tododata(request, todo_id):
    try:
        tododata = Todolist.objects.get(todo_id=todo_id)
        tododata.delete()
        messages.success(request, '刪除成功。')
        return redirect('todo:index')
    except Todolist.DoesNotExist:
        messages.error(request, '待辦事項不存在，刪除失敗。')
        print('doesNotExist')
    except Todolist.MultipleObjectsReturned:
        messages.error(request, '待辦事項有異常重覆，刪除失敗。')
        print('multipleObjectsReturned')

    return redirect('todo:index')
