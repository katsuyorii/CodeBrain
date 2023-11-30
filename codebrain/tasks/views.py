from django.views.generic import TemplateView, ListView, DetailView
from .models import Task, Solutiuon


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


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task-detail.html'
    context_object_name = 'task'
    slug_url_kwarg = 'task_slug'

    def get_queryset(self):
        queryset = Task.objects.filter(slug=self.kwargs.get(self.slug_url_kwarg)).select_related('complexity')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['solutions'] = Solutiuon.objects.filter(task_id=self.object.pk).select_related('prog_lang')

        return context
