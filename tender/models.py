from django.db import models

# Create your models here.
class Type_tender(models.Model):
    name = models.CharField(max_length=200, verbose_name='Вид тендера')
    nomer=models.IntegerField(null=True,verbose_name='Порядковый номер')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['nomer']
        verbose_name_plural='Тип конкурсов'
        verbose_name='Тип конкурса'

class Region(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    my_id=models.IntegerField(unique=True, default='1')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Регионы'
        verbose_name='Регион'

class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    region=models.ForeignKey(Region,on_delete=models.SET_NULL, null=True,verbose_name='Регион')
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['region','name']
        verbose_name_plural='Города'
        verbose_name='Город'

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='Контрагент')

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural='Контрагенты'
        verbose_name='Контрагент'

class Organizations(models.Model):
    name = models.CharField(max_length=200, verbose_name='Юридические лица')
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='Контрагент')

    def __str__(self):
        return f'{(self.name)}, Контрагент: {self.company}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Юридические лица'
        verbose_name = 'Юридическое лицо'

class Client(models.Model):
    name = models.CharField(max_length=200)
    inn=models.CharField(max_length=50, verbose_name='ИНН')
    city=models.ForeignKey(City,on_delete=models.SET_NULL, null=True,verbose_name='Город')

    def __str__(self):
        return f'{(self.name)}, ИНН: {self.inn}'

    class Meta:
        ordering = ['name']
        verbose_name_plural='Заказчики'
        verbose_name='Заказчик'

class Group_prod(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товарная группа')
    nomer=models.IntegerField(null=True,verbose_name='Порядковый номер')
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['nomer']
        verbose_name_plural='Товарные группы'
        verbose_name='Товарная группа'

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    my_id = models.CharField(max_length=50,verbose_name='Артикул', default='0')
    price = models.CharField(max_length=10,blank=True, default='0.00', verbose_name='Цена')
    status = models.CharField(max_length=2, verbose_name='Статус', null=True)
    ss = models.CharField(max_length=10,blank=True, default='0.00', verbose_name='СС с НДС УЗМК')
    price2 = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name='Цена контракта')
    group_prod = models.ForeignKey(Group_prod, on_delete=models.SET_NULL, null=True, verbose_name='Товарная группа')
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Продукция'
        verbose_name='Продукт'

class Filial(models.Model):
    name = models.CharField(max_length=200,verbose_name='Юр. лицо филиала (Техноимпорт, Промет, Инвалиды и тп')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Филиалы'
        verbose_name='Филиал'

class Staffer(models.Model):
    name = models.CharField(max_length=200,verbose_name='Фамилия сотрудника')
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

class Tab(models.Model):
    # YES='Да'
    # NO='Нет'
    # CHOICES = [(YES, 'Да'), (NO, 'Нет'),]
    # protection = models.CharField(max_length=3, choices=CHOICES, default=YES,verbose_name='Защита')
    protection = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name='Защита')
    protection_info = models.CharField(max_length=200, blank=True, verbose_name='Примечание по защите')
    F = 'Филиал'
    D = 'Дилер'
    N = 'Другой'
    Net = 'Нет'
    CHOI = [(F, 'Филиал'), (D, 'Дилер'), (N, 'Другой'), (Net, 'Нет'),]
    win = models.CharField(max_length=6, choices=CHOI, default=F,verbose_name='Победитель')

    number_tender = models.CharField(max_length=50,blank=True, verbose_name='Номер тендера или ссылка')
    number_zakaza = models.CharField(max_length=50, blank=True, verbose_name='Номер заказа')
    number_scheta = models.CharField(max_length=50, blank=True, verbose_name='Номер счета')
    schet_info = models.CharField(max_length=200, blank=True, verbose_name='Примечание к счету (R%, затраты и тп)')
    url_tender = models.CharField(max_length=50, blank=True, verbose_name='Ссылка на папку с тендером')


    type_tender=models.ForeignKey(Type_tender,on_delete=models.SET_NULL, null=True,verbose_name='Тип тендера')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True,blank=True, verbose_name='Заказчик')
    price1=models.DecimalField(max_digits=20, decimal_places=2, null=True,blank=True, verbose_name='Начальная цена')

    data1=models.DateTimeField(null=True,blank=True,verbose_name='Дата начала')
    data2 = models.DateTimeField(null=True,blank=True, verbose_name='Дата конца')
    group_prod=models.ForeignKey(Group_prod,on_delete=models.SET_NULL, null=True,verbose_name='Товарная группа 1')

    info=models.CharField(max_length=200,blank=True, verbose_name='Примечание к товарным группам')
    filial=models.ForeignKey(Filial,on_delete=models.SET_NULL, null=True,verbose_name='Филиал')
    price2 = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True,verbose_name='Цена контракта')
    staffer = models.ForeignKey(Staffer, on_delete=models.SET_NULL, null=True, verbose_name='отв. Сотрудник')
    def __str__(self):
        return f'{self.number_tender} Заказчик: {self.client}'

    class Meta:
        ordering = ['data1']
        verbose_name_plural = 'Данные таблицы тендеров'
        verbose_name = 'Данные тендеров'

class Protection(models.Model):
    data1 = models.DateTimeField(null=True, verbose_name='Дата внесения')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Заказчик')
    data2 = models.DateTimeField(null=True, blank=True, verbose_name='Должен состояться до: ')
    product_info = models.TextField(max_length=500, blank=True, verbose_name='Примечание по ТМЦ')
    company=models.ForeignKey(Company,on_delete=models.SET_NULL, null=True,verbose_name='Дилер')

    def __str__(self):
        return str(self.company)

    class Meta:
        ordering = ['data1']
        verbose_name_plural = 'Данные таблицы защиты'
        verbose_name = 'Данные защиты'