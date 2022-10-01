# from django.contrib import admin
# from .models import EmergencyService, Applicant, Request

#
# @admin.register(EmergencyService)
# class EmergencyServiceAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'service_name', 'service_code', 'phone_number')
#     list_editable = ('phone_number', 'service_code')
#
#
# @admin.register(Applicant)
# class ApplicantAdmin(admin.ModelAdmin):
#     list_display = (
#         'pk', 'first_name', 'last_name', 'middle_name',
#         'birthdate', 'health_status', 'phone_number', 'gender',
#         'image',
#     )
#     list_editable = ('phone_number', 'gender')
#
#
# @admin.register(Request)
# class RequestAdmin(admin.ModelAdmin):
#     list_display = (
#         'pk', 'request_number', 'request_date', 'applicant', 'injured',
#         'do_not_call', 'status', 'get_service'
#     )
#
#     def get_service(self, obj):
#         return "\n".join([s.service_name for s in obj.emergency_service.all()])
