from django.db import models
import uuid


class EmergencyService(models.Model):
    """Экстренная служба."""
    service_name = models.CharField(
        max_length=255,
        verbose_name='Имя экстренной службы',
    )
    service_code = models.IntegerField(
        verbose_name='Код экстренной службы',
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Телефон экстренной службы',
    )

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ('-service_code',)

    def __str__(self):
        return self.service_name[:10]


class Applicant(models.Model):
    """Заявитель."""
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = (
        (MALE, "Мужчина"),
        (FEMALE, "Женщина"),
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя заявителя',
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия заявителя',
    )
    middle_name = models.CharField(
        max_length=255,
        verbose_name='Отчество заявителя',
    )
    birthdate = models.DateField(verbose_name='Дата рождения заявителя')
    health_status = models.TextField(
        max_length=255,
        verbose_name='Состояние здоровья',
        default='Практически здоров',
        help_text='аллергоанамез, хроническе, заболевания и т.п.',
        blank=True,
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Телефон заявителя',
        blank=True,
    )
    gender = models.CharField(
        max_length=255,
        choices=GENDER_CHOICES,
        verbose_name='Пол',
    )
    image = models.ImageField(
        verbose_name='Изображение заявителя',
        help_text='Добавьте изображения заявителя',
        upload_to='photos/applicants/%Y/%m/%d',
        blank=True,
    )
    request = models.ForeignKey(
        'Request',
        related_name='applicants',
        on_delete=models.CASCADE,
        verbose_name='Обращение',
    )

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('-first_name',)

    def __str__(self):
        return self.first_name


class Request(models.Model):
    """Обращение."""
    IN_WORK = 'Male'
    COMPLETED = 'Female'
    STATUS_CHOICES = (
        (IN_WORK, "В работе"),
        (COMPLETED, "Завершено"),
    )
    request_number = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name='Номер карточки',
    )
    request_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')
    injured = models.IntegerField(verbose_name='Количество пострадавших')      # ?
    do_not_call = models.CharField(max_length=255, verbose_name='Не звонить')  # ?
    # Импортируем модели явно, не используя *. from emergency_request import models; m = models.Model.objects.all()
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0],
        verbose_name='Статус',
    )
    emergency_service = models.ForeignKey(
        'EmergencyService',
        related_name='requests',
        on_delete=models.CASCADE,
        verbose_name='Экстренная служба',
    )

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('-request_number', '-request_date',)

    def __str__(self):
        return str(self.request_number)
