# Generated by Django 4.1.1 on 2022-10-30 14:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя заявителя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия заявителя')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество заявителя')),
                ('birthdate', models.DateField(verbose_name='Дата рождения заявителя')),
                ('health_status', models.TextField(blank=True, default='Практически здоров', help_text='Аллергоанамез, хроническе, заболевания и т.п.', max_length=255, verbose_name='Состояние здоровья')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='Телефон заявителя')),
                ('gender', models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default='Мужчина', max_length=255, verbose_name='Пол')),
                ('image', models.ImageField(blank=True, help_text='Добавьте изображения заявителя', upload_to='photos/applicants/%Y/%m/%d', verbose_name='Изображение заявителя')),
            ],
            options={
                'verbose_name': 'Заявитель',
                'verbose_name_plural': 'Заявители',
                'ordering': ('first_name', 'last_name', 'patronymic'),
            },
        ),
        migrations.CreateModel(
            name='EmergencyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255, verbose_name='Имя экстренной службы')),
                ('service_code', models.CharField(max_length=255, verbose_name='Код экстренной службы')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Телефон экстренной службы')),
            ],
            options={
                'verbose_name': 'Экстренная служба',
                'verbose_name_plural': 'Экстренные службы',
                'ordering': ('service_code',),
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Описание')),
                ('number', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Номер карточки')),
                ('dc', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('injured', models.PositiveIntegerField(verbose_name='Количество пострадавших')),
                ('do_not_call', models.BooleanField(default=False, verbose_name='Не звонить')),
                ('status', models.CharField(choices=[('В работе', 'В работе'), ('Завершено', 'Завершено')], default='В работе', max_length=255, verbose_name='Статус')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='emergency_request.applicant', verbose_name='Заявитель')),
                ('emergency_service', models.ManyToManyField(related_name='requests', to='emergency_request.emergencyservice', verbose_name='Экстренная служба')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
                'ordering': ('dc',),
            },
        ),
    ]
