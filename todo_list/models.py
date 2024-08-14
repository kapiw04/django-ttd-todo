from django.db import models
from django.core.exceptions import ValidationError
import os

# Create your models here.

class TodoItem(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=30)
  desc = models.CharField(max_length=500)
  date = models.DateField(auto_now=True)
  completed = models.BooleanField(default=False)

  def clean(self) -> None:
    if self.title.strip() == "":
      os.system("echo 'Title cannot be empty.' >> error.log")
      raise ValidationError("Title cannot be empty.")