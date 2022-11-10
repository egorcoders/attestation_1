from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from emergency_request import models


class AddEmergencyService(forms.ModelForm):
    class Meta:
        model = models.EmergencyService
        fields = ('name', 'number', 'code')


class AddRequest(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].empty_label = 'Заявитель не выбрана'

    class Meta:
        model = models.Request
        fields = ('status_appeal', 'service', 'applicant', 'number_cases',
                  'not_call')


class AddApplicant(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = ('photo_applicant', 'surname', 'name', 'name_father', 'gender',
                  'date', 'health_status', 'number', 'slug')

    def clean_number(self):
        nummber = self.cleaned_data['number']
        if len(nummber) > 11:
            raise ValidationError('Длинна больше 11')
        return nummber

    def clean_date(self):
        dt = self.cleaned_data['date']
        if date.today() < dt:
            raise ValidationError('Неправильная дата рождения')
        return dt
