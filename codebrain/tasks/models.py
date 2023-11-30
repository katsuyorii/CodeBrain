from django.db import models
from django.urls import reverse
from users.models import User


class Tag(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Complexity(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'


class ProgLang(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программиирования'


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок задачки', max_length=255)
    description = models.TextField(verbose_name='Описание задачки')
    complexity = models.ForeignKey(verbose_name='Сложность', to=Complexity, on_delete=models.CASCADE)
    tags = models.ManyToManyField(verbose_name='Теги', to=Tag)
    slug = models.SlugField(verbose_name='Слаг', max_length=255, null=True)
    content = models.TextField(verbose_name='Примеры и доп. описание', null=True, blank=True, help_text='*Необязательно')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"task_slug": self.slug})

    class Meta:
        verbose_name = 'Задачка'
        verbose_name_plural = 'Задачки'


class Solutiuon(models.Model):
    task = models.ForeignKey(verbose_name='Задача', to=Task, on_delete=models.CASCADE)
    prog_lang = models.ForeignKey(verbose_name='Язык программирования', to=ProgLang, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Решение задачки')

    def __str__(self):
        return f'{self.prog_lang.name} | {self.task.title}'

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'


class Comment(models.Model):
    task = models.ForeignKey(verbose_name='Задача', to=Task, on_delete=models.CASCADE)
    author = models.ForeignKey(verbose_name='Автор', to=User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст комментария')
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.author.username} | {self.task.title}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
