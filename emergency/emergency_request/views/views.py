from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from emergency_request.models import EmergencyService, Applicant, Request
from emergency_request.forms import EmergencyServiceForm, ApplicantForm, RequestForm
from emergency_request.consts import color_choices


class EmergencyServiceListView(ListView):
    model = EmergencyService
    template_name = 'emergency_request/emergency_list_view.html'
    context_object_name = 'emergencies'


class ApplicantListView(ListView):
    model = Applicant
    template_name = 'emergency_request/applicant_list_view.html'
    context_object_name = 'applicants'


class RequestListView(ListView):
    model = Request
    template_name = 'emergency_request/request_list_view.html'
    context_object_name = 'requests'


class EmergencyServiceDetailView(DetailView):
    model = EmergencyService
    template_name = 'emergency_request/emergency_view.html'
    context_object_name = 'emergency'


class ApplicantDetailView(DetailView):
    model = Applicant
    template_name = 'emergency_request/applicant_view.html'
    context_object_name = 'applicant'


class RequestDetailView(DetailView):
    model = Request
    template_name = 'emergency_request/request_view.html'
    context_object_name = 'single_request'


class EmergencyServiceCreateView(CreateView):
    form_class = EmergencyServiceForm
    template_name = 'emergency_request/form.html'
    success_url = '/views/emergency_list'


class ApplicantCreateView(CreateView):
    form_class = ApplicantForm
    template_name = 'emergency_request/form.html'
    success_url = '/views/applicant_list'


class RequestCreateView(CreateView):
    form_class = RequestForm
    template_name = 'emergency_request/form.html'
    success_url = '/views/request_list'


class EmergencyServiceUpdateView(UpdateView):
    model = EmergencyService
    template_name = 'emergency_request/form.html'
    success_url = '/views/emergency_list'
    fields = '__all__'


class ApplicantUpdateView(UpdateView):
    model = Applicant
    template_name = 'emergency_request/form.html'
    success_url = '/views/applicant_list'
    fields = '__all__'


class RequestUpdateView(UpdateView):
    model = Applicant
    template_name = 'emergency_request/form.html'
    success_url = '/views/request_list'
    fields = '__all__'
