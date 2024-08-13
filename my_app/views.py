from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()

    return render(request,"home.html")


def register(request):
    name=request.POST['name']
    password=request.POST['password']
    address=request.POST['address']
    mail=request.POST['mail']
    return render(request,"output.html",{'Name':name,'Password':password,'Address':address,'Mail':mail})


