from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date')
    inlines = [
        CategoryInline,
    ]

@admin.register(Category)
class Catagoryadmin(admin.ModelAdmin):
    exclude = ('posts',)

