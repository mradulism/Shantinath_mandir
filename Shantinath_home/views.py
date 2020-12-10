from django.shortcuts import render
from django.http import request,HttpResponse
from .models import Abhishek
# Create your views here.
def index(request):
    return render(request,'Shantinath_home/index.html')
def contact(request):
    return HttpResponse('contact')
def abhishek(request):
    if(request.method=='POST'):
        name=request.POST.get('name',"")
        familyname=request.POST.get('familyname',"")
        address=request.POST.get('address',"")
        contact=request.POST.get('contact',"")
        email=request.POST.get('email',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
        eventdate=request.POST.get('eventdate',"")
        pincode=request.POST.get('pincode',"")
        BookingObj=Abhishek(name=name,familyname=familyname,address=address,contact=contact,email=email,city=city,state=state,pincode=pincode,eventdate=eventdate)
        BookingObj.save()
    return render(request,'Shantinath_home/Abhishek.html')
    