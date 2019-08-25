from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/text', views.get_tweets_page, name='tweets_page'),
    path('home/text/data', views.get_tweets_data, name='tweets_data'),

    path('home/media', views.get_media_page, name='media_page'),
    path('home/media/data', views.get_media_data, name='media_data'),
]
