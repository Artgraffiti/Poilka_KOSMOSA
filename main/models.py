from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=125, verbose_name='Название категории')
    slug = models.SlugField(unique=True, max_length=255, editable=False, verbose_name='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время первой публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

