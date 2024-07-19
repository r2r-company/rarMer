# views.py
import json
from api.models import ComputerInfo
from django.shortcuts import render
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from equipment.models import EquipmentInventory
from workers.models import Worker

from .models import Task, TaskComment
from .forms import TaskForm, TaskCommentForm
from django.core.paginator import Paginator

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def add_comment(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = TaskCommentForm(initial={'task': task, 'user': request.user})
    return render(request, 'tasks/add_comment.html', {'form': form, 'task': task})

@login_required
def task_list(request):
    tasks_created_by_user = Task.objects.filter(created_by=request.user)
    tasks_assigned_to_user = Task.objects.filter(assigned_to=request.user)
    context = {
        'tasks_created_by_user': tasks_created_by_user,
        'tasks_assigned_to_user': tasks_assigned_to_user,
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    comments = TaskComment.objects.filter(task=task)
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments})

@login_required
def my_tasks(request):
    user_tasks = Task.objects.filter(assigned_to=request.user)
    new_tasks = user_tasks.filter(status='Новий')
    in_progress_tasks = user_tasks.filter(status='В процесі')
    completed_tasks = user_tasks.filter(status='Завершено')
    context = {
        'new_tasks': new_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'tasks/my_tasks.html', context)

@login_required
def take_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.assigned_to == request.user:
        task.status = 'В процесі'
        task.save()
    return redirect('my_tasks')

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.assigned_to == request.user:
        task.status = 'Завершено'
        task.save()
    return redirect('my_tasks')

@login_required
def task_update_status(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.status = request.POST.get('status')
        task.save()
    return redirect('my_tasks')

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = TaskComment.objects.filter(task=task)
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments})

@login_required
def new_tasks(request):
    tasks = Task.objects.filter(status='Новий')
    tasks_list = [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
    return JsonResponse(tasks_list, safe=False)

@login_required
def dashboard(request):
    new_tasks_count = Task.objects.filter(status='Новий').count()
    computer_infos = ComputerInfo.objects.all().order_by('-timestamp')[:10]
    return render(request, 'api/dashboard.html', {
        'new_tasks_count': new_tasks_count,
        'computer_infos': computer_infos,
    })

@login_required
def notify(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hostname = data.get('hostname')
        ip_address = data.get('ip_address')
        timestamp = timezone.now()

        ComputerInfo.objects.create(hostname=hostname, ip_address=ip_address, timestamp=timestamp)
        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def assign_task(request, equipment_id):
    equipment = get_object_or_404(EquipmentInventory, id=equipment_id)
    workers = Worker.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.equipment = equipment
            task.created_by = request.user
            task.save()
            return redirect('task_list')  # Редирект до списку задач або інша відповідна сторінка
    else:
        form = TaskForm()

    return render(request, 'tasks/assign_task.html', {
        'form': form,
        'equipment': equipment,
        'workers': workers,
    })


