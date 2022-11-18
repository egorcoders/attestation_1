from django import forms

from emergency_request import models
import django_filters


class EmergencyServiceFilter(django_filters.FilterSet):
    class Meta:
        model = models.EmergencyService
        fields = '__all__'


class ApplicantFilter(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = '__all__'


class RequestFilter(forms.ModelForm):
    class Meta:
        model = models.Request
        fields = '__all__'
