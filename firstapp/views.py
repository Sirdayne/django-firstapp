from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def articles(request):
    return HttpResponse('articles')

def articlesDetails(request, id):
    response = 'id: ' + str(id)
    return HttpResponse(response)

