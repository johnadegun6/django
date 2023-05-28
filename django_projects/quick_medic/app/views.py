from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

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
    

# class DoctorDetail(DetailView):
#     model = Doctor


# class DoctorList(ListView):
#     model = Doctor

# @login_required(login_url="accounts/login")
# def removeDoctor(request):
#     pass

# class RemoveDoctor(LoginRequiredMixin, DeleteView)
#     model = Doctor
#     success_url = ""
    

# class UpdateteDoctor(UpdateView):
#     model = Doctor
#     fields = "__all__"


# DOCTOR VIEW

class CreateUser(View):
    def post(self, request):
        # user_username = request.POST.get('username')
        content_type = ContentType.objects.get_for_model(RequestConsultation)
        user_permission = Permission.objects.filter(content_type = content_type)
        user = User(username = 'user1', first_name= 'maru', last_name = 'koch', password= "1234")
        user.user_permissions.add(user_permission)
        user.save()

class CreateDoctor(CreateView):
    model = Doctor
    fields= "_all_"
    exclude = ['is_verified', 'is_booked']
    success_url = "/"
    # template_name_suffix


class DoctorDetail(DetailView):
    model = Doctor
    permission_required = ('app.can_view_doctor_detail')


class DoctorList(ListView):
    model = Doctor


class RemoveDoctor(LoginRequiredMixin, DeleteView):
    model = Doctor
    login_url = "/"


class UpdateDoctor(UpdateView):
    model = Doctor
    fields = "_all_"




# REQUEST VIEWS
class CreateRequest(CreateView):
    model = RequestConsultation
    fields = "__all__"
    template_name_suffix = "_form"

class RequestDetail(PermissionRequiredMixin, DetailView):
    model = RequestConsultation
    permission_required = ['can_consult']


class RequestList(ListView):
    model = RequestConsultation

class RemoveRequest(LoginRequiredMixin, DeleteView):
    model = RequestConsultation
    login_url = "/"


class UpdateRequest(UpdateView):
    model = RequestConsultation
    fields = "_all_"




# APPOINTMENT VIEWS
class CreateAppointment(CreateView):
    model = Appointment
    fields = "__all__"
    template_name_suffix = "app/doctor_form.html"

class AppointmentDetail(PermissionRequiredMixin, DetailView):
    model = Appointment

class AppointmentList(ListView):
    model = Appointment

class RemoveAppointment(LoginRequiredMixin, DeleteView):
    model = Appointment
    login_url = "/"


class UpdateAppointment(UpdateView):
    model = Appointment
    fields = "_all_"




# SPECIALIZATION VIEW
class CreateSpecialization(CreateView):
    model = specialization
    fields= "_all_"
    # success_url = "/"


class SpecializationDetail(PermissionRequiredMixin, DetailView):
    model = specialization


class SpecializationList(ListView):
    model = specialization
    # template_name= "app/create_doctor.html"

class RemoveSpecialization(LoginRequiredMixin, DeleteView):
    model = specialization
    login_url = "/"

class UpdateSpecialization(UpdateView):
    model = specialization
    fields = "_all_"