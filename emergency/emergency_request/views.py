from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import EmergencyService, Applicant


def views_1(request):
    """
    Создать представление, отображающее количество всех происшествий.
    Выводить 404, если их нет.
    """
    emergencies = EmergencyService.objects.all()
    context = {'emergencies': emergencies}
    return render(request, 'emergency_request/views_1.html', context)


def views_2(request, applicant_id):
    """
    Создать представление, отображающее номер телефона заявителя с определенным id,
    указанным в качестве параметра к запросу. Вернуть 404 если такого заявителя не существует.
    """
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'emergency_request/views_2.html', {'applicant': applicant})


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
    context = {'attributes': attributes}
    return render(request, 'emergency_request/views_4.html', context)


def views_5(request):
    """
    Создать представление, которое отображает данные заявителя.
    Номер телефона которого передается в параметрах запроса. (querydict)
    """
    attributes = request.headers
    context = {'attributes': attributes}
    return render(request, 'emergency_request/views_5.html', context)


def views_6(request):
    """
    Создать представление, отдающее данные заявителя в json-формате. (JsonResponse).
    """
    return JsonResponse({'text': 'Just rendering some JSON :)'})
