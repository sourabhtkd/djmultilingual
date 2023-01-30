from django.contrib import admin
from website import models as website_models


# class ArticleInline(admin.StackedInline):
#     model = website_models.Article
#     extra = 0


# Register your models here.
@admin.register(website_models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_title', 'lang']
    list_display_links = ['id', 'get_title']

    def get_title(self, obj):
        if obj.parent:
            return f"{obj.parent.title}: {obj.lang}"
        return f"{obj.title}: {obj.lang}"

    get_title.short_description = 'Title'
    get_title.admin_order_field = 'title'
