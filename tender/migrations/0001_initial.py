# Generated by Django 4.1.1 on 2022-10-17 07:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['region', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('inn', models.CharField(max_length=50, verbose_name='ИНН')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Контрагент')),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Юр. лицо филиала (Техноимпорт, Промет, Инвалиды и тп')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group_prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Товарная группа')),
                ('nomer', models.IntegerField(null=True, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Товарная группа',
                'verbose_name_plural': 'Товарные группы',
                'ordering': ['nomer'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('my_id', models.IntegerField(default='1', unique=True)),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Staffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Фамилия сотрудника')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Type_tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Вид тендера')),
                ('nomer', models.IntegerField(null=True, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Тип конкурса',
                'verbose_name_plural': 'Тип конкурсов',
                'ordering': ['nomer'],
            },
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_info', models.TextField(blank=True, max_length=500, verbose_name='Описание задачи')),
                ('win', models.CharField(blank=True, choices=[('Филиал', 'Филиал'), ('Дилер', 'Дилер'), ('Другой', 'Другой'), ('Нет', 'Нет')], default='Филиал', max_length=6, null=True, verbose_name='Победитель')),
                ('number_tender', models.CharField(blank=True, max_length=50, verbose_name='Номер тендера или ссылка')),
                ('number_zakaza', models.CharField(blank=True, max_length=50, verbose_name='Номер заказа')),
                ('number_scheta', models.CharField(blank=True, max_length=50, verbose_name='Номер счета')),
                ('profit_info', models.CharField(blank=True, max_length=200, verbose_name='Ценность задачи (Нач цена, R%, затраты и тп)')),
                ('url_tender', models.CharField(blank=True, max_length=50, verbose_name='Ссылка на папку с тендером')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время создания')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Начальная цена')),
                ('data1', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала')),
                ('data2', models.DateTimeField(blank=True, null=True, verbose_name='Сделать до:')),
                ('info', models.CharField(blank=True, max_length=200, verbose_name='Примечание к товарным группам')),
                ('price2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена контракта')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.city', verbose_name='Город')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.client', verbose_name='Заказчик')),
                ('filial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.filial', verbose_name='Филиал')),
                ('group_prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.group_prod', verbose_name='Товарная группа 1')),
                ('protection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.company', verbose_name='Защита')),
                ('staffer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.staffer', verbose_name='отв. Сотрудник')),
                ('type_tender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.type_tender', verbose_name='Тип тендера')),
            ],
            options={
                'verbose_name': 'Данные тендеров',
                'verbose_name_plural': 'Данные таблицы тендеров',
                'ordering': ['data1'],
            },
        ),
        migrations.CreateModel(
            name='Protection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.DateTimeField(null=True, verbose_name='Дата внесения')),
                ('data2', models.DateTimeField(blank=True, null=True, verbose_name='Должен состояться до: ')),
                ('product_info', models.TextField(blank=True, max_length=500, verbose_name='Примечание по ТМЦ')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.city', verbose_name='Город')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.client', verbose_name='Заказчик')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.company', verbose_name='Дилер')),
            ],
            options={
                'verbose_name': 'Данные защиты',
                'verbose_name_plural': 'Данные таблицы защиты',
                'ordering': ['data1'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('my_id', models.CharField(default='0', max_length=50, verbose_name='Артикул')),
                ('price', models.CharField(blank=True, default='0.00', max_length=10, verbose_name='Цена')),
                ('status', models.CharField(max_length=2, null=True, verbose_name='Статус')),
                ('ss', models.CharField(blank=True, default='0.00', max_length=10, verbose_name='СС с НДС УЗМК')),
                ('price2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена контракта')),
                ('group_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.group_prod', verbose_name='Товарная группа')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукция',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Юридические лица')),
                ('inn', models.CharField(max_length=50, verbose_name='ИНН')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.company', verbose_name='Контрагент')),
            ],
            options={
                'verbose_name': 'Юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.region', verbose_name='Регион'),
        ),
    ]
