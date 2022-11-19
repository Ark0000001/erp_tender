from django.contrib import admin

# Register your models here.
from import_export import resources,fields
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .forms import *
from import_export.tmp_storages import CacheStorage
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
User = get_user_model()


# def all_tasks(modeladmin, request,queryset):
#     for qs in queryset:
#         print (qs.staffer)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'nomer')
    list_display_links = ('name','nomer')
    search_fields = ('name',)
admin.site.register(Type_tender, TypeAdmin)


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
    class Meta:
        model = City
class CityAdmin(ImportExportModelAdmin):
    list_display = ('name', 'region')
    list_display_links = ('name', 'region')
    search_fields = ('name',)
    resource_class=CityResource
admin.site.register(City,CityAdmin)

class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name',)
    resource_class = CompanyResource
admin.site.register(Company,CompanyAdmin)


class OrganizationsResource(resources.ModelResource):
    class Meta:
        model = Organizations
class OrganizationsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'company', 'inn')
    list_display_links = ('name','inn')
    search_fields = ('name',)
    resource_class = OrganizationsResource
admin.site.register(Organizations,OrganizationsAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn')
    list_display_links = ('name', 'inn')
    search_fields = ('name','inn')
    form = ClientForm
admin.site.register(Client,ClientAdmin)

class GroupResource(resources.ModelResource):
    class Meta:
        model = Group_prod
class GroupAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    resource_class = GroupResource
admin.site.register(Group_prod,GroupAdmin)

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
class ProductAdmin(ImportExportModelAdmin):
    tmp_storage_class = CacheStorage
    list_display = ('group_prod','name','article','price', 'status')
    list_display_links = ('name',)
    search_fields = ('name',)
    resource_class =ProductResource
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

from django.forms import CheckboxSelectMultiple
class TabAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'group_prod': CheckboxSelectMultiple},
    }
    list_display = ('is_active','data2','staffer','type_tender','task_info','created','number_tender','url_tender','number_scheta','number_zakaza','protection','data1','price1','city','client','group_prod','info','filial','win','price2')
    list_display_links = ('staffer','number_tender','type_tender','client','data2','task_info')
    search_fields = ('staffer__name','client__name','task_info')
    actions = ('complete_tasks', 'incomplete_tasks',)

    def complete_tasks(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, f'Отметили как завершенные, следующее количество: {count} ')

    complete_tasks.short_description = 'Отметить как завершенные'

    def incomplete_tasks(self, request, queryset):
        count = queryset.update(is_active=False)
        self.message_user(request, f'Отметили как незавершенные, следующее количество: {count} ')

    incomplete_tasks.short_description = 'Отметить как незавершенные'

    def get_form(self,request,obj=None,**kwargs):
        form=super(TabAdmin,self).get_form(request,obj,**kwargs)
        form.base_fields['author'].initial=request.user

        if str(request.user)!='admin':
            form.base_fields['author'].disabled = request.user



        if request.user.groups.filter(name='MyGroup').exists():
            self.exclude=('created',)

        return form

admin.site.register(Tab,TabAdmin)


class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('city','client','product_info','company','data2')
    list_display_links = ('city','client','product_info','company','data2')
    search_fields = ('client__name','company__name')
admin.site.register(Protection,ProtectionAdmin)

class DealerResource(resources.ModelResource):
    class Meta:
        model = DealerTab
class DealerTabAdmin(ImportExportModelAdmin):

    list_display = ('is_active','organizations','company','pismo_ur_lic','dogovor','dop','dogovor_p','dogovor_v','protokol','sverka_v_1','sverka_v_2','sverka_v_3','sverka_v_4','sverka_1','sverka_2','sverka_3','sverka_4','ur_dokument','ur_doc_info','reshenie')
    list_display_links = ('organizations','company')
    search_fields = ('organizations','company')
    resource_class =DealerResource

    actions = ('complete_tasks', 'incomplete_tasks',)

    def complete_tasks(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, f'Отметили как завершенные, следующее количество: {count} ')

    complete_tasks.short_description = 'Отметить как завершенные'

    def incomplete_tasks(self, request, queryset):
        count = queryset.update(is_active=False)
        self.message_user(request, f'Отметили как незавершенные, следующее количество: {count} ')

    incomplete_tasks.short_description = 'Отметить как незавершенные'

admin.site.register(DealerTab,DealerTabAdmin)

admin.site.register(IconsDealers)

class PostavResource(resources.ModelResource):
    class Meta:
        model = PostavTab

class PostavTabAdmin(ImportExportModelAdmin):

    list_display = ('name','inn','dogovor','dop','sverka_1','sverka_2','sverka_3','sverka_4','pismo_ur_lic','ur_dokument','ur_doc_info','reshenie')
    list_display_links = ('name','inn')
    search_fields = ('name',)
    resource_class = PostavResource

admin.site.register(PostavTab,PostavTabAdmin)