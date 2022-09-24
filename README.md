# 1.1. Django Модели

## Определение моделей


## Установка

1. Клонировать репозиторий:

   ```python
   git clone https://github.com/egorcoders/hw04_tests.git
   ```

2. Перейти в папку с проектом:

   ```python
   cd hw04_tests/
   ```

3. Установить виртуальное окружение для проекта:

   ```python
    -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```python
   # для OS Lunix и MacOS
   source venv/bin/activate

   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```python
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```python
   cd attestation
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

7. Запустить проект локально:

   ```python
   python3 manage.py runserver

   # адрес запущенного проекта
   http://127.0.0.1:8000
   ```

8. Зарегистирировать суперпользователя Django:

   ```python
   python3 manage.py createsuperuser

   # адрес панели администратора
   http://127.0.0.1:8000/admin
   ```


## Настройка проекта

Для создания проекта:

   ```python
   django-admin startproject emergency
   ```

Для создания приложения:

   ```python
   python3 manage.py startapp emergency_request
   ```

## Создание моделей

В модуле models.py опишите модели:

1. Модель экстренной службы:

   ```python
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

   ```

2. Модель заявителя:

   ```python
   class Applicant(models.Model):
    """Заявитель. """
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

   ```

3. Модель обращения:

   ```python
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
    injured = models.IntegerField(verbose_name='Количество пострадавших')  # ?
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

   ```

## 1.2 Поля моделей

1. Для модели заявитель "поле состояние здоровья" сделайте необязательным для заполнения
   ```python
   blank=True
   ```

2. Для модели заявитель сделайте поле "Номер телефона" необязательным для заполнения
   ```python
   blank=True
   ```

3. Заявителю добавьте поле "пол" с двумя вариантами значений
   ```python
   # создаем константу GENDER_CHOICES
   GENDER_CHOICES = (
       (MALE, "Мужчина"),
       (FEMALE, "Женщина"),
   )
   
   # прописываем в модели атрибут
   choices=GENDER_CHOICES
   ```

4. Сделайте поле "номер" для карточки происшествия индексируемым на уровне базы данных
   ```python
   db_index=True
   ```

5. Сделайте для поля "состояние здоровья" модели Заявителя значение по умолчанию "практически здоров"
   ```python
   default='Практически здоров'
   ```

6. Сделайте поле "номер карточки" модели "Обращение" не редактируемым
   ```python
   editable=False,
   ```

7. Сделайте поле "номер карточки" модели "Обращение" уникальным
   ```python
   unique=True
   ```

8. Добавьте для поля "состояние здоровья" примечание на уровне модели со следующим содержанием "аллергоанамнез,
хронические заболевания и т.п."
   ```python
   help_text='аллергоанамез, хроническе, заболевания и т.п.',
   ```

9. Добавьте поле "Изображение" в модель Заявителя
   ```python
   image = models.ImageField(
       verbose_name='Изображение заявителя',
       help_text='Добавьте изображения заявителя',
       upload_to='photos/applicants/%Y/%m/%d',
       blank=True,
   )
   ```

10. Сделайте поле "Дата" в модели обращения автоматически добавляемым при создании
    ```python
    auto_now_add=True
    ```

11. Добавьте поле "Статус" в модель "Обращение" с вариантами "В работе" (по умолчанию) и "Завершено".
    ```python
    # создаем константу STATUS_CHOICES
    STATUS_CHOICES = (
        (IN_WORK, "В работе"),
        (COMPLETED, "Завершено"),
    )

    # прописываем в модели статус
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0],
        verbose_name='Статус',
    )
    ```

12. Добавьте поле "Количество пострадавших" в модель происшествие
    ```python
    injured = models.IntegerField(verbose_name='Количество пострадавших')
    ```
   
13. Добавьте поле "Не звонить" в модель происшествие
    ```python
    do_not_call = models.CharField(max_length=255, verbose_name='Не звонить')
    ```

## Миграции

   ```python
   cd attestation
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

## 1.3 QuerySet

### Сохранение объектов в БД

1. Сохраните несколько объектов модели "Экстренных служб", "Заявителя" и "Обращения" двумя способами (методом сrеаtе
уровня менеджера запросов ***objects*** и методом ***savе*** уровня экземпляра модели)
   ```python
   # сохранение объекта модели экстренных служб методом save
   e = models.EmergencyService(5, 'Охрана среды', 898, '+73482900405')
   e.save()
   # сохранение объекта модели экстренных служб методом create
   models.EmergencyService.objects.create(service_name='Navy', service_code=25, phone_number='+922829')

   # сохранение объекта модели обращения методом save
   r = models.Request(5, 'eef066b7-de68-422e-a061-44c09ab60f04', '1988-10-22', 2, 'Да', 'Female')
   r.save()
   # сохранение объекта модели обращения методом create
   models.Request.objects.create(request_number='eef066b7-de68-422e-a061-44c09ab60f04', request_date='1988-10-22', injured=True, do_not_call='Ok', status=1, emergency_service_id=3)
 
   # сохранение объекта модели заявителя методом save
   a = models.Applicant(5, 'Jack', 'Long', 'Milkovich', '1988-05-13', 'Healthy', '+2982928282', 'Мужчина', '/', 2)
   e.save()
   # сохранение объекта модели заявителя методом create
   models.Applicant.objects.create(first_name='Daniel', last_name='Longi', middle_name='Milkovich', birthdate='1988-05-13', health_status='Healthy', phone_number='+2982928282', gender='Мужчина', image='/',  request_id=5)
   ```
2. Создайте "Обращение" через менеджер запросов от объекта "Заявитель"
   ```python
   a = models.Applicant.objects.get(pk=1)
   r = models.Request.objects.get(pk=1)
   a.request = r
   r.save()
   ```
3. Добавьте "Обращению" несколько "экстренных служб" двумя способами (add, set)
   ```python
   s1 = models.EmergencyService.objects.get(pk=1)
   s3 = models.EmergencyService.objects.get(pk=2)
   r = models.Request.objects.get(pk=1)
   r.emergency_service.add(s1, s2)

   ```

### Запрос в БД

1. Получить объект заявителя с идентификатором в базе данных = 1 тремя способами.
   ```python
   # 1
   models.Applicant.objects.get(id=1)
   # 2
   models.Applicant.objects.get(pk=1)
   # 3
   models.Applicant.objects.filter(pk=1).first()
   ```
   
2. Получить все обращения заявителя двумя способами
   ```python
   # 1
   models.Request.objects.all()
   # 2
   models.Request.objects.values_list()
   # 3
   models.Request.objects.values()
   ```
   
3. Получить первые три экстренные службы
   ```python
   models.EmergencyService.objects.order_by('pk')[:3]
   ```
   
4. Получить последние пять заявителей
   ```python
   models.Applicant.objects.order_by('-pk')[:5]
   ```

5. Получить самое старое и самое новое обращение двумя способами (latest, earlest, order_by)
   ```python
   models.Request.objects.earliest('request_date')
   models.Request.objects.latest('request_date')
   models.Request.objects.order_by('request_date').first()
   models.Request.objects.order_by('request_date').last()
   ```

6. Получить каждое второе обращение
   ```python
   models.Request.objects.all()[::2]
   ```

7. Если дважды проитерироваться по полученному ОuеrуSеt, то сколько будет сделано обращений в БД? С помощью конструкции len(connection.) можно проверить количество запросов в БД. Для сброса следует использовать reset_queries() из django.db.

8. Вывести общее число обращений
   ```python
   models.Request.objects.count()
   ```

9. Получить случайное обращение
   ```python
   models.Request.objects.order_by('?').first()
   ```

## Фильтрация

1. Получить обращение с заявителем, идентификатор которого равен 1
   ```python
   models.Applicant.objects.get(id=1).request.request_number
   ```
2. Получить всех заявителей определенного пола и без обращений
   ```python
   models.Applicant.objects.filter(gender='Female', request__isnull=True)
   ```
3. Отсортировать всех заявителей по идентификатору.
   ```python
   models.Applicant.objects.order_by('pk')
   ```
4. Получить всех несовершеннолетних заявителей
5. Получить всех совершеннолетних заявителей
6. Узнать есть ли вообще какие-нибудь заявители
   ```python
   models.Applicant.objects.exists()
   ```
7. Узнать, есть ли какие-нибудь заявители с похожими именами (пример: Алексей, Александра)
8. Получить все обращения, кроме тех, у которых не назначены службы
   ```python
   models.Applicant.objects.exists()
   ```
9. Среди обращений со службой с кодом "ОЗ" вывести дату самого первого обращения
10. Получить все обращения, которые созданы до определенной даты
11. Получить всех заявителей без изображения и/или без номера телефона
12. Получить всех заявителей, с определенным кодом оператора (917)
13. Получить результат объединения, пересечения и разницы предыдущих двух запросов.
14. Вывести все обращения, созданные в определенный период
15. Получить количество заявителей без номера телефона
16. Выведите все уникальные записи модели заявитель
17. Получить все обращения, в описании которых есть какое то ключевое слово в любом регистре.
18. Выбрать всех заявителей, при этом получить только значения поля "номер телефона"
19. Выбрать всех заявителей, при этом получить все поля, кроме состояния здоровья
20. Вывести все службы используя за! запрос
21. Выберите или создайте заявителя с номером "12341234"
22. Измените номер заявителя с номером "12341234" на любой другой, если заявителя, то запрос должен его создать.
23. Создайте сразу несколько заявителей.
24. Измените несколько заявителей. Для поля "состояние здоровья" задайте значение "Полностью здоров"
25. Выведите имя заявителя у какого-либо обращения. Убедитесь, что было сделано не более одного запроса.
26. Выведите список всех обращений с указанием списка задействованных экстренных служб в следующем формате: "номер
обращения: ‚ список кодов служ
27. Выведите все значения дат создания происшествий. Поместите даты в список.

 