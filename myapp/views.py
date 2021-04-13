from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def adminlogin(request):
    return render(request,'adminlogin.html')   

def userlogin(request):
    return render(request,'userlogin.html')     

# Create your views here.
