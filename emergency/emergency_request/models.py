from django.db import models
import uuid
from . import consts



class EmergencyService(models.Model):
    """Экстренные службы."""
    service_name = models.CharField('Имя экстренной службы', max_length=255)
    service_code = models.CharField('Код экстренной службы', max_length=255)
    phone_number = models.CharField('Телефон экстренной службы', max_length=255)

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ('service_code',)

    def __str__(self):
        return self.service_name


class Applicant(models.Model):
    """Заявитель."""
    first_name = models.CharField('Имя заявителя', max_length=255)
    last_name = models.CharField('Фамилия заявителя', max_length=255)
    patronymic = models.CharField('Отчество заявителя', max_length=255)
    birthdate = models.DateField('Дата рождения заявителя')
    health_status = models.TextField(
        'Состояние здоровья',
        max_length=255,
        default='Практически здоров',
        help_text='Аллергоанамез, хроническе, заболевания и т.п.',
        blank=True,
    )
    phone_number = models.CharField('Телефон заявителя', max_length=255, blank=True)
    gender = models.CharField(
        'Пол',
        max_length=255,
        choices=consts.GENDER_CHOICES,
        default=consts.MALE,
    )
    image = models.ImageField(
        'Изображение заявителя',
        help_text='Добавьте изображения заявителя',
        upload_to='photos/applicants/%Y/%m/%d',
        blank=True,
    )

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('first_name', 'last_name', 'patronymic')

    def __str__(self):
        return self.first_name


class Request(models.Model):
    """Обращение."""
    text = models.TextField(
        'Описание',
        help_text='Текст описания вашего обращения',
        blank=True
    )
    number = models.UUIDField(
        'Номер карточки',
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )
    dc = models.DateTimeField('Дата создания', auto_now_add=True)
    injured = models.PositiveIntegerField(
        'Количество пострадавших',
    )
    do_not_call = models.BooleanField('Не звонить', default=False)
    status = models.CharField(
        'Статус',
        max_length=255,
        choices=consts.STATUS_CHOICES,
        default=consts.IN_WORK,
    )
    emergency_service = models.ManyToManyField(
        'EmergencyService',
        related_name='requests',
        verbose_name='Экстренная служба',
    )
    applicant = models.ForeignKey(
        'Applicant',
        related_name='requests',
        on_delete=models.CASCADE,
        verbose_name='Заявитель',
    )

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('dc',)

    # def __str__(self):
    #     return f'{self.pk} {self.applicant}'
