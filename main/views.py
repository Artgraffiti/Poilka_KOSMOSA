from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Post


def index(request):
    categories = Category.objects.all()
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)  # 6 элементов на странице
    page = paginator.get_page(1)  # Первая страница по умолчанию
    context = {
        'page': page,
        'categories': categories,
        'posts': page.object_list,
    }
    return render(request, 'index.html', context)


def posts_by_page(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)  # Показывать по 6 постов на каждой странице
    page_number = request.GET.get('page', 2)  # Получаем номер страницы из параметров запроса
    page = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'pbp.html', {'page': page, 'posts': page.object_list})

