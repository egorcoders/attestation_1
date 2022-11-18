from django.urls import path, include
from emergency_request.views import functions, views

app_name = 'emergency_request'

urlpatterns = [
    path('', functions.index, name='index', ),
    path('functions/', include([
        path('emergency_list/', functions.emergency_list, name='emergency_list_function'),
        path('applicant_list/', functions.applicant_list, name='applicant_list_function'),
        path('request_list/', functions.request_list, name='request_list_function'),

        path('emergency_detail/<slug:slug>/', functions.emergency_detail, name='emergency_detail_function'),
        path('applicant_detail/<int:pk>/', functions.applicant_detail, name='applicant_detail_function'),
        path('request_detail/<int:pk>/', functions.request_detail, name='request_detail_function'),

        path('emergency_create/', functions.emergency_create, name='emergency_create_function'),
        path('emergency_update/<slug:slug>/', functions.emergency_update, name='emergency_update_function'),

        path('applicant_create/', functions.applicant_create, name='applicant_create_function'),
        path('applicant_update/<int:pk>/', functions.applicant_update, name='applicant_update_function'),

        path('request_create/', functions.request_create, name='request_create_function'),
        path('request_update/<int:pk>/', functions.request_update, name='request_update_function'),

        path('applicant_id/', functions.applicant_id, name='applicant_id_function'),
        path('applicant_phone/', functions.applicant_phone, name='applicant_phone_function'),

    ])),
    path('views/', include([
        path('emergency_list/', views.EmergencyServiceListView.as_view(), name='emergency_list_view'),
        path('applicant_list/', views.ApplicantListView.as_view(), name='applicant_list_view'),
        path('request_list/', views.RequestListView.as_view(), name='request_list_view'),

        path('emergency_detail/<slug:slug>/', views.EmergencyServiceDetailView.as_view(), name='emergency_detail_view'),
        path('applicant_detail/<int:pk>/', views.ApplicantDetailView.as_view(), name='applicant_detail_view'),
        path('request_detail/<int:pk>/', views.RequestDetailView.as_view(), name='request_detail_view'),

        path('emergency_create/', views.EmergencyServiceCreateView.as_view(), name='emergency_create_view'),
        path('applicant_create/', views.ApplicantCreateView.as_view(), name='applicant_create_view'),
        path('request_create/', views.RequestCreateView.as_view(), name='request_create_view'),

        path('emergency_update/<slug:slug>/', views.EmergencyServiceUpdateView.as_view(), name='emergency_update_view'),
        path('applicant_update/<int:pk>/', views.ApplicantUpdateView.as_view(), name='applicant_update_view'),
        path('request_update/<int:pk>/', views.RequestUpdateView.as_view(), name='request_update_view'),

        path('applicant_id/', views.ApplicantIdView.as_view(), name='applicant_id_view'),
        path('applicant_phone/', views.ApplicantPhoneView.as_view(), name='applicant_phone_view'),
    ])),

    path('views_1/', functions.views_1, name='views_1'),
    path('views_3/', functions.views_3, name='views_3'),
    path('views_4/', functions.views_4, name='views_4'),
    path('views_6/<int:pk>/', functions.views_6, name='views_6'),

]
