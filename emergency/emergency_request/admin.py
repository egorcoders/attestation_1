from django.contrib import admin
from .models import EmergencyService, Applicant, Request


class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'service_name', 'service_code', 'phone_number')
    list_editable = ('phone_number', 'service_code')
    list_filter = ('service_code',)
    search_fields = ['service_name', 'service_code']


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'first_name', 'patronymic', 'birthdate',
        'health_status', 'phone_number', 'gender', 'image',
    )
    list_editable = ('gender',)
    list_filter = ('gender', 'requests__emergency_service')
    search_fields = ['first_name']
    readonly_fields = ('first_name', 'patronymic')
    empty_value_display = '-text-'


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'number', 'dc', 'injured',
        'do_not_call', 'status', 'get_service', 'applicant'
    )
    list_filter = ('applicant',)
    ordering = ('dc',)
    search_fields = ['first_name']

    def get_service(self, obj):
        return "\n".join([s.service_name for s in obj.emergency_service.all()])


admin.site.register(EmergencyService, EmergencyServiceAdmin)
