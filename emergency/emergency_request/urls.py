from django.urls import path

from emergency_request import views, models

app_name = 'emergency_request'

urlpatterns = [
    path('', views.extra_3, name='extra_3',),
    path('emergency_f/<slug:slug>/', views.emergency_f, name='emergency_f'),
    path('emergencies_f/', views.emergencies_f, name='emergencies_f'),
    path('applicant_f/<int:applicant_id>/', views.applicant_f, name='applicant_f'),
    path('applicants_f/', views.applicants_f, name='applicants_f'),
    path('request_f/<int:request_id>/', views.request_f, name='request_f'),
    path('requests_f/', views.requests_f, name='requests_f'),
    path('views_1/', views.views_1, name='views_1'),
    path('applicant_f/<int:applicant_id>/', views.applicant_f, name='applicant_f'),
    path('views_3/', views.views_3, name='views_3'),
    path('views_4/', views.views_4, name='views_4'),
    path('views_5/', views.views_5, name='views_5'),
    path('views_6/<int:applicant_id>/', views.views_6, name='views_6'),
    path('emergencies_v/', views.EmergencyServiceView.as_view(), name='emergencies_v'),
    path('emergency_v/<slug:slug>/', views.EmergencyServiceViewDetail.as_view(), name='emergency_v'),
    path('applicants_v/', views.ApplicantView.as_view(), name='applicants_v'),
    path('applicant_v/<int:pk>/', views.ApplicantViewDetail.as_view(), name='applicant_v'),
    path('requests_v/', views.RequestView.as_view(), name='requests_v'),
    path('request_v/<int:pk>/', views.RequestViewDetail.as_view(), name='request_v'),
]
