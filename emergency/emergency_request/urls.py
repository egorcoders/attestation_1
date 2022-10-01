from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'emergency_request'

router = DefaultRouter()

router.register('emergency_services', EmergencyServiceViewset, basename='emergency_services')
router.register('applicants', ApplicantViewset, basename='applicants')
router.register('requests', RequestViewset, basename='requests')

urlpatterns = [
    path('service/', EmergencyServiceView.as_view()),
    path('', index),
]

urlpatterns += router.urls
