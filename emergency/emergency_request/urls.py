from django.urls import path

from . import views

app_name = 'emergency_request'

urlpatterns = [
    path('', views.extra_3, name='extra_3',),
    path('model_1/<int:emergency_id>/', views.model_1, name='model_1'),
    path('models_1/', views.models_1, name='models_1'),
    path('model_2/<int:applicant_id>/', views.model_2, name='model_2'),
    path('models_2/', views.models_2, name='models_2'),
    path('model_3/<int:request_id>/', views.model_3, name='model_3'),
    path('models_3/', views.models_3, name='models_3'),
    path('views_1/', views.views_1, name='views_1'),
    path('views_2/<int:applicant_id>/', views.views_2, name='views_2'),
    path('views_3/', views.views_3, name='views_3'),
    path('views_4/', views.views_4, name='views_4'),
    path('views_5/', views.views_5, name='views_5'),
    path('views_6/<int:applicant_id>/', views.views_6, name='views_6'),
]
