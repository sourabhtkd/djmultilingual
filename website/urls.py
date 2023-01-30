from django.urls import path, re_path

from website import views

app_name = 'website'

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    re_path(r'articles/(?P<lang>[a-zA-Z]{2})/$', views.ArticleListView.as_view(), name='article_list_lang'),

]
