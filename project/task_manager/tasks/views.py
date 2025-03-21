from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import date

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date = request.POST.get('due_date', None)

        if due_date:
            try:
                due_date = date.fromisoformat(due_date)
                if due_date > date.today():
                    status = 'Upcoming'
                elif due_date == date.today():
                    status = 'Due Today'
                else:
                    status = 'Overdue'
            except ValueError:
                return render(request, 'task_create.html', {'error': 'Invalid date format!'})
        else:
            due_date = None
            status = 'Upcoming'

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status
        )
        return redirect('task_list')  # Redirect to task list

    return render(request, 'task_create.html')


def task_list(request):
    tasks = Task.objects.all()
    today = date.today()

    for task in tasks:
        if task.due_date:
            if task.due_date < today:
                task.status = 'Overdue'
                task.css_class = 'text-danger'  # Red for overdue
            elif task.due_date == today:
                task.status = 'Due Today'
                task.css_class = 'text-warning'  # Yellow for due today
            else:
                task.status = 'Upcoming'
                task.css_class = 'text-success'  # Green for upcoming
            task.save(update_fields=['status'])  # Optimize DB updates

    return render(request, 'task_list.html', {'tasks': tasks})


def task_update(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title', task.title).strip()
        task.description = request.POST.get('description', task.description).strip()
        due_date = request.POST.get('due_date', None)

        if due_date:
            try:
                due_date = date.fromisoformat(due_date)
                task.due_date = due_date
                if due_date > date.today():
                    task.status = 'Upcoming'
                elif due_date == date.today():
                    task.status = 'Due Today'
                else:
                    task.status = 'Overdue'
            except ValueError:
                return render(request, 'task_update.html', {'task': task, 'error': 'Invalid date format!'})

        task.save()
        return redirect('task_list')

    return render(request, 'task_update.html', {'task': task})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':  # Confirm deletion
        task.delete()
        return redirect('task_list')

    return render(request, 'task_delete.html', {'task': task})  # Show confirmation
