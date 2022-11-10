import random

# Статусы обращений
IN_WORK = 'В работе'
COMPLETED = 'Завершено'

STATUS_CHOICES = (
    (IN_WORK, IN_WORK),
    (COMPLETED, COMPLETED)
)

# Пол заявителя
MALE = 'Мужчина'
FEMALE = 'Женщина'

GENDER_CHOICES = (
    (MALE, MALE),
    (FEMALE, FEMALE)
)

COLOR_CHOICES = (
    "table-active",
    "table-default",
    "table-primary",
    "table-secondary",
    "table-success",
    "table-danger",
    "table-warning",
    "table-info",
    "table-light",
    "table-dark",
)

color_choices = random.choice(COLOR_CHOICES)
