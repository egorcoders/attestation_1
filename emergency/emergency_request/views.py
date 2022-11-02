from django.shortcuts import get_object_or_404, render

from . models import EmergencyService, Applicant


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
