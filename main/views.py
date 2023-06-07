from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Post


def index(request):
    PER_PAGE = 6
    category = request.GET.get('category')
    all_posts = Post.objects.all()

    if category:
        all_posts = all_posts.filter(category__slug=category)

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        paginator = Paginator(all_posts, PER_PAGE)
        page_number = request.GET.get('page', 2)  # Получаем номер страницы из параметров запроса
        page = paginator.get_page(page_number)  # Получаем объект страницы

        return render(request, 'index-ajax.html', {'page': page, 'posts': page.object_list})
    else:
        categories = Category.objects.all()
        paginator = Paginator(all_posts, PER_PAGE)
        page = paginator.get_page(1)  # Первая страница по умолчанию
        context = {
            'page': page,
            'categories': categories,
            'posts': page.object_list,
        }
        return render(request, 'index.html', context)

