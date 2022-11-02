from django.urls import path

from . import views

app_name = 'emergency_request'

urlpatterns = [
    path('views_1/', views.views_1, name='views_1'),
    path('views_2/<int:applicant_id>/', views.views_2, name='views_2'),
]
