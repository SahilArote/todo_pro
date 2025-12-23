from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/local/login/')
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title or description:
            Todo.objects.create(title=title, description=description, owner=request.user)

        return redirect('home')
    todos = Todo.objects.filter(owner=request.user)
    return render(request, 'home.html', {'todos': todos})

def toggle_complete(request, id):
    todo = get_object_or_404(Todo, id=id, owner=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')


def delete(request, id):
    todo = get_object_or_404(Todo, id=id, owner=request.user)
    todo.delete()
    return redirect('home')

@login_required(login_url='/accounts/local/login/')
def history(request, id):
    todo = get_object_or_404(Todo, id=id, owner=request.user)
    records = todo.history.all()
    return render(request, 'history.html', {'todo': todo, 'records': records})

def history_index(request):
    todos = Todo.objects.filter(owner=request.user)
    return render(request, 'history_index.html', {'todos': todos})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def local_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def local_logout(request):
    auth_logout(request)
    return redirect('home')


# ...existing code...
# Create your views here.
