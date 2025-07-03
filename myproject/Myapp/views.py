from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"Myapp/index.html")

def contact(request):
    return render(request,"Myapp/contact.html")

def name(request):
    return render(request,"Myapp/name.html")