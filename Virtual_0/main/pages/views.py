from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello Django community!')
    return render(request, 'pages/index.html',{'name':'Mourad','age':23,'lname':None})

def about(request):
    return render(request, 'pages/about.html')