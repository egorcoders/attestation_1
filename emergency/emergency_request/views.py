from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from pprint import pprint
from rest_framework import viewsets

from .serializers import *
from .models import *


def index(request):
    return HttpResponse('hi')


class EmergencyServiceView(APIView):
    def get(self, request):
        services = EmergencyService.objects.all()
        serializers = EmergencyServiceSerializer(services)
        return Response(serializers.data)

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'


# @api_view(http_method_names=['GET', 'POST'])
# @permission_classes([AllowAny])
# def hello_world(request):
#     if request.method == 'GET':
#         pprint(request.query_params)
#         n = request.query_params['pk']
#         n_new = int(n) * 3
#         return Response({'text': n_new})
#     return Response({'text': 'hello_world', 'data': request.data})


class EmergencyServiceViewset(viewsets.ModelViewSet):
    serializer_class = EmergencyServiceSerializer

    def get_queryset(self):
        services = EmergencyService.objects.all()
        return services

    def retrieve(self, request, *args, **kwargs):
        services = EmergencyService.objects.filter(phone_number__icontains=kwargs['pk'])
        serializer = EmergencyServiceSerializer(services, many=True)
        return Response(serializer.data)


class ApplicantViewset(viewsets.ModelViewSet):
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        applicants = Applicant.objects.all()
        return applicants



class RequestViewset(viewsets.ModelViewSet):
    serializer_class = RequestSerializer

    def get_queryset(self):
        requests = Request.objects.all()
        return requests

