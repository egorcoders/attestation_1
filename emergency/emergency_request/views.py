from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from emergency_request import models
from emergency_request.consts import color_choices


def extra_3(request):
    """
    Создать представление, отображающее количество всех происшествий.
    Выводить 404, если их нет.
    """
    emergencies = models.EmergencyService.objects.all().order_by('id')
    context = {
        'emergencies': emergencies,
    }
    return render(request, 'emergency_request/extra_3.html', context)


def emergency_f(request, slug):
    """
    Вывод экземпляра класса экстренной службы
    """
    emergency = models.EmergencyService.objects.get(slug=slug)
    context = {
        'emergency': emergency,
    }
    return render(request, 'emergency_request/emergency.html', context)


def applicant_f(request, applicant_id):
    """
    Вывод экземпляра класса заявителя
    """
    applicant = models.Applicant.objects.get(id=applicant_id)
    context = {
        'applicant': applicant,
    }
    return render(request, 'emergency_request/applicant.html', context)


def request_f(request, request_id):
    """
    Вывод экземпляра класса экстренной обращения
    """
    single_request = models.Request.objects.get(id=request_id)
    context = {
        'single_request': single_request,
    }
    return render(request, 'emergency_request/request.html', context)


def emergencies_f(request):
    """
    Вывод экстренных служб
    """
    emergencies = models.EmergencyService.objects.all().order_by('id')
    context = {
        'color_choices': color_choices,
        'emergencies': emergencies,
    }
    return render(request, 'emergency_request/emergencies.html', context)


def applicants_f(request):
    """
    Вывод заявителей
    """
    applicants = models.Applicant.objects.all().order_by('id')
    context = {
        'color_choices': color_choices,
        'applicants': applicants,
    }
    return render(request, 'emergency_request/applicants.html', context)


def requests_f(request):
    """
    Вывод обращений
    """
    requests = models.Request.objects.all().order_by('id')
    context = {
        'color_choices': color_choices,
        'requests': requests,
    }
    return render(request, 'emergency_request/requests.html', context)


def views_1(request):
    """
    Создать представление, отображающее количество всех происшествий.
    Выводить 404, если их нет.
    """
    emergencies = models.EmergencyService.objects.all().order_by('id')
    context = {
        'emergencies': emergencies,
    }
    return render(request, 'emergency_request/views_1.html', context)


def views_2(request, applicant_id):
    """
    Создать представление, отображающее номер телефона заявителя с определенным id,
    указанным в качестве параметра к запросу. Вернуть 404 если такого заявителя не существует.
    """
    applicant = get_object_or_404(models.Applicant, pk=applicant_id)
    context = {
        'applicant': applicant,
    }
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
    }
    return render(request, 'emergency_request/views_4.html', context)


def views_5(request):
    """
    Создать представление, которое отображает данные заявителя.
    Номер телефона которого передается в параметрах запроса. (querydict)
    """
    phone_number = request.GET["phone_number"]
    applicant = get_object_or_404(models.Applicant, phone_number__icontains=phone_number)
    context = {'applicant': applicant}
    return render(request, 'emergency_request/views_5.html', context)


def views_6(request, applicant_id):
    """
    Создать представление, отдающее данные заявителя в json-формате. (json response)
    """
    applicant = get_object_or_404(models.Applicant, pk=applicant_id)
    context = {
        'json': JsonResponse(model_to_dict(applicant), json_dumps_params={'ensure_ascii': False}).content
    }
    return render(request, 'emergency_request/views_6.html', context)


class EmergencyServiceView(ListView):
    model = models.EmergencyService
    template_name = 'emergency_request/emergencies_v.html'
    context_object_name = 'emergencies'


class ApplicantView(ListView):
    model = models.Applicant
    template_name = 'emergency_request/applicants_v.html'
    context_object_name = 'applicants'


class RequestView(ListView):
    model = models.Request
    template_name = 'emergency_request/requests_v.html'
    context_object_name = 'requests'


class EmergencyServiceViewDetail(DetailView):
    model = models.EmergencyService
    template_name = 'emergency_request/emergency.html'
    context_object_name = 'emergency'


class ApplicantViewDetail(DetailView):
    model = models.Applicant
    template_name = 'emergency_request/applicant.html'
    context_object_name = 'applicant'


class RequestViewDetail(DetailView):
    model = models.Request
    template_name = 'emergency_request/request.html'
    context_object_name = 'single_request'
