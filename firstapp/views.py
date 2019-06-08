from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Record

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

def records(request):
    records = Record.objects.all()
    return render(request, "records.html", {"records": records})

def recordsCreate(request):
    if request.method == 'POST':
        record = Record()
        record.name = request.POST.get('name', '')
        record.description = request.POST.get('description', '')
        record.startTime = request.POST.get('startTime', '')
        record.endTime = request.POST.get('endTime', '')
        record.userId = request.POST.get('userId', '')
        record.save()
    return HttpResponseRedirect('/records')

def recordsEdit(request, id):
    try:
        record = Record.objects.get(id = id)

        if request.method == 'POST':
            record.name = request.POST.get('name', '')
            record.description = request.POST.get('description', '')
            record.startTime = request.POST.get('startTime', '')
            record.endTime = request.POST.get('endTime', '')
            record.userId = request.POST.get('userId', '')
            record.save()
            return HttpResponseRedirect('/records')
        else:
            return render(request, "recordsEdit.html", {"record": record})
    except Record.DoesNotExist:
        return HttpResponseNotFound("<h2>There is no such record</h2>")

def recordsDelete(request, id):
    try:
        record = Record.objects.get(id = id)
        record.delete()
        return HttpResponseRedirect('/records')
    except Record.DoesNotExist:
        return HttpResponseNotFound("<h2>There is no such record</h2>")
