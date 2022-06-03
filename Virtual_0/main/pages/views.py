from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello Django community!')
    return render(request, 'pages/index.html')

def about(request):
    return HttpResponse('About page.')