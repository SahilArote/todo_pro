from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from list.models import * # your model
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/local/login/')
def search(request):
    query = request.GET.get('q', '')

    todos = Todo.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    ) if query else []

    return render(request, 'search.html', {
        'todos': todos,
        'query': query,
    })

