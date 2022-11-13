from django import forms

from emergency_request import models


class EmergencyServiceForm(forms.ModelForm):
    class Meta:
        model = models.EmergencyService
        fields = '__all__'


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = '__all__'


class RequestForm(forms.ModelForm):
    class Meta:
        model = models.Request
        fields = '__all__'
