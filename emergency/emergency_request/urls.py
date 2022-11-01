from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'emergency_request'

router = DefaultRouter()

# router.register('emergency_services', EmergencyServiceViewset, basename='emergency_services')
# router.register('applicants', ApplicantViewset, basename='applicants')
# router.register('requests', RequestViewset, basename='requests')

urlpatterns = [
    path('', views.index),
    path('main_page/', views.main_page),
    path('ice_cream_number/<int:pk>/', views.ice_cream_number),
    path('ice_cream_slug/<str:slug>/', views.ice_cream_slug),
    path('applicant_list/', views.applicant_list),
]

urlpatterns += router.urls
