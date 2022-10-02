from django.db import models

# Create your models here.


class Type_tender(models.Model):
    name = models.CharField(max_length=200)
    nomer=models.IntegerField(null=True,verbose_name='Порядковый номер')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['nomer']
        verbose_name_plural='Тип конкурсов'
        verbose_name='Тип конкурса'

class Region(models.Model):
    name = models.CharField(max_length=200)
    my_id=models.IntegerField(unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Регионы'
        verbose_name='Регион'

class City(models.Model):
    name = models.CharField(max_length=200)
    region=models.ForeignKey(Region,on_delete=models.SET_NULL, null=True,verbose_name='Регион')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['region','name']
        verbose_name_plural='Города'
        verbose_name='Город'

class Company(models.Model):
    name = models.CharField(max_length=200)
    inn=models.CharField(max_length=50, verbose_name='ИНН')

    def __str__(self):
        return f'{(self.name)}, ИНН: {self.inn}'

    class Meta:
        ordering = ['name']
        verbose_name_plural='Юридические лица'
        verbose_name='Юридическое лицо'

class Dealer(models.Model):
    name = models.CharField(max_length=200)
    company=models.ForeignKey(Company,on_delete=models.SET_NULL, null=True,verbose_name='Юридическое лицо')



    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Контрагенты'
        verbose_name='Контрагент'

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

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Продукция'
        verbose_name='Продукт'

class Filial(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural='Филиалы'
        verbose_name='Филиал'

class Staffer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

class Tab(models.Model):
    YES='Да'
    NO='Нет'
    CHOICES = [(YES, 'Да'), (NO, 'Нет'),]
    protection = models.CharField(max_length=3, choices=CHOICES, default=YES,verbose_name='Защита' )

    F = 'Филиал'
    D = 'Дилер'
    N = 'Другой'

    CHOI = [(F, 'Филиал'), (D, 'Дилер'), (N, 'Другой'), ]
    win = models.CharField(max_length=6, choices=CHOI, default=F,verbose_name='Победитель')


    number_tender = models.CharField(max_length=50, verbose_name='Номер тендера')
    type_tender=models.ForeignKey(Type_tender,on_delete=models.SET_NULL, null=True,verbose_name='Тип тендера')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Заказчик')
    price1=models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Начальная цена')

    data1=models.DateTimeField(null=True,verbose_name='Дата начала')
    data2 = models.DateTimeField(null=True, verbose_name='Дата конца')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, null=True,verbose_name='Продукт')
    dealer=models.ForeignKey(Dealer,on_delete=models.SET_NULL, null=True,verbose_name='Дилер')
    filial=models.ForeignKey(Filial,on_delete=models.SET_NULL, null=True,verbose_name='Филиал')
    price2 = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True,verbose_name='Цена контракта')

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
    data2 = models.DateTimeField(null=True, verbose_name='Должен состояться до: ')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, null=True,verbose_name='Продукт')
    dealer=models.ForeignKey(Dealer,on_delete=models.SET_NULL, null=True,verbose_name='Дилер')

    def __str__(self):
        return str(self.dealer)

    class Meta:
        ordering = ['data1']
        verbose_name_plural = 'Данные таблицы защиты'
        verbose_name = 'Данные защиты'
