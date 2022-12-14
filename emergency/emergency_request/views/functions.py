from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from emergency_request.consts import color_choices
from emergency_request.forms import EmergencyServiceForm, ApplicantForm, RequestForm
from emergency_request.models import EmergencyService, Applicant, Request


def index(request):
    """Главная страница."""
    emergencies = EmergencyService.objects.all().order_by('id')
    return render(request, 'emergency_request/index.html', {'emergencies': emergencies})


def emergency_detail(request, slug: str):
    """Вывод экземпляра класса экстренной службы."""
    emergency = get_object_or_404(EmergencyService, slug=slug)
    return render(request, 'emergency_request/emergency_function.html', {'emergency': emergency})


def applicant_detail(request, pk: int):
    """Вывод экземпляра класса заявителя."""
    applicant = get_object_or_404(Applicant, pk=pk)
    return render(request, 'emergency_request/applicant_function.html', {'applicant': applicant})


def request_detail(request, pk):
    """Вывод экземпляра класса экстренного обращения."""
    single_request = get_object_or_404(Request, pk=pk)
    return render(request, 'emergency_request/request_function.html', {'single_request': single_request})


def emergency_list(request):
    """Вывод всех экстренных служб."""
    emergencies = EmergencyService.objects.all().order_by('id')
    context = {
        'color_choices': color_choices,
        'emergencies': emergencies,
    }
    return render(request, 'emergency_request/emergency_list_function.html', context)


def applicant_list(request):
    """Вывод заявителей."""
    applicants = Applicant.objects.all().order_by('id')
    context = {
        'color_choices': color_choices,
        'applicants': applicants,
    }
    return render(request, 'emergency_request/applicant_list_function.html', context)


def request_list(request):
    """Вывод обращений."""
    requests = Request.objects.all().order_by('id')
    context = {
        'color_choices': color_choices,
        'requests': requests,
    }
    # отдавать 404 если их нет
    return render(request, 'emergency_request/request_list_function.html', context)


def views_1(request):
    """
    Создать представление, отображающее количество всех происшествий.
    Выводить 404, если их нет.
    """
    emergencies = EmergencyService.objects.all().order_by('id')
    context = {
        'emergencies': emergencies,
    }
    return render(request, 'emergency_request/views_1.html', context)


def applicant_id(request):
    """
    Создать представление, отображающее номер телефона заявителя с определенным id,
    указанным в качестве параметра к запросу. Вернуть 404 если такого заявителя не существует.
    """
    applicant_id = request.GET["id"]
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'emergency_request/applicant_function.html', {'applicant': applicant})


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
    return render(request, 'emergency_request/views_4.html', {'attributes': attributes})


def applicant_phone(request):
    """
    Создать представление, которое отображает данные заявителя.
    Номер телефона которого передается в параметрах запроса. (query dict)
    """
    phone_number = request.GET["phone_number"]
    applicant = get_object_or_404(Applicant, phone_number__icontains=phone_number)
    return render(request, 'emergency_request/applicant_function.html', {'applicant': applicant})


def views_6(request, pk):
    """
    Создать представление, отдающее данные заявителя в json-формате. (json response)
    """
    applicant = Applicant.objects.filter(pk=pk).values().first()
    return render(request, 'emergency_request/views_6.html', {'json': JsonResponse({'result': applicant}).content})


def emergency_create(request):
    form = EmergencyServiceForm()
    if request.method == 'POST':
        form = EmergencyServiceForm(request.POST)
        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.save()
            return redirect('emergency_request:emergency_detail_function', slug=emergency.slug)
    elif request.method == 'GET':
        form = EmergencyServiceForm()
    return render(request, 'emergency_request/form.html', {'form': form})


def applicant_create(request):
    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return redirect('emergency_request:applicant_detail_function', pk=applicant.pk)
    elif request.method == 'GET':
        return render(request, 'emergency_request/form.html', {'form': form})


def request_create(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            single_request = form.save(commit=False)
            single_request.save()
            return redirect('emergency_request:request_detail_function', pk=single_request.pk)
    elif request.method == 'GET':
        form = RequestForm()
    return render(request, 'emergency_request/form.html', {'form': form})


def emergency_update(request, slug):
    emergency = get_object_or_404(EmergencyService, slug=slug)
    if request.method == 'POST':
        form = EmergencyServiceForm(request.POST, instance=emergency)
        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.save()
            return redirect('emergency_request:emergency_detail_function', slug=emergency.slug)
    elif request.method == 'GET':
        form = EmergencyServiceForm(instance=emergency)
    return render(request, 'emergency_request/form.html', {'form': form})


def applicant_update(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return redirect('emergency_request:applicant_detail_function', pk=applicant.pk)
    elif request.method == 'GET':
        form = ApplicantForm(instance=applicant)
    return render(request, 'emergency_request/form.html', {'form': form})


def request_update(request, pk):
    single_request = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=single_request)
        if form.is_valid():
            single_request = form.save(commit=False)
            single_request.save()
            return redirect('emergency_request:request_detail_function', pk=single_request.pk)
    elif request.method == 'GET':
        form = RequestForm(instance=single_request)
    return render(request, 'emergency_request/form.html', {'form': form})
