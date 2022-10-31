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
