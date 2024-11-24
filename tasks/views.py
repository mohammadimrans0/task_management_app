from django.shortcuts import render, redirect
from .forms import TaskForm
from tasks.models import TaskModel

# Add Task
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = TaskForm()

    return render(request, 'add_task.html', {'form': task_form})

# Show Task
def show_task(request):
    data = TaskModel.objects.all()
    print(data)

    return render(request, 'show_task.html', {'tasks': data})


# Edit Task
def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')

    return render(request, 'add_task.html', {'form': task_form})

# Delete Task
def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
