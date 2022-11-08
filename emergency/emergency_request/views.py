from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import EmergencyService, Applicant, Request


def extra_3(request):
    """
    Создать представление, отображающее количество всех происшествий.
    Выводить 404, если их нет.
    """
    emergencies = EmergencyService.objects.all().order_by('id')
    context = {
        'emergencies': emergencies,
        'navbar': 'views_1'}
    return render(request, 'emergency_request/extra_3.html', context)


def model_1(request, emergency_id):
    """
    Вывод экземпляра класса экстренной службы
    """
    emergency = EmergencyService.objects.get(id=emergency_id)
    context = {
        'emergency': emergency,
        'navbar': 'models_1'}
    return render(request, 'emergency_request/model_1.html', context)


def model_2(request, applicant_id):
    """
    Вывод экземпляра класса заявителя
    """
    applicant = Applicant.objects.get(id=applicant_id)
    context = {
        'applicant': applicant,
        'navbar': 'models_2'}
    return render(request, 'emergency_request/model_2.html', context)


def model_3(request, request_id):
    """
    Вывод экземпляра класса экстренной обращения
    """
    single_request = Request.objects.get(id=request_id)
    context = {
        'single_request': single_request,
        'navbar': 'models_3'}
    return render(request, 'emergency_request/model_3.html', context)


def models_1(request):
    """
    Вывод экстренных служб
    """
    emergencies = EmergencyService.objects.all().order_by('id')
    context = {
        'emergencies': emergencies,
        'navbar': 'models_1'}
    return render(request, 'emergency_request/models_1.html', context)


def models_2(request):
    """
    Вывод заявителей
    """
    applicants = Applicant.objects.all().order_by('id')
    context = {
        'applicants': applicants,
        'navbar': 'models_2'}
    return render(request, 'emergency_request/models_2.html', context)


def models_3(request):
    """
    Вывод обращений
    """
    requests = Request.objects.all().order_by('id')
    context = {
        'requests': requests,
        'navbar': 'models_3'}
    return render(request, 'emergency_request/models_3.html', context)


def views_1(request):
    """
    Создать представление, отображающее количество всех происшествий.
    Выводить 404, если их нет.
    """
    emergencies = EmergencyService.objects.all().order_by('id')
    context = {
        'emergencies': emergencies,
        'navbar': 'views_1'}
    return render(request, 'emergency_request/views_1.html', context)


def views_2(request, applicant_id):
    """
    Создать представление, отображающее номер телефона заявителя с определенным id,
    указанным в качестве параметра к запросу. Вернуть 404 если такого заявителя не существует.
    """
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    context = {
        'applicant': applicant,
        'navbar': 'views_2'}
    return render(request, 'emergency_request/views_2.html', context)


def views_3(request):
    """
    Создать представление, которое перенаправляет пользователя на другую страницу.
    """
    return redirect('https://www.djangoproject.com')


def views_4(request):
    """
    Создать представление, которое отображает данные входящего запроса (HttpRequest Attributes)
    """
    attributes = request.headers
    context = {
        'attributes': attributes,
        'navbar': 'views_4'}
    return render(request, 'emergency_request/views_4.html', context)


def views_5(request):
    """
    Создать представление, которое отображает данные заявителя.
    Номер телефона которого передается в параметрах запроса. (querydict)
    """
    attributes = request.headers
    context = {'attributes': attributes}
    return render(request, 'emergency_request/views_5.html', context)


def views_6(request, applicant_id):
    """
    Создать представление, отдающее данные заявителя в json-формате. (json response)
    """
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    context = {
        'navbar': 'views_6',
        'json': JsonResponse(model_to_dict(applicant), json_dumps_params={'ensure_ascii': False}).content
    }
    return render(request, 'emergency_request/views_6.html', context)
