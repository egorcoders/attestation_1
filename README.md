## 1.3 QuerySet

### Сохранение объектов в БД

1. Сохраните несколько объектов модели "Экстренных служб", "Заявителя" и "Обращения" двумя способами (методом сrеаtе
   уровня менеджера запросов ***objects*** и методом ***savе*** уровня экземпляра модели)
   ```python
   # сохранение объекта модели экстренных служб методом save
   models.EmergencyService(5, 'Охрана среды', 898, '+73482900405', 'gos').save()
   # сохранение объекта модели экстренных служб методом create
   models.EmergencyService.objects.create(service_name='Navy', service_code=25, phone_number='+922829')

   # сохранение объекта модели обращения методом save
   models.Request(6, 'text',  'eef066b7-de68-422e-a061-52c09ab60f04',  '1988-10-22', 2, 1, 'Завершено', 3).save()
   # сохранение объекта модели обращения методом create
   models.Request.objects.create(text='text', number='eef066b7-de68-422e-a061-44c09ab60f04', dc='1988-10-22', 
   injured=2, do_not_call=1, status=1, applicant_id=4)
 
   # сохранение объекта модели заявителя методом save
   models.Applicant(5, 'Jack', 'Long', 'Milkovich', '1988-05-13', 'Healthy', '+2982928282', 'Мужчина', '/').save()
   # сохранение объекта модели заявителя методом create
   models.Applicant.objects.create(first_name='Daniel', last_name='Longi', patronymic='Milkovich', 
   birthdate='1988-05-13', health_status='Healthy', phone_number='+2982928282', gender='Мужчина', image='/')
   ```
2. Создайте "Обращение" через менеджер запросов от объекта "Заявитель"
   ```python
   r = models.Request.objects.get(pk=1)
   models.Applicant.objects.get(pk=1).request.add(r)
   ```
3. Добавьте "Обращению" несколько "экстренных служб" двумя способами (add, set)
   Разница в том, что set ожидает список, а add - кортеж. Add - добавляет к новым, а set заменяет 
   на новый набор значений
   ```python
   #1 добавляет один 
   s1 = models.EmergencyService.objects.get(pk=1)
   s3 = models.EmergencyService.objects.get(pk=2)
   models.Request.objects.get(pk=1).emergency_service.add(s1, s3)
   
   #2 добавляет множество
   s1 = models.EmergencyService.objects.get(pk=1)
   r = models.Request.objects.get(pk=1)
   r.emergency_service.set([s1, s2])
   ```

### Запрос в БД

1. Получить объект заявителя с идентификатором в базе данных = 1 тремя способами.
   ```python
   # 1
   models.Applicant.objects.get(id=1)
   # 2
   models.Applicant.objects.filter(Q(pk=1)).first()
   # 3
   models.Applicant.objects.filter(pk=1).first()
   ```

2. Получить все обращения заявителя двумя способами
   ```python3
   # 1
   models.Request.objects.filter(applicant__id=7)
   # 2
   models.Request.objects.filter(Q(applicant__id=7))
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
   С помощью конструкции len(connection.queries) можно проверить количество запросов в БД. Для сброса следует
   использовать reset_queries() из django.db.
   ```python
   from django.db import connection, reset_queries
   reset_queries()
   # Возвращает 0
   len(connection.queries)
   r = models.Request.objects.all()
   # После первого обращения к БД, результат преобразуется в модели Django, которые заносятся в переменную _result_cache
   for i in r:
      print(i.number)
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
   models.Request.objects.filter(applicant_id=1).first()
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
   models.Applicant.objects.filter(birthdate__year__gte=(today.year - 18)) 
   ```
5. Получить всех совершеннолетних заявителей
   ```python
   models.Applicant.objects.filter(birthdate__year__lt=(today.year - 18))
   ```
6. Узнать есть ли вообще какие-нибудь заявители
   ```python
   models.Applicant.objects.exists()
   ```
7. Узнать, есть ли какие-нибудь заявители с похожими именами (пример: Алексей, Александра)
   ```python
   models.Applicant.objects.filter(first_name__icontains='алекс') 
   ```
8. Получить все обращения, кроме тех, у которых не назначены службы
   ```python
   models.Request.objects.filter(emergency_service__service_name__isnull=True)
   ```
9. Среди обращений со службой с кодом "ОЗ" вывести дату самого первого обращения
   ```python
   str(models.Request.objects.filter(emergency_service__service_code='03').latest('-dc').dc.date())
   ```
10. Получить все обращения, которые созданы до определенной даты
   ```python
   from datetime import datetime
   models.Request.objects.filter(request_date__lt=datetime(2022, 9, 23))
   ```
11. Получить всех заявителей без изображения и/или без номера телефона
   ```python
   from django.db.models import Q
   a = models.Applicant.objects.filter(Q(phone_number__isnull=True) | Q(image__exact__isnull=True))
   ```
12. Получить всех заявителей, с телефоном (917) со службой 01 !!!
   ```python
   models.Applicant.objects.filter(Q(requests__emergency_service__service_code='01') & Q(phone_number__icontains='917'))
   ```
13. Получить результат объединения, пересечения и разницы предыдущих двух запросов
   ```python
   a.union(b)
   a.intersection(b)
   a.difference(b)
   ```
14. Вывести все обращения, созданные в определенный период
   ```python
   models.Request.objects.filter(request_date__range=[datetime(2022, 1, 1), datetime(2022, 12, 12)])
   ```
15. Получить количество заявителей без номера телефона
   ```python
   models.Applicant.objects.filter(phone_number__isnull=True).count()
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
   models.Applicant.objects.all().values_list('phone_number', flat=True) 
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
   applicant, _ = models.Applicant.objects.get_or_create(
      id='12341234', first_name='Daniel', last_name='Longi',
      birthdate='1988-05-13', health_status='Healthy', gender='Мужчина')
   ```
22. Измените номер заявителя с номером "12341234" на любой другой, если заявителя, то запрос должен его создать.
   ```python
   applicant, _ = models.Applicant.objects.update_or_create(id='12341234', defaults={'id': '123412369'})
   ```
23. Создайте сразу несколько заявителей.
   ```python
      models.Applicant.objects.bulk_create([Applicant(first_name='Misha'), Applicant(first_name='Masha')])
   ```
24. Измените несколько заявителей. Для поля "состояние здоровья" задайте значение "Полностью здоров" !!!
   ```python
   a = models.Applicant.objects.get(pk=1)
   b = models.Applicant.objects.get(pk=2)
   a.health_status = b.health_status = 'Полностью здоров'
   models.Applicant.objects.bulk_update([a, b], 'health_status')
   ```
25. Выведите имя заявителя у какого-либо обращения. Убедитесь, что было сделано не более одного запроса !!!
   ```python # prefetch related
   models.Applicant.objects.filter(request__id=4).first().first_name  # prefetch_related
   ```
26. Выведите список всех обращений с указанием списка задействованных экстренных служб в следующем формате: "номер
    обращения: список кодов служб !!!
   ```python
   r = models.Request.objects.all()
   for i in r:
      print(f'{i.number} :{[k.service_code for k in set(i.emergency_service.all())]}')
   ```
27. Выведите все значения дат создания происшествий. Поместите даты в список. !!!
   ```python
   str(i.date()) for i in list(str(models.Request.objects.values_list('dc', flat=True).date()))
   ```
28. Создайте queryset, который будет всегда пустым
   ```python
   models.Request.objects.none()
   ```
29. Вывести среднее количество пострадавших в происшествиях
   ```python
   from django.db.models import Avg
   models.Request.objects.aggregate(Avg('injured'))
   ```
30. Вывести общее количество пострадавших в происшествиях !!!
   ```python
   from django.db.models import Sum
   models.Request.objects.aggregate(Sum('injured'))
   ```
31. Вывести количество вызванных экстренных служб для каждого происшествия !!!
   ```python
   from django.db.models import Count
   emergency_services = models.Request.objects.annotate(Count('emergency_service'))
   for i in range(emergency_services.count()):
      print(emergency_services[i].num_services)
   ```
32. Вывести среднее количество вызванных экстренных служб !!!
   ```python
   from django.db.models import Avg
   models.Request.objects.aggregate(Avg('injured'))  # чекнуть 
   ```
33. Вывести наибольшее и наименьшее количество пострадавших !!!
   ```python
   from django.db.models import Min, Max
   models.Request.objects.aggregate(Max('injured'), Min('injured'))
   ```
34. Сформировать запрос к модели заявитель, в котором будет добавлено поле
    с количеством обращений каждого заявителя. !!!
   ```python
   from django.db.models import Count
   a = models.Applicant.objects.annotate(num_requests = Count('requests'))
   for i in range(a.count()):
      print(a[i].num_requests)
   ```
35. Всем обращениям, у которых назначены службы, присвоить статус "Завершено".
   ```python
   models.Request.objects.filter(emergency_service__isnull=False).update(status='Завершено')
   ```
36. Удалить всех заявителей без номера телефона.
   ```python
   models.Applicant.objects.filter(phone_number__isnull=True).delete()
   ```