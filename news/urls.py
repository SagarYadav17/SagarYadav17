from django.urls import path
from news import views

urlpatterns = [
    path("fetch-news/", views.FetchNews.as_view(), name="fetch-news"),
    path("news/", views.News.as_view(), name="news"),
]
