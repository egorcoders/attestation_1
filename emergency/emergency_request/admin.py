from django.contrib import admin
from .models import EmergencyService, Applicant, Request
from typing import Union


class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'service_name', 'service_code', 'phone_number', 'slug')
    list_editable = ('phone_number', 'service_code')
    list_filter = ('service_code',)
    search_fields = ['service_name', 'service_code']
    search_help_text = 'Поиск по имени и коду'
    empty_value_display = '-empty-'
    prepopulated_fields = {"slug": ("service_name",)}


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'first_name', 'patronymic', 'birthdate',
        'health_status', 'phone_number', 'gender', 'get_request'
    )
    list_editable = ('gender',)
    list_filter = ('gender', 'requests__emergency_service')
    search_fields = ['first_name']
    search_help_text = 'Поиск по имени'
    readonly_fields = ('first_name', 'patronymic')
    empty_value_display = '-text-'

    def get_request(self, obj):
        return "\n".join([s.text for s in obj.requests.all()])

    def get_inlines(self, request: Request, obj: None) -> Union[tuple, str]:
        inlines = (
            ApplicantRequest,
        )
        return inlines


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'number', 'dc', 'injured',
        'do_not_call', 'status', 'get_service', 'applicant'
    )
    list_filter = ('applicant',)
    ordering = ('dc',)
    search_fields = ['first_name']
    search_help_text = 'Поиск по имени'
    readonly_fields = ('dc',)
    empty_value_display = '-empty-'

    def get_service(self, obj):
        return "\n".join([s.service_name for s in obj.emergency_service.all()])


admin.site.register(EmergencyService, EmergencyServiceAdmin)


class ApplicantRequest(admin.TabularInline):
    model = Request
    extra = 0
