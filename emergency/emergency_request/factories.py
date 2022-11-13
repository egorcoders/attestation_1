import factory
from factory import fuzzy
from faker import Factory
import uuid
from . import consts
from django.conf import settings
import zoneinfo

from . import models

factory_ru = Factory.create('ru_RU')


class EmergencyService(factory.django.DjangoModelFactory):
    service_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    service_code = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=50))
    phone_number = factory.Sequence(lambda n: factory_ru.phone_number())
    slug = factory.LazyAttribute(lambda o: '%s' % o.service_name.lower().replace(' ', '_'))

    class Meta:
        model = models.EmergencyService


class Applicant(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    last_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    patronymic = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    birthdate = factory.Sequence(lambda n: factory_ru.date())
    health_status = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    phone_number = factory.Sequence(lambda n: factory_ru.phone_number())
    gender = fuzzy.FuzzyChoice(i[0] for i in consts.GENDER_CHOICES)
    image = factory.Sequence(lambda n: factory_ru.image_url())

    class Meta:
        model = models.Applicant


class Request(factory.django.DjangoModelFactory):
    text = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=25))
    number = factory.Sequence(lambda n: str(uuid.uuid4()))
    dc = factory.Sequence(lambda n: factory_ru.date_time(
        tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)))
    injured = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=50))
    do_not_call = factory.Sequence(lambda n: factory_ru.boolean(chance_of_getting_true=50))
    status = fuzzy.FuzzyChoice(i[0] for i in consts.STATUS_CHOICES)
    applicant = factory.SubFactory(Applicant)

    class Meta:
        model = models.Request

    @factory.post_generation
    def emergency_service(self, create: bool, extracted: bool, **kwargs: dict) -> None:
        if not create:
            return
        if extracted:
            for service in extracted:
                self.emergency_service.add(service)
        else:
            self.emergency_service.add(EmergencyService())
