from django.shortcuts import render
from .models import News
# Create your views here.

def index(request):
    c=News.objects.all()
    return render(request,"Blog\Home.html",{'c':c})

def contact(request):
    return render(request,"Blog\Aboutme.html",{'content':['if you would like to contact me, please E-mail me','smukul9747@gmail.com']})