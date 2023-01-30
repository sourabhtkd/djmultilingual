from django.contrib import admin
from website import models as website_models


# class ArticleInline(admin.StackedInline):
#     model = website_models.Article
#     extra = 0


# Register your models here.
@admin.register(website_models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'lang']
    list_display_links = ['id', 'title']
