from django.db import models

# Create your models here.
class Abhishek(models.Model):
    Booking_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    familyname=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    pincode=models.IntegerField()
    eventdate=models.DateField()
def __str__(self):
    return self.name
    