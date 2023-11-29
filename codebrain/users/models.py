from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(verbose_name='Изображение', upload_to='profile-avatars', default='default.png')