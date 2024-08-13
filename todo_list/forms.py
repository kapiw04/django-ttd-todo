from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
  class Meta:
    model = TodoItem
    fields = ("title", "desc")
    labels = {
      "title": "Title",
      "desc": "Description"
    }
    ids = {
      "title": "input_title",
      "desc": "input_desc"
    }


