from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.

def index(request):
    data=Task.objects.all()
    return render(request,'work/index.html',{'data':data})
    return HttpResponse('Hello World')


def add(request):
    if(request.method=='POST'):
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        data=Task(title=title, desc=desc)
        data.save()
        data=Task.objects.all()
    return redirect('/',{'data':data})

def delete(request, id):
    result=Task.objects.get(id=id)
    result.delete()
    return redirect('/')

def update(request,id):
    result=Task.objects.get(id=id)

    return render(request,'work/update.html',{'data':result})

def updater(request,id):
    result=Task.objects.get(id=id)
    result.title=request.POST.get('title')
    result.desc=request.POST.get('desc')
    result.save()
    return redirect('/')
    