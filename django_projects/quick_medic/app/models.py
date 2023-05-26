from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.contrib.gis import models

# Create your models here.

STATUS = (('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'))

class location(models.Model):
    pass
    # country
    # state
    # city
    # zip code- longitude, latitude


class specialization(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("specialization_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.name
    

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    speciality = models.ForeignKey(specialization, on_delete=models.SET_NULL, null=True)
    portfolio_number = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.speciality.name}"
    

class Patient(models.Model):
    pass

class RequestConsultation(models.Model):
    """Patience request consultation with available doctor. The doctor sets appointment if consultation is accepted"""
    Patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "requests")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name= "appointments", verbose_name='request for consultation')
    symptoms = models.TextField()
    ststus = models.CharField(max_length=200, choices=STATUS)

    def __str__(self) -> str:
        return f"{self.patient}-{self.status}"


class Appointment(models.Model):
    consult = models.ForeignKey(RequestConsultation, on_delete=models.CASCADE)
    type = models.CharField(max_length=200,  choices = (('virtual', 'Virtual'), ('physical', 'Physical'), ('private','Private')))
    date = models.DateTimeField(verbose_name= "Date and Time for appointment")

    def __str__(self) -> str:
        return f"{self.type}-{self.date}"
    

class symptoms(models.Model):
    name = models.CharField(max_length=200, verbose_name='Symptoms')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    

class Drugs(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name of the drugs')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name= "Medical History")
    illness = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(symptoms)
    drugs =  models.ManyToManyField(Drugs)
    allergies = models.TextField()
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name= "Patients Attended")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.illness}-{self.doctor}-{self.date}"

#GIS