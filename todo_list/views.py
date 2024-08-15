from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from todo_list.models import TodoItem
from .forms import TodoItemForm

# Create your views here.
class TodoItemListView(ListView):
  model = TodoItem
  template_name = "index.html"

  def get_context_data(self, **kwargs) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context["tasks"] = TodoItem.objects.filter(completed=False)
    context["completed"] = TodoItem.objects.filter(completed=True)
    context["form"] = TodoItemForm()
    return context
  


class TodoItemCreateView(CreateView):
  model = TodoItem
  fields = ["title", "desc"]
  success_url = reverse_lazy("index") 
  
  def form_invalid(self, form):
    response = HttpResponse("Error validating form: " + str(form.errors))
    response.status_code = 400
    return response
  
class TodoItemUpdateView(UpdateView):
  model = TodoItem
  fields = ["title", "desc"]
  pk_url_kwarg = "id"
  success_url = reverse_lazy("index")

  def form_invalid(self, form):
    response = HttpResponse("Error validating form: " + str(form.errors))
    response.status_code = 400
    return response
  
class TodoItemToggleCompleteView(UpdateView):
  model = TodoItem
  fields = ["completed"]
  pk_url_kwarg = "id"
  success_url = reverse_lazy("index")

class TodoItemDeleteView(DeleteView):
  model = TodoItem  
  pk_url_kwarg = "id"
  success_url = reverse_lazy("index")

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
