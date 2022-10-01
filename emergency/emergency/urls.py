from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emergency_request.urls', namespace='emergency_request')),
]
