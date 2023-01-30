from django.http import Http404
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView

from core.constants import LanguageChoice
from website import models as website_models


class ArticleListView(ListView):
    model = website_models.Article
    template_name = 'website/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        lang = self.kwargs.get('lang')
        # we can create separate function for this task
        if not lang or lang.lower() not in LanguageChoice.get_enabled_languages():
            lang = LanguageChoice.get_default()
        return website_models.Article.objects.filter(lang__iexact=lang)
