from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class location(models.Model):
    pass
    # country
    # state
    # city
    # zip code- longitude, latitude


class specialization(models.Model):
    name = models.CharField(max_length=200)

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    speciality = models.CharField(specialization, on_delete=models.SET_DEFAULT, null=True)
    portfolio_number = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField()
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return 
    

class Patient(models.Model):
    pass

class Appointment(models.Model):
    Patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "my_appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name= "appointments")
    reason = models.TextField()
    date = models.DateTimeField(verbose_name= "Date and Time for appointment")





#GIS