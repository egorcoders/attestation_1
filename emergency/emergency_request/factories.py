import factory
from django.contrib.auth import models


class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = 'John'
    last_name = 'Doe'


class FakeUserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class AdminFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = 'Admin'
    last_name = 'User'
