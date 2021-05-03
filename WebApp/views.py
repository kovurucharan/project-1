from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from WebApp.models import ItemsList

def Items(request):
    obj=ItemsList.objects.all()
    return render(request,'MyApp/item.html',{'obj':obj})

def create(request):
    return render(request,'MyApp/create.html')

def Cook(request):
    print(request.FILES)
    ItemsList.objects.create(itemname=request.POST["iname"],
                             ingredients=request.POST["ingredients"],
                             process=request.POST["process"],
                             image=request.FILES["image"])
    return HttpResponseRedirect('/home/item/')


def detail(request,id=None):
    jk= ItemsList.objects.get(id=id)
    return render(request,'MyApp/details.html',{'jk':jk})


def delete(request,id=None):
    ItemsList.objects.get(id=id).delete()
    return HttpResponseRedirect('/home/item/')

