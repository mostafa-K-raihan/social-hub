from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.get_tweets_page, name='tweets_page'),
    path('home/data', views.get_tweets_data, name='tweets_data'),
]
