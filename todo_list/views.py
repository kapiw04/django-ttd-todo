from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, View, DeleteView
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


class AddTodoItemView(View):
  form_class = TodoItemForm

  def post(self, request, *args, **kwargs):
    if request.method != "POST":
      return

    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()

    return redirect("index")


class UpdateTodoItemView(View):
  form_class = TodoItemForm

  def post(self, request, *args, **kwargs):
    pk = kwargs.get('id')
    if request.method != "POST":
      return

    form = self.form_class(request.POST)
    if form.is_valid():
      task = TodoItem.objects.get(pk=pk)
      task.title = form.cleaned_data["title"]
      task.desc = form.cleaned_data["desc"]
      task.save()

    return redirect("index")

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
