from django.contrib import admin
from emergency_request.models import EmergencyService, Applicant, Request


class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'service_name', 'service_code', 'phone_number')
    list_editable = ('phone_number', 'service_code')
    # list_display_links = ('text', 'author')
    # list_filter = ('pub_date', 'group')
    # empty_value_display = '-пусто-'
    # search_fields = ('text',)


class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'first_name', 'last_name', 'middle_name',
        'birthdate', 'health_status', 'phone_number', 'gender',
        'image', 'request',
    )
    list_editable = ('phone_number',)


class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'request_number', 'request_date', 'injured',
        'do_not_call', 'status', 'emergency_service',
    )


admin.site.register(EmergencyService, EmergencyServiceAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Request, RequestAdmin)