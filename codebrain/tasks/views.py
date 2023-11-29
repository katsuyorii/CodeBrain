from django.views.generic import TemplateView, ListView
from .models import Task, ProgLang, Complexity, Tag


class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class TasksView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'objects'

    def get_queryset(self):
        queryset = {
            'tasks': Task.objects.select_related('complexity').all(),
            'prog_lang': ProgLang.objects.all(),
            'complexity': Complexity.objects.all(),
            'tags': Tag.objects.all(),
        }

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачки по программированию'

        return context
