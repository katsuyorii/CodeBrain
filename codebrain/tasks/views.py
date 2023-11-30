from django.views.generic import TemplateView, ListView, DetailView
from .models import Task, Solutiuon, Comment
from .forms import AddCommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


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


class TaskDetailView(DetailView, FormMixin):
    model = Task
    template_name = 'tasks/task-detail.html'
    context_object_name = 'task'
    slug_url_kwarg = 'task_slug'
    form_class = AddCommentForm

    def get_queryset(self):
        queryset = Task.objects.filter(slug=self.kwargs.get(self.slug_url_kwarg)).select_related('complexity')

        return queryset

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'task_slug': self.kwargs.get(self.slug_url_kwarg)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['solutions'] = Solutiuon.objects.filter(task_id=self.object.pk).select_related('prog_lang')
        context['comments'] = Comment.objects.filter(task_id=self.object.pk).select_related('author')
        context['form'] = self.get_form()

        return context

    def post(self, request, *args, **kwargs):
        current_task = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comm = form.save(commit=False)
            comm.author_id = request.user.pk
            comm.task_id = current_task.pk
            comm.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
