from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.
def index(request):
    return render(request,'Shantinath_home/index.html')
def contact(request):
    return HttpResponse('contact')
