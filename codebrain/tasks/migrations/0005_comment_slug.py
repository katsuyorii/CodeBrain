# Generated by Django 4.2.7 on 2023-12-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_comment_date_created_alter_task_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(max_length=255, null=True, verbose_name='Слаг'),
        ),
    ]