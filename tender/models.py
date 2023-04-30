from django.db import models
# from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
import uuid

# import erp_tender.settings


class User(AbstractUser):
    pass


class Type_tender(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тип задачи (конкурса)')
    nomer = models.IntegerField(null=True, verbose_name='Порядковый номер')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Тип задач (конкурса)'
        verbose_name = 'Тип задачи (конкурса)'


class Region(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    my_id = models.IntegerField(unique=True, default='1')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name='Регион')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['region', 'name']
        verbose_name_plural = 'Города'
        verbose_name = 'Город'


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='Контрагент')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Контрагенты'
        verbose_name = 'Контрагент'


class Organizations(models.Model):
    name = models.CharField(max_length=200, verbose_name='Юридические лица')
    inn = models.CharField(max_length=50, null=True, blank=True, verbose_name='ИНН')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Контрагент')

    def __str__(self):
        return f'{(self.name)}, Контрагент: {(self.company)}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Юридические лица'
        verbose_name = 'Юридическое лицо'


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='Клиент/Заказчик')

    inn = models.CharField(max_length=50, verbose_name='ИНН', unique=True, default=uuid.uuid1)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')

    def __str__(self):
        return f'{(self.name)}, ИНН: {self.inn}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Заказчики'
        verbose_name = 'Заказчик'


class Group_prod(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товарная группа')
    nomer = models.IntegerField(null=True, verbose_name='Порядковый номер')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['nomer']
        verbose_name_plural = 'Товарные группы'
        verbose_name = 'Товарная группа'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    article = models.CharField(max_length=50, verbose_name='Артикул', unique=True, default='0')
    price = models.CharField(max_length=10, blank=True, default='0.00', verbose_name='Цена')
    status = models.CharField(max_length=2, blank=True, verbose_name='Статус', null=True)

    group_prod = models.CharField(max_length=200, null=True, verbose_name='Товарная группа')
    data1 = models.DateTimeField(null=True, blank=True, verbose_name='Дата пересчета 1')
    data2 = models.DateTimeField(null=True, blank=True, verbose_name='Дата пересчета 2')
    raznica1 = models.IntegerField(null=True, verbose_name='Отклонения 1', default=0)
    raznica2 = models.IntegerField(null=True, verbose_name='Отклонения 2', default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Продукция'
        verbose_name = 'Продукт'


class Filial(models.Model):
    name = models.CharField(max_length=200, verbose_name='Юр. лицо филиала (Техноимпорт, Промет, Инвалиды и тп')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Филиалы'
        verbose_name = 'Филиал'


class Staffer(models.Model):
    name = models.CharField(unique=True,max_length=200, verbose_name='Фамилия сотрудника')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'


import datetime
def upload_to(instance, filename):
    now = datetime.datetime.now()
    return 'file/zakaz/{}/{}/{}/{}'.format(now.year, now.month, now.day, filename)


class ZakazTab(models.Model):
    is_active = models.BooleanField(default=False, db_index=True, verbose_name='Завершено?')

    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True,
                                verbose_name='отв. Сотрудник')
    nomer_zakaz = models.CharField(max_length=50, blank=True, verbose_name='№ Заказа')
    name_zakaz = models.CharField(null=True,max_length=500, verbose_name='Имя заказа')
    data_zakaz = models.DateTimeField(null=True, blank=True, verbose_name='Дата заказа')
    srok_zakaz = models.DateField(null=True, blank=True, verbose_name='Срок выполнения')
    info_zakaz = models.TextField(max_length=1000, blank=True, verbose_name='Описание заказа')
    info_client = models.TextField(max_length=1000, blank=True, verbose_name='Клиент/контакты')

    schet = models.CharField(max_length=50, blank=True, verbose_name='№ Счета')


    zakaz_pdf = models.FileField(null=True, blank=True, upload_to=upload_to)
    created = models.DateTimeField('Дата и время создания', default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'№{self.nomer_zakaz}, до: {self.srok_zakaz}, имя: {self.name_zakaz}'

    class Meta:
        ordering = ['nomer_zakaz']
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'



class TenderTab(models.Model):
    is_active=models.BooleanField(default=False,db_index=True, verbose_name='Завершено?')
    created = models.DateTimeField('Дата и время создания', default=timezone.now)
    data_win = models.DateTimeField(null=True, blank=True, verbose_name='Дата победы')
    price1 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Цена договора')
    name_project = models.CharField(max_length=200, blank=True, verbose_name='Имя проекта')
    task_info = models.TextField(max_length=5000, blank=True, verbose_name='Описание проекта')
    economic = models.TextField(max_length=5000, blank=True, verbose_name='Экономика проекта')
    comment_info = models.TextField(max_length=5000, blank=True, verbose_name='Комментарий - ход событий')
    data_dog = models.DateTimeField(null=True, blank=True, verbose_name='Дата договора')

    type_tender = models.ForeignKey(Type_tender, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='Тип проекта')


    srok_postavki = models.DateTimeField(verbose_name='Срок поставки до:')
    penya = models.CharField(max_length=20, blank=True, verbose_name='Пеня за день просрочки:')


    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник')
    number_scheta = models.CharField(max_length=50, blank=True, verbose_name='Номер счета')
    number_zakaza = models.CharField(max_length=50, blank=True, verbose_name='Номер заказа')

    number_tender = models.CharField(max_length=1000, blank=True, verbose_name='Номер тендера или ссылка')

    url_tender = models.CharField(max_length=1000, blank=True, verbose_name='Ссылка на папку с проектом')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')

    updated = models.DateTimeField(auto_now=True)


    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город поставки')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заказчик')
    info_client = models.CharField(max_length=200, blank=True, verbose_name='Контакты заказчика')


    group_prod = models.ForeignKey(Group_prod, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Товарная группа')

    info = models.CharField(max_length=200, blank=True, verbose_name='Примечание к товарным группам')
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Филиал от кого?')

    def __str__(self):
        return f'№{self.id}, {self.name_project}'

    class Meta:
        ordering = ['data_win']
        verbose_name_plural = 'Проекты/тендера'
        verbose_name = 'Проект/тендер'



class Tab(models.Model):
    is_active=models.BooleanField(default=False,db_index=True, verbose_name='Завершено?')
    # YES='Да'
    # NO='Нет'
    # CHOICES = [(YES, 'Да'), (NO, 'Нет'),]
    # protection = models.CharField(max_length=3, choices=CHOICES, default=YES,verbose_name='Защита')
    profit_info = models.CharField(max_length=200, blank=True,
                                   verbose_name='Имя задачи')
    task_info = models.TextField(max_length=5000, blank=True, verbose_name='Описание задачи')
    project = models.ForeignKey(TenderTab, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Проект')

    zakaz = models.ForeignKey(ZakazTab, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Заказ')

    data2 = models.DateTimeField(verbose_name='Сделать до:')
    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник')
    type_tender = models.ForeignKey(Type_tender, on_delete=models.SET_NULL, blank=True,null=True,verbose_name='Тип задачи (конкурса)', editable=False)
    protection = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Защита', editable=False)
    created = models.DateTimeField('Дата и время создания', default=timezone.now)
    F = 'Филиал'
    D = 'Дилер'
    N = 'Другой'
    Net = 'Нет'
    CHOI = [(F, 'Филиал'), (D, 'Дилер'), (N, 'Другой'), (Net, 'Нет'), ]
    win = models.CharField(max_length=6, choices=CHOI, blank=True, null=True, default=F, verbose_name='Победитель', editable=False)

    number_tender = models.CharField(max_length=50, blank=True, verbose_name='Номер тендера или ссылка', editable=False)
    number_zakaza = models.CharField(max_length=50, blank=True, verbose_name='Номер заказа', editable=False)
    number_scheta = models.CharField(max_length=50, blank=True, verbose_name='Номер счета', editable=False)

    url_tender = models.CharField(max_length=50, blank=True, verbose_name='Ссылка на папку с задачей', editable=False)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')

    updated = models.DateTimeField(auto_now=True)


    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город', editable=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заказчик', editable=False)
    price1 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Начальная цена', editable=False)

    data1 = models.DateTimeField(null=True, blank=True, verbose_name='Дата начала')

    group_prod = models.ForeignKey(Group_prod, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Товарная группа', editable=False)

    info = models.CharField(max_length=200, blank=True, verbose_name='Примечание к товарным группам', editable=False)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Филиал', editable=False)
    price2 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name='Цена контракта', editable=False)


    def __str__(self):
        return f'{self.task_info} Заказчик: {self.type_tender}'

    class Meta:
        ordering = ['data1']
        verbose_name_plural = 'Данные таблицы задач'
        verbose_name = 'Данные задачи'


class Protection(models.Model):
    data1 = models.DateTimeField(null=True, verbose_name='Дата внесения')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Заказчик')
    data2 = models.DateTimeField(null=True, blank=True, verbose_name='Должен состояться до: ')
    product_info = models.TextField(max_length=500, blank=True, verbose_name='Примечание по ТМЦ')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='Дилер')

    def __str__(self):
        return str(self.company)

    class Meta:
        ordering = ['data1']
        verbose_name_plural = 'Данные таблицы защиты'
        verbose_name = 'Данные защиты'


class DealerTab(models.Model):
    Y = 'Да'
    N = 'Нет'
    NT = 'Не треб.'

    CHOI = ((Y, 'Да'), (N, 'Нет'), (NT, 'Не треб.'),)

    is_active = models.BooleanField(default=False, db_index=True, verbose_name='Не нужен контроль')
    organizations = models.CharField(max_length=200, null=True, blank=True,verbose_name='Юридические лица')

    inn = models.CharField(max_length=50, null=True, blank=True, verbose_name='ИНН')
    company = models.CharField(max_length=200, null=True, blank=True, verbose_name='Контрагент')
    pismo_ur_lic = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Письмо юр. лиц - Да/Нет')
    dogovor=models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Договор - Да/Нет')
    dop = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Доп. соглашение - Да/Нет')
    dogovor_p = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Договор поручительства - Да/Нет')
    dogovor_v = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Договор выставки - Да/Нет')
    protokol = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Протокол встреч - Да/Нет')
    sverka_v_1 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка выставки 1 кв. - Да/Нет')
    sverka_v_2 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка выставки 2 кв. - Да/Нет')
    sverka_v_3 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка выставки 3 кв. - Да/Нет')
    sverka_v_4 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка выставки 4 кв. - Да/Нет')
    sverka_1 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка 1 кв. - Да/Нет')
    sverka_2 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка 2 кв. - Да/Нет')
    sverka_3 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка 3 кв. - Да/Нет')
    sverka_4 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Сверка 4 кв. - Да/Нет')

    ur_dokument = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Юр. документы - Да/Нет')
    ur_doc_info = models.TextField(max_length=5000, blank=True, verbose_name='Доп. инфо. к юр. док-ам')
    task_info = models.TextField(max_length=5000, blank=True, verbose_name='Задачи по таблице дилеров')
    is_active_tasks = models.BooleanField(default=False, db_index=True, verbose_name='Поставлена задача')
    reshenie = models.DateTimeField(null=True, blank=True, verbose_name='Срок действия решения (назначение директора)')

    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.organizations} Контрагент: {self.company}'

    class Meta:
        ordering = ['company']
        verbose_name_plural = 'Данные наличия документов юр. лиц'
        verbose_name = 'Данные юр. лица'


class IconsDealers(models.Model):
    pismo = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    org = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    comp = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    dog = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    dogp = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    dogv = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    dop = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    v1 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    v2 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    v3 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    v4 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    s1 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    s2 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    s3 = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    s4 = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    urdoc = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    info = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    resh = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    sotr = models.ImageField(null=True, blank=True, upload_to="images/profile/")



# from datetime import datetime, timedelta
class PostavTab(models.Model):
    Y = 'Да'
    P = '1Пролонг.'
    N = 'Нет'
    NT = 'Не треб.'

    CHOI = ((Y, 'Да'), (P, '1Пролонг.'), (N, 'Нет'), (NT, 'Не треб.'),)

    is_active = models.BooleanField(default=False, db_index=True, verbose_name='Не нужен контроль')
    uslugi_vidy = models.TextField(max_length=500, blank=True, verbose_name='Виды услуг')
    organizations = models.CharField(max_length=200, null=True, blank=True, verbose_name='Юридические лица')

    inn = models.CharField(max_length=50, null=True, blank=True, verbose_name='ИНН')


    dogovor = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                               verbose_name='Договор - Да/Нет')
    nomer_dogovor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер договора')

    date_dogovor = models.DateField(null=True, blank=True, verbose_name='Дата договора')
    date_do_dogovor = models.DateField(null=True, blank=True, verbose_name='До какой даты договор')
    dop = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                           verbose_name='Доп. соглашение - Да/Нет')
    date_dop = models.DateField(null=True, blank=True, verbose_name='Дата доп. соглашения')
    protokol = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                verbose_name='Протокол встреч - Да/Нет')
    date_protokol = models.DateField(null=True, blank=True, verbose_name='Дата протокола')

    # @property
    # def is_past_due(self):
    #     if not self.date_dogovor:
    #         return 'no'
    #     return (self.date_dogovor + timedelta(days=365) < timezone.now().date())

    sverka_1 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                verbose_name='Сверка 1 кв. - Да/Нет')
    sverka_2 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                verbose_name='Сверка 2 кв. - Да/Нет')
    sverka_3 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                verbose_name='Сверка 3 кв. - Да/Нет')
    sverka_4 = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                verbose_name='Сверка 4 кв. - Да/Нет')
    sverka_god = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                verbose_name='Годовая сверка - Да/Нет')

    ur_dokument = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет',
                                   verbose_name='Юр. документы - Да/Нет')
    ur_doc_info = models.TextField(max_length=5000, blank=True, verbose_name='Доп. инфо. к юр. док-ам')
    task_info = models.TextField(max_length=5000, blank=True, verbose_name='Задачи по таблице поставщиков')
    is_active_tasks = models.BooleanField(default=False, db_index=True, verbose_name='Поставлена задача')

    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    SROK_DOGOVOR = models.TextField(max_length=5000, blank=True, verbose_name='Срок хранения договора', default='365')

    def __str__(self):
        return str(self.organizations)

    class Meta:
        ordering = ['is_active','organizations',]
        verbose_name_plural = 'Данные наличия документов поставщиков'
        verbose_name = 'Данные поставщика'


class ControlProduct(models.Model):


    product = models.CharField(max_length=200, null=True, blank=True, verbose_name='Юридические лица')

    kol = models.IntegerField(null=True, verbose_name='Количество')

    data1 = models.DateTimeField(null=True, verbose_name='Дата запроса')
    info_schet = models.TextField(max_length=500, blank=True, verbose_name='№№ Счет, Заказ, Заявка')

    data2 = models.DateTimeField(null=True, blank=True, verbose_name='Плановая дата сдачи')
    data3 = models.DateTimeField(null=True, blank=True, verbose_name='Дата фуры')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='Дилер')
    info = models.TextField(max_length=500, blank=True, verbose_name='Дополнительная информация')


    def __str__(self):
        return f'{self.product} Количество: {self.kol}'

    class Meta:
        ordering = ['product']
        verbose_name_plural = 'Контролируемая продукция'
        verbose_name = 'Контролируемый продукт'


class Info(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True, verbose_name='Наименование')
    created = models.DateTimeField('Дата и время создания', default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    content = models.TextField(null=True,blank=True, verbose_name='Статьи')


    text = models.TextField(max_length=100000,null=True, blank=True, verbose_name='Полезная информация')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)

    class Meta:
        ordering = ['-updated']
        verbose_name_plural = 'Полезные информации'
        verbose_name = 'Полезная информация'



class Gruz(models.Model):

    is_active = models.BooleanField(default=False, db_index=True, verbose_name='Оплачен')

    created = models.DateTimeField('Дата и время создания', default=timezone.now)
    name_gruz = models.CharField(max_length=200,blank=True,null=True, verbose_name='Грузоперевозчик')
    data_gruz = models.DateTimeField(null=True, verbose_name='Дата загрузки')

    schet = models.CharField(max_length=50, blank=True, verbose_name='№ Счет')
    data_schet = models.DateTimeField(null=True, blank=True, verbose_name='Дата счета')
    price_schet = models.CharField(max_length=100, blank=True, verbose_name='Сумма счета')


    city_1 = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город загрузки', related_name='gruz_city_1')
    city_2 = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город поставки', related_name='gruz_city_2')

    info_map = models.TextField(max_length=500, blank=True, verbose_name='Инфо к маршруту')

    Y = 'Да'
    N = 'Нет'
    NT = 'Не треб.'
    CHOI = ((Y, 'Да'), (N, 'Нет'), (NT, 'Не треб.'),)
    to = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Нет', verbose_name='Внесен в ТО: Да/Нет')
    data_to = models.DateTimeField(null=True, blank=True, verbose_name='Дата в ТО')

    M = 'Микс'
    C = 'СиМ'
    D = 'Двери'
    CHOI = ((M, 'Микс'), (C, 'СиМ'), (D, 'Двери'),)
    miks = models.CharField(max_length=16, choices=CHOI, blank=True, null=True, default='Микс',
                          verbose_name='Микс/СиМ/Двери')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник за доставку')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_gruz}, Дата погрузки: {self.data_gruz}, Маршрут: {self.city_1}-{self.city_2}, Товар: {self.miks}'

    class Meta:
        ordering = ['-data_gruz']
        verbose_name_plural = 'Доставки'
        verbose_name = 'Доставка'


