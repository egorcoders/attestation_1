from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers


def index(request):
    return HttpResponse('Привет')


def main_page(request):
    return HttpResponse('Главная страница')


def ice_cream_number(request, pk: int):
    return HttpResponse(f'Главная страница, {pk}')


def ice_cream_slug(request, slug: str):
    return HttpResponse(f'Главная страница, {slug}')


@api_view(['GET'])
def applicant_list(request) -> Response:
    applicants = models.Applicant.objects.all().orer_by('-')
    serializer = serializers.ApplicantSerializer(applicants, many=True)
    return Response(serializer.data)
