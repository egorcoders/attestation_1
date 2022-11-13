from django.urls import path, include
from emergency_request.views import functions

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
    ])),
    path('views/', include([
        path('emergency_list/', functions.EmergencyServiceView.as_view(), name='emergency_list_view'),
        path('applicant_list/', functions.ApplicantView.as_view(), name='applicant_list_view'),
        path('request_list/', functions.RequestView.as_view(), name='request_list_view'),

        path('emergency_detail/<slug:slug>/', functions.EmergencyServiceViewDetail.as_view(), name='emergency_detail_view'),
        path('applicant_detail/<int:pk>/', functions.ApplicantViewDetail.as_view(), name='applicant_detail_view'),
        path('request_detail/<int:pk>/', functions.RequestViewDetail.as_view(), name='request_detail_view'),
    ])),
    path('views_1/', functions.views_1, name='views_1'),
    path('views_3/', functions.views_3, name='views_3'),
    path('views_4/', functions.views_4, name='views_4'),
    path('views_5/', functions.views_5, name='views_5'),
    path('views_6/<int:pk>/', functions.views_6, name='views_6'),

    path('emergency_create/', functions.emergency_create, name='emergency_create'),
    path('emergency_update/<slug:slug>/', functions.emergency_update, name='emergency_update'),

    path('applicant_create/', functions.applicant_create, name='applicant_create'),
    path('applicant_update/<int:pk>/', functions.applicant_update, name='applicant_update'),

    path('request_create/', functions.request_create, name='request_create'),
    path('request_update/<int:pk>/', functions.request_update, name='request_update'),

    # path('emergencies_v/', functions.EmergencyServiceView.as_view(), name='emergencies_v'),
    # path('emergency_v/<slug:slug>/', functions.EmergencyServiceViewDetail.as_view(), name='emergency_v'),
    # path('applicants_v/', functions.ApplicantView.as_view(), name='applicants_v'),
    # path('applicant_v/<int:pk>/', functions.ApplicantViewDetail.as_view(), name='applicant_v'),
    # path('requests_v/', functions.RequestView.as_view(), name='requests_v'),
    # path('request_v/<int:pk>/', functions.RequestViewDetail.as_view(), name='request_v'),
    # path('applicant/<int:pk>/update/', functions.ApplicantUpdate.as_view(), name='applicant_update'),
]

#
# urlpatterns = [
#
#     path('views_1/', functions.views_1, name='views_1'),
#     path('applicant_f/<int:applicant_id>/', functions.applicant_detail, name='applicant_detail'),
#     path('views_3/', functions.views_3, name='views_3'),
#     path('views_4/', functions.views_4, name='views_4'),
#     path('views_5/', functions.views_5, name='views_5'),
#     path('views_6/<int:applicant_id>/', functions.views_6, name='views_6'),
#     path('emergencies_v/', functions.EmergencyServiceView.as_view(), name='emergencies_v'),
#     path('emergency_v/<slug:slug>/', functions.EmergencyServiceViewDetail.as_view(), name='emergency_v'),
#     path('applicants_v/', functions.ApplicantView.as_view(), name='applicants_v'),
#     path('applicant_v/<int:pk>/', functions.ApplicantViewDetail.as_view(), name='applicant_v'),
#     path('requests_v/', functions.RequestView.as_view(), name='requests_v'),
#     path('request_v/<int:pk>/', functions.RequestViewDetail.as_view(), name='request_v'),
#     path('applicant/<int:pk>/update/', functions.ApplicantUpdate.as_view(), name='applicant_update'),
# ]
