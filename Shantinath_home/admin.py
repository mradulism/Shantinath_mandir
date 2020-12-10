from django.contrib import admin
from .models import Abhishek
# Register your models here.

@admin.register(Abhishek)
class AbhishekAdmin(admin.ModelAdmin):
    list_display=['Booking_id','name','familyname','address','contact','email','city','state','pincode','eventdate']