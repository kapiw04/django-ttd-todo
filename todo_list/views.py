from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, View, DeleteView, CreateView, UpdateView
from todo_list.models import TodoItem
from .forms import TodoItemForm

# Create your views here.


class HomeView(TemplateView):
  form_class = TodoItemForm
  template_name = "index.html"

  def get(self, request, *args, **kwargs):
    form = self.form_class()

    tasks = TodoItem.objects.all()
    return render(request, self.template_name,
                  {"form": form,
                   "tasks": tasks}
                  )


class TodoItemCreateView(CreateView):
  model = TodoItem
  fields = ["title", "desc"]

  def get_success_url(self) -> str:
    return reverse_lazy("index")
  
class TodoItemUpdateView(UpdateView):
  model = TodoItem
  fields = ["title", "desc"]
  pk_url_kwarg = "id"

  def get_success_url(self) -> str:
    return reverse_lazy("index")
class TodoItemDeleteView(DeleteView):
  model = TodoItem  
  success_url = reverse_lazy("index")
  pk_url_kwarg = "id"

class TodoItemDetailView(DetailView):
  model = TodoItem
  template_name = "detail.html"
  pk_url_kwarg = "id"
  form_class = TodoItemForm

  def get_context_data(self, **kwargs) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context["task"] = self.object
    context["form"] = TodoItemForm(instance=self.object)
    return context
