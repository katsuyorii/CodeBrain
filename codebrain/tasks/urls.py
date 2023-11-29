from django.urls import path
from .views import IndexView, TasksView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', TasksView.as_view(), name='tasks'),
]
