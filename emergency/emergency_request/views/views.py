import django_filters
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django_filters import views

from emergency_request.filters import EmergencyServiceFilter, ApplicantFilter, RequestFilter
from emergency_request.forms import EmergencyServiceForm, ApplicantForm, RequestForm
from emergency_request.models import EmergencyService, Applicant, Request


class ApplicantIdView(TemplateView):
    template_name = 'emergency_request/applicant_view.html'

    def get_context_data(self, **kwargs):
        pk = self.request.GET['id']
        applicant = get_object_or_404(Applicant, pk=pk)
        return {'applicant': applicant}


class ApplicantPhoneView(TemplateView):
    template_name = 'emergency_request/applicant_view.html'

    def get_context_data(self, **kwargs):
        phone = self.request.GET['phone_number']
        applicant = get_object_or_404(Applicant, phone_number__contains=phone)
        return {'applicant': applicant}


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


class EmergencyServiceFilter(django_filters.views.FilterView):
    model = EmergencyService
    template_name = 'emergency_service_filter.html'
    filterset_class = EmergencyServiceFilter


class ApplicantFilter(django_filters.views.FilterView):
    model = Applicant
    template_name = 'applicant_filter.html'
    filterset_class = ApplicantFilter


class RequestFilter(django_filters.views.FilterView):
    model = Request
    template_name = 'request_filter.html'
    filterset_class = RequestFilter
