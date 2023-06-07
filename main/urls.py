from django.urls import path, include
from .views import index, posts_by_page

app_name = 'main'


urlpatterns = [
    path('', index, name='home'),
    path('pbp', posts_by_page, name='pbp'),
]
