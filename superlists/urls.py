"""
URL configuration for superlists project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from todo_list.views import (
    TodoItemListView,
    TodoItemDetailView,
    TodoItemUpdateView,
    TodoItemCreateView,
    TodoItemDeleteView,
    TodoItemToggleCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoItemListView.as_view(), name="index"),
    path("task/<int:id>/", TodoItemDetailView.as_view(), name="details"),
    path("add/", TodoItemCreateView.as_view(), name="add"),
    path("task/update/<int:id>/", TodoItemUpdateView.as_view(), name="update"),
    path("task/delete/<int:id>/", TodoItemDeleteView.as_view(), name="delete"),
    path("task/complete/<int:id>/", TodoItemToggleCompleteView.as_view(), name="complete"),
]
