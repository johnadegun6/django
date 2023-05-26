from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


from.models import(
    Doctor,
    RequestConsultation,
    Appointment,
    symptoms,
    Drugs,
    MedicalHistory,
    specialization

)


def view_movie(request):
    pass

class Home(View):
    def get(self, request):
        return HttpResponse('This is home page')

    # def post(self, request):
    #     pass


class CreateDoctor(CreateView):
    model = Doctor
    fields= "_all_"
    exclude = ['is_verified', 'is_booked']
    success_url = "/"
    # template_name_suffix


class CreateSpecialization(CreateView):
    model = specialization
    fields= "_all_"
    success_url = "/"


class SpecializationDetail(DetailView):
    model = specialization


class SpecializationList(ListView):
    model = specialization
    # template_name= "app/create_doctor.html"

class RemoveSpecialization(LoginRequiredMixin, DeleteView):
    model = specialization
    login_url = "/"

class UpdateSpecialization(DeleteView):
    model = specialization