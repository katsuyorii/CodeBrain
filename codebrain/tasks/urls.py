from django.urls import path
from .views import IndexView, TasksView, TaskDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('tasks/<slug:task_slug>', TaskDetailView.as_view(), name='task-detail'),
]
