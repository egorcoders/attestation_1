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

1. Создать модель экстренной службы, обращения и заявителя.

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
   #1
   s1 = models.EmergencyService.objects.get(pk=1)
   s3 = models.EmergencyService.objects.get(pk=2)
   r = models.Request.objects.get(pk=1)
   r.emergency_service.add(s1, s2)
   
   #2
   s1 = models.EmergencyService.objects.get(pk=1)
   r = models.Request.objects.get(pk=1)
   r.emergency_service.set([s1,])
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

7. Если дважды проитерироваться по полученному ОuеrуSеt, то сколько будет сделано обращений в БД?
С помощью конструкции len(connection.queries) можно проверить количество запросов в БД. Для сброса следует использовать reset_queries() из django.db.
   ```python
   from django.db import connection, reset_queries
   reset_queries()
   # Возвращает 0
   len(connection.queries)
   r = models.Request.objects.all()
   # После первого обращения к БД, результат преобразуется в модели Django, которые заносятся в переменную _result_cache
   for i in r:
      print(i.request_number)
   # При повторном обращении, данные берутся из кэша
   for i in r:
      print(i.request_date)
   len(connection.queries)

   # Возвращает 1
   len(connection.queries)   
   ```

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
   ```python
   models.Applicant.objects.filter(birthdate__year__lt=(today.year - 18))
   ```
5. Получить всех совершеннолетних заявителей
   ```python
   models.Applicant.objects.filter(birthdate__year__gte=(today.year - 18))
   ```
6. Узнать есть ли вообще какие-нибудь заявители
   ```python
   models.Applicant.objects.exists()
   ```
7. Узнать, есть ли какие-нибудь заявители с похожими именами (пример: Алексей, Александра)
   ```python
   models.Applicant.objects.filter(first_name__contains='Алекс')
   ```
8. Получить все обращения, кроме тех, у которых не назначены службы
   ```python
   models.Applicant.objects.exists()
   ```
9. Среди обращений со службой с кодом "ОЗ" вывести дату самого первого обращения
   ```python
   models.Request.objects.filter(emergency_service__service_code='02').order_by('request_date').first()
   ```
10. Получить все обращения, которые созданы до определенной даты
   ```python
   from datetime import datetime
   models.Request.objects.filter(request_date__lt=datetime(2022, 9, 23))
   ```
11. Получить всех заявителей без изображения и/или без номера телефона
   ```python
   models.Applicant.objects.filter(Q(phone_number__exact="") | Q(image__exact=""))
   ```
12. Получить всех заявителей, с определенным кодом оператора (917) со службой 01
   ```python
   models.Applicant.objects.filter(requests__emergency_service__service_code='01')
   ```
13. Получить результат объединения, пересечения и разницы предыдущих двух запросов
14. Вывести все обращения, созданные в определенный период
   ```python
   models.Request.objects.filter(request_date__range=[datetime(2022, 1, 1), datetime(2022, 12, 12)])
   ```
15. Получить количество заявителей без номера телефона
   ```python
   models.Applicant.objects.filter(phone_number__exact='').count()
   ```
16. Выведите все уникальные записи модели заявитель
   ```python
   models.Applicant.objects.distinct()
   ```
17. Получить все обращения, в описании которых есть какое-то ключевое слово в любом регистре.
   ```python
   models.Request.objects.filter(description__icontains='so')
   ```
18. Выбрать всех заявителей, при этом получить только значения поля "номер телефона"
   ```python
   Applicant.objects.all().values_list('phone_number', flat=True)
   ```
19. Выбрать всех заявителей, при этом получить все поля, кроме состояния здоровья
   ```python
   models.Applicant.objects.all().defer('health_status')
   ```
20. Вывести все службы используя SQL запрос
   ```python
   for i in models.EmergencyService.objects.raw('SELECT * FROM emergency_request_emergencyservice'):
      print(i.service_name)
   ```
21. Выберите или создайте заявителя с номером "12341234"
   ```python
      obj, created = models.Applicant.objects.get_or_create(
         id='12341234', first_name='Daniel', last_name='Longi', middle_name='Milkovich', 
         birthdate='1988-05-13', health_status='Healthy', phone_number='+2982928282', gender='Мужчина',
         image='/')
   ```
22. Измените номер заявителя с номером "12341234" на любой другой, если заявителя, то запрос должен его создать.
   ```python
      obj, created = models.Applicant.objects.update_or_create(
         id='12341234', first_name='Daniel', last_name='Longi', middle_name='Milkovich',
         birthdate='1988-05-12', health_status='Healthy', phone_number='+2982928282', gender='Мужчина',
         image='/', defaults={'id': '123412369'})
   ```
23. Создайте сразу несколько заявителей.
   ```python
      Applicant.objects.bulk_create([Applicant(first_name='Misha'), Applicant(first_name='Masha')])
   ```
24. Измените несколько заявителей. Для поля "состояние здоровья" задайте значение "Полностью здоров"
   ```python
   models.Applicant.objects.all().update(health_status='Полностью здоров')
   ```
25. Выведите имя заявителя у какого-либо обращения. Убедитесь, что было сделано не более одного запроса.
   ```python
   models.Applicant.objects.filter(request__id=4).first().first_name
   ```
26. Выведите список всех обращений с указанием списка задействованных экстренных служб в следующем формате: "номер
обращения: ‚ список кодов служб
   ```python
   r = models.Request.objects.all()
   r.values_list('request_number', 'emergency_service')
   ```
27. Выведите все значения дат создания происшествий. Поместите даты в список.
   ```python
   lst = []
   models.Request.objects.all().values()
   for i in _: lst.append(i['request_date'].date())
   lst
   ```
 