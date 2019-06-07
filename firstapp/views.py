from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def articles(request):
    search = request.GET.get('search', '')
    response = 'articles'
    if search:
        response = ' ' + search
    return HttpResponse(response)

def articlesDetails(request, id):
    response = 'id: ' + str(id)
    return HttpResponse(response)

