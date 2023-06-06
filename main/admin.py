from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'author', 'category',)
    list_display_links = ('title', 'content', 'category',)

    def save_model(self, request, obj, form, change):

        if not change:  # Проверяем, что пост только создается
            obj.author = request.user  # Присваеваем полю автор текущего пользователя

        super(PostAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )



