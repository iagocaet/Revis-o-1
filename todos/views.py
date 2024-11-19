from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list")

class TodoListView(ListView):
    model =Todo

def todo_list(request):
        todos = Todo.objects.all()
        return render(request, "todo_list.html", {"todos": todos})
# Create your views here.
