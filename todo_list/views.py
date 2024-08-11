from django.shortcuts import render
from django.views.generic import TemplateView

from todo_list.models import TodoItem

from .forms import TodoItemForm

# Create your views here.
class HomeView(TemplateView):
  form_class = TodoItemForm
  template_name = "index.html"

  def get(self, request, *args, **kwargs):
    form = self.form_class()
    tasks = TodoItem.objects.all()
    return render(request, self.template_name, {"form": form, "tasks": tasks})
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()


    tasks = TodoItem.objects.all()
    return render(request, self.template_name, {"form": form, "tasks": tasks})

  
  