from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .twitter import tweePy
from .serializers import *
from  django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'application.html')


def get_tweets_page(request):
    return index(request)


def get_tweets_data(request):
    serializer = TweetSerializer(tweePy.get_tweets(page=int(request.GET.get('page', 0))), many=True)
    return JsonResponse(serializer.data, safe=False)


def get_media_page(request):
    return index(request)


def get_media_data(request):
    serializer = MediaSerializer(tweePy.get_media(page=int(request.GET.get('page', 0))), many=True)
    return JsonResponse(serializer.data, safe=False)


