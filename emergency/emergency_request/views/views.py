from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from emergency_request.models import EmergencyService, Applicant, Request
from emergency_request.forms import EmergencyServiceForm, ApplicantForm, RequestForm
from emergency_request.consts import color_choices


class EmergencyServiceView(ListView):
    model = EmergencyService
    template_name = 'emergency_request/emergency_list_view.html'
    context_object_name = 'emergencies'


class ApplicantView(ListView):
    model = Applicant
    template_name = 'emergency_request/applicant_list_view.html'
    context_object_name = 'applicants'


class RequestView(ListView):
    model = Request
    template_name = 'emergency_request/request_list_view.html'
    context_object_name = 'requests'


class EmergencyServiceViewDetail(DetailView):
    model = EmergencyService
    template_name = 'emergency_request/emergency.html'
    context_object_name = 'emergency'


class ApplicantViewDetail(DetailView):
    model = Applicant
    template_name = 'emergency_request/applicant.html'
    context_object_name = 'applicant'


class RequestViewDetail(DetailView):
    model = Request
    template_name = 'emergency_request/request.html'
    context_object_name = 'single_request'


class ApplicantUpdate(UpdateView):
    model = Applicant
    template_name = 'emergency_request/form.html'
    fields = ['first_name']

    def form_valid(self, form):
        return redirect('/')
