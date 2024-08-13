from typing import Any
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
    context["tasks"] = TodoItem.objects.all() 
    context["form"] = TodoItemForm()
    return context
  



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
