from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()
# Create your views here.
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
        return redirect("/")

    context = {"tasks":tasks, "form":form}
    return render(request, 'tasks/task_list.html', context)

@login_required
def UpdateTask(request, pk):
    task = Task.objects.get(id=pk , user=request.user)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form  = TaskForm(request.POST, instance=task)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
        return redirect("/")

    context = {"form":form}
    return render(request, 'tasks/update_list.html', context)


@login_required
def CompleteTask(request, pk):
    item  = get_object_or_404(Task, id=pk , user=request.user)
    item.complete = True
    item.save()
    return redirect("/")

@login_required
def DeleteTask(request, pk):
    item = get_object_or_404(Task, id=pk , user=request.user)
    item.delete()
    return redirect("/")