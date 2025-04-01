from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Project
from .forms import TaskForm

# Dashboard View (Home page)
def dashboard(request):
    projects = Project.objects.all()  # Fetch all projects
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'task_manager/dashboard.html', {
        'projects': projects,
        'tasks': tasks
    })

# Task Create View
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after creating a task
    else:
        form = TaskForm()
    return render(request, 'task_manager/task_create.html', {'form': form})

# Task List View
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from database
    return render(request, 'task_manager/task_list.html', {'tasks': tasks})

# Task Update View
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after updating a task
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_manager/task_update.html', {'form': form, 'task': task})

# Task Delete View
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect to task list after deleting a task
    return render(request, 'task_manager/task_delete.html', {'task': task})

# Calendar View
def calendar_view(request):
    tasks = Task.objects.all()
    events = []
    for task in tasks:
        events.append({
            'title': task.title,
            'start': task.deadline.isoformat(),  # Using ISO format for FullCalendar
            'end': task.deadline.isoformat(),
        })
    return render(request, 'task_manager/calendar.html', {'events': events})
