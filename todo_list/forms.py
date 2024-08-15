from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
  class Meta:
    model = TodoItem
    fields = ("title", "desc", "completed")
    widgets = {
      "title": forms.TextInput(attrs={"id": "title-input", "class": "form-control"}),
      "desc": forms.Textarea(attrs={"id": "desc-input", "class": "form-control"}),
      "completed": forms.CheckboxInput(attrs={"id": "check-button", "onchange": "this.form.submit()",})
    } 
