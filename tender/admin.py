from django.contrib import admin

# Register your models here.
from import_export import resources,fields
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
admin.site.register(Type_tender)


class RegResource(resources.ModelResource):

    class Meta:
        model = Region


class RegAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_display_links = ('name', )
    search_fields = ('name', )
    resource_class=RegResource
admin.site.register(Region,RegAdmin)



class CityResource(resources.ModelResource):
    region = fields.Field(
        column_name='region',
        attribute='region',
        widget=ForeignKeyWidget(Region,'name'))

    class Meta:
        model = City
        fields = 'region'


class CityAdmin(ImportExportModelAdmin):
    list_display = ('name', 'region')
    list_display_links = ('name', 'region')
    search_fields = ('name', 'region')
    resource_class=CityResource
admin.site.register(City,CityAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn')
    list_display_links = ('name', 'inn')
    search_fields = ('name','inn')
admin.site.register(Company,CompanyAdmin)


class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Dealer,DealerAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn')
    list_display_links = ('name', 'inn')
    search_fields = ('name','inn')
admin.site.register(Client,ClientAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Product,ProductAdmin)


class FilialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Filial,FilialAdmin)


class StafferAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Staffer,StafferAdmin)


class TabAdmin(admin.ModelAdmin):
    list_display = ('number_tender','protection','data1','data2','price1','type_tender','city','client','product','dealer','filial','win','price2')
    list_display_links = ('number_tender','type_tender','client')
    search_fields = ('client__name',)
admin.site.register(Tab,TabAdmin)


class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('city','client','product','dealer','data2')
    list_display_links = ('city','client','product','dealer','data2')
    search_fields = ('client__name','dealer_name')
admin.site.register(Protection,ProtectionAdmin)