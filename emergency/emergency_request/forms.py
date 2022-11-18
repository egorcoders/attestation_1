from datetime import datetime as dt

from django import forms
from django.core.exceptions import ValidationError

from emergency_request import models


class EmergencyServiceForm(forms.ModelForm):
    class Meta:
        model = models.EmergencyService
        fields = '__all__'


class ApplicantForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        birthdate = cleaned_data.get('birthdate')
        phone_number = cleaned_data.get('phone_number')

        if birthdate.year > dt.now().year:
            raise ValidationError(f'Год рождения заявителя {birthdate.year} превышает текущий {dt.now().year}')
        if len(phone_number) > 11:
            raise ValidationError(f'Телефон {phone_number} превышает 11 знаков')

    class Meta:
        model = models.Applicant
        fields = '__all__'


class RequestForm(forms.ModelForm):
    class Meta:
        model = models.Request
        fields = '__all__'
