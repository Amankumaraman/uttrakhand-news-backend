from django.urls import path
from .views import fetch_live_news

urlpatterns = [
    path('fetch-news/', fetch_live_news),
]
