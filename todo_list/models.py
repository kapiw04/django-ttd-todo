from django.db import models

# Create your models here.

class TodoItem(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=30)
  desc = models.CharField(max_length=500)
  date = models.DateField(auto_now=True)
  completed = models.BooleanField()
