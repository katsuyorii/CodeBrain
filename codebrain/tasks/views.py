from django.views.generic import TemplateView, ListView
from .models import Task, ProgLang, Complexity, Tag


class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class TasksView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    paginate_by = 3

    def get_queryset(self):
        queryset = Task.objects.all().select_related('complexity')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачки по программированию'

        return context
