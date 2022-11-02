from django.urls import path

from . import views

app_name = 'emergency_request'

urlpatterns = [
    path('views_1/', views.views_1, name='views_1'),
    path('views_2/<int:applicant_id>/', views.views_2, name='views_2'),
    path('views_3/', views.views_3, name='views_3'),
    path('views_4/', views.views_4, name='views_4'),
    path('views_5/', views.views_5, name='views_5'),
    path('views_6/', views.views_6, name='views_6'),
]

