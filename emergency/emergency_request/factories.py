import factory
from factory import fuzzy
from faker import Factory
import uuid

from . import models

factory_ru = Factory.create('ru_RU')


class Applicant(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    last_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    middle_name = factory.Sequence(lambda n: factory_ru.phone_number())
    birthdate = factory.Sequence(lambda n: factory_ru.date())
    health_status = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    phone_number = factory.Sequence(lambda n: factory_ru.phone_number())
    gender = fuzzy.FuzzyChoice(i for i in ['Мужчина', 'Женщина'])
    image = factory.Sequence(lambda n: factory_ru.image_url())

    class Meta:
        model = models.Applicant


class EmergencyService(factory.django.DjangoModelFactory):
    service_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
    service_code = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=50))
    phone_number = factory.Sequence(lambda n: factory_ru.phone_number())

    class Meta:
        model = models.EmergencyService


class Request(factory.django.DjangoModelFactory):
    request_number = factory.Sequence(lambda n: str(uuid.uuid4()))
    request_date = factory.Sequence(lambda n: factory_ru.date())
    injured = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=50))
    do_not_call = fuzzy.FuzzyChoice(i for i in ['Да', 'Нет'])
    status = fuzzy.FuzzyChoice(i for i in ['В работе', 'Завершено'])
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

#
# class Applicant(factory.django.DjangoModelFactory):
#     first_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
#     last_name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
#     middle_name = factory.Sequence(lambda n: factory_ru.phone_number())
#     birthdate = factory.Sequence(lambda n: factory_ru.date(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     health_status = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=10))
#     phone_number = factory.Sequence(lambda n: factory_ru.phone_number())
#     gender = factory.Sequence(lambda n: factory_ru.word())
#     image = factory.Sequence(lambda n: factory_ru.word())
#     request = factory.SubFactory(Request)
#
#     class Meta:
#         model = models.Applicant
#
#
# class UserProfile(factory.django.DjangoModelFactory):
#     user = factory.SubFactory(User)
#     first_name = factory.Sequence(lambda n: factory_ru.word())
#     last_name = factory.Sequence(lambda n: factory_ru.word())
#     patronymic = factory.Sequence(lambda n: factory_ru.word())
#     queue = factory.SubFactory('call_center.factories.Queue')
#     is_main = factory.Sequence(lambda n: factory_ru.boolean(chance_of_getting_true=50))
#     is_blocked = factory.Sequence(lambda n: factory_ru.boolean(chance_of_getting_true=50))
#     description = factory.Sequence(lambda n: factory_ru.text())
#
#     class Meta:
#         model = models.UserProfile
#
#     @factory.post_generation
#     def vpbx_group(self, create: bool, extracted: bool, **kwargs: dict) -> None:
#         if not create:
#             return
#         if extracted:
#             for vpbx in extracted:
#                 self.vpbx_group.add(vpbx)
#         else:
#             self.vpbx_group.add(VPBXGroup())
#
#
# class CallCenterGroup(factory.django.DjangoModelFactory):
#     name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=30))
#
#     class Meta:
#         model = models.CallCenterGroup
#
#     @factory.post_generation
#     def admins(self, create: bool, extracted: bool, **kwargs: dict) -> None:
#         if not create:
#             return
#         if extracted:
#             for admin in extracted:
#                 self.admins.add(admin)
#         else:
#             self.admins.add(User())
#
#
# class CallCenterSubGroup(factory.django.DjangoModelFactory):
#     name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=30))
#     group = factory.SubFactory(CallCenterGroup)
#
#     class Meta:
#         model = models.CallCenterSubGroup
#
#     @factory.post_generation
#     def admins(self, create: bool, extracted: bool, **kwargs: dict) -> None:
#         if not create:
#             return
#         if extracted:
#             for admin in extracted:
#                 self.admins.add(admin)
#         else:
#             self.admins.add(User())
#
#
# class VPBX(factory.django.DjangoModelFactory):
#     name = factory.Sequence(lambda n: factory_ru.text(max_nb_chars=30))
#     group = factory.SubFactory(CallCenterSubGroup)
#     domain = factory.Sequence(lambda n: (factory_ru.hostname(3)).replace('-', '_'))
#     description = factory.Sequence(lambda n: factory_ru.word())
#     sub_capacity_start = factory.Sequence(lambda n: factory_ru.random_int(min=1000, max=1999))
#     sub_capacity_end = factory.Sequence(lambda n: factory_ru.random_int(min=2000, max=2999))
#     group_capacity_start = factory.Sequence(lambda n: factory_ru.random_int(min=3000, max=3999))
#     group_capacity_end = factory.Sequence(lambda n: factory_ru.random_int(min=4000, max=4999))
#     conf_capacity_start = factory.Sequence(lambda n: factory_ru.random_int(min=5000, max=5999))
#     conf_capacity_end = factory.Sequence(lambda n: factory_ru.random_int(min=6000, max=6999))
#     is_enabled = factory.Sequence(lambda n: factory_ru.boolean(chance_of_getting_true=50))
#     need_callback_long_wait = factory.Sequence(lambda n: factory_ru.boolean(chance_of_getting_true=50))
#     need_callback_connection_break = factory.Sequence(lambda n: factory_ru.boolean(chance_of_getting_true=50))
#     sip_timeout = factory.Sequence(lambda n: factory_ru.random_digit_not_null())
#
#     class Meta:
#         model = models.VPBX
#
#     @factory.post_generation
#     def admins(self, create: bool, extracted: bool, **kwargs: dict) -> None:
#         if not create:
#             return
#         if extracted:
#             for admin in extracted:
#                 self.admins.add(admin)
#         else:
#             self.admins.add(User())
#
#
# class VPBXGroup(factory.django.DjangoModelFactory):
#     vpbx = factory.SubFactory(VPBX)
#     name = factory.Sequence(lambda n: factory_ru.word())
#     description = factory.Sequence(lambda n: factory_ru.text())
#     group_number = factory.Sequence(lambda n: factory_ru.random_digit_not_null())
#
#     class Meta:
#         model = models.VPBXGroup
#
#
# class VPBXCodec(factory.django.DjangoModelFactory):
#     vpbx = factory.SubFactory(VPBX)
#     codec = factory.SubFactory('configuration.factories.Codec')
#     priority = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=5))
#
#     class Meta:
#         model = models.VPBXGroup
#
#
# class SIPChanelEventLog(factory.django.DjangoModelFactory):
#     source_ip = factory.Sequence(lambda n: factory_ru.ipv4())
#     destination_ip = factory.Sequence(lambda n: factory_ru.ipv4())
#     source_port = factory.Sequence(lambda n: factory_ru.port_number())
#     destination_port = factory.Sequence(lambda n: factory_ru.port_number())
#     protocol = fuzzy.FuzzyChoice(i[1] for i in core.consts.PROTOCOL_CHOICES)
#     sdp = factory.Sequence(lambda n: factory_ru.text())
#
#
# class ContactBase(factory.django.DjangoModelFactory):
#     phone = factory.Sequence(lambda n: factory_ru.phone_number())
#     description = factory.Sequence(lambda n: factory_ru.text())
#     expiration_date = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     dc = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     dm = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     modified = factory.SubFactory(User)
#
#     class Meta:
#         model = models.ContactBase
#
#
# class ContactGroup(factory.django.DjangoModelFactory):
#     name = factory.Sequence(lambda n: factory_ru.word())
#     description = factory.Sequence(lambda n: factory_ru.text())
#     vpbx = factory.SubFactory('core.factories.VPBX')
#
#     class Meta:
#         model = models.ContactGroup
#
#
# class Contact(factory.django.DjangoModelFactory):
#     name = factory.Sequence(lambda n: factory_ru.word())
#     group = factory.SubFactory(ContactGroup)
#     modified = factory.SubFactory(User)
#
#     class Meta:
#         model = models.Contact
#
#
# class WhiteContact(factory.django.DjangoModelFactory):
#     vpbx = factory.SubFactory(VPBX)
#     phone = factory.Sequence(lambda n: factory_ru.phone_number())
#     description = factory.Sequence(lambda n: factory_ru.text())
#     expiration_date = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     dc = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     dm = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     modified = factory.SubFactory(User)
#
#     class Meta:
#         model = models.WhiteContact
#
#
# class BlackContact(factory.django.DjangoModelFactory):
#     vpbx = factory.SubFactory(VPBX)
#     phone = factory.Sequence(lambda n: factory_ru.phone_number())
#     description = factory.Sequence(lambda n: factory_ru.text())
#     expiration_date = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     dc = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     dm = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     modified = factory.SubFactory(User)
#
#     class Meta:
#         model = models.BlackContact
#
#
# class ChangeLog(factory.django.DjangoModelFactory):
#     action = fuzzy.FuzzyChoice(i[0] for i in core.consts.LOG_ACTIONS_CHOICES)
#     dc = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     user = factory.Sequence(lambda n: factory_ru.random_int(min=1, max=5))
#     model_name = factory.Sequence(lambda n: factory_ru.word())
#     model_name_rus = factory.Sequence(lambda n: factory_ru.word())
#     old_data = factory.Sequence(lambda n: factory_ru.json())
#     new_data = factory.Sequence(lambda n: factory_ru.json())
#
#     class Meta:
#         model = models.ChangeLog
#
#
# class Break(factory.django.DjangoModelFactory):
#     break_start = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#     break_end = factory.Sequence(lambda n: factory_ru.date_time(
#         tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)
#     ))
#
#     @factory.post_generation
#     def operators(self, create: bool, extracted: bool, **kwargs: dict) -> None:
#         if not create:
#             return
#         if extracted:
#             for operator in extracted:
#                 self.operators.add(operator)
#         else:
#             self.operators.add(User())
#
#     class Meta:
#         model = models.Break
